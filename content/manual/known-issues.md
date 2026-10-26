+++
title = "Known issues"
description = "What is unfinished in the alpha, what doesn't work yet, and what to expect."
weight = 12
+++

nibOS {{ config.extra.release.version }} is an **alpha**: the second version anyone outside the
project can install. Everything on the RG DS+ works, and every change was tried on a real one,
but it has been tried on few devices and few cards, and some things that a finished
system has are still to come. This page says what.

## Not there yet

- **Updates** are new: 0.1.0-alpha2 is the first release a device takes over the air
  ([Updates](@/manual/updates.md)). Cards built from source (development cards) don't update
  themselves; image cards do.
- **Packages.** nibOS's own packages (kernel, hardware layer, DSlot, the emulators) aren't in a
  package repository: they come with the system and its updates, not with `pacman`, so the
  base edition can't add DSlot.
- **Security.** There are no passwords unless `provision.toml` sets one: the console logs in by
  itself and `sudo` asks for nothing, so anyone holding the DS+ has full control of it. SSH is
  off until you give a key, and never takes passwords. The system partition is writable.
- **Installing** needs a computer to write the card; there is no installer on the device.
- **One device.** nibOS runs on the Anbernic RG DS+ only.

## Games and emulators

- **PlayStation**: most games play, but occasional frames take nearly a whole frame's time,
  which shows as a stutter in some games. Higher internal resolution is off until that is
  understood.
- **Famicom Disk System**: set up, and its BIOS check tested, but not yet played with a game.
- **DS games at a higher 3D resolution** cost more: 4x is too slow for most games, and at 2x or
  3x the heaviest scenes can fall behind, when DSperate shows every other frame and then drops
  the 3D to 1x by itself until it catches up. They also warm the DS+ and drain the battery
  faster.
- **inktick** (Game & Watch) is a preview: units that use the SM5A chip (the Silver and Gold
  series and a few others) aren't supported yet. nibcase plays Game & Watch too, from `.mgw`
  files.
- **Carts** are drawn for the DS, GBA, Game Boy, Game Boy Color, SNES, NES, Mega Drive, Game Gear
  and Lynx; the other systems show boxes.
- **slot CFW saves**: GBA battery saves from a slot card aren't picked up by themselves; copy
  them across ([Games, BIOS and saves](@/manual/games.md#a-card-set-up-for-slot-cfw)). Save
  states never carry over between emulators.
- **Snes9x**, the SNES emulator core, has a non-commercial licence: the DSlot edition may not be
  sold, or passed on as part of anything sold ([Licences](@/licences.md)).

## PortMaster

- Ports that need RetroArch don't start; nibOS has no RetroArch.
- Ports that need 32-bit libraries aren't offered.
- PortMaster is downloaded on first use, so Get PortMaster needs Wi-Fi.

## Hardware

- **A warm restart can leave the top screen striped** (alternate lines). A cold power-on is
  clean: power off, then on.
- **A complete kernel hang** (no interrupts at all) stays dark until you hold power to switch
  off; every other hang restarts the DS+ by itself. The same goes for a shutdown from
  overheating.
- **USB around sleep**: the USB host controller is switched off while the DS+ sleeps (suspending
  it hangs the kernel, cause unknown), so a USB device reconnects after waking.
- **Speakers**: nibOS's own speaker tuning is set conservatively, so they are not as loud as
  they can be. The official tuning can be imported from your own stock firmware
  ([Sleep, charging and the battery](@/manual/power.md#the-speakers)). The amplifiers sometimes
  fail to start at first during start-up and then recover; a start with silent speakers is
  possible, though it hasn't been seen. A restart brings them back.
- **Bluetooth audio** hasn't yet been tested with real headphones. SBC, aptX, LDAC and Opus; no
  AAC.
- **Battery life** isn't yet what it will be: the processor's deeper idle states aren't used
  yet, and Wi-Fi's power saving is off (with it on, the DS+'s Wi-Fi drops off the network).
  On the shelf the DS+ draws about 0.5 A. Turn Wi-Fi off when you don't need it; on a fresh
  card it starts off.
- **The console's touch keyboard** is new, and hasn't yet had much use on the device.

## Reporting what you find

Found something not on this page? [Report it](@/manual/troubleshooting.md#reporting-a-bug),
with the log from the card.
