+++
title = "nibOS"
template = "index.html"

[extra]
eyebrow = "Arch Linux for the Anbernic RG DS+"
headline = "A real Linux system, on both screens."
lede = "nibOS is mainline Linux and U-Boot, all of Arch Linux ARM, and a hardware layer that makes the RG DS+'s two screens, buttons, sound, sleep and charging simply work. It starts into a console with a touch keyboard; SSH in, pacman install, build on it."
hero_alt = "An illustration of an RG DS+ running nibOS: a shell prompt on the top screen, a touch keyboard on the bottom one."

stats = [
  { value = "0.65", unit = "s", label = "from reset to the kernel" },
  { value = "1.5", unit = "s", label = "to a picture on both screens" },
  { value = "≈5", unit = "s", label = "to the console" },
  { value = "49", unit = "mA", label = "drawn in deep sleep" },
]

stack = [
  { name = "Your programs", note = "Or DSlot and its emulators: the game system built on nibOS" },
  { name = "nibkit", note = "The SDK: both screens, buttons, touch, the shared menu" },
  { name = "nibos-hw", note = "The hardware layer: one gamepad, sound that follows the jack, sleep, charging" },
  { name = "Arch Linux ARM", note = "systemd, pacman, a full userland" },
  { name = "Linux 7.3, mainline", note = "With Panfrost, the open GPU driver" },
  { name = "U-Boot, mainline", note = "SPL in Falcon mode: the kernel 0.65 s after reset" },
]

[[extra.features]]
kicker = "The console"
title = "A terminal on top, a keyboard below"
text = "The console fills the top screen and a touch keyboard the bottom one, with Ctrl, Alt, Esc and the shortcuts a shell needs. The buttons type too: the D-pad is the arrows, A is Enter. Menu + X hides the keyboard; a USB or Bluetooth keyboard works beside it."
console = "[nibos@nibos ~]$ uname -m\naarch64\n[nibos@nibos ~]$ sudo pacman -S "
alt = "An illustration of nibOS's console on an RG DS+: commands on the top screen, the touch keyboard on the bottom."
link = "@/manual/console.md"
link_text = "Using the console"

[[extra.features]]
kicker = "One command"
title = "The whole device, through nib"
text = "Each screen's brightness, battery protect, Wi-Fi and Bluetooth, the lid, when the network comes up, the speaker tuning, the clock and the updater: nib drives the parts of the DS+ that Linux alone leaves you to work out, and nib help lists them."
console = "$ nib brightness top 40\n$ nib battery protect on\n$ nib wifi on\n$ sudo nib net mode deferred\n$ nib update check\n$ "
alt = "An illustration of nib commands typed in nibOS's console on an RG DS+."
link = "@/manual/console.md#nib"
link_text = "Every nib command"

[[extra.cards]]
icon = "moon"
title = "Sleeps like it should"
text = "Close the lid: deep sleep at 49 mA, and Wi-Fi back about two seconds after you open it."

[[extra.cards]]
icon = "bolt"
title = "Charges asleep"
text = "Plug in a switched-off DS+ and it charges dark, amber light on. Battery protect stops at 80%."

[[extra.cards]]
icon = "shield"
title = "Updates itself"
text = "Signed updates over Wi-Fi into a second copy of the system. If one ever fails to start, it rolls back by itself."

[[extra.cards]]
icon = "wave"
title = "Wi-Fi and Bluetooth"
text = "Up at every start, from a network named on the card. Headphones and keyboards pair; sound follows the headphones."

[[extra.cards]]
icon = "terminal"
title = "SSH, by key"
text = "Give a public key on the card before the first start and log in as nibos@nibos.local. No passwords over SSH, ever."

[[extra.cards]]
icon = "box"
title = "Build for it"
text = "nibkit gives a program both screens, the buttons by their labels, touch and settings; a template app runs as it is."

+++

nibOS was built with AI agents (Claude, in Claude Code), directed by one person and run on a
real RG DS+ every step of the way. Want to join in, with or without AI?
[Contributing](@/contributing.md) says how.
