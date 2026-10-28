+++
title = "First start"
description = "What the first start does, how long it takes, and putting your first games on the card."
weight = 2
+++

## What you see

1. About **1.5 seconds** after the power button, the DSlot logo is on the top screen.
2. The **first start only**: nibOS makes the games partition, **NIBOS-DATA**, over the rest of
   the card, and formats it. It takes a few seconds more than later starts. If the power goes
   while it is doing this, it carries on where it stopped at the next start.
3. If you wrote a `provision.toml`, it is applied now (or rejected, with the reason on the
   NIBOS partition: [Installing](@/manual/install.md#optional-an-ssh-key-provision-toml)).
4. The **DSlot edition** shows the shelf on both screens, about 5 seconds after power-on on later
   starts. The **base edition** shows a console on the top screen and a keyboard on the bottom
   one.

On a fresh card **Wi-Fi and Bluetooth are off**, except that Wi-Fi comes on by itself when
`provision.toml` named a network. Turn them on in DSlot's menu, or with `nib wifi on` and
`nib bluetooth on` in the console. Each radio then stays as you leave it, across restarts. On
the DSlot edition the network comes up only when something needs it, saving battery; on the
base edition it comes up at every start.

## Putting games on the card

A new card has no games, so the shelf has nothing to show yet. To add some:

1. Turn the DS+ off (hold power, then **Power off**) and put the card in your computer. It
   shows a drive called **NIBOS-DATA**.
2. Copy your games into the right folder under `Roms`: DS games in `Roms/NDS`, Game Boy Advance
   in `Roms/GBA`, and so on. The full list, with the BIOS files some systems need, is in
   [Games, BIOS and saves](@/manual/games.md).
3. Eject the card, put it back in TF1, and turn the DS+ on.

DSlot makes a folder for every system it has an emulator for, each with a `_README.txt` saying
what goes in it, which BIOS it needs and where its saves go. Its first start after you add
games reads every new game once to make its cart and box; later starts are quick.

You can also copy games while nibOS runs, over the network ([The console and the base
edition](@/manual/console.md#copying-files)), or put them on a second card in TF2; a game
copied onto a card appears on its page about a second after the copy finishes.

## Then

- [The DSlot shelf](@/manual/shelf.md): finding your way around.
- [Controls](@/manual/controls.md): every button, everywhere.
- [Wi-Fi and Bluetooth](@/manual/connections.md): joining a network, pairing headphones.
