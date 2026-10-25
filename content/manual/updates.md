+++
title = "Updates"
description = "Updating from DSlot or the console, what an update keeps, going back to the previous version, and writing a new image instead."
weight = 9
+++

nibOS updates itself from its releases on GitHub, over Wi-Fi. An update replaces the whole
system in one piece; **your games, saves and settings stay**.

## How an update works

The card holds two copies of the system, **A** and **B**. One runs; the other is spare.

1. An update is downloaded and written into the spare copy, while you carry on using the DS+.
   The copy that is running is never written, so a power cut, a lost connection or a bad
   download at any point leaves the DS+ starting what it started before.
2. Every piece is checked against the release's signed list, as it is written and again after,
   and an update that isn't signed with nibOS's key is refused before anything is written.
3. You restart into the new version. If it reaches its shelf (or the console) and is still
   running 30 seconds later, it is kept.
4. If it doesn't start three times running, or lands in the safe mode, the DS+ goes back to the
   version it came from, by itself.

An update needs Wi-Fi, and the battery at 30% or more (or the charger in).

## What an update keeps

| Kept | Not kept |
|---|---|
| Games, BIOS files and saves (NIBOS-DATA) | **Your password**, if you set one (below) |
| Your home folder: DSlot's and the emulators' settings, play times, ratings, `~/.ssh` | Packages you installed with `pacman` |
| Wi-Fi networks (also those joined in DSlot), Bluetooth pairings, and the radios on or off | Any other change to the system's files outside your home folder |
| The SSH keys from `provision.toml`, and the device's own SSH host keys | |
| Brightness, the lid setting, battery protect, an imported speaker tuning | |

> [!WARNING]
> **A password isn't kept by an update** in this release, whether you set it with `passwd` or in
> `provision.toml`: after an update the device has no password again, and the console logs in by
> itself. Set it again with `passwd`. This will be fixed in a later release.

## From DSlot

Press **X** for the menu and go to the **Update** page. It shows the version and edition
running, and the channel (Stable or Beta).

- **Update** checks for a newer version. If there is one, the row reads **Download (N MB)** and
  the line above says which version; **What's new** shows its notes.
- The download runs in the background: the shelf and games carry on. **A** pauses it and
  resumes it.
- When it is in, **Restart to update** (A, then A again) restarts into it.
- After the update, DSlot opens on the Update page once, saying "Updated to nibOS …", or, if the
  new version didn't start and the DS+ went back, which version it is on.
- **Go back to the previous version** (A twice) is offered while the other copy holds a good one.

A problem (no network, the battery low, a damaged download) is said on the page, and **Try
again** repeats the step. "No updates published yet" means there is no newer release for your
DS+: it isn't an error. {{ config.extra.release.version }} is the first release, so that is what
it says for now.

## From the console

```sh
nib update check       # is there a newer version?
nib update download    # fetch it, in the background; the DS+ stays usable
nib update apply       # restart into it
nib update rollback    # back to the previous version
```

## Writing a new image instead

You can also update by writing the newer image to the card, as you did to
[install](@/manual/install.md). On a card set up by **nibOS 0.1.0-alpha1 or later** this keeps
the NIBOS-DATA partition, so your games and saves stay. Everything else is reset: the system's
settings, the Wi-Fi networks you joined, your paired Bluetooth devices, and what
`provision.toml` set. If you used a `provision.toml` (for an SSH key), put it on the NIBOS drive
again.

> [!WARNING]
> A card set up by anything older than 0.1.0-alpha1 (the test builds before the first release)
> is **erased once**, games and saves included. Copying your `Saves/` folder to your computer
> first is wise either way.

## Going back by hand

DSlot's **Go back to the previous version**, or `nib update rollback` in the console, starts the
other copy again, as long as it holds a version that ran well. In the console,
`sudo nibos-bootctl status` shows which copy is running and how its last starts went.
