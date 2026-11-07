+++
title = "Projects"
description = "nibOS and the projects around it: the nibkit SDK, and DSlot with its emulators DSperate, inkdot, nibcase and inktick."
+++

nibOS is the operating system. Around it are separate projects, each with its own repository,
documentation and licence: **nibkit**, the SDK for programs on the DS+, and **DSlot**, the game
system built on nibOS, with its emulators. DSlot and its emulators come on
[DSlot's own card image]({{ config.extra.dslot_site }}/), not on nibOS's.

## nibOS and nibkit

<ul class="app-list">
<li>
<h3>nibOS</h3>
<p class="meta">The operating system · GPL-3.0-or-later</p>
<p>Mainline Linux and U-Boot, Arch Linux ARM, the hardware layer (<code>nibos-hw</code> and the <code>nib</code> command), the safe mode and recovery, and the image build.</p>
<p><a href="https://github.com/abradburne/nibos">Repository</a> · <a href="https://github.com/abradburne/nibos/blob/main/docs/architecture.md">Architecture</a> · <a href="https://github.com/abradburne/nibos/blob/main/docs/roadmap.md">Roadmap</a></p>
</li>
<li>
<h3>nibkit</h3>
<p class="meta">The SDK · Rust (and a C interface) · MIT</p>
<p>What an app on nibOS needs: where the two screens are, the buttons by their printed labels, touch, each screen's brightness, volume, Wi-Fi and Bluetooth, where files go, settings at three levels, and DSlot's menu for any app. The same app builds for nibOS, the stock system or a desktop computer. With a template app and a guide for people and AI agents alike.</p>
<p><a href="https://github.com/abradburne/nibkit">nibkit</a> · <a href="https://github.com/abradburne/nibos/tree/main/sdk/template">Template app</a> · <a href="https://github.com/abradburne/nibos/blob/main/AGENTS.md">App developer's guide</a></p>
</li>
</ul>

## DSlot and its emulators

<ul class="app-list">
<li>
<h3>DSlot</h3>
<p class="meta">The game shelf · Rust · GPL-3.0-or-later</p>
<p>The game system built on nibOS, with <a href="{{ config.extra.dslot_site }}/">its own site and image</a>: your games as carts over a card slot on the touch screen, their boxes, play time and ratings on the top one, a page for each system, the system picker and cards, resume points, and the settings for the device, Wi-Fi and Bluetooth. It also runs on the RG DS+'s stock system, as an app.</p>
<p><a href="{{ config.extra.dslot_site }}/">Site</a> · <a href="https://github.com/abradburne/DSlot">Repository</a> · <a href="https://github.com/abradburne/DSlot#readme">Guide</a></p>
</li>
<li>
<h3>DSperate</h3>
<p class="meta">DS and Game Boy Advance · C++ · GPL-3.0-or-later</p>
<p>A Nintendo DS emulator with a JIT recompiler, written for ARM handhelds. This fork adds a Game Boy Advance mode, 3D at higher resolution on the GPU, frame pacing locked to the DS+'s panels, and the shared menu. The fork is of <a href="https://github.com/beebono/DSperate">beebono's DSperate</a>.</p>
<p><a href="https://github.com/abradburne/DSperate">Repository</a> · <a href="https://github.com/abradburne/DSperate/blob/main/docs/rk3568-port.md">The RG DS+ port</a></p>
</li>
<li>
<h3>inkdot</h3>
<p class="meta">Game Boy and Game Boy Color · Rust · MIT or Apache-2.0</p>
<p>Written from scratch for the DS+: the game at an exact 5× scale on the top screen, the looks of the Game Boy Color, Game Boy, Pocket and Light, save states with their pictures. Its core passes the standard Game Boy test suites in full.</p>
<p><a href="https://github.com/abradburne/inkdot">Repository</a> · <a href="https://github.com/abradburne/inkdot/blob/main/docs/using.md">Guide</a></p>
</li>
<li>
<h3>nibcase</h3>
<p class="meta">A libretro frontend · Rust · MIT or Apache-2.0</p>
<p>Plays libretro emulator cores with the same menu, buttons, saves and pacing as DSlot's other emulators: SNES, NES and Famicom Disk System, Mega Drive, Master System, SG-1000, Game Gear, PC Engine and PC Engine CD, PlayStation, Atari Lynx, Neo Geo Pocket, WonderSwan, and Game & Watch across both screens. Each core is a package of its own, under its own licence.</p>
<p><a href="https://github.com/abradburne/nibcase">Repository</a> · <a href="https://github.com/abradburne/nibcase/blob/main/docs/systems.md">Systems, cores and BIOS</a></p>
</li>
<li>
<h3>inktick <small>(preview)</small></h3>
<p class="meta">Game & Watch · Rust · MIT or Apache-2.0</p>
<p>A Game & Watch emulator written from scratch: the Sharp SM510, SM511 and SM512 chips, LCD segments that fade like the real glass, the piezo's sound, and each unit's clock set from the system's. It plays MAME's Game & Watch sets, with their artwork if you have it.</p>
<p><a href="https://github.com/abradburne/inktick">Repository</a> · <a href="https://github.com/abradburne/inktick/blob/main/docs/using.md">Guide</a></p>
</li>
</ul>

## Not ours, and welcome

- **[PortMaster](https://portmaster.games)** installs ports of Linux games. DSlot supports it,
  downloading it on first use ([DSlot's manual]({{ config.extra.dslot_site }}/manual/portmaster/)).
- **The libretro cores** that nibcase plays are their authors' projects, each under its own
  licence: Snes9x, Nestopia UE, BlastEm, Gearsystem, Handy, Beetle PCE Fast, Beetle NeoPop,
  Beetle Cygne, gw-libretro and PCSX ReARMed.

## Writing your own

A program for nibOS is a Linux program: anything that builds for 64-bit ARM runs. For both
screens, the buttons and touch, start from
[the template app](https://github.com/abradburne/nibos/tree/main/sdk/template) and nibkit, and
read [the app developer's guide](https://github.com/abradburne/nibos/blob/main/AGENTS.md). To
appear in DSlot too, an app with an `app.toml` in `APPS/` on a card, or installed in
`/usr/share/dslot/apps`, shows on DSlot's Apps page; an emulator describes itself to DSlot with
a small file: [DSlot's guide to apps](https://github.com/abradburne/DSlot/blob/main/docs/apps.md)
and [to emulators](https://github.com/abradburne/DSlot/blob/main/docs/emulators.md).
