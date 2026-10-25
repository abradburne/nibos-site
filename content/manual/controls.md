+++
title = "Controls"
description = "Every button: on the shelf, in a game's menu, in each emulator, the power button, the console keyboard."
weight = 4
+++

The buttons are named as printed on the DS+. A, B, X and Y mean the printed letters
everywhere, in DSlot and in every emulator.

## Anywhere

| Press | Does |
|---|---|
| Power, a short press | Sleep. Press again to wake. |
| Power, held for a second | The **power menu**: Sleep, Restart, Power off, Cancel. During a game, the game is saved and put away first; Cancel carries on with it. In the console (no DSlot), holding power powers off cleanly. |
| Power, held for about 10 seconds | Cuts the power, whatever is running, without saving anything. Use it only when nothing else answers. |
| Closing the lid | Sleep. Opening it wakes the DS+. |
| Volume up / down | The volume, in steps of 5%, on the speakers or the headphones, whichever is playing. |
| **Menu** + Volume up / down | Both screens' brightness, in steps of 5%. Works in games too. |

Plugging in headphones moves the sound to them; unplugging moves it back to the speakers.

## On the shelf (DSlot)

| Press | Does |
|---|---|
| D-pad left / right, or swipe | Browse. In a list: jump to the previous / next letter. |
| D-pad up / down | Jump to the previous / next letter (a row in the cover grid, a game in a list). |
| L / R, or tap a tab | The previous / next page. |
| Select | The system picker. Up / Down to choose, A to go there, B or Select to close. |
| A, Start, or drag the cart down into the slot | Play the game. |
| Tap a neighbouring cart | Bring it to the middle. |
| Tap a cover or a name, then tap it again | Choose it, then play it. |
| Y | Mark or unmark the game as a favourite. |
| X | The menu. |
| Select + Start | Leave DSlot for the console (on the DSlot edition; DSlot starts again at the next power-on). |

**Menu** does nothing on the shelf: it is the button that brings you back from a game.

In DSlot's menu: L / R or a tap on a tab changes page, Up / Down picks a row, Left / Right or A
changes it, Y clears a setting so it inherits again, B closes the menu.

## In any game

Every emulator in nibOS shares the same buttons for leaving, saving and its menu, and the same
menu, drawn as DSlot's:

| Press | Does |
|---|---|
| **Menu** | Save where you are and go back to the shelf. The next start resumes there. |
| **Back**, or a tap on the bottom screen | Open or close the game's menu on the bottom screen. The game pauses. (On a DS game, Back alone, since the bottom screen is the game's.) |
| **Menu** + R / **Menu** + L | Quick save / quick load. |
| **Menu** + Volume | Both screens' brightness. |
| Power, held | The power menu (the game is saved first). |

The game's menu has these pages; L / R change page, Up / Down choose a row, A acts on it, B
goes back to the game:

| Page | Holds |
|---|---|
| **Play** | Resume, save and load a state, fast-forward, start over, save and quit. |
| **States** | The resume point (where you last left the game) at the left, then six save slots, each with its picture and when it was saved. A loads; X saves into a slot (X again to save over a used one). |
| **Game** | Settings for this game only. |
| **The console** (DS, GBA, GB, …) | Settings for every game of that system. |
| **System** | Volume, each screen's brightness, the clock (12- or 24-hour). |
| **Connections** | Wi-Fi and Bluetooth on or off, paired headphones connected or disconnected. Joining networks and pairing are in DSlot's menu. |

Settings in a game's menu and in DSlot's menu are the same settings: a change in one shows in
the other.

## Each emulator

### DS and GBA (DSperate)

| Press | Does |
|---|---|
| D-pad, A, B, X, Y, L, R, Start, Select | The DS's buttons (in GBA games, the GBA's). |
| Touch the bottom screen | The stylus (DS games). |
| R2, held | Fast-forward. |
| Menu + Right / Left | The next / previous quick-save slot. |
| Menu + Start, or Back | The game's menu. |

In a DS game the menu goes on the bottom screen, and the top screen shows the game dimmed. The
DS console's page also has DSperate's own options: 3D resolution, anti-aliasing, frame skip,
smooth scaling, layout, controls. DSperate keeps ten state slots; the menu shows six, and any of
slots 7 to 10 that hold a state.

### Game Boy and Game Boy Color (inkdot)

| Press | Does |
|---|---|
| D-pad or stick, A, B, Select, Start | The Game Boy's buttons. |
| X, Y | Turbo A, turbo B. |
| R2, held | Fast-forward (silent). |
| Menu + Select | Fast-forward on or off. |

The bottom screen is blank while you play. inkdot's settings include the look of a Game Boy
game (Game Boy Color, Game Boy, Pocket, Light or plain grey), the LCD texture and the timing:
[inkdot's guide](https://github.com/abradburne/inkdot/blob/main/docs/using.md).

### Other systems (nibcase)

SNES, NES, Mega Drive, Master System, Game Gear, PC Engine, Neo Geo Pocket, WonderSwan, Atari
Lynx, PlayStation and Game & Watch play in nibcase.

| Press | Does |
|---|---|
| D-pad, face buttons, L, R, Select, Start | The console's own pad. The face buttons follow their printed letters. |
| The stick | The D-pad (a setting), or a PlayStation DualShock's left stick. |
| Menu + Select | Fast-forward while held. |

On PlayStation games, the **Controller** setting picks Digital pad (the default) or DualShock;
a game of several discs has a **Disc** row on the Play page to change discs. On Game & Watch
units, **Select** moves to the unit's next key (Game A, Game B, Time, …) and **Start** presses
it; units that open like a book are shown across both screens. Every system's details:
[nibcase's systems guide](https://github.com/abradburne/nibcase/blob/main/docs/systems.md).

### Game & Watch, preview (inktick)

inktick, a Game & Watch emulator of nibOS's own, comes with the DSlot edition as a preview. It
plays MAME's Game & Watch sets (`gnw_*.zip` or `.7z`), with their artwork if you have it.

| Press | Does |
|---|---|
| D-pad or stick | The unit's directions. |
| A, B (X, B on units with a button in each corner) | The unit's action buttons. |
| Start / Select | GAME A / GAME B. |
| L / R | TIME / ALARM. |

On a single-screen unit, the bottom screen shows the unit's buttons to touch. More:
[inktick's guide](https://github.com/abradburne/inktick/blob/main/docs/using.md).

### Ports (PortMaster)

A port plays on the top screen; the bottom screen shows its name and how to leave it.
**Select + Start** or **Menu + Start** quits it; holding power opens the power menu. Each port's
own controls are its own. See [PortMaster](@/manual/portmaster.md).

## In the console (keyboard on the bottom screen)

When the console is on screen (the base edition, or after leaving DSlot with Select + Start),
the top screen is the console and the bottom one a touch keyboard. The buttons type too:

| Press | Types |
|---|---|
| D-pad | The arrow keys |
| A | Enter |
| B | Backspace |
| X | Tab |
| Y | Ctrl-C |
| L, held | Shift |
| R, held | Ctrl |
| **Menu + X** | Hide the keyboard (the bottom screen goes black), or show it again. A touch on the black screen shows it too. |

On the touch keyboard, Shift, Ctrl, Alt and Fn apply to the next key; tap one twice to keep it
on. A row of shortcuts gives Esc, Ctrl-C, Ctrl-D, Ctrl-Z, Ctrl-L, Home, End, Page Up and Page
Down. A USB keyboard (in the host USB-C port, not the charging one) or a Bluetooth keyboard works beside it. More:
[The console and the base edition](@/manual/console.md).
