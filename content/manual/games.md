+++
title = "Games, BIOS and saves"
description = "Which folder each system's games go in, the files each takes, the BIOS files some need, where saves are kept, and using a second card or a slot CFW card."
weight = 5
+++

## The folders

Games go in `Roms/<folder>`, one folder per system, on the nibOS card's NIBOS-DATA drive or on a
second card in TF2, exFAT or FAT32, named anything ([Which card](#which-card)). The folders are
the ones the DS+'s stock system uses, so a games card you already have works as it is. DSlot
makes the folder of every system it has an emulator for, each with a `_README.txt` saying what goes in
it; nothing on a card is ever renamed, moved or deleted.

| System | Folder | Files | Plays in | BIOS (in `BIOS/`) |
|---|---|---|---|---|
| Nintendo DS | `Roms/NDS` | `.nds`, `.zip` | DSperate | None needed |
| Game Boy Advance | `Roms/GBA` | `.gba`, `.zip` | DSperate | None needed |
| Game Boy | `Roms/GB` | `.gb`, `.zip` | inkdot | None |
| Game Boy Color | `Roms/GBC` | `.gbc`, `.zip` | inkdot | None |
| SNES / Super Famicom | `Roms/SFC` | `.sfc`, `.smc`, `.zip` | nibcase (Snes9x) | None |
| NES / Famicom | `Roms/FC` | `.nes`, `.unf`, `.unif`, `.zip` | nibcase (Nestopia UE) | None |
| Famicom Disk System | `Roms/FDS` | `.fds` | nibcase (Nestopia UE) | `disksys.rom`, required |
| Mega Drive / Genesis | `Roms/MD` | `.md`, `.gen`, `.bin`, `.smd`, `.zip` | nibcase (BlastEm) | None |
| Master System | `Roms/SMS` | `.sms`, `.zip` | nibcase (Gearsystem) | None |
| SG-1000 | `Roms/SG1000` | `.sg`, `.zip` | nibcase (Gearsystem) | None |
| Game Gear | `Roms/GG` | `.gg`, `.zip` | nibcase (Gearsystem) | None |
| PC Engine / TurboGrafx-16 | `Roms/PCE` | `.pce`, `.zip` | nibcase (Beetle PCE Fast) | None |
| PC Engine CD | `Roms/PCECD` | `.cue` with its tracks, `.chd` | nibcase (Beetle PCE Fast) | `syscard3.pce`, required |
| PlayStation | `Roms/PS` | `.chd`, `.cue` with its tracks, `.pbp`, `.m3u` | nibcase (PCSX ReARMed) | `scph5501.bin` and others, optional |
| Atari Lynx | `Roms/LYNX` | `.lnx`, `.zip` | nibcase (Handy) | `lynxboot.img`, required |
| Neo Geo Pocket (Color) | `Roms/NGP` | `.ngp`, `.ngc`, `.zip` | nibcase (Beetle NeoPop) | None |
| WonderSwan (Color) | `Roms/WS` | `.ws`, `.wsc`, `.zip` | nibcase (Beetle Cygne) | None |
| Game & Watch | `Roms/GW` | `.mgw` (nibcase); `gnw_*.zip`, `gnw_*.7z` (inktick, preview) | nibcase, inktick | None |
| Ports | `Roms/PORTS` | Installed by PortMaster | PortMaster | None |

- **Zipped games**: a cartridge game may be a `.zip` holding one game. Disc games (PC Engine CD,
  PlayStation) are never zipped.
- **Discs**: put a `.cue` with its `.bin` tracks beside it; DSlot lists the `.cue` and hides the
  tracks. A PlayStation game of several discs is an `.m3u`, a text file listing the discs, one
  file name a line:

  ```
  Game (USA) (Disc 1).chd
  Game (USA) (Disc 2).chd
  ```

  DSlot then shows the `.m3u` and hides the discs it lists.
- **Names**: the shelf shows a game by its file name, less what is in brackets
  (`Lantern Tide (USA) (Rev 1)` shows as `Lantern Tide`).
  DS games show the title stored in the game itself.

## BIOS files

A few systems need a BIOS file: a copy of the console's own start-up program. nibOS doesn't
come with any: bring your own, from your own console. Put them in `BIOS/` at the root
of either card, named exactly as below. A system that needs one won't start without it, and says
which file is missing and where it looked.

| File | For | Needed | MD5 |
|---|---|---|---|
| `disksys.rom` | Famicom Disk System | Yes | `ca30b50f880eb660a320674ed365ef7a` |
| `syscard3.pce` | PC Engine CD | Yes | `38179df8f4ac870017db21ebcbf53114` |
| `lynxboot.img` | Atari Lynx | Yes | `fcd403db69f54290b51035d82f835e7b` |
| `scph5501.bin` | PlayStation | No, recommended | `490f666e1afb15b7362b406ed1cea246` |
| `scph1001.bin`, `scph7001.bin`, `scph101.bin`, `PSXONPSP660.bin` | PlayStation | No | [nibcase's list](https://github.com/abradburne/nibcase/blob/main/docs/systems.md#bios) |

Without a PlayStation BIOS, the emulator's own replacement plays most games, and the game's menu
says which file to add. The DS and GBA need no BIOS: DSperate has its own replacements built in.

## Saves

Every game's saves are kept together in one folder, `Saves/<folder>/<game>/`, on the
NIBOS-DATA partition of the nibOS card ([Which card](#which-card)): its battery save (the game's own save, as the cartridge kept it), its
clock, its save states and its resume point. A game is known by its system folder and its file
name, so moving a game between cards, or between `Roms/` and a slot CFW `Games/` folder, keeps
its saves.

| File | What |
|---|---|
| `<game>.sav`, `<game>.srm` | The battery save. This is the one to keep: it is the game's own progress, and other emulators can read it. |
| `<game>.auto.state` and similar | The resume point: where you left the game. |
| `<game>.state1` … and similar | Save states, made from the game's menu. |

Save states are snapshots of one emulator's memory: they can't be loaded by another emulator, or
by a different version of the same one. Battery saves carry over anywhere.

To start a game again from the beginning, clear its resume point (DSlot's menu (X) → Game →
Clear resume state). **Delete saves** in the same place deletes everything in the game's saves
folder, after asking twice.

**Writing a newer image** over the card keeps `Saves/`, `Roms/` and `BIOS/` on a card set up by
nibOS 0.1.0-alpha1 or later ([Updates](@/manual/updates.md)). Copying `Saves/` to your computer
first is still wise.

## Which card

The DS+ has two card slots. nibOS starts from the card in **TF1**; a second card in **TF2** is
optional.

- **Games** are found on both cards: `Roms/` on the nibOS card's NIBOS-DATA partition, and
  `Roms/` on the card in TF2. A game on both is listed once.
- **BIOS files** are found in `BIOS/` on either card.
- **Saves** always go in `Saves/` on NIBOS-DATA, on the nibOS card in TF1.
- A card in TF2 can be formatted **exFAT** or **FAT32** and named anything. On a card with
  several volumes, one named `DS` is the one read. FAT32 names in Japanese and other scripts read right.

## A card set up for slot CFW

A card set up for slot CFW works as it is, beside the stock layout, and nothing on it is moved:

| On a slot card | In nibOS |
|---|---|
| `Games/GBA`, `Games/GB`, `Games/GBC` | Read as game folders, after `Roms/`. |
| `Labels/<system>/<game>.png` (Cart Studio's labels) | The carts' labels. |
| `Labels/cart_shell.txt` | The carts' shape, colour and finish. |
| `BIOS/` | The same folder nibOS's emulators use. |

**Battery saves**: slot's aren't picked up by themselves yet, except for Game Boy and Game Boy
Color games, whose `.sav` beside the game is copied in the first time the game starts. For a GBA
game, copy its `.sav` into `Saves/GBA/<game>/` yourself, named after the game file
(`<game>.sav`). Save states don't carry over between slot and nibOS. Details:
[DSlot's slot card guide](https://github.com/abradburne/DSlot/blob/main/docs/slot-cards.md).

## Box art

Optional: see [The DSlot shelf](@/manual/shelf.md#carts-boxes-and-lists).
