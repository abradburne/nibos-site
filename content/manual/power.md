+++
title = "Sleep, charging and the battery"
description = "Sleep and wake, the power menu, charging while off, the LEDs, battery protect and brightness."
weight = 8
+++

## Sleep

- **Close the lid**, or **tap power**: the DS+ sleeps (suspend to RAM). A game in progress is
  held where it is.
- **Open the lid**, or **press power**: it wakes. Wi-Fi reconnects about 2 seconds later. The
  press that wakes it does nothing else.

Asleep, the DS+ uses little power, but it does use some: for days away, power it off.

## The power menu

**Hold power for a second**: Sleep, Restart, Power off, Cancel. During a game, the game is saved
and put away first; Cancel carries on with it, and so does waking from Sleep. In DSlot, its menu
(X) → System → **Power off** does the same.

At power-off and restart, a goodbye picture stays on screen until the power goes.

## Charging

Charge from the DS+'s charging USB-C port (the other one is for USB devices).

| You see | Means |
|---|---|
| Green LED | Running. |
| Amber LED | The charger is plugged in (charging or full), awake or asleep. |
| Dark screens, amber LED | Charging while "off" (below). |

**Charging while off.** Plugging a charger into a DS+ that is off switches it on: the hardware
does that by itself. Rather than start the shelf because a cable went in, nibOS charges it
asleep, screens dark, with the amber LED lit. Press **power** (or open the lid) to start it
properly; unplug it and it switches off again.

## The battery

DSlot's status bar shows the charge, with a bolt or a plug while charging. DSlot's menu (X) → System
shows it too, with what the battery is doing: charging, with an estimate of the time to full;
holding for battery protect; or full.

The charge shown is counted by the power chip as charge goes in and out of the battery.

**Battery protect** stops charging at about 80% and starts again at 75%, so a DS+ left on its
charger ages its battery more slowly. Turn it on in DSlot's menu (System → Battery protect), or
in the console with `nib battery protect on`. `nib battery` shows the charge and the setting.

Long, demanding sessions (3D DS games at higher resolution) warm the DS+ and drain the battery
faster; charging while playing them warms it further.

## Brightness and volume

- **Menu + Volume up / down**: both screens' brightness, from anywhere, in steps of 5%.
- Each screen has its own level: DSlot's menu → System → Top screen, Bottom screen, or
  `nib brightness top 40` in the console. The lowest level is dim, never off.
- **Volume up / down**: the volume of whatever is playing (speakers, wired or Bluetooth
  headphones), in steps of 5%.

Brightness is kept across restarts.

## The speakers

The DS+'s speaker amplifiers need a tuning file to play. nibOS ships its own, set
conservatively. If you have the stock firmware, you can use its official
tuning instead: DSlot's menu → System → **Import official tuning** reads it from a stock card in
TF2 (or a stock firmware image in `Roms`), which can take a few minutes. It applies at the next
restart, which the page then offers. In the console, `sudo nib audio import-tuning` does the
same. Headphones don't need either.
