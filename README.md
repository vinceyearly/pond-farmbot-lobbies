# Farmbot community lobbies

Build your own [pond.gg](https://pond.gg) Duck Game lobby. Pick a base mode, change the
settings you care about, add your own maps, open a pull request. Once it's merged, anyone
in the pond can start it:

```
@mode terrible-ideas-night        (in game - starts a vote, like any mode switch)
@quack start terrible-ideas-night (on Discord)
@lobbies                          (in game - lists what's available)
```

> **Status:** the repo, settings reference and checks are live. Farmbot loading these
> lobbies in game is the next step, so a merged lobby isn't playable *yet*. Build one
> now and it'll be among the first.

## A lobby is one folder

```
lobbies/
  terrible-ideas-night/
    lobby.json        required - what your lobby changes
    README.md         optional - tell people what it's about
    preview.png       optional - a screenshot, up to 500 KB
    maps/*.lev        optional - your maps, up to 100, 1 MB each
```

The folder name is what players type after `@mode`, so keep it short: lowercase
letters, numbers and dashes.

## lobby.json

```json
{
  "$schema": "../../lobby.schema.json",
  "name": "Terrible Ideas Night",
  "author": "galleta",
  "description": "Every other round is a cursed kit. Spawn-killers get it back.",
  "base": "ffa",
  "settings": {
    "TerribleIdeaChance": 50,
    "TerribleIdeaMinPlayers": 2,
    "SpawnKillPenaltyEnabled": true,
    "RoundsToWin": 10
  }
}
```

- **base** is the mode you start from: `ffa`, `24p`, `teams` or `vanilla`. Anything you
  don't set keeps that mode's value.
- **settings** can only use what's listed in **[docs/settings.md](docs/settings.md)**.
  That page shows every setting, its allowed range and what each base mode uses today.
- **maps** lists your map files, for example `["maps/*.lev"]`. If you add maps, you'll
  usually want `CustomMapsPercent` at 100 so your maps are the ones that get played.

Point your editor at `lobby.schema.json` (the `$schema` line above does it in VS Code)
and you get autocomplete and range checks while you type.

## The rules every community lobby plays by

- **Unrated.** Community lobbies never move anyone's FFA rating.
- **Half blues.** Blues are earned at half the normal rate, so nobody builds a money
  farm.
- **Allowlist only.** Credentials, server plumbing and anything that creates blues are
  locked. The full list is at the bottom of [docs/settings.md](docs/settings.md).
- **Checked twice.** Every pull request runs `tools/validate.py`, and the farmbot host
  checks again when it loads a lobby.

## Try the checks yourself

```
python tools/validate.py                         # every lobby
python tools/validate.py terrible-ideas-night    # just yours
```

Python 3, nothing to install.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the pull request steps.
