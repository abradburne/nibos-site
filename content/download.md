+++
title = "Download"
description = "The nibOS image for the Anbernic RG DS+, how to check it, the release notes, licences and source."
+++

{% set r = config.extra.release %}
{% set ds = config.extra.dslot_site %}
{% if not r.published %}
> [!NOTE]
> nibOS {{ r.version }} isn't published yet.
{% endif %}

> [!TIP]
> **Here to play games?** This image starts into a Linux console. The game shelf and its
> emulators are [DSlot]({{ ds }}/), which has [its own image]({{ ds }}/download/), nibOS
> included.

## nibOS {{ r.version }}

The second beta, released {{ r.date }}: nibOS 0.1.0's features are all in, and the betas from
here to 0.1.0 bring fixes. For the **Anbernic RG DS+** only. A DS+ running nibOS's image
(0.1.0-alpha1 or later) can take it as an [update](@/manual/updates.md) instead of a new card.
Write the image to a microSD card of 16 GB or more with Raspberry Pi Imager or `dd`, or with
balenaEtcher once it is unpacked: [Installing](@/manual/install.md) has every step.

{{ <release_images release={r} /> }}

Every file of the release, with the release notes, is on its
[GitHub release page]({{ r.url }}). The same release carries DSlot's image, which is offered on
[DSlot's site]({{ ds }}/download/).

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
What is signed is each image's **update manifest**, which lists the checksum of the update
payload and of every 16 MiB piece of it. A device takes an update only if that signature checks
out. To check a manifest yourself:

```sh
minisign -Vm nibos-{{ r.version }}-rgds.manifest.json -P {{ r.public_key }}
```

The `.manifest.json`, `.manifest.json.minisig` and `.slot` files are what a device's updater
downloads (nibOS's are the `nibos-…-rgds.*` ones; `-rgds-dslot` is DSlot's); to write a card,
use the `.img.xz`.

## What's in it

- **nibOS**: mainline U-Boot v2026.10 (SPL in Falcon mode: the kernel 0.65 s after reset),
  mainline Linux 7.3-rc7 with nibOS's patches, Arch Linux ARM, nibOS's hardware layer, the safe
  mode, the start-up and goodbye pictures, and the updater.
- **The console**: on the top screen, with the touch keyboard on the bottom one; SSH (with a
  key from `provision.toml`) and Wi-Fi at boot.
- **Not in it**: DSlot and the emulators, which are on [DSlot's image]({{ ds }}/download/).

## Release notes

What changed since 0.1.0-beta2:

- **The power key starts the DS+ after a power-off.** Since beta1 it could stay dark until the
  power key was held for a reset; a tap now starts it (the PMIC's sleep line is routed only
  while asleep).
- **Asleep too long, it really powers off**, instead of going back to sleep every hour.
- **Help files**: `/usr/share/nibos/help/` and this release's `/usr/share/nibos/whats-new.txt`,
  which DSlot's System → Help and nibkit 0.5's `guide` show.

[0.1.0-beta2](https://github.com/abradburne/nibos/releases/tag/v0.1.0-beta2) brought the
updater's step-by-step status, the volume and brightness announcements and two Panfrost fixes.
[0.1.0-beta1](https://github.com/abradburne/nibos/releases/tag/v0.1.0-beta1) brought power off
when asleep (`sudo nib sleep off-after`), deep sleep at 49 mA, and the whole system partition
for updated devices.

What changed in DSlot and the emulators is on [DSlot's download page]({{ ds }}/download/#release-notes).
The earlier releases' notes are on their release pages:
[0.1.0-beta2](https://github.com/abradburne/nibos/releases/tag/v0.1.0-beta2),
[0.1.0-beta1](https://github.com/abradburne/nibos/releases/tag/v0.1.0-beta1),
[0.1.0-alpha6](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha6),
[0.1.0-alpha5](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha5),
[0.1.0-alpha4](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha4),
[0.1.0-alpha3](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha3),
[0.1.0-alpha2](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha2),
[0.1.0-alpha1](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha1).

What isn't finished: [Known issues](@/manual/known-issues.md). Every change, day by day:
nibOS's [changelog](https://github.com/abradburne/nibos/blob/{{ r.tag }}/CHANGELOG.md).

## Licences and source

The image carries, on its NIBOS partition:

- `NOTICE`: every component, its version and licence; the non-free firmware named as such;
  the written source offer.
- `packages.txt`: every Arch Linux ARM package in the image, with its version and licence.
- `licenses/`: the licence texts that no package installs.

nibOS's own code is under the GNU GPL, version 3 or later ([Licences](@/licences.md)).

**Source code.** The complete corresponding source for the GPL and LGPL software in this
image, and for at least three years after this release was last offered:

| Part | Source |
|---|---|
| nibOS: kernel and U-Boot patches, device tree, hardware layer, tools | [abradburne/nibos](https://github.com/abradburne/nibos/tree/{{ r.tag }}) at `{{ r.tag }}` |
| Arch Linux ARM packages | The source packages of the GPL and LGPL packages in `packages.txt`, attached to the [release]({{ r.url }}) |

DSlot's image adds DSlot, its emulators and nibkit, whose sources are listed on
[its download page]({{ ds }}/download/#licences-and-source).

The kernel is mainline Linux at `0fcb05b` with the patches in nibOS's `kernel/`,
`socs/rk3568/kernel/` and `boards/rg-ds-plus/kernel/`; U-Boot is v2026.10 with the patches in
`uboot/`, `socs/rk3568/uboot/` and `boards/rg-ds-plus/uboot/`.
