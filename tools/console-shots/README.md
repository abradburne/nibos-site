# console-shots

The home page's console pictures: both RG DS+ screens as nibOS shows them in the console. The top
screen is the kernel console (fbcon) in Terminus 16x32, the font nibOS boots with
(`fbcon=font:TER16x32`), 64 x 24 cells in the Linux console's colours. The bottom one is the
touch keyboard, drawn by the code nibos-keys draws it with (nibkit v0.1.0's `menu::keys` and
`menu::raster`). The text of each scene is what those commands print, from their source in nibOS
0.1.0-beta2; the pictures are drawn on a computer, not captured from the device.

```sh
# The font bitmap, 16384 bytes, from a Linux tree's lib/fonts/font_ter16x32.c:
python3 -c "import re,sys; s=open(sys.argv[1]).read(); s=s[s.index('FONTDATAMAX, 0 }'):]; \
  open('ter16x32.bin','wb').write(bytes(int(n,16) for n in re.findall(r'0x[0-9a-f]{2}',s)[:16384]))" \
  ~/linux/lib/fonts/font_ter16x32.c
cargo run --release -- scenes/shell.txt press:t shell.png ter16x32.bin
```

`SCENE KEYS OUT FONT`: a scene is text with a few SGR escapes (`\e[0m`, `1`, `7`, `34`) and
`\x01` where the cursor is; `KEYS` is `plain`, `ctrl`, `shift` or `press:<key>`. The output is
1024 x 1536, the top screen above the bottom one. The site's WebPs are these at 768 x 1152.
`hero.txt` is the render's (`../rgds-plus.py`).
