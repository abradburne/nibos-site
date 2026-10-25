+++
title = "Licences"
description = "Which licence each part of nibOS is under, and what that means for you."
+++

Everything nibOS's projects wrote is free software: you may use it, study it, change it and pass
it on. Two kinds of licence are used, chosen for what each part is for: the GPL, and the
permissive MIT and Apache-2.0.

## The split

| Part | Licence | Why |
|---|---|---|
| **nibOS**'s own code: the hardware layer (`nibos-hw`, `nib`), the tools, the image build, the system's scripts and units, the safe mode, the start-up pictures | GPL-3.0-or-later | An operating system: whoever ships it, changed or not, ships its source too. |
| **DSlot**, the game shelf | GPL-3.0-or-later | The same: it is nibOS's face. |
| **DSperate**, DS and GBA | GPL-3.0-or-later | The licence of the project it is forked from. |
| **nibkit**, the SDK, and the **template app** | MIT | A library and a starting point for anyone's apps and emulators, whatever their licence. |
| **inkdot**, **inktick**, **nibcase** | MIT or Apache-2.0, at your option | Emulators written from scratch, free for anyone to build on. |

The GNU General Public License, version 3 or later, is the Free Software Foundation's text,
unchanged. MIT and Apache-2.0 are the usual permissive licences; both let you use the code in
anything, with the copyright notice kept.

## What keeps its own licence

| Part | Licence |
|---|---|
| Linux, with nibOS's kernel patches | GPL-2.0 |
| U-Boot, with nibOS's patches | GPL-2.0-or-later |
| The RG DS+'s device tree | GPL-2.0-or-later or MIT |
| Arch Linux ARM's packages | Each its own, listed in the image's `packages.txt` |
| Roboto Condensed, the font in DSlot and the menus | SIL Open Font License 1.1 |
| The system cards' console photos | Public domain, or CC BY 4.0, credited on each card |
| The libretro cores nibcase plays | Each its own: GPL-2.0, GPL-3.0 or Zlib, except **Snes9x** (below) |
| nibOS's PortMaster profile | MIT, PortMaster's own licence |

**Snes9x**, the SNES core, is under its own **non-commercial** licence, the only part of the
DSlot edition that is. Because of it, the DSlot edition may not be sold, or passed on as part of
anything sold. The base edition doesn't include it.

## Not free, and named as such

Two pieces of firmware the RG DS+ needs aren't free software. nibOS includes them, unchanged,
under the licences that allow passing them on, and says so in every image's `NOTICE`:

- Rockchip's memory initialisation and TF-A (`rkbin`), run once at power-on.
- Realtek's Wi-Fi and Bluetooth firmware (from `linux-firmware`).

## Not included

- **Games and BIOS files.** nibOS comes with none; they are yours to supply.
- **Anything from the stock firmware**, including the official speaker tuning, which you can
  import from your own copy ([Sleep, charging and the battery](@/manual/power.md#the-speakers)).
- **PortMaster** and the ports it installs, which it downloads under their own licences.

## The source

Every image's `NOTICE` gives the commit of each project in it and the written offer of the
complete corresponding source for its GPL and LGPL parts, which is published beside each
release. The repositories are on [GitHub](https://github.com/abradburne); each has its
`LICENSE` and, where it builds in other people's code, a list of it with its licences.

## This site

- **The text and pictures**: this manual and the site's pages are under
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). You may copy, translate and
  adapt them, for any purpose, as long as you credit "the nibOS manual" with a link to this
  site, and share what you make under the same licence.
- **The templates and stylesheet** are under the MIT licence.
- **The screenshots** come from DSlot's documentation and are GPL-3.0-or-later, like DSlot. The
  font, Roboto Condensed, is under the SIL Open Font License 1.1.

The site's [repository](https://github.com/abradburne/nibos-site) has the licence texts.
