+++
title = "What to do if…"
description = "When it doesn't start, freezes, or a game won't play: the safe mode, holding A at power-on, the logs, and reporting a bug."
weight = 11
+++

Problems are listed from the most common. nibOS recovers from most of them by itself; nothing
here can harm the DS+ itself, since everything nibOS has is on its card.

## It won't start

- **Nothing at all on screen.** Check the card is in **TF1**, and charge the DS+ for a while: a
  flat battery doesn't start. If the amber LED is on and the screens are dark, it is charging
  while off; press power ([Sleep, charging and the battery](@/manual/power.md#charging)).
- **The logo shows, then nothing.** Wait a minute: a first start makes the games partition, and
  a start after an update may try a few times (below). Then hold power for about 10 seconds to
  cut the power, and start again.
- **Still not starting: hold A while you press power**, and keep holding it until text appears.
  That starts nibOS the plain way, with no start-up picture and the system's messages on the
  screens, whatever is wrong with the usual way. If it gets to the shelf or the console, the
  problem was in the start-up itself: [report it](#reporting-a-bug) with the logs.

## "This card was not written correctly"

About a minute after a card's first start, nibOS checks every file the image shipped against the
image's own list. This notice on the shelf means some differ: the imaging tool wrote the card
wrongly (balenaEtcher 2.1.6 does, given a `.img.xz`), and programs fail in odd ways, such as one
emulator quitting at once while another plays. Write the image again with Raspberry Pi Imager
or `dd` ([Installing](@/manual/install.md#3-write-the-card)); your games on NIBOS-DATA stay.
Updates are refused until the card is rewritten.

## "DSlot stopped working"

DSlot crashed several times in a row, and nibOS's safe mode took over. The top screen says what
failed; the bottom one offers **Restart DSlot**, **Restart the device**, **Open a console** and
**Power off**, with the D-pad and A.

Choose Restart DSlot. If it keeps happening, [report it](#reporting-a-bug): the logs on the card
were written at the moment it failed. Just after an update the safe mode also offers **Go back
to the previous version**.

## It froze

It restarts by itself: about 30 seconds after the system stops answering (the hardware
watchdog), or 10 seconds after a kernel crash. If you can't wait, hold power for about 10
seconds to cut the power.

## A game won't start

- **It says a BIOS file is missing.** The message names the file and where it looked: put your
  copy in `BIOS/` at a card's root ([Games, BIOS and saves](@/manual/games.md#bios-files)).
- **It comes straight back to the shelf.** The shelf says why in a notice: the emulator's own
  last line ("DSperate stopped (exit 1): launch: … ZIP NOT SUPPORTED", or where it crashed).
  Press **Y** there to send a bug report (below); any other button closes it. On 0.1.0-alpha3
  and earlier, a DS or GBA game that came back at once with "signal 9" and no other reason
  was the kernel's real-time watchdog catching the emulator's start-up; 0.1.0-alpha4 fixes it.
- **It says the file can't be read**, or the zip is damaged: copy the game onto the card again.
  A `.zip` must hold one game; disc games can't be zipped.
- **It isn't on the shelf.** Check the folder ([Games, BIOS and saves](@/manual/games.md#the-folders))
  and the file's extension. DSlot's menu (X) → System → **Rescan games** looks again. A page with no
  games isn't shown.
- **A game starts where you didn't expect.** It is resuming where you left it: clear its resume
  point with X → Game → Clear resume state.

## No sound from the speakers

Check the volume (Volume up), and that no headphones are plugged in or connected over
Bluetooth: sound goes to headphones while they are there. If the speakers still say nothing,
restart the DS+, then [report it](#reporting-a-bug).

## Wi-Fi doesn't connect

- Is Wi-Fi on? DSlot's menu → Wi-Fi, or its icon in the status bar.
- Check the password: on the Wi-Fi page, forget the network (Y twice) and join it again.
- `provision.toml` not applied? Look for `provision.error.txt` on the NIBOS drive: it says why
  ([Installing](@/manual/install.md#optional-an-ssh-key-provision-toml)).

## An update went back to the old version

If a new version doesn't reach its shelf in three tries, the DS+ goes back to the version it
was running, by itself. It is working as intended; DSlot's Update page says which version it
is on. [Report it](#reporting-a-bug), with the logs.

## Going back to the stock system

Turn the DS+ off and put the stock card back in TF1. Nothing else is needed.

## Reporting a bug

**From the DS+:** when a game comes straight back, the notice offers **Y: send a bug report** (on 0.1.0-alpha2 the button did nothing; 0.1.0-alpha3 fixed it);
from the console, `nib bug-report send`. Either saves a copy of this start's log on the card as
`nibos/bug-report-<date>.txt` on the NIBOS-DATA drive, with your Wi-Fi network names and
passphrases, MAC and IP addresses and the hostname taken out, and, with Wi-Fi on, sends it to
nibOS's bug tracker. The shelf then shows a short **report code**: quote it when you report the
problem, and nothing else needs attaching. With no Wi-Fi the file is saved all the same; attach
it instead. `nib bug-report` without `send` only saves the file.

**By hand:** every start leaves its logs on the card, readable on any computer even when the DS+ can't get
to its shelf:

- **Where**: on the **NIBOS-DATA** drive, in `nibos/log/`, files named `boot-<date>.txt`. The
  last 10 starts are kept.
- **When**: 20 seconds into each start, again at power-off and restart, and at once when DSlot
  fails.
- **What**: the kernel's messages and the system journal for that start. They can
  include the names of your Wi-Fi networks and Bluetooth devices: read them before you share
  them.

A start that stops before the system is up leaves no log: try holding A at power-on (above),
which usually gets far enough to write one.

When you report a bug, say:

1. The image you installed (its file name) and the edition.
2. What you did, what you expected, and what happened instead. A photo of the screens helps.
3. Whether it happens every time.
4. Attach the log of the start where it happened (the newest file, if you report it straight
   away).

Bug reports go to the issue tracker of the project the bug is in: nibOS itself, DSlot, or an
emulator ([Apps](@/apps.md) lists them). If you aren't sure which, report it to
[nibOS](https://github.com/abradburne/nibos/issues).

From the console, `journalctl -b` shows this start's log and `journalctl -u dslot -b` DSlot's;
`nib help` lists nibOS's own commands.

## More

For people who build nibOS or change its bootloader, [nibOS's recovery
guide](https://github.com/abradburne/nibos/blob/main/docs/recovery.md) goes further: the A/B
slots and `nibos-bootctl`, and putting a card back as it was.
