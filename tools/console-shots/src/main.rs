//! Both DS+ screens as nibOS shows them in the console: the kernel console (fbcon, Terminus
//! 16x32, 64 x 24 cells) on top, and nibos-keys' keyboard (nibkit's own draw list and
//! rasteriser) below. Writes one 1024 x 1536 PNG, the top screen above the bottom one.
//!
//! console-shots SCENE KEYS OUT FONT
//!   SCENE: text with a few SGR escapes (0 1 7 34) and \x01 for the cursor
//!   KEYS:  plain | ctrl | shift | press:<char>
use nibkit::menu::keys::Keys;
use nibkit::menu::raster::{Canvas, Fonts};
use nibkit::menu::Draw;

const W: usize = 1024;
const H: usize = 768;

fn main() {
    let a: Vec<String> = std::env::args().collect();
    let scene = std::fs::read_to_string(&a[1]).unwrap().replace("\\e", "\x1b");
    let font = std::fs::read(&a[4]).unwrap();
    let mut img = vec![0u8; W * H * 2 * 4];
    for p in img.chunks_mut(4) {
        p[3] = 255;
    }
    console(&mut img, &scene, &font);

    let mut keys = Keys::new();
    let find = |keys: &Keys, label: &str| {
        keys.draws().into_iter().find_map(|d| match d {
            Draw::Text { text, x, y, size, .. } if text == label => Some((x, y + size * 0.3)),
            _ => None,
        })
    };
    match a[2].as_str() {
        "plain" => {}
        m @ ("ctrl" | "shift") => {
            let (x, y) = find(&keys, if m == "ctrl" { "Ctrl" } else { "shift" }).unwrap();
            keys.touch_down(x, y);
            keys.touch_up();
        }
        p if p.starts_with("press:") => {
            let c = p[6..].chars().next().unwrap();
            let (x, y) = keys.centre_of(c).unwrap();
            keys.touch_down(x, y);
        }
        o => panic!("keys: {o}"),
    }
    let fonts = Fonts::new();
    let mut canvas = Canvas::new(1.0);
    canvas.draw(&fonts, &keys.draws(), |_| None);
    assert_eq!((canvas.w, canvas.h), (W, H));
    img[W * H * 4..].copy_from_slice(&canvas.px[..W * H * 4]);

    let f = std::fs::File::create(&a[3]).unwrap();
    let mut e = png::Encoder::new(std::io::BufWriter::new(f), W as u32, (H * 2) as u32);
    e.set_color(png::ColorType::Rgba);
    e.set_depth(png::BitDepth::Eight);
    e.write_header().unwrap().write_image_data(&img).unwrap();
}

/// The Linux console's 16 colours (drivers/tty/vt default_red/grn/blu).
fn palette(i: usize) -> [u8; 3] {
    const P: [[u8; 3]; 16] = [
        [0, 0, 0], [170, 0, 0], [0, 170, 0], [170, 85, 0],
        [0, 0, 170], [170, 0, 170], [0, 170, 170], [170, 170, 170],
        [85, 85, 85], [255, 85, 85], [85, 255, 85], [255, 255, 85],
        [85, 85, 255], [255, 85, 255], [85, 255, 255], [255, 255, 255],
    ];
    P[i]
}

fn console(img: &mut [u8], scene: &str, font: &[u8]) {
    let (mut col, mut row) = (0usize, 0usize);
    let (mut fg, mut bold, mut rev) = (7usize, false, false);
    let mut chars = scene.chars().peekable();
    let mut cursor = None;
    while let Some(c) = chars.next() {
        match c {
            '\x1b' => {
                chars.next(); // [
                let mut n = String::new();
                for d in chars.by_ref() {
                    if d == 'm' {
                        break;
                    }
                    n.push(d);
                }
                for p in n.split(';') {
                    match p {
                        "" | "0" => (fg, bold, rev) = (7, false, false),
                        "1" => bold = true,
                        "7" => rev = true,
                        p => fg = p.parse::<usize>().unwrap() - 30,
                    }
                }
            }
            '\x01' => cursor = Some((col, row)),
            '\n' => (col, row) = (0, row + 1),
            c => {
                if col == 64 {
                    (col, row) = (0, row + 1);
                }
                let f = palette(fg + if bold { 8 } else { 0 });
                let (f, b) = if rev { (palette(0), f) } else { (f, palette(0)) };
                cell(img, font, col, row, c as u32, f, b);
                col += 1;
            }
        }
    }
    // fbcon's underline cursor: the cell's bottom rows.
    if let Some((cx, cy)) = cursor {
        for y in 32 - 6..32 - 2 {
            for x in 0..16 {
                put(img, cx * 16 + x, cy * 32 + y, palette(7));
            }
        }
    }
}

fn cell(img: &mut [u8], font: &[u8], col: usize, row: usize, c: u32, f: [u8; 3], b: [u8; 3]) {
    let g = match c {
        0x20..=0x7e => c as usize,
        0xb7 => 0xfa,
        _ => '?' as usize,
    };
    for y in 0..32 {
        let bits = u16::from_be_bytes([font[g * 64 + y * 2], font[g * 64 + y * 2 + 1]]);
        for x in 0..16 {
            let on = bits & (0x8000 >> x) != 0;
            put(img, col * 16 + x, row * 32 + y, if on { f } else { b });
        }
    }
}

fn put(img: &mut [u8], x: usize, y: usize, c: [u8; 3]) {
    if x < W && y < H {
        let i = (y * W + x) * 4;
        img[i..i + 3].copy_from_slice(&c);
    }
}
