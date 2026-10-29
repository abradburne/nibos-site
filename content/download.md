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

The first beta, released {{ r.date }}: nibOS 0.1.0's features are all in, and the betas from
here to 0.1.0 bring fixes. For the **Anbernic RG DS+** only. A DS+ on 0.1.0-alpha1 to alpha6
can take it as an [update](@/manual/updates.md) instead of a new card. Write an image
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
  PortMaster support (PortMaster itself downloads on first use).
- **The base edition**: a console on the top screen, with SSH and Wi-Fi at boot.
- **Not in it**: games and BIOS files. Bring your own.

## Release notes

What changed since 0.1.0-alpha6:

- **RetroAchievements on seven more systems.** Game Boy Advance in DSperate, and SNES, NES, Mega
  Drive, Game Gear, Atari Lynx and PlayStation in nibcase, earn achievements (Casual), joining
  DS, Game Boy and Game Boy Color. Sign in once from DSlot's Achievements page and play.
- **DSlot 0.5.0.** The menu's longer pages come in sections under the tabs, moved through with
  L2 / R2 or a tap; Wi-Fi and Bluetooth share one **Network** tab. Carts flicked on the shelf
  glide on and settle on a cart. **Earned achievements** lists everything you have unlocked,
  the latest first.
- **Choose when a sleeping device powers off:** DSlot's menu → System → Power → **Power off when
  asleep**. With the lid closed, the DS+ powers off at that time and stays off.
- **Deep sleep draws less:** 49 mA asleep, from 52 mA.
- **Mega Drive buttons match the console's pad:** Y, B and A are A, B and C; X, L and R are X, Y
  and Z; Select is Mode.
- **Updated systems use their whole partition:** a DS+ updated from an alpha gets 1.3 GB back on
  its first start of this release.

The alphas' notes are on their release pages:
[0.1.0-alpha6](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha6),
[0.1.0-alpha5](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha5),
[0.1.0-alpha4](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha4),
[0.1.0-alpha3](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha3),
[0.1.0-alpha2](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha2),
[0.1.0-alpha1](https://github.com/abradburne/nibos/releases/tag/v0.1.0-alpha1).

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
| DSlot | [abradburne/DSlot](https://github.com/abradburne/DSlot/tree/v0.5.0) at `v0.5.0` |
| DSperate | [abradburne/DSperate](https://github.com/abradburne/DSperate/tree/00f759d) at `00f759d` |
| inkdot | [abradburne/inkdot](https://github.com/abradburne/inkdot/tree/1ecf49f) at `1ecf49f` |
| nibcase | [abradburne/nibcase](https://github.com/abradburne/nibcase/tree/afcbf36) at `afcbf36` |
| inktick | [abradburne/inktick](https://github.com/abradburne/inktick/tree/9ad1e00) at `9ad1e00` |
| nibkit | [abradburne/nibkit](https://github.com/abradburne/nibkit), at the tags each project pins (DSlot: `v0.3.0`) |
| Arch Linux ARM packages | The source packages of the GPL and LGPL packages in `packages.txt`, attached to the [release]({{ r.url }}) |

The kernel is mainline Linux at `0fcb05b` with the patches in nibOS's `kernel/`,
`socs/rk3568/kernel/` and `boards/rg-ds-plus/kernel/`; U-Boot is v2026.10 with the patches in
`uboot/`, `socs/rk3568/uboot/` and `boards/rg-ds-plus/uboot/`.
