# nibos-site

The nibOS website and its user manual, for the Anbernic RG DS+, from one set of Markdown
files, so the two never drift. nibOS is the Linux system, and this site offers its image, which
starts into a console. DSlot, the game system built on nibOS, has its own site and manual at
https://dslot.alanb.dev/ ([dslot-site](https://github.com/abradburne/dslot-site)), built from
the same templates; a change to the design goes into both. It's a static site: no scripts, no tracking, no cookies and no
requests to other sites. Light and dark follow the reader's setting. It uses DSlot's look, in
blue where DSlot's is gold: Roboto Condensed (self-hosted, subset to Latin) and near-black
panels. The home page shows an RG DS+ rendered in Blender (`tools/rgds-plus.py`) and three
pictures of the console, drawn by `tools/console-shots` with nibOS's own keyboard code and
kernel font.

```sh
brew install zola      # Zola 0.23 (one binary; https://www.getzola.org for other systems)
make                   # build into public/; every internal link and anchor is checked
make serve             # http://127.0.0.1:1111, rebuilt on every change
make check             # and every external link
```

## Layout

| Path | What |
|---|---|
| `content/_index.md` | The home page. Its front matter holds the words: the headline, the render and console pictures, the two features, the figures, the notes, the steps and the stack |
| `content/download.md` | The image, how to check it, release notes, licences, the source |
| `content/manual/` | The manual, one chapter per file, ordered by each file's `weight` |
| `content/apps.md` (Projects), `faq.md`, `contributing.md`, `licences.md` | The other pages |
| `zola.toml` | The site's settings, and the release: `[extra.release]` is the one place where a release's version, files, sizes, checksums and update key are written. The home and download pages read it. `dslot_site` is DSlot's site's address |
| `templates/` | The pages' HTML (Tera 2) and `404.html`; `components.html` holds the components: two-screen pictures, screenshots, icons and the download cards |
| `static/` | The stylesheet, the font, the icon, the render (`img/rgds-plus.webp`) and the console pictures (`img/console-*.webp`) |
| `tools/` | `rgds-plus.py`, the RG DS+ in Blender (`--shell` and `--buttons` set its colours; this site's is `--shell "#101a38" --buttons "#0b1124"`), and `console-shots`, the console pictures |
| `.github/workflows/pages.yml` | Builds the site and publishes it on GitHub Pages |

## Publishing

The site lives at **https://nibos.alanb.dev/**. The workflow runs on every push to `main`, or
by hand from the Actions tab: it installs a pinned Zola release, checking its checksum, builds
the site and deploys it to GitHub Pages.

- **GitHub:** Settings → Pages → Source: **GitHub Actions**; Custom domain: `nibos.alanb.dev`;
  then **Enforce HTTPS** once GitHub has issued the certificate.
- **DNS:** a `CNAME` record `nibos` → `abradburne.github.io`.
- The address is written in two places, which must agree: `base_url` in `zola.toml` (links,
  the canonical link, the sitemap) and `static/CNAME`.

## A new release

Each nibOS release also carries DSlot's image; [dslot-site](https://github.com/abradburne/dslot-site)
offers it, and changes with this one.

1. In `zola.toml`, under `[extra.release]`, set the version, tag, date and commit, the image's
   file name (`nibos-<version>-rg-ds-plus.img.xz`), size and SHA-256 (copied from the release's
   `SHA256SUMS`), and `published = true` once the files are on the release page.
2. Update the release notes in `content/download.md`.
3. Change the manual wherever behaviour has changed, and update Known issues.

## Writing

- Plain, precise English, to a reference standard. Describe what is true of the image a reader
  installs, and nothing that hasn't been run on a device.
- No comparisons with other firmwares or emulators. No ROMs, BIOS files or game artwork, in
  text or pictures.
- For engineering detail, link the projects' own documentation rather than repeating it.
- Links between pages take the form `@/manual/install.md#anchor`. Zola checks each one when it
  builds, so a renamed heading breaks the build rather than the site.
- Notes use GitHub's alert syntax (`> [!NOTE]`, `> [!WARNING]`), which renders on GitHub too.

## Licences

| | Licence |
|---|---|
| Roboto Condensed (`static/fonts/`) | SIL Open Font License 1.1 ([OFL.txt](static/fonts/OFL.txt)), copyright 2011 The Roboto Project Authors; subset to Latin |
| The text (`content/`), the icon, the render and the console pictures (`static/img/`) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) ([LICENSE-CC-BY-SA-4.0.txt](LICENSE-CC-BY-SA-4.0.txt)) |
| The templates, stylesheet, `tools/`, `zola.toml`, `Makefile` and workflow | MIT ([LICENSE-MIT](LICENSE-MIT)) |

[LICENSE](LICENSE) says which licence covers which file.
