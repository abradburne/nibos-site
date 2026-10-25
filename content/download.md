+++
title = "Download"
description = "nibOS images for the Anbernic RG DS+, how to check them, the release notes, licences and source."
+++

{% set r = config.extra.release %}
{% if not r.published %}
> [!NOTE]
> nibOS {{ r.version }} isn't published yet.
{% endif %}

## nibOS {{ r.version }}

The first public build, released {{ r.date }}. For the **Anbernic RG DS+** only. Write an image
to a microSD card of 16 GB or more with balenaEtcher, Raspberry Pi Imager or `dd`:
[Installing](@/manual/install.md) has every step. Both editions have the same system
underneath, and either can be written over the other.

{{ <release_images release={r} /> }}

Every file of the release, with the release notes, is on its
[GitHub release page]({{ r.url }}).

## Checking the download

**`SHA256SUMS`** lists the SHA-256 checksum of every file in the release. Download it beside
your image, then, in that folder:

```sh
sha256sum -c SHA256SUMS --ignore-missing          # Linux
shasum -a 256 -c SHA256SUMS --ignore-missing      # macOS
```

Each file you have should say `OK`. On Windows, `Get-FileHash <file>` in PowerShell prints the
checksum to compare with the cards above. A file that doesn't match: download it again, and
don't write it.

**Signatures.** Releases are signed with nibOS's update key, a
[minisign](https://jedisct1.github.io/minisign/) Ed25519 key with key ID
**{{ r.key_id }}**:

```
untrusted comment: minisign public key {{ r.key_id }}
{{ r.public_key }}
```

The same key is in every image (`/usr/lib/nibos/update.pub`) and in the nibOS repository
([`hw/files/usr/lib/nibos/update.pub`](https://github.com/abradburne/nibos/blob/{{ r.tag }}/hw/files/usr/lib/nibos/update.pub)).
What is signed is each edition's **update manifest**, which lists the checksum of the update
payload and of every 16 MiB piece of it. A device takes an update only if that signature checks
out. To check a manifest yourself:

```sh
minisign -Vm nibos-{{ r.version }}-rgds-dslot.manifest.json -P {{ r.public_key }}
```

The `.manifest.json`, `.manifest.json.minisig` and `.slot` files are what a device's updater
downloads; to write a card, use the `.img.xz`.

## What's in it

- **nibOS**: mainline U-Boot v2026.10 (SPL in Falcon mode: the kernel 0.65 s after reset),
  mainline Linux 7.3-rc7 with nibOS's patches, Arch Linux ARM, nibOS's hardware layer, the safe
  mode, the start-up and goodbye pictures, and the updater.
- **The DSlot edition** adds DSlot, DSperate (DS, GBA), inkdot (Game Boy, Game Boy Color),
  nibcase with its emulator cores (SNES, NES, Famicom Disk System, Mega Drive, Master System,
  SG-1000, Game Gear, PC Engine and PC Engine CD, PlayStation, Atari Lynx, Neo Geo Pocket,
  WonderSwan, Game & Watch), inktick (Game & Watch, a preview), Mesa for the GPU, and nibOS's
  PortMaster support (PortMaster itself downloads on first use). Wi-Fi comes on only when you
  turn it on.
- **The base edition**: a console on the top screen, with SSH and Wi-Fi at boot.
- **Not in it**: games, BIOS files, the speakers' official tuning, and anything from the stock
  firmware.

## Release notes

The first public alpha. In short:

- **Images to write to a card**, with first-start setup from `provision.toml`: Wi-Fi, SSH keys,
  a password, the time zone.
- **DSlot** as the start-up screen, about 5 seconds from power-on: a page per system, the system
  picker and cards, resume points, Cart Studio labels and shells, Wi-Fi and Bluetooth settings,
  the power menu.
- **One menu** shared by DSlot and every emulator; saves for every system kept together in
  `Saves/`.
- **The whole board works**: both screens and touch, the buttons, speakers and headphones,
  Wi-Fi and Bluetooth, both card slots, USB, deep sleep with Wi-Fi back on wake, charging while
  off, battery protect.
- **Looks after itself**: a safe mode when DSlot fails, a watchdog that restarts a hung device,
  and two copies of the system so a bad update goes back by itself.
- **System updates**: signed releases written to the copy of the system that isn't running,
  from DSlot's Update page or `nib update`. Games, saves and settings stay. This is the first
  release, so there is nothing to update to yet: "No updates published yet" is expected.
- **The console** with an on-screen keyboard; PortMaster on request.

What isn't finished: [Known issues](@/manual/known-issues.md). Every change, day by day:
nibOS's [changelog](https://github.com/abradburne/nibos/blob/{{ r.tag }}/CHANGELOG.md).

## Licences and source

Each image carries, on its NIBOS partition:

- `NOTICE`: every component, its version and licence; the non-free firmware named as such;
  the written source offer.
- `packages.txt`: every Arch Linux ARM package in the image, with its version and licence.
- `licenses/`: the licence texts that no package installs.

nibOS's own code is under the GNU GPL, version 3 or later; nibkit and the emulators written for
nibOS are MIT or Apache-2.0 ([Licences](@/licences.md)). One emulator core, **Snes9x**, has a
non-commercial licence: the DSlot edition may not be sold, or included in anything sold.

**Source code.** The complete corresponding source for the GPL and LGPL software in these
images, and for at least three years after this release was last offered:

| Part | Source |
|---|---|
| nibOS: kernel and U-Boot patches, device tree, hardware layer, tools | [abradburne/nibos](https://github.com/abradburne/nibos/tree/{{ r.tag }}) at `{{ r.tag }}` |
| DSlot | [abradburne/DSlot](https://github.com/abradburne/DSlot) at `84d2f35` |
| DSperate | [abradburne/DSperate](https://github.com/abradburne/DSperate) at `fc88c53` |
| inkdot | [abradburne/inkdot](https://github.com/abradburne/inkdot) at `9c8d768` |
| nibcase | [abradburne/nibcase](https://github.com/abradburne/nibcase) |
| inktick | [abradburne/inktick](https://github.com/abradburne/inktick) |
| nibkit | [abradburne/nibkit](https://github.com/abradburne/nibkit) at `v0.1.0` |
| Arch Linux ARM packages | The source packages of the GPL and LGPL packages in `packages.txt`, attached to the [release]({{ r.url }}) |

The kernel is mainline Linux at `0fcb05b` with the patches in nibOS's `kernel/`,
`socs/rk3568/kernel/` and `boards/rg-ds-plus/kernel/`; U-Boot is v2026.10 with the patches in
`uboot/`, `socs/rk3568/uboot/` and `boards/rg-ds-plus/uboot/`.
