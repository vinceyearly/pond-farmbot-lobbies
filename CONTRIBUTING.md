# Adding a lobby

1. **Fork** this repo and make a folder under `lobbies/`. The folder name becomes the
   `@mode` word: `lobbies/sniper-alley/` is started with `@mode sniper-alley`.
2. **Write `lobby.json`.** Copy `lobbies/terrible-ideas-night/lobby.json` and change it.
   Every setting you can use is in [docs/settings.md](docs/settings.md).
3. **Add maps (optional).** Put `.lev` files in `maps/` inside your folder and list
   them in `"maps"`. They must be levels saved by the Duck Game editor, 1 MB or less.
   Only upload maps you made, or ones the creator has said can be shared, and credit
   them in your README.
4. **Run the checks:** `python tools/validate.py your-folder`.
5. **Open a pull request.** The same checks run automatically. A maintainer plays it,
   then merges it.

## What gets a lobby merged

- It's **different** from the four base modes in a way you can say in one line.
- It **plays**: a lobby that never reaches a third round, or that is one long spawn
  fight, gets sent back with notes.
- **One lobby per pull request**, and only your own folder. A change to `allowlist.json`,
  `lobby.schema.json`, `docs/` or `tools/` won't be merged. Those are generated from
  farmbot's source. If you want a setting opened up, open an issue saying what you'd
  build with it.

## Changing a lobby later

Open a pull request against your own folder. Anyone can suggest changes to a lobby, but
the author has the final word.
