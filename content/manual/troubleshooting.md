+++
title = "What to do if…"
description = "When it doesn't start, freezes or won't connect: holding A at power-on, a card written wrongly, the logs, and reporting a bug."
weight = 8
+++

nibOS recovers from most problems by itself. For the rest, start here, most common first.

## It won't start

- **Nothing at all on screen.** Check the card is in **TF1**, and charge the DS+ for a while: a
  flat battery doesn't start. If the amber LED is on and the screens are dark, it is charging
  while off; press power ([Sleep, charging and the battery](@/manual/power.md#charging)).
- **The logo shows, then nothing.** Wait a minute: a first start makes the data partition, and
  a start after an update may try a few times (below). Then hold power for about 10 seconds to
  cut the power, and start again.
- **Still not starting: hold A while you press power**, and keep holding it until text appears.
  That starts nibOS the plain way, with no start-up picture and the system's messages on the
  screens, whatever is wrong with the usual way. If it gets to the console, the
  problem was in the start-up itself: [report it](#reporting-a-bug) with the logs.

## "This card was not written correctly"

About a minute after a card's first start, nibOS checks every file the image shipped against the
image's own list. When some differ, it says so in the journal (`journalctl -b | grep
root-verify`), and `nib update` gives this message: the imaging tool wrote the card wrongly
(balenaEtcher 2.1.6 does, given a `.img.xz`), and programs fail in odd ways. Write the image again with Raspberry Pi Imager
or `dd` ([Installing](@/manual/install.md#3-write-the-card)); what is on NIBOS-DATA stays.
Updates are refused until the card is rewritten.

## It froze

It restarts by itself: about 30 seconds after the system stops answering (the hardware
watchdog), or 10 seconds after a kernel crash. If you can't wait, hold power for about 10
seconds to cut the power.

## No sound from the speakers

Check the volume (Volume up), and that no headphones are plugged in or connected over
Bluetooth: sound goes to headphones while they are there. If the speakers still say nothing,
restart the DS+, then [report it](#reporting-a-bug).

## Wi-Fi doesn't connect

- Is Wi-Fi on? `nib wifi status`; `nib net status` says whether the network is up.
- Check the password: `iwctl known-networks "My network" forget`, then join it again
  ([Wi-Fi and Bluetooth](@/manual/connections.md)).
- `provision.toml` not applied? Look for `provision.error.txt` on the NIBOS drive: it says why
  ([Installing](@/manual/install.md#optional-an-ssh-key-provision-toml)).

## An update went back to the old version

If a new version doesn't start properly in three tries, the DS+ goes back to the version it
was running, by itself. `sudo nibos-bootctl status` says which copy runs and what happened. [Report it](#reporting-a-bug), with the logs.

## Going back to the stock system

Turn the DS+ off and put the stock card back in TF1. Nothing else is needed.

## Reporting a bug

**From the DS+:** `nib bug-report send` saves a copy of this start's log on the card as
`nibos/bug-report-<date>.txt` on the NIBOS-DATA drive, with personal details like Wi-Fi
details and addresses taken out, and, with Wi-Fi on, sends it to
nibOS's bug tracker. It then prints a short **report code**: quote it when you report the
problem, and nothing else needs attaching. With no Wi-Fi the file is saved all the same; attach
it instead. `nib bug-report` without `send` only saves the file.

**By hand:** every start leaves its logs on the card, readable on any computer even when the DS+ can't get
to its console:

- **Where**: on the **NIBOS-DATA** drive, in `nibos/log/`, files named `boot-<date>.txt`. The
  last 10 starts are kept.
- **When**: 20 seconds into each start, and again at power-off and restart.
- **What**: the kernel's messages and the system journal for that start. They can
  include the names of your Wi-Fi networks and Bluetooth devices: read them before you share
  them.

A start that stops before the system is up leaves no log: try holding A at power-on (above),
which usually gets far enough to write one.

When you report a bug, say:

1. The image you installed (its file name).
2. What you did, what you expected, and what happened instead. A photo of the screens helps.
3. Whether it happens every time.
4. Attach the log of the start where it happened (the newest file, if you report it straight
   away).

Bug reports go to [nibOS's issue tracker](https://github.com/abradburne/nibos/issues), or, for
DSlot and its emulators, to theirs ([Projects](@/apps.md) lists them).

From the console, `journalctl -b` shows this start's log; `nib help` lists nibOS's own
commands.

## More

For people who build nibOS or change its bootloader, [nibOS's recovery
guide](https://github.com/abradburne/nibos/blob/main/docs/recovery.md) goes further: the A/B
slots and `nibos-bootctl`, and putting a card back as it was.
