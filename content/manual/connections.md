+++
title = "Wi-Fi and Bluetooth"
description = "Turning the radios on, joining networks, pairing headphones and controllers."
weight = 6
+++

On a fresh card both radios are off. Each stays as you leave it, across restarts. Turning
Wi-Fi off when you don't need it gives you noticeably more battery.

## Wi-Fi

In DSlot, press **X** for the menu and go to the **Wi-Fi** page (or tap the Wi-Fi icon in the
status bar):

- **Wi-Fi**: the switch.
- The network you are on.
- **Look for networks**, then each network in range with its signal, and whether it is saved.
- **A** on a network joins it. One that needs a password brings up the keyboard.
- **A twice** on the network you are on leaves it. **Y twice** on a saved network forgets it.

The keyboard: the D-pad and **A** type (or tap the keys), **B** deletes, **X** types a space,
**Y** shows the password as you type it, **L** is Shift, **R** symbols, **Start** is Done and
**Select** cancels.

Other ways to add a network:

- In `provision.toml`, before a start ([Installing](@/manual/install.md#optional-an-ssh-key-provision-toml)).
- As a file on NIBOS-DATA, read at every start: `nibos/wifi/<network>.psk`, holding

  ```ini
  [Security]
  Passphrase=the-network-password
  ```

  A network whose name has anything but letters, digits, `-` and `_` needs its name written in
  hex: `=` followed by the name's bytes, `=4d79204e6574.psk` for "My Net". An open network is
  `<network>.open`, empty.
- In the console: `iwctl station wlan0 connect <network>`.

After sleep, Wi-Fi reconnects about 2 seconds after the DS+ wakes.

### Network info

The Wi-Fi page shows your address (**Address**) under the network you are on. For the rest,
choose **Network info** (or press **Y** on the Wi-Fi page): whether Wi-Fi is on and connected,
the network and its signal, the address, gateway and DNS servers, the device's name on the
network (`nibos.local`, what to `ssh` to), the Wi-Fi MAC address, and whether the internet,
nibOS's update server and its bug tracker can be reached ("Reachable", "No route" or "DNS
failed"). It updates as you watch; **A** runs the checks again, **B** goes back. When asking for
help with a connection or a bug report that won't send, this is the page to read out.

In a game, the menu's **Connections** page turns Wi-Fi and Bluetooth on or off; choosing a
network is in DSlot.

## Bluetooth

In DSlot's menu (X), the **Bluetooth** page:

- **Bluetooth**: the switch.
- Your paired devices (headphones, controllers, keyboards), with their battery where they
  report it. **A** connects or disconnects one; **Y twice** forgets it.
- **Pair a new device**: put your device in pairing mode first, then choose this. nibOS looks
  for devices; **A** on one pairs it, asking for a PIN, or to check a passkey on both, where the
  device needs one, and connects it.

**Headphones.** When Bluetooth headphones connect, the sound moves to them; the volume keys then
set their volume. The codecs are SBC, aptX, LDAC and Opus. Bluetooth audio is new:
[tell us](@/manual/troubleshooting.md#reporting-a-bug) how your headphones get on. In a game, the menu's **Connections** page connects
or disconnects paired headphones with one press.

**Controllers and keyboards** pair the same way. A Bluetooth keyboard types in the console.

## SSH

With a key given in `provision.toml` and Wi-Fi on, you can log in from a computer on the same
network: `ssh nibos@nibos.local`. See [The console and the base edition](@/manual/console.md).
