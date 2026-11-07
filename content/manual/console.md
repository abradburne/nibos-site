+++
title = "The console"
description = "The Linux console on the DS+: the touch keyboard, SSH, copying files, nib, installing software and building programs."
weight = 3
+++

nibOS is Arch Linux ARM, with nibOS's own hardware layer, and it starts into a console. There
are two ways in:

- **On the DS+'s screens**: the console is on the top screen and a touch keyboard on the bottom
  one.
- **Over SSH**, from a computer (below).

On a [DSlot]({{ config.extra.dslot_site }}/) card, the same console is under the game shelf:
leaving DSlot with **Select + Start** opens it.

## The keyboard

The top screen is the console and the bottom one a touch keyboard.
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
on with `nib wifi on` in the console; it stays on.

## Copying files

With SSH, any program that speaks SFTP or SCP copies files to and from the DS+: `scp` in a
terminal, or a file manager that connects over SFTP:

```sh
scp notes.txt nibos@nibos.local:
```

Your home folder (`/home/nibos`) is kept by updates. `/mnt/roms` is the NIBOS-DATA partition,
the part of the card any computer's card reader can read, and `/mnt/ds` a card in TF2 (exFAT or
FAT32).

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
| `nib clock` | The time and zone. `sudo nib clock zone Asia/Tokyo`, `sudo nib clock sync`, `sudo nib clock set '2026-10-27 11:30'`. |
| `nib sleep` | How long the DS+ sleeps on battery before it powers off. `sudo nib sleep off-after 15`, or `never`. |
| `nib bug-report` | Save this start's log, scrubbed, on the card; `send` sends it too ([Reporting a bug](@/manual/troubleshooting.md#reporting-a-bug)). |

## Installing software

nibOS is Arch Linux ARM, so `sudo pacman -S <package>` installs from Arch Linux ARM's
repositories. Worth knowing:

- nibOS's own packages (its kernel and hardware layer) are built for nibOS and aren't in a
  repository yet. Don't replace them from Arch Linux ARM's.
- A full system upgrade (`pacman -Syu`) moves you onto packages nibOS hasn't been tested with.
  It usually works; if it doesn't, write the image again ([Updates](@/manual/updates.md)).
- **A nibOS update replaces the whole system**, so packages you installed with `pacman`, and any
  other change to the system's files outside your home folder, are gone after it. Keep what
  you need in your home folder, which is kept, and install packages again after an update.

## Building for nibOS

Programs for the DS+ get both screens, the buttons by their printed labels, touch, brightness,
sound and settings from **nibkit**, the SDK, which builds the same program for nibOS, the stock
system or a desktop computer. Start from the
[template app](https://github.com/abradburne/nibos/tree/main/sdk/template) and the
[app developer's guide](https://github.com/abradburne/nibos/blob/main/AGENTS.md), which is
written for people and AI agents alike. [Projects](@/apps.md) has the rest.
