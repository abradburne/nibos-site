+++
title = "The console and the base edition"
description = "The Linux console on the DS+: the touch keyboard, SSH, copying files, nib, installing software, and the base edition."
weight = 10
+++

Underneath both editions is the same Linux system: Arch Linux ARM, with nibOS's own hardware
layer. The console is a way into it.

## Getting to the console

- **The base edition** starts into it.
- **On the DSlot edition**, leave DSlot with **Select + Start**. To go back to the shelf, restart
  (`sudo reboot`). The safe mode's **Open a console** leads here too.
- **Over SSH**, from a computer (below).

On the DS+'s screens, the console is on the top screen and a touch keyboard on the bottom one.
The buttons type too; **Menu + X** hides the keyboard and shows it again. Every key is in
[Controls](@/manual/controls.md#in-the-console-keyboard-on-the-bottom-screen).

The user is called `nibos`. With no password set in `provision.toml`, the console logs in by
itself and `sudo` asks for nothing; with one, both ask for it.

> [!WARNING]
> With no password, anyone holding the DS+ has full control of it. Set one in
> `provision.toml`, or with `passwd` in the console, before you take it anywhere that matters.

## SSH

SSH is off until `provision.toml` gives it a public key; there is no password login over SSH.
With a key given and Wi-Fi on, from a computer on the same network:

```sh
ssh nibos@nibos.local
```

`nibos.local` is the DS+'s name on the local network (every nibOS device has this name). If your computer doesn't find it, use the
DS+'s address instead (`ip addr` in the console shows it).

Wi-Fi has to be on: on a fresh card it is off unless `provision.toml` named a network. Turn it
on with `nib wifi on` in the console, or in DSlot's menu on the DSlot edition; it stays on.

## Copying files

With SSH, any program that speaks SFTP or SCP copies files to and from the DS+: `scp` in a
terminal, or a file manager that connects over SFTP. Games go in `/mnt/roms/Roms/<folder>`
(NIBOS-DATA) or `/mnt/ds/Roms/<folder>` (the card in TF2):

```sh
scp "My Game.gba" nibos@nibos.local:/mnt/roms/Roms/GBA/
```

DSlot notices them by itself.

## nib

`nib` is nibOS's command for the device. `nib help` lists what this DS+ has; the common ones:

| Command | Does |
|---|---|
| `nib update check` / `download` / `apply` / `rollback` | System updates ([Updates](@/manual/updates.md)). |
| `nib battery` | The charge, and battery protect. `nib battery protect on` / `off`. |
| `nib brightness` | Each screen's brightness. `nib brightness top 40`, `bottom`, `all`. |
| `nib wifi on` / `off` / `status` | The Wi-Fi radio. |
| `nib bluetooth on` / `off` | The Bluetooth radio. |
| `nib net status` | Whether the network is up, and when it comes up. |
| `sudo nib net mode boot` / `deferred` / `demand` | When the network comes up from the next start: with the system, once start-up has finished, or only when something asks for it. |
| `nib lid sleep` / `ignore` | Whether closing the lid sleeps. |
| `nib audio` | Which speaker tuning is in use. `sudo nib audio import-tuning` imports the official one from your own stock card or image. |
| `sudo nib boot-ui on` / `off` | Start into DSlot, or into the console. |

## Installing software

nibOS is Arch Linux ARM, so `sudo pacman -S <package>` installs from Arch Linux ARM's
repositories. Two things to know in the alpha:

- nibOS's own packages (its kernel, hardware layer, graphics, DSlot and the emulators) are
  built for nibOS and aren't in a repository yet. Don't replace them from Arch Linux ARM's
  (`mesa`, for one).
- A full system upgrade (`pacman -Syu`) moves you onto packages nibOS hasn't been tested with.
  It usually works; if it doesn't, write the image again ([Updates](@/manual/updates.md)).
- **A nibOS update replaces the whole system**, so packages you installed with `pacman`, and any
  other change to the system's files outside your home folder, are gone after it. Keep what
  you need in your home folder, which is kept, and install packages again after an update.

## The base edition

The base edition is the same system without DSlot and the emulators: it starts into the console
in about 5 seconds, brings the network up at every start once Wi-Fi is on, and is meant to be
used as a small Linux computer, over SSH or with a keyboard. DSlot can't be added to it: for
games, write the DSlot edition over it, which keeps your games and saves
([Updates](@/manual/updates.md#writing-a-new-image-instead)).

Building programs for nibOS, both screens, the buttons and touch: the
[app developer's guide](https://github.com/abradburne/nibos/blob/main/AGENTS.md) and the
[template app](https://github.com/abradburne/nibos/tree/main/sdk/template).
