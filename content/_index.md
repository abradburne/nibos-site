+++
title = "nibOS"
template = "index.html"

[extra]
eyebrow = "A Linux system of its own for the Anbernic RG DS+"
headline = "Two screens. Five seconds. Your games."
lede = "Mainline Linux, Arch Linux ARM and DSlot, a game shelf made for the clamshell. Press power, and your carts are waiting over the slot."

stats = [
  { value = "0.65", unit = "s", label = "from reset to the kernel" },
  { value = "1.5", unit = "s", label = "to a picture on both screens" },
  { value = "≈5", unit = "s", label = "to the game shelf" },
  { value = "18", unit = "", label = "systems, one menu" },
]

systems = [
  { name = "Nintendo DS", colour = "#c9ccd3" },
  { name = "Game Boy Advance", colour = "#6b5bd6" },
  { name = "Game Boy", colour = "#8fae4b" },
  { name = "Game Boy Color", colour = "#b0427a" },
  { name = "SNES", colour = "#8a7fd1" },
  { name = "NES", colour = "#c23b32" },
  { name = "Famicom Disk System", colour = "#d9a441" },
  { name = "Mega Drive", colour = "#3b4a6b" },
  { name = "Master System", colour = "#c0392b" },
  { name = "SG-1000", colour = "#7f8c8d" },
  { name = "Game Gear", colour = "#2c3e50" },
  { name = "PC Engine", colour = "#e5e5e5" },
  { name = "PC Engine CD", colour = "#e67e22" },
  { name = "PlayStation", colour = "#9aa0a6" },
  { name = "Atari Lynx", colour = "#d35400" },
  { name = "Neo Geo Pocket", colour = "#1f6fb2" },
  { name = "WonderSwan", colour = "#16a085" },
  { name = "Game & Watch", colour = "#b8860b" },
  { name = "PortMaster ports", colour = "#f5c542" },
]

stack = [
  { name = "DSlot and the emulators", note = "The shelf, DSperate, inkdot, nibcase, inktick" },
  { name = "nibkit", note = "The SDK: both screens, buttons, touch, the shared menu" },
  { name = "nibos-hw", note = "The hardware layer: one gamepad, sound that follows the jack, sleep, charging" },
  { name = "Arch Linux ARM", note = "systemd, pacman, a full userland" },
  { name = "Linux 7.3, mainline", note = "With Panfrost and Mesa: open graphics" },
  { name = "U-Boot, mainline", note = "SPL in Falcon mode: the kernel 0.65 s after reset" },
]

[[extra.features]]
kicker = "The shelf"
title = "Push a cart into the slot"
text = "Your games as carts over a card slot on the touch screen, their boxes, play time and ratings on the top one. Or a cover grid, or a list: flick it and it glides. A page for each system, a picker on Select, and a card for every console, with its history and cited facts."
image = "grid.png"
alt = "DSlot's cover grid on the touch screen, with the selected game's box and play time on the top screen."
link = "@/manual/shelf.md"
link_text = "Tour the shelf"

[[extra.features]]
kicker = "One menu"
title = "Every emulator, the same buttons"
text = "Back opens the menu, Menu saves and takes you home, and the next start carries on where you left off. Six save slots with pictures, settings per game or per system, Wi-Fi and Bluetooth: the same menu in DSlot, DSperate, inkdot, nibcase and inktick."
image = "menu.png"
alt = "DSlot's menu on the touch screen: favourite, rating, view, sort, sounds, start at power-on, power off."
link = "@/manual/controls.md"
link_text = "Every control"

[[extra.cards]]
icon = "moon"
title = "Sleeps like it should"
text = "Close the lid: deep sleep, and Wi-Fi back about two seconds after you open it."

[[extra.cards]]
icon = "bolt"
title = "Charges asleep"
text = "Plug in a switched-off DS+ and it charges dark, amber light on. Battery protect stops at 80%."

[[extra.cards]]
icon = "shield"
title = "Updates itself"
text = "Signed updates over Wi-Fi, installed while you play. If one ever fails to start, it rolls back by itself."

[[extra.cards]]
icon = "wave"
title = "Bluetooth and Wi-Fi"
text = "Join networks and pair headphones and controllers from the shelf's menu. Sound follows the headphones."

[[extra.cards]]
icon = "terminal"
title = "A real computer"
text = "Leave the shelf for a console with a touch keyboard on the bottom screen. SSH, pacman, the lot."

[[extra.cards]]
icon = "box"
title = "PortMaster on tap"
text = "Get PortMaster from the Apps page and install ports over Wi-Fi; they appear on their own shelf page."

+++

nibOS, DSlot and the emulators were built with AI agents (Claude, in Claude Code), directed by
one person and played on a real RG DS+ every step of the way. Want to join in, with or without
AI? [Contributing](@/contributing.md) says how.
