+++
title = "Questions"
description = "Common questions about nibOS: devices, safety, games, the stock system, updates and AI."
+++

## Which devices does it run on?

The **Anbernic RG DS+** only, for now. nibOS is laid out so that other handhelds can be added,
one board at a time, done thoroughly; the next ones aren't decided.

## Can installing it harm my DS+?

No. The RG DS+ starts from the card in its TF1 slot, and nibOS writes only to its own card:
nothing on the device is changed. Take the nibOS card out and put the stock card back, and you
have the stock system again.

## Do I lose the stock system?

Not if you use a separate card for nibOS, which is what the manual suggests. Writing the nibOS
image erases the card it is written to; keep your stock card as it is.

## Does it come with games?

No. nibOS includes no games, no BIOS files and no artwork from any game. Play games you own, or
the free homebrew games made for these systems. Pictures on this site use made-up games.

## Which systems does it play?

DS, Game Boy Advance, Game Boy, Game Boy Color, SNES, NES, Famicom Disk System, Mega Drive,
Master System, SG-1000, Game Gear, PC Engine and PC Engine CD, PlayStation, Atari Lynx, Neo Geo
Pocket, WonderSwan and Game & Watch, and PortMaster's ports. The folders and file types for each
are in [Games, BIOS and saves](@/manual/games.md).

## Can I use my existing games card?

Yes. nibOS uses the same `Roms/` folders as the stock system, so a games card works as it is in
TF2, as long as it is exFAT and labelled `DS`; so does a card set up for slot CFW. Saves made by other emulators may need copying across:
battery saves carry over, save states don't.

## Is it fast?

A picture on both screens 1.5 seconds after the power button, the shelf at about 5 seconds; a
game from the shelf in about 2 seconds, and back in under one.

## How long does the battery last?

That depends on what you play and how bright the screens are; nibOS doesn't yet publish a
figure it has measured. Wi-Fi off, a lower brightness and sleep (close the lid) all help.
[Sleep, charging and the battery](@/manual/power.md).

## How do I update it?

Over Wi-Fi: DSlot's menu → **Update**, or `nib update` in the console. An update replaces the
whole system in one piece and keeps your games, saves and settings; if the new version doesn't
start, the DS+ goes back to the old one by itself. [Updates](@/manual/updates.md).

## Is it a full Linux system?

Yes: Arch Linux ARM with systemd, a console with a touch keyboard, SSH, `pacman`. The
[base edition](@/manual/console.md#the-base-edition) starts into the console instead of the
game shelf.

## Can I write apps for it?

Yes. nibkit, the SDK, gives an app both screens, the buttons, touch, brightness, sound and
settings, and DSlot's menu; a template app runs on the device as it is. See
[Apps](@/apps.md#writing-your-own).

## Was it made with AI?

Yes, openly. nibOS, DSlot and the emulators were written by AI agents (Claude, in Claude Code),
several at a time, steered by a person who decided what mattered and tested every change on a
real RG DS+. Nothing is claimed to work that wasn't run on the device, and the history of every
decision, with the measurements behind it, is kept in the repositories. Contributions made with
AI are welcome under the same rules as any other ([Contributing](@/contributing.md)).

## Where do I report a bug?

On the issue tracker of the project it's in; if you aren't sure which,
[nibOS's](https://github.com/abradburne/nibos/issues). Include the log
from the card: [Reporting a bug](@/manual/troubleshooting.md#reporting-a-bug).
