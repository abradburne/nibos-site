+++
title = "First start"
description = "What the first start does, how long it takes, and logging in."
weight = 2
+++

## What you see

1. About **1.5 seconds** after the power button, the start-up picture is on the top screen.
2. The **first start only**: nibOS makes the data partition, **NIBOS-DATA**, over the rest of
   the card, and formats it. It takes a few seconds more than later starts. If the power goes
   while it is doing this, it carries on where it stopped at the next start.
3. If you wrote a `provision.toml`, it is applied now (or rejected, with the reason on the
   NIBOS partition: [Installing](@/manual/install.md#optional-an-ssh-key-provision-toml)).
4. The console is on the top screen and a touch keyboard on the bottom one, about 5 seconds
   after power-on on later starts. With no password set, it logs in by itself as `nibos`.

On a fresh card **Wi-Fi and Bluetooth are off**, except that Wi-Fi comes on by itself when
`provision.toml` named a network. Turn them on with `nib wifi on` and `nib bluetooth on`. Each
radio then stays as you leave it, across restarts, and with Wi-Fi on the network comes up at
every start.

## Logging in

- **On the DS+**: type on the touch keyboard, or with the buttons, or plug in a USB keyboard
  (in the host USB-C port, not the charging one). [The console](@/manual/console.md).
- **Over SSH**, with the key from `provision.toml` and Wi-Fi on, from a computer on the same
  network:

  ```sh
  ssh nibos@nibos.local
  ```

## First things to do

- **Set a password**, with `passwd`, unless `provision.toml` set one: without it, anyone holding
  the DS+ has full control of it.
- **Set the time zone**, if `provision.toml` didn't: `nib clock zones` lists them,
  `sudo nib clock zone Asia/Tokyo` sets one. The clock itself is set from the network.
- **See what the device has**: `nib help`.

## Then

- [The console](@/manual/console.md): the keyboard, SSH, copying files, `nib`, installing
  software.
- [Wi-Fi and Bluetooth](@/manual/connections.md): joining a network, pairing a keyboard or
  headphones.
- [Updates](@/manual/updates.md): keeping nibOS up to date.
