+++
title = "Updates"
description = "Updating from the console, what an update keeps, going back to the previous version, and writing a new image instead."
weight = 7
+++

nibOS updates itself from its releases on GitHub, over Wi-Fi. An update replaces the whole
system in one piece; **your home folder, data and settings stay**.

## How an update works

The card holds two copies of the system, **A** and **B**. One runs; the other is spare.

1. An update is downloaded and written into the spare copy, while you carry on using the DS+.
   The running copy is never touched, so a power cut or a dropped connection can't break
   anything.
2. Every piece is checked against the release's signed list, as it is written and again after,
   and an update that isn't signed with nibOS's key is refused before anything is written.
3. You restart into the new version. If it reaches the console and is still running 30
   seconds later, it is kept.
4. If it doesn't start three times running, or lands in the safe mode, the DS+ goes back to the
   version it came from, by itself.

An update needs Wi-Fi, and the battery at 30% or more (or the charger in).

## What an update keeps

| Kept | Not kept |
|---|---|
| Everything on NIBOS-DATA (`/mnt/roms`) | Packages you installed with `pacman` |
| Your home folder, `~/.ssh` included | Any other change to the system's files outside your home folder |
| Wi-Fi networks, Bluetooth pairings, and the radios on or off | |
| The SSH keys from `provision.toml`, and the device's own SSH host keys | |
| Brightness, the lid setting, battery protect, the network mode, the time zone, an imported speaker tuning | |
| Your password, set with `passwd` or in `provision.toml` | |

## From the console

```sh
nib update check       # is there a newer version?
nib update download    # fetch it, in the background; the DS+ stays usable
nib update apply       # restart into it
nib update rollback    # back to the previous version
```

`nib update` alone shows where an update stands: its second line is the status, and the new
version's notes follow it. A problem (no network, the battery low, a damaged download) is said
there, and running the same step again carries on.

## Writing a new image instead

You can also update by writing the newer image to the card, as you did to
[install](@/manual/install.md). On a card set up by **nibOS 0.1.0-alpha1 or later** this keeps
the NIBOS-DATA partition, so what is on it stays, and from **0.1.0-alpha6** the settings in your
home folder's `.config` too: nibOS keeps a copy of it on NIBOS-DATA (`nibos/settings/`) and
puts it back the first time the new card starts. The rest of your home folder, `~/.ssh`
included, isn't kept: copy what you need off the card first. Reset are the Wi-Fi networks you joined, your paired Bluetooth devices and
what `provision.toml` set. To start with default settings, delete `nibos/settings/` on the
NIBOS-DATA drive before writing the image. If you used a `provision.toml` (for an SSH key), put it on the NIBOS drive
again.

## Switching to DSlot

An update keeps a card what it is: nibOS stays nibOS. To play games, write
[DSlot's image]({{ config.extra.dslot_site }}/download/) over the card the same way; it is nibOS
with DSlot on top, and it keeps NIBOS-DATA as above. Going back is writing nibOS's image again.

## Going back by hand

`nib update rollback` starts the other copy again, as long as it holds a version that ran well. In the console,
`sudo nibos-bootctl status` shows which copy is running and how its last starts went.
