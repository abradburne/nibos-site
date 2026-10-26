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

The second alpha, released {{ r.date }}. For the **Anbernic RG DS+** only. A DS+ on
0.1.0-alpha1 can take it as an [update](@/manual/updates.md) instead of a new card. Write an image
to a microSD card of 16 GB or more with Raspberry Pi Imager or `dd`, or with balenaEtcher
once the image is unpacked: [Installing](@/manual/install.md) has every step. Both editions have the same system
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

What changed since 0.1.0-alpha1:

- **The first update over the air.** A DS+ on 0.1.0-alpha1 is offered this release on DSlot's
  Update page (X → System → Update), and `nib update` in the console. Games, saves and
  settings stay; a password set on alpha1 is kept too.
- **Starting with no card in TF2 no longer takes minutes.** The second card is mounted the
  moment it is put in and let go when it is taken out, and the shelf leaves it out when the
  slot is empty.
- **A game that comes straight back says why.** When an emulator stops at once, the shelf
  shows a notice with the emulator's own last line, and offers **Y: send a bug report**.
- **Bug reports from the device.** A copy of the start's log, with Wi-Fi names, passphrases,
  addresses and the hostname taken out, saved on the card as `nibos/bug-report-<date>.txt` and,
  with Wi-Fi on, sent to nibOS's bug tracker; the shelf shows a report code to quote
  ([What to do if…](@/manual/troubleshooting.md#reporting-a-bug)).
- **A card that wasn't written right says so.** About a minute after the first start, nibOS
  checks every file the image shipped and, if the card was written wrongly, says so on the
  shelf ([What to do if…](@/manual/troubleshooting.md#this-card-was-not-written-correctly)).
- DSlot 0.3.1 and nibkit 0.1.1.

The first alpha's notes are on its [release page](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha1).

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
| DSlot | [abradburne/DSlot](https://github.com/abradburne/DSlot/tree/e224fc5) at `e224fc5` |
| DSperate | [abradburne/DSperate](https://github.com/abradburne/DSperate/tree/7c88c8f) at `7c88c8f` |
| inkdot | [abradburne/inkdot](https://github.com/abradburne/inkdot/tree/ba0f50c) at `ba0f50c` |
| nibcase | [abradburne/nibcase](https://github.com/abradburne/nibcase) |
| inktick | [abradburne/inktick](https://github.com/abradburne/inktick) |
| nibkit | [abradburne/nibkit](https://github.com/abradburne/nibkit/tree/v0.1.1) at `v0.1.1` |
| Arch Linux ARM packages | The source packages of the GPL and LGPL packages in `packages.txt`, attached to the [release]({{ r.url }}) |

The kernel is mainline Linux at `0fcb05b` with the patches in nibOS's `kernel/`,
`socs/rk3568/kernel/` and `boards/rg-ds-plus/kernel/`; U-Boot is v2026.10 with the patches in
`uboot/`, `socs/rk3568/uboot/` and `boards/rg-ds-plus/uboot/`.
