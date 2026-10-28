+++
title = "Privacy"
description = "What nibOS sends anywhere (almost nothing, and only when you ask), what a bug report carries, and this site."
+++

**nibOS collects nothing about you.** It has no accounts, no analytics and no telemetry, and
nothing on the device reports on you in the background. Your device only uses the network for
things you start yourself, listed below. The one thing that goes to nibOS's project is a
**bug report, and only when you choose to send one.**

## Bug reports

When a game stops unexpectedly DSlot offers to send a report, and `nib bug-report send` sends
one by hand. Nothing is sent unless you choose to.

**What a report holds:** the log of the current start, the kernel's and the system's, with
DSlot's and the emulators' lines in it. That is its first 150 lines and its last 3,000. It also
carries the nibOS version, build, edition and board, and the one-line reason DSlot gives (for
example "DSperate stopped (signal 9)").

**What is taken out on the device, before it leaves:**

- Wi-Fi network names and passphrases, and any password in the log;
- MAC addresses and IP addresses;
- the device's name and your user name, if you changed them from nibOS's own.

**What stays:** the names of the games you played, because they are usually the point of the
report, and everything else the log says about the system.

**Read it first:** every report is saved before it is sent, as `nibos/bug-report-<date>.txt` on
the card's NIBOS-DATA drive, so you can read exactly what would go, or attach it to a report
yourself instead of sending it.

**Where it goes:** to nibOS's own bug tracker (GlitchTip, run by the project at
`tracker.alanb.dev`). The device can only write to it; reading reports needs the project's
login. Like any web request, the server sees your connection's IP address; nibOS doesn't put it
in the report. Sending prints the report's code: quote it in a
[GitHub issue](https://github.com/abradburne/nibos/issues) to talk about it, or to ask for it to
be deleted.

## What the device connects to, and when

Each of these happens only when you do the thing it is for, and goes to someone else's service,
under that service's own privacy policy.

| When | Where | What they see |
|---|---|---|
| You check for or download an update (**System → Update**, `nib update`) | GitHub (`api.github.com`, `github.com`) | Your IP address, and which release you download |
| You sign in to **RetroAchievements**, and while you play signed in | RetroAchievements (`retroachievements.org`, `media.retroachievements.org`) | Your username, your password once at sign-in (only the token it answers with is kept, on the device), which games you play (by a fingerprint of the file) and the achievements you earn |
| The network is up | Public time servers (NTP), and your network's name servers (DNS) | Your IP address: the clock is set from them, and names are looked up |
| You use **PortMaster** | GitHub | Your IP address, and the ports you download |
| You open DSlot's **Network info** page | Cloudflare (`one.one.one.one`, standing for "the internet"), GitHub and the bug tracker | A connection test, to say whether each can be reached; nothing else is sent |

On a new card Wi-Fi is off until you switch it on or give it a network in `provision.toml`, and
on the DSlot edition it only starts once something needs it.

## On the device

nibOS keeps a log of each start on the card's NIBOS-DATA drive (`nibos/log/`), for bug reports
and for you to read. It stays on your card unless you send a report. Your RetroAchievements token is kept in DSlot's
settings folder, readable only by your user, and goes when you sign out.

## This website

This site has no tracking, no cookies and no scripts. It is served by GitHub Pages, and the
downloads come from GitHub Releases, so GitHub sees your visit the way any web host does:
see [GitHub's privacy statement](https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement).

## Changes

If what nibOS sends ever changes, this page changes with it, and the release notes say so.
Questions: [open an issue](https://github.com/abradburne/nibos/issues).
