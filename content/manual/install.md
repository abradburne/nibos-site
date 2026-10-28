+++
title = "Installing"
description = "Download an image, check it, write it to a microSD card and start the DS+; and, for SSH, provision.toml."
weight = 1
+++

Installing nibOS takes one image, one microSD card and a few minutes. The DS+ itself is never
touched: put the stock card back any time and you're on stock again.

## What you need

- An **Anbernic RG DS+**.
- A **microSD card of 16 GB or more**. Everything on it is erased, so use a spare, not the card
  the DS+ came with.
- A computer with a card reader, and an imaging program.
  [Raspberry Pi Imager](https://www.raspberrypi.com/software/) works on macOS, Windows and Linux
  and writes the downloaded file as it is; `dd` works too. balenaEtcher works only with the
  image unpacked first (below).

## 1. Download

From the [download page](@/download.md), pick an edition:

- **DSlot edition** (`{{ config.extra.release.images[0].file }}`): starts into the game shelf.
  Choose this to play.
- **Base edition** (`{{ config.extra.release.images[1].file }}`): starts into a Linux console. Choose this to use the DS+ as a
  small computer ([The console and the base edition](@/manual/console.md)).

The file is compressed (`.xz`). Raspberry Pi Imager and `dd` write it as it is; for
balenaEtcher, unpack it first.

## 2. Check the download

Each image has a SHA-256 checksum on the download page and in the release's `SHA256SUMS`. A
matching checksum means the file arrived whole and is the one that was published. In a
terminal, in the folder the file is in (for the base edition, use its file name):

| On | Command |
|---|---|
| macOS | `shasum -a 256 {{ config.extra.release.images[0].file }}` |
| Linux | `sha256sum {{ config.extra.release.images[0].file }}` |
| Windows (PowerShell) | `Get-FileHash {{ config.extra.release.images[0].file }}` |

Or, with `SHA256SUMS` in the same folder, `sha256sum -c SHA256SUMS --ignore-missing` (Linux)
or `shasum -a 256 -c SHA256SUMS --ignore-missing` (macOS) checks every file you have.

The long string printed must be exactly the one on the download page. If it isn't, download
the file again; don't write a file that doesn't match.

## 3. Write the card

### With Raspberry Pi Imager

1. Open Raspberry Pi Imager. If it asks which Raspberry Pi you have, any answer will do: it
   only filters its own list.
2. For the operating system, choose **Use custom**, then the `.img.xz` you downloaded.
3. For storage, choose your microSD card. Check the size: choosing the wrong drive erases it.
4. If it offers OS customisation (user name, Wi-Fi), skip it: that is for Raspberry Pi OS.
   nibOS's own settings go in `provision.toml` (below).
5. Write. It writes, then reads the card back to check it.

### With dd (macOS and Linux)

Find the card's device name first, and be certain of it: `dd` writes wherever it is told.

The commands use the DSlot edition's file; for the base edition, use its name. On macOS,
`diskutil list` shows the card as `/dev/diskN` (check the size), then:

```sh
diskutil unmountDisk /dev/diskN
xzcat {{ config.extra.release.images[0].file }} | sudo dd of=/dev/rdiskN bs=4m
sync
```

On Linux, `lsblk` shows it as `/dev/sdX` or `/dev/mmcblkN`, then:

```sh
xzcat {{ config.extra.release.images[0].file }} | sudo dd of=/dev/sdX bs=4M conv=fsync status=progress
```

### With balenaEtcher

balenaEtcher can't write the `.img.xz` directly, so unpack it first:

1. Unpack the `.img.xz`: on macOS, double-click it; on Windows, use [7-Zip](https://www.7-zip.org);
   on Linux, `unxz` it. You get a `.img` of about 7 GB.
2. Open balenaEtcher and choose **Flash from file**: the `.img`.
3. **Select target**: your microSD card. Check the size: choosing the wrong drive erases it.
4. **Flash**. It writes, then reads the card back to check it.

When the card is written, your computer shows a small drive called **NIBOS**, and you can eject
the card.

> [!WARNING]
> The card has other partitions that macOS and Windows can't read. If your computer says the
> disk is unreadable, or **offers to format it, say no** (Ignore, Eject or Cancel; on macOS
> never **Initialise**): formatting would erase nibOS. The message can appear while the card is
> still being written; answer it the same way and let the writing finish.

## 4. Into the DS+

1. Turn the DS+ off.
2. Put the card in the slot marked **TF1** (TF1/INT). A second card in **TF2** is optional: it
   can hold games: exFAT or FAT32, named anything ([Games, BIOS and saves](@/manual/games.md#which-card)).
3. Turn it on. [First start](@/manual/first-boot.md) says what to expect.

## Optional: an SSH key (provision.toml)

You need this only to **log in to the DS+ from a computer over SSH**: SSH stays off until the
device has your public key, and this file is how you give it one. Everything else can be
done on the DS+ itself: join Wi-Fi in DSlot's menu ([Wi-Fi and Bluetooth](@/manual/connections.md)),
and set a password with `passwd` in the console.

Before you start the DS+, on the **NIBOS** drive, copy `provision.toml.example` to
`provision.toml`, in the same place, and open it in a text editor. Every line starting with `#`
is switched off; remove the `#` from the ones you want and fill them in. The file can also set
a Wi-Fi network, a password and the time zone, which saves doing them on the device:

```toml
timezone = "Europe/London"

[wifi]
ssid = "My network"
password = "the network password"

[user]
password = "a password"

[ssh]
authorized_keys = ["ssh-ed25519 AAAA... me@my-computer"]
```

| Setting | What it does |
|---|---|
| `timezone` | The time zone, as a name from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones): `Asia/Tokyo`, `America/New_York`. The clock is set from the internet once Wi-Fi is up. |
| `[wifi]` `ssid`, `password` | A Wi-Fi network to join. Leave `password` out for an open network; otherwise it is 8 to 63 characters. You can also join networks later on the device ([Wi-Fi and Bluetooth](@/manual/connections.md)). |
| `[user]` `password` | A password for the user, who is called `nibos`. With none, the console logs in by itself and `sudo` asks for nothing. With one, the console asks for it, and so does `sudo`. The DSlot edition goes to the shelf either way. |
| `[ssh]` `authorized_keys` | Public keys allowed to log in over SSH. **SSH stays off until a key is given**, and only ever takes keys. |
| `data_card` | Reserved for a later release. |

Leave out any part you don't need. Save the file, eject the card properly, and put it in the
DS+.

**What happens to the file.** At the next start nibOS checks it. If everything in it is right,
it applies it and **erases `provision.toml`**. If anything is wrong, nothing in it is applied:
it is renamed `provision.rejected-1.toml`, and `provision.error.txt` beside it says what was
wrong. Fix it, rename it back to `provision.toml`, and start again.

To change a setting later, write a new `provision.toml` with only what changes: a part left out
keeps what was set.

## Going back to the stock system

Turn the DS+ off, take the nibOS card out of TF1 and put the stock card back. That's it.

To use the nibOS card for something else, write another image to it, or format it on a
computer (on a Mac, Disk Utility's **Erase** on the whole card, not one partition).
