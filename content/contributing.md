+++
title = "Contributing"
description = "How to report bugs and contribute changes to nibOS and its apps: the DCO, the rules for every change, and AI-assisted contributions."
+++

nibOS and its apps welcome bug reports, documentation, testing on devices, and code. The same
rules apply to every project in the family (nibOS, DSlot, nibcase, inkdot, inktick and nibOS's
DSperate fork); each repository's `CONTRIBUTING.md` has them in full, with what is particular to
it.

## Without writing code

- **Report bugs**, with the log from the card: [Reporting a bug](@/manual/troubleshooting.md#reporting-a-bug).
- **Test** an image on your DS+ and your cards, and say what worked as well as what didn't.
- **Improve this manual**: it is Markdown, in [its own repository](https://github.com/abradburne/nibos-site).
  A translation is welcome; Japanese is planned.

## How changes are made

- **Open an issue first** for new features, new dependencies, and anything touching the
  bootloader, the partitions or the boot chain.
- **One logical change per pull request**, a few hundred changed lines at most unless agreed.
  No unrelated refactors or reformatting mixed in.
- **Say what, why and how**: the problem with its evidence (logs, measurements), the
  alternatives considered, the risk, and how it was tested: the project's checks (`make check`)
  green, and on a device, which device, which build, what you ran and what happened.
  Performance claims come with before and after numbers from the project's benchmarks; anything
  visible, with a photo or screenshot.
- **Tests** for new behaviour where it can be tested; a regression test for a bug fix where
  possible.
- **Hardware safety**: a change that could stop a device starting says so at the top, with the
  way back.
- **Docs and the changelog** change in the same pull request as the code.

## Sign-off: the DCO

Every commit in a pull request carries a `Signed-off-by:` line from the person who submits it
(`git commit -s`). It is their statement, under the
[Developer Certificate of Origin](https://developercertificate.org/), that they have the right
to contribute the change under the project's licence. A check on every pull request refuses
commits without one. There is no contributor licence agreement: a contribution stays under the
licence of the part it changes ([Licences](@/licences.md)).

## AI-assisted contributions

**They are accepted**, openly. Most of nibOS was written by AI agents, steered by a person who
tested every change on the device, and the same way of working is open to everyone. The rules
are the same for every change, whoever or whatever wrote it:

- **A person is accountable** for every pull request: they have read the change, run it, and
  stand behind it.
- **Say so.** Disclose AI help in the pull request, and with a `Co-Authored-By:` trailer on the
  commits, as the projects' own histories do.
- **An AI agent never adds `Signed-off-by:`**: the person does, when submitting.
- **Never claim a test or a device run that didn't happen.** Say plainly what wasn't checked.

Maintainers may close without a detailed review pull requests that ignore these rules: mass
rewrites, unverified hardware claims, speculative "improvements", invented APIs.

For agents, each repository's `AGENTS.md` is the short version, and nibOS's
[AGENTS.md](https://github.com/abradburne/nibos/blob/main/AGENTS.md) is also the guide to
writing apps for it.

## Clean-room emulators

inkdot and inktick are written from public documentation and black-box
testing only: no other emulator's source is read while writing them. Contributions to them must
be written the same way; say in the pull request what you worked from.
