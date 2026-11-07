+++
title = "Known issues"
description = "What is unfinished in the beta, what doesn't work yet, and what to expect."
weight = 9
+++

nibOS {{ config.extra.release.version }} is a **beta**. Everything on the RG DS+ works; this
page lists what's still to come.

## Not there yet

- **Updates**: cards built from source (development cards) don't update themselves; image
  cards do ([Updates](@/manual/updates.md)).
- **Packages.** nibOS's own packages (kernel, hardware layer) aren't in a package
  repository: they come with the system and its updates, not with `pacman`. Nor are DSlot and
  its emulators, so they can't be added to a nibOS card: write
  [DSlot's image]({{ config.extra.dslot_site }}/download/) instead.
- **Security.** There are no passwords unless `provision.toml` sets one: the console logs in by
  itself and `sudo` asks for nothing, so anyone holding the DS+ has full control of it. SSH is
  off until you give a key, and never takes passwords. The system partition is writable.
- **Installing** needs a computer to write the card; there is no installer on the device.
- **One device.** nibOS runs on the Anbernic RG DS+ only.

## Hardware

- **A warm restart can leave the top screen striped** (alternate lines). A cold power-on is
  clean: power off, then on.
- **A complete kernel hang** (no interrupts at all) stays dark until you hold power to switch
  off; every other hang restarts the DS+ by itself. The same goes for a shutdown from
  overheating.
- **USB around sleep**: the USB host port is switched off while the DS+ sleeps, so a USB device
  reconnects after waking.
- **Speakers**: nibOS's own speaker tuning isn't as loud as they can go. Import the official
  tuning from your own stock firmware for more
  ([Sleep, charging and the battery](@/manual/power.md#the-speakers)).
- **Bluetooth audio** is new: SBC, aptX, LDAC and Opus, no AAC. Tell us how your headphones do.
- **Battery life** will get better: the processor's deeper idle states and Wi-Fi power saving
  are still to come. Turn Wi-Fi off when you don't need it.

DSlot's and its emulators' own known issues are in
[DSlot's manual]({{ config.extra.dslot_site }}/manual/known-issues/).

## Reporting what you find

Found something not on this page? [Report it](@/manual/troubleshooting.md#reporting-a-bug),
with the log from the card.
