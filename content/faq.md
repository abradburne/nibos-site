+++
title = "Questions"
description = "Common questions about nibOS: what it is, DSlot, devices, safety, the stock system, updates, software and AI."
+++

## What is nibOS?

A Linux system of its own for the **Anbernic RG DS+**: mainline Linux and U-Boot, Arch Linux
ARM, and a hardware layer that makes the DS+'s two screens, buttons, sound, sleep and charging
work. Its image starts into a console on the top screen with a touch keyboard on the bottom
one, for using the DS+ as a small Linux computer and building programs for it.

## I want to play games. Is this what I need?

You want **[DSlot]({{ config.extra.dslot_site }}/)**: the game system built on nibOS, with a game
shelf on both screens and emulators for eighteen systems. It has its own image, which includes
nibOS, and its own manual. nibOS's image has no shelf and no emulators.

## Which devices does it run on?

The **Anbernic RG DS+**, for now. nibOS is built to grow to more handhelds.

## Can installing it harm my DS+?

No. nibOS lives entirely on its own card and never touches the device. Put the stock card
back and you're on stock again.

## Do I lose the stock system?

No. Write nibOS to a card of its own and keep your stock card as it is.

## Is it a full Linux system?

Yes: Arch Linux ARM with systemd, `pacman`, SSH and a full userland, on a 64-bit ARM processor
with the open Panfrost GPU driver in the kernel. [The console](@/manual/console.md).

## Is it fast?

A picture on both screens 1.5 seconds after the power button, the console at about 5 seconds:
the bootloader's first stage starts the kernel 0.65 seconds after reset.

## How do I update it?

`nib update check`, `download`, `apply`. An update replaces the whole system in one piece and
keeps your home folder, data and settings; if the new version doesn't start, the DS+ goes back
to the old one by itself. Packages added with `pacman` need installing again after it.
[Updates](@/manual/updates.md).

## Can I add DSlot to it later?

Not with `pacman`: DSlot and its emulators aren't in a package repository yet. Write
[DSlot's image]({{ config.extra.dslot_site }}/download/) over the card instead; it keeps the
NIBOS-DATA partition.

## Can I write programs for it?

Yes. Anything that builds for 64-bit ARM Linux runs. nibkit, the SDK, gives a program both
screens, the buttons, touch, brightness, sound and settings; a template app runs on the device
as it is. See [Projects](@/apps.md#writing-your-own).

## Was it made with AI?

Yes. nibOS was written by AI agents (Claude, in Claude Code), directed by one person and run on
a real RG DS+ throughout. Contributions made with AI are welcome
([Contributing](@/contributing.md)).

## Where do I report a bug?

On [nibOS's issue tracker](https://github.com/abradburne/nibos/issues). Include the log from
the card: [Reporting a bug](@/manual/troubleshooting.md#reporting-a-bug).
