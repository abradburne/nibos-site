+++
title = "The nibOS manual"
description = "Installing nibOS on the RG DS+, the console and its keyboard, SSH, nib, the radios, power, updates and what to do when something goes wrong."
sort_by = "weight"
template = "manual.html"
page_template = "manual.html"
+++

This manual is for people who use nibOS on an **Anbernic RG DS+** as a Linux system: installing
it, working in its console and over SSH, and getting out of trouble. It covers
{{ config.extra.release.version }}.

nibOS starts into a Linux console on the top screen, with a touch keyboard on the bottom one.
For games, [DSlot]({{ config.extra.dslot_site }}/) is nibOS with a game shelf and emulators on
top; it has its own image and [its own manual]({{ config.extra.dslot_site }}/manual/). The two
cards can be written over each other, and an update never turns one into the other.

What a word means here:

| Word | Means |
|---|---|
| TF1, TF2 | The DS+'s two microSD slots. TF1 (marked TF1/INT) is the one the device starts from. |
| NIBOS | A small partition on the card with the licences, a README and the settings file `provision.toml`. |
| NIBOS-DATA | The card's data partition, over the rest of the card, at `/mnt/roms`. It is what a computer shows when the card is in its reader, and where the logs are kept. |
| `nib` | nibOS's command for the device: brightness, battery, radios, updates. |
| Menu | The DS+'s Menu button, below the screen, named as on the device. |
