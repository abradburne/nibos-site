+++
title = "PortMaster"
description = "Getting PortMaster, installing ports, playing and quitting them."
weight = 7
+++

[PortMaster](https://portmaster.games) installs *ports*: Linux builds of games and game engines,
packaged for handhelds. On nibOS it runs on the top screen with the DS+'s controls, installs
ports over Wi-Fi, and DSlot lists them on its **Ports** page.

## Getting PortMaster

nibOS fetches PortMaster from its own site the first time you ask for it.

1. In DSlot, go to the **Apps** page (or the **Ports** page) and choose **Get PortMaster**.
2. nibOS asks before downloading, turns Wi-Fi on if it is off, and sets PortMaster up.
3. PortMaster opens. From then on the entry reads **PortMaster**, and PortMaster keeps itself up
   to date.

## Installing and playing ports

Open PortMaster from the Apps page, or from **Get more ports**, the first tile on the Ports page.
Ports it installs go in `Roms/PORTS` on the games card and appear on DSlot's **Ports** page when
PortMaster closes, each with its name and picture.

Choose a port on the Ports page to play it, as you would a game. It plays on the top screen;
the bottom screen shows its name and how to leave it:

- **Select + Start** or **Menu + Start** quits the port.
- **Holding power** opens the power menu; the port is stopped first.

Ports keep their own saves, in their own folders.

## What doesn't work yet

- Ports that need **RetroArch** don't start: nibOS has no RetroArch.
- Ports that need **32-bit** libraries aren't offered: nibOS is 64-bit only.
