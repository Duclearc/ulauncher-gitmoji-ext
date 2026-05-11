# Gitmoji para Ulauncher

[Ulauncher](https://ulauncher.io/) extension inspired by the workflow [alfred-gitmoji](https://github.com/techouse/alfred-gitmoji): searches **gitmojis** offline (packaged list) and copies either the **code** (`:bug:`) or the **emoji** (`🐛`) onto the clipboard.

The data is provided by the official [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) repository (file: `data/gitmojis.json`).

## Prerequisites

- Ulauncher with **Extension API v2** (see *Preferences → About*).

## Instalation

### Via Git Repository (recommended for development)

1. Clone this repo (or copy the project's folder).
2. Create a symlink in Ulauncher's `extensions` folder:

   ```bash
   mkdir -p ~/.local/share/ulauncher/extensions
   ln -sf /absolute/path/to/ulauncher_gitmoji_extension \
     ~/.local/share/ulauncher/extensions/ulauncher-gitmoji
   ```

3. Restart Ulauncher (or reload the Extensions in the Preferences).

### Via GitHub URL (for access to the public repository)

1. Open *Ulauncher → Preferences → Extensions → Add extension*.
2. Paste the repository's URL (HTTPS), for example:  
   `https://github.com/YOUR_USERNAME/ulauncher_gitmoji_extension.git`

Ulauncher uses the file [`versions.json`](versions.json) to choose which branch is compatible with the API (here: `main` + API `2`). If, for example, the default branch for your repository is `master`, change the `commit` field in `versions.json` to `master`.

## Usage

1. Open Ulauncher (default shortcut).
2. Type a the configured keyword (default: **`gm`**).

| Command | Behaviour |
|---------|----------------|
| **`gm `** (keyword only, no search-terms) | Shows **5** initial gitmojis (quick suggestions). |
| **`gm <search-term>`** | Searches by code, name or description; up to **25** results. E.g. `gm bug`, `gm performance`. |
| **`gm all`** | Lists **all** gitmojis (~73), without limits. |
| **`gm all <search-term>`** | Same as regular search, only **without limits** on the result hits. |

3. Each gitmoji appears as **a single item** (emoji + code in the title; description below).
4. Pressing **Enter** upon the item: copies the configured value as *Copied format* (code `:nome:` or emoji unicode) and closes Ulauncher.

## Preferences

Under *Preferences → Extensions → Gitmoji*:

| Preferece | Description |
|-------------|-----------|
| **Gitmoji** (keyword) | Word that triggers the extension (default `gm`). |
| **Copied format** | Defines if pressing **Enter** copies the **code** (`:bug:`) or the **emoji unicode** (`🐛`). |

## Development and manual testing

1. Install the extension via symlink (see  *Installation* above).
2. Run Ulauncher in verbose mode to see the extension logs:

   ```bash
   ulauncher -v
   ```

3. Test in the launcher: `gm`, `gm bug`, `gm all`, `gm all fix`.
4. After selecting an item, paste it on an editor andverify if the copied text is correct (code vs emoji).

## Credits

- Inspiration: [techouse/alfred-gitmoji](https://github.com/techouse/alfred-gitmoji)
- Data and gitmoji convention: [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji)
- Icon: assets from the gitmoji website ([`packages/website/public/static`](https://github.com/carloscuesta/gitmoji/tree/master/packages/website/public/static))
- English translation [Duclearc](https://duclearc.com)

## License

MIT — see [LICENSE](LICENSE).
