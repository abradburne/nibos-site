+++
title = "nibOS"
template = "index.html"

[extra]
headline = "A real Linux system for the RG DS+."
lede = "nibOS is mainline Linux and U-Boot, all of Arch Linux ARM, and a hardware layer for the DS+'s two screens, buttons, sound, sleep and charging. It starts into a console on the top screen with a touch keyboard on the bottom one. SSH in, install with pacman, build on it."
hero_render = { src = "rgds-plus.webp", width = 1267, height = 1283, alt = "An Anbernic RG DS+ in dark blue, open, running nibOS: a shell on the top screen, the touch keyboard on the bottom one." }

shots = [
  { src = "console-shell.webp", caption = "The shell", alt = "nibOS's console: nib battery, nib wifi status and uname on the top screen; the touch keyboard below, its t key pressed." },
  { src = "console-nib.webp", caption = "nib, for the device", alt = "nibOS's console: nib net status, nib brightness and nib battery protect on the top screen; the touch keyboard below, Ctrl on." },
  { src = "console-vim.webp", caption = "Vim, out of the box", alt = "Vim editing a short notes file on the top screen; the touch keyboard below." },
]

figures = [
  { value = "0.65", unit = "s", label = "from reset to the kernel" },
  { value = "1.5", unit = "s", label = "to a picture on both screens" },
  { value = "≈5", unit = "s", label = "to the console" },
  { value = "49", unit = "mA", label = "drawn in deep sleep" },
]

stack = [
  { part = "Bootloader", what = "U-Boot, mainline" },
  { part = "Kernel", what = "Linux 7.3, mainline" },
  { part = "Graphics", what = "Panfrost and Mesa" },
  { part = "Userland", what = "Arch Linux ARM" },
  { part = "Hardware", what = "nibos-hw" },
  { part = "SDK", what = "nibkit" },
]

[extra.console]
title = "A terminal on top, a keyboard below"
text = "The console fills the top screen and a touch keyboard the bottom one, with Esc, Ctrl, Alt and the shortcuts a shell needs. The buttons type too: the D-pad is the arrows, A is Enter, B Backspace. Menu + X hides the keyboard; a USB or Bluetooth keyboard works beside it."
link = "@/manual/console.md"
link_text = "Using the console"

[extra.nib]
title = "The whole device, through nib"
text = "Each screen's brightness, battery protect, Wi-Fi and Bluetooth, the lid, when the network comes up, the speaker tuning, the clock and updates: nib drives the parts of the DS+ that Linux alone leaves you to work out. nib help lists them."
link = "@/manual/console.md#nib"
link_text = "Every nib command"

[[extra.notes]]
title = "Sleep"
text = "Close the lid: deep sleep at 49 mA, and Wi-Fi back about two seconds after you open it."
[[extra.notes]]
title = "Charging"
text = "Plug in a switched-off DS+ and it charges dark, amber light on. Battery protect stops at about 80%."
[[extra.notes]]
title = "Updates"
text = "Signed updates over Wi-Fi into a second copy of the system. If one fails to start, it rolls back by itself."
[[extra.notes]]
title = "Wi-Fi and Bluetooth"
text = "Up at every start, from a network named on the card. Headphones and keyboards pair; sound follows the headphones."
[[extra.notes]]
title = "SSH, by key"
text = "Give a public key on the card before the first start and log in as nibos@nibos.local. No passwords over SSH."
[[extra.notes]]
title = "Build for it"
text = "nibkit gives a program both screens, the buttons by their labels, touch and settings; a template app runs as it is."

[[extra.steps]]
title = "Download the image"
text = "One file for the DS+, with its checksum."
link = "@/download.md"
[[extra.steps]]
title = "Write it to a card"
text = "With Raspberry Pi Imager or dd, your SSH key beside it. The stock card stays as it is."
link = "@/manual/install.md"
[[extra.steps]]
title = "Power on"
text = "The console on the screens, or ssh nibos@nibos.local."
link = "@/manual/first-boot.md"

+++

Built with AI agents (Claude, in Claude Code), directed by one person and run on a real RG DS+
at every step. [Contributing](@/contributing.md) says how to join in, with or without AI.
