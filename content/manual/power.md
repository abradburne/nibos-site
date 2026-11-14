+++
title = "Sleep, charging and the battery"
description = "Sleep and wake, powering off, charging while off, the LEDs, battery protect, brightness and the speakers."
weight = 6
+++

## Sleep

- **Close the lid**, or **tap power**: the DS+ sleeps (suspend to RAM). What is running is held
  where it is.
- **Open the lid**, or **press power**: it wakes. Wi-Fi reconnects about 2 seconds later. The
  press that wakes it does nothing else.

Asleep on battery for an hour, the DS+ powers off, so the battery lasts; on the charger it
sleeps on. `nib sleep` shows how long; `sudo nib sleep off-after 15` sets it in minutes, and
`never` sleeps until woken. `nib lid ignore` stops the lid sleeping the DS+ (`nib lid sleep`
puts it back).

## Powering off

**Hold power for a second** to power off cleanly, or `sudo poweroff` (`sudo reboot` to
restart). Holding it for about 10 seconds cuts the power without saving anything: only for a
DS+ that doesn't answer.

At power-off and restart, a goodbye picture stays on screen until the power goes.

## Charging

Charge from the DS+'s charging USB-C port (the other one is for USB devices).

| You see | Means |
|---|---|
| Green LED | Running. |
| Amber LED | The charger is plugged in (charging or full), awake or asleep. |
| Dark screens, amber LED | Charging while "off" (below). |
| Red LED blinking | The battery is low: 10% or under, blinking faster at 5% ([below](#the-battery)). |

**Charging while off.** Plug a charger into a switched-off DS+ and it charges quietly, screens
dark, amber LED lit. Press **power** (or open the lid) to start it; unplug it and it switches
off again.

## The battery

`nib battery` shows the charge, what the battery is doing (charging, holding for battery
protect, or full) and the battery protect setting.

**Battery protect** stops charging at about 80% and starts again at 75%, so a DS+ left on its
charger ages its battery more slowly: `nib battery protect on` (or `off`).

**Low battery.** At 10% and again at 5% the red LED blinks, faster when lower; apps can read
the level from `/run/nibos/battery-alert`. At 2%, or if the cell stays at 3.45 V or under, the
DS+ powers itself off before the battery runs flat. Plugging in the charger clears it.

Long, demanding work (compiling, the GPU flat out) warms the DS+ and drains the battery faster;
charging at the same time warms it further.

## Brightness and volume

- **Menu + Volume up / down**: both screens' brightness, from anywhere, in steps of 5%.
- Each screen has its own level: `nib brightness` shows both, `nib brightness top 40` sets one
  (`bottom`, `all`). The lowest level is dim, never off. **Menu + X** in the console blanks the
  keyboard's screen.
- **Volume up / down**: the volume of whatever is playing (speakers, wired or Bluetooth
  headphones), in steps of 5%.

Brightness is kept across restarts.

## The speakers

nibOS ships its own speaker tuning. If you have the stock firmware, you can import its
official tuning for more volume, from a stock card in TF2 or a stock firmware image:

```sh
nib audio                          # which tuning the speakers use
sudo nib audio import-tuning       # the official one, from your own stock firmware
sudo nib audio tuning nibos        # back to nibOS's
```

It can take a few minutes, and applies at the next restart. Headphones don't need either.
