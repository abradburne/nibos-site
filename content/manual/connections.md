+++
title = "Wi-Fi and Bluetooth"
description = "Turning the radios on, joining networks, when the network comes up, pairing keyboards and headphones, and SSH."
weight = 5
+++

On a fresh card both radios are off, except that Wi-Fi comes on by itself when `provision.toml`
named a network. Each stays as you leave it, across restarts. Turning Wi-Fi off when you don't
need it gives you noticeably more battery.

## Wi-Fi

```sh
nib wifi on                                  # the radio; off, status
iwctl station wlan0 scan
iwctl station wlan0 get-networks             # the networks in range
iwctl station wlan0 connect "My network"     # asks for the password
```

`iwctl` is iwd's own tool; run it alone for an interactive prompt. Networks it joins are kept.

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

After sleep, Wi-Fi reconnects about 2 seconds after the DS+ wakes.

### When the network comes up

With Wi-Fi on, nibOS brings the network up at every start. `nib net status` says whether it is
up and when it comes up; `sudo nib net mode` changes that from the next start:

| Mode | The network comes up |
|---|---|
| `boot` | With the system: the default. |
| `deferred` | Once start-up has finished, at the lowest priority. |
| `demand` | Only when something asks for it (`sudo nib net up`), which saves battery. |

`sudo nib net up` and `down` bring it up or down now.

## Bluetooth

```sh
nib bluetooth on
bluetoothctl
```

In `bluetoothctl`: `scan on`, then `pair <address>`, `trust <address>` and
`connect <address>` for the device you want, and `exit`. Paired devices are kept, and connect
again by themselves.

**Headphones.** When Bluetooth headphones connect, the sound moves to them; the volume keys then
set their volume. The codecs are SBC, aptX, LDAC and Opus. Bluetooth audio is new:
[tell us](@/manual/troubleshooting.md#reporting-a-bug) how your headphones get on.

**Keyboards** pair the same way, and type in the console.

## SSH

With a key given in `provision.toml` and Wi-Fi on, you can log in from a computer on the same
network: `ssh nibos@nibos.local`. See [The console](@/manual/console.md#ssh).
