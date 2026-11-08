# The Anbernic RG DS+, open, built procedurally. Units: 1 = 1 cm.
# Closed: 16.7 x 9.6 x 2.4 cm. Screens: 4.3", 4:3 (8.74 x 6.55 cm).
# blender -b -P rgds-plus.py -- --shot capture.png --out render.png [--samples 256] [--res 1600]
#   [--shell #RRGGBB --buttons #RRGGBB]: the shell's and the buttons' colours (default: black)
import bpy, bmesh, math, sys, os
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(name, default):
    return argv[argv.index(name) + 1] if name in argv else default
SHOT = arg("--shot", "")
OUT = arg("--out", "/tmp/rgds.png")
SAMPLES = int(arg("--samples", "128"))
RES = int(arg("--res", "1400"))
OPEN = float(arg("--open", "62"))       # lid angle up from flat-behind, degrees
CAM = arg("--cam", "front")
BLEND = arg("--blend", "")
SHELL_HEX = arg("--shell", "#24262b")
BUTTON_HEX = arg("--buttons", "#17181c")

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

W, D = 16.7, 9.6          # footprint of each half
BASE_H, LID_H = 1.35, 1.05
SW, SH = 8.74, 6.55       # screen active area
HINGE_R = 0.62
AXIS = Vector((0, -HINGE_R, HINGE_R))   # hinge axis (along X), world


# ---------- materials ----------
def principled(name, color, rough=0.5, coat=0.0, metal=0.0, spec=0.5):
    m = bpy.data.materials.new(name)
    try: m.use_nodes = True
    except Exception: pass
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if "Coat Weight" in b.inputs: b.inputs["Coat Weight"].default_value = coat
    if "Specular IOR Level" in b.inputs: b.inputs["Specular IOR Level"].default_value = spec
    return m

def lin(h):  # sRGB hex -> linear
    h = h.lstrip("#"); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    return tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c)

SHELL = principled("shell", lin(SHELL_HEX), rough=0.42, spec=0.45)
SHELL_INNER = principled("shell_inner", tuple(c * 1.06 for c in lin(SHELL_HEX)), rough=0.5, spec=0.4)
BEZEL = principled("bezel", lin("#0a0b0d"), rough=0.12, coat=0.6)
BUTTON = principled("button", lin(BUTTON_HEX), rough=0.3, coat=0.3)
RUBBER = principled("rubber", lin("#121315"), rough=0.75, spec=0.3)
HOLE = principled("hole", (0.0, 0.0, 0.0), rough=0.9)
PRINT = principled("print", lin("#8a8f99"), rough=0.6)
LED = principled("led", lin("#2a2a2a"), rough=0.3)

def screen_material(name, top):
    m = bpy.data.materials.new(name)
    try: m.use_nodes = True
    except Exception: pass
    nt = m.node_tree; n = nt.nodes; l = nt.links
    b = n.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (0, 0, 0, 1)
    b.inputs["Roughness"].default_value = 0.04
    if "Coat Weight" in b.inputs: b.inputs["Coat Weight"].default_value = 0.0
    if "Coat Roughness" in b.inputs: b.inputs["Coat Roughness"].default_value = 0.03
    if "Specular IOR Level" in b.inputs: b.inputs["Specular IOR Level"].default_value = 0.02
    if SHOT:
        tex = n.new("ShaderNodeTexImage")
        tex.image = bpy.data.images.load(SHOT)
        tex.interpolation = "Cubic"
        tc = n.new("ShaderNodeTexCoord"); mp = n.new("ShaderNodeMapping")
        mp.inputs["Scale"].default_value = (1, 0.5, 1)
        mp.inputs["Location"].default_value = (0, 0.5 if top else 0.0, 0)
        l.new(tc.outputs["UV"], mp.inputs["Vector"]); l.new(mp.outputs["Vector"], tex.inputs["Vector"])
        l.new(tex.outputs["Color"], b.inputs["Emission Color"])
        b.inputs["Emission Strength"].default_value = 1.15
    return m


# ---------- geometry helpers ----------
def rrect(w, d, r, seg=12, cx=0, cy=0):
    pts = []
    for (sx, sy, a0) in ((1, 1, 0), (-1, 1, 90), (-1, -1, 180), (1, -1, 270)):
        ccx, ccy = cx + sx * (w / 2 - r), cy + sy * (d / 2 - r)
        for i in range(seg + 1):
            a = math.radians(a0 + 90 * i / seg)
            pts.append((ccx + r * math.cos(a), ccy + r * math.sin(a)))
    return pts

def finish(obj, mat, bevel=0.0, seg=4, angle=35):
    obj.data.materials.append(mat)
    if bevel:
        m = obj.modifiers.new("bevel", "BEVEL")
        m.width = bevel; m.segments = seg; m.limit_method = "ANGLE"
        m.angle_limit = math.radians(angle); m.harden_normals = False
    obj.data.shade_smooth()
    try: obj.data.set_sharpness_by_angle(angle=math.radians(angle))
    except Exception: pass
    return obj

def slab(name, w, d, h, r, z0, cx=0, cy=0, mat=SHELL, bevel=0.0, seg=12, parent=None):
    bm = bmesh.new()
    vs = [bm.verts.new((x, y, z0)) for x, y in rrect(w, d, r, seg, cx, cy)]
    f = bm.faces.new(vs)
    ext = bmesh.ops.extrude_face_region(bm, geom=[f])
    for v in [e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)]:
        v.co.z += h
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); scene.collection.objects.link(ob)
    if parent: ob.parent = parent
    return finish(ob, mat, bevel)

def disc(name, r, h, loc, mat, bevel=0.0, verts=64, rot=(0, 0, 0), parent=None):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=loc, rotation=rot)
    ob = bpy.context.active_object; ob.name = name
    if parent: ob.parent = parent
    return finish(ob, mat, bevel)

def plane(name, w, h, loc, mat, parent=None):
    bpy.ops.mesh.primitive_plane_add(size=1, location=loc)
    ob = bpy.context.active_object; ob.name = name; ob.scale = (w, h, 1)
    ob.data.materials.append(mat)
    if parent: ob.parent = parent
    return ob

def text(body, size, loc, mat, parent=None, align="CENTER"):
    bpy.ops.object.text_add(location=loc)
    ob = bpy.context.active_object; ob.data.body = body; ob.data.size = size
    ob.data.align_x = align; ob.data.align_y = "CENTER"
    ob.data.extrude = 0.002; ob.data.materials.append(mat)
    if parent: ob.parent = parent
    return ob


# ---------- base ----------
slab("base", W, D, BASE_H, 1.05, -BASE_H, cy=-D / 2, bevel=0.32, seg=16)
# lower screen: raised black frame, then the panel
LCY = -5.35
slab("lower_frame", SW + 1.0, SH + 0.95, 0.07, 0.35, -0.01, cy=LCY, mat=BEZEL, bevel=0.03)
plane("lower_screen", SW, SH, (0, LCY, 0.0605), screen_material("lower_screen", False))

# d-pad
DX, DY = -6.45, -3.05
for n, (w, d) in (("dpad_h", (1.75, 0.58)), ("dpad_v", (0.58, 1.75))):
    slab(n, w, d, 0.16, 0.09, 0.0, cx=DX, cy=DY, mat=BUTTON, bevel=0.05)
disc("dpad_well", 1.12, 0.02, (DX, DY, 0.0), HOLE, verts=64)
# analogue stick: dark well, rubber cap
SX, SY = -6.45, -5.95
disc("stick_well", 0.98, 0.03, (SX, SY, 0.0), HOLE)
disc("stick_ring", 0.98, 0.04, (SX, SY, 0.01), BUTTON, bevel=0.015)
disc("stick_base", 0.55, 0.22, (SX, SY, 0.1), RUBBER, bevel=0.06)
disc("stick_cap", 0.68, 0.16, (SX, SY, 0.24), RUBBER, bevel=0.07)
# the two small round buttons under the stick
for i, x in enumerate((-7.05, -5.85)):
    disc(f"small_{i}", 0.3, 0.12, (x, -8.15, 0.05), BUTTON, bevel=0.04)
# ABXY
AX, AY, AS = 6.45, -3.15, 0.78
for n, (dx, dy) in {"X": (0, 1), "A": (1, 0), "B": (0, -1), "Y": (-1, 0)}.items():
    disc(f"btn_{n}", 0.34, 0.16, (AX + dx * AS, AY + dy * AS, 0.06), BUTTON, bevel=0.06)
    text(n, 0.3, (AX + dx * AS, AY + dy * AS, 0.142), PRINT)
# start / select pills, with their names
for i, (y, name) in enumerate(((-6.55, "START"), (-7.45, "SELECT"))):
    slab(f"pill_{i}", 0.62, 0.32, 0.1, 0.16, 0.0, cx=6.2, cy=y, mat=BUTTON, bevel=0.04)
    text(name, 0.2, (6.75, y, 0.002), PRINT, align="LEFT")
# power LED (side) and a mic hole on the hinge
disc("led", 0.06, 0.02, (7.6, -1.8, 0.0), LED, verts=24)

# hinge: base knuckles at the ends, raised from the base's back edge
for i, (x0, x1) in enumerate(((-W / 2 + 0.35, -6.2), (6.2, W / 2 - 0.35))):
    disc(f"knuckle_{i}", HINGE_R, x1 - x0, (AXIS.x + (x0 + x1) / 2, AXIS.y, AXIS.z), SHELL, bevel=0.18,
         rot=(0, math.radians(90), 0))
slab("hinge_bed", W - 0.8, 1.2, HINGE_R, 0.3, 0.0, cy=-HINGE_R, mat=SHELL, bevel=0.1)


# ---------- lid, built flat behind the hinge, then turned up ----------
pivot = bpy.data.objects.new("lid_pivot", None); scene.collection.objects.link(pivot)
pivot.location = AXIS
lid_parts = []
def lp(ob): ob.parent = pivot; lid_parts.append(ob); return ob

disc_l = disc("lid_knuckle", HINGE_R * 0.92, 12.2, (0, 0, 0), SHELL, bevel=0.15, rot=(0, math.radians(90), 0), parent=pivot)
LY0 = 0.35                                   # lid's hinge-side edge, from the axis
lid = slab("lid", W, D, LID_H, 1.05, -LID_H / 2, cy=LY0 + D / 2, bevel=0.3, seg=16, parent=pivot)
LZ = LID_H / 2                               # inner face
TCY = LY0 + D / 2 + 0.15
slab("top_bezel", SW + 1.35, SH + 1.2, 0.03, 0.3, LZ - 0.01, cy=TCY, mat=BEZEL, bevel=0.015, parent=pivot)
lp(plane("top_screen", SW, SH, (0, TCY, LZ + 0.021), screen_material("top_screen", True)))
# speaker grilles: a hexagon of holes either side
for side in (-1, 1):
    cx, cy = side * 6.55, TCY - 0.2
    pts = [(0, 0)] + [(0.3 * math.cos(math.radians(a)), 0.3 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
    for j, (px, py) in enumerate(pts):
        disc(f"spk_{side}_{j}", 0.055, 0.02, (cx + px, cy + py, LZ), HOLE, verts=16, parent=pivot)
# small marks near the top corners
for side in (-1, 1):
    slab(f"mark_{side}", 0.22, 0.22, 0.01, 0.04, LZ - 0.005, cx=side * 7.35, cy=LY0 + D - 0.9, mat=HOLE, parent=pivot)

# open the lid: rotate about X; at OPEN degrees from flat-behind
pivot.rotation_euler = (math.radians(OPEN), 0, 0)
bpy.context.view_layer.update()


# ---------- floor, light, camera ----------
bpy.ops.mesh.primitive_plane_add(size=400, location=(0, 0, -BASE_H - 0.001))
floor = bpy.context.active_object; floor.name = "floor"
floor.is_shadow_catcher = True

world = bpy.data.worlds.new("world"); scene.world = world
try: world.use_nodes = True
except Exception: pass
bg = world.node_tree.nodes.get("Background")
bg.inputs["Color"].default_value = (*lin("#e9e6df"), 1); bg.inputs["Strength"].default_value = 0.35

def area(name, loc, size, energy, color="#ffffff", target=(0, -2, 1)):
    bpy.ops.object.light_add(type="AREA", location=loc)
    L = bpy.context.active_object; L.name = name
    L.data.size = size; L.data.energy = energy; L.data.color = lin(color)
    d = Vector(target) - Vector(loc); L.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    return L
area("key", (-38, -20, 60), 34, 90000, "#fff6ea")
fill = area("fill", (35, -30, 48), 55, 22000, "#eaf0ff")
try: fill.visible_shadow = False
except Exception: pass
area("rim", (5, 45, 40), 25, 45000)

cam_data = bpy.data.cameras.new("cam"); cam = bpy.data.objects.new("cam", cam_data)
scene.collection.objects.link(cam); scene.camera = cam
target = Vector((0, -1.0, 2.2))
if CAM == "front":
    cam.location = Vector((-24, -78, 66)); cam_data.lens = 100
else:
    cam.location = Vector((0, -95, 30)); cam_data.lens = 110
cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()
cam_data.dof.use_dof = False

# ---------- render ----------
scene.render.engine = "CYCLES"
prefs = bpy.context.preferences.addons["cycles"].preferences
try:
    prefs.compute_device_type = "METAL"; prefs.refresh_devices()
    for d in prefs.devices: d.use = True
    scene.cycles.device = "GPU"
except Exception as e:
    print("GPU unavailable:", e)
scene.cycles.samples = SAMPLES
scene.cycles.use_denoising = True
scene.render.film_transparent = True
scene.render.resolution_x = RES
scene.render.resolution_y = int(RES * 0.82)
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "AgX - Medium High Contrast" if "AgX - Medium High Contrast" in [l for l in []] else "None"
scene.render.filepath = OUT
if BLEND: bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)
print("WROTE", OUT)
