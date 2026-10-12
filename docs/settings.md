# Lobby settings

Everything a community lobby can change. Anything not on this page is locked.
This page is generated from farmbot's source by `tools/lobby/gen.py`, so it always
matches what the host actually accepts. Don't edit it by hand.

Put these under `"settings"` in your `lobby.json`. Leave a setting out to keep the
base mode's value - the ffa / teams / 24p / vanilla columns show what each base
mode uses today.

## Match

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `RoundsToWin` | int | 3 - 50 | 30 | 30 | 30 | 30 | Rounds a duck must win to take the match. |
| `RoundsPerIntermission` | int | 1 - 30 | 15 | 15 | 15 | 15 | Rounds between scoreboard breaks. |
| `MatchStartSeconds` | int | 15 - 300 | 90 | 90 | 90 | 90 | Lobby countdown once enough ducks are in. |
| `MinimumPlayers` | int | 2 - 8 | 3 | 3 | 4 | 3 | Ducks needed before a match starts. |
| `MaximumPlayers` | int | 2 - 24 | 24 | 24 | 6 | 24 | Lobby size cap. Over 8 needs base "24p". |
| `WinByKills` | bool | true / false | true | true | true | true | Score by kills instead of rounds won. |
| `SkipExcessRounds` | bool | true / false | true | true | true | true | End the match early once the result is decided. |
| `MidGameJoining` | bool | true / false | true | true | true | true | Let ducks join during a match. |

## Lobby

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `LobbyName` | string | up to 32 chars | "\|DGGREEN\|FARMBOT" | "\|DGGREEN\|FARMBOT \|WHITE\|24-player" | "\|DGGREEN\|FARMBOT teams" | "\|DGGREEN\|Vanilla" | Name in the server browser. Duck Game colour tags like \|DGGREEN\| are allowed. |

## Maps

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `CustomMapsPercent` | int | 0 - 100 | 45 | 45 | 45 | 0 | Share of rounds on custom maps (your lobby's maps folder). The four map percentages must add up to 100. |
| `NormalMapsPercent` | int | 0 - 100 | 45 | 45 | 45 | 90 | Share of rounds on the game's built-in maps. |
| `RandomMapsPercent` | int | 0 - 100 | 9 | 9 | 9 | 10 | Share of rounds on randomly generated maps. |
| `InternetMapsPercent` | int | 0 - 100 | 1 | 1 | 1 | 0 | Share of rounds on maps downloaded from the workshop. |
| `MapScoresInRotation` | bool | true / false | true | true | true | true | Let skip votes and play counts push unpopular maps down the rotation. |

## Chaos

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `EnableTerribleIdeas` | bool | true / false | true | true | true | true | Some rounds hand every duck the same cursed kit. |
| `TerribleIdeaChance` | int | 0 - 100 | 8 | 8 | 8 | 8 | Percent of rounds that are a Terrible Idea. |
| `TerribleIdeaMinPlayers` | int | 2 - 8 | 3 | 3 | 3 | 3 | Ducks needed for a Terrible Idea round. |
| `EnableSuddenDeath` | bool | true / false | false | false | false | false | Long rounds turn into sudden death. |
| `SuddenDeathSeconds` | int | 10 - 120 | 25 | 25 | 25 | 25 | Seconds into a round before sudden death. |
| `EnableCarePackages` | bool | true / false | false | false | false | false | Supply drops land mid-round. |
| `CarePackageMinSeconds` | int | 5 - 120 | 15 | 15 | 15 | 15 | Earliest a care package can drop. |
| `CarePackageMaxSeconds` | int | 5 - 120 | 35 | 35 | 35 | 35 | Latest a care package can drop. |
| `CarePackageMinAlive` | int | 2 - 8 | 3 | 3 | 3 | 3 | Ducks alive needed for a drop. |

## Fairness

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `SpawnKillPenaltyEnabled` | bool | true / false | false | false | false | false | RICOCHET: a kill right after GO kills the killer too. |
| `SpawnKillGraceSeconds` | double | 0 - 2 | 1.0 | 1.0 | 1.0 | 1.0 | How soon after GO a kill counts as a spawn-kill. |
| `EnableKonamiPenalty` | bool | true / false | true | true | true | true | Penalise the Konami-code cheat input. |
| `KonamiScorePenalty` | int | 0 - 5 | 1 | 1 | 1 | 1 | Points lost for it. |
| `TrickShotPointBonus` | int | 0 - 10 | 3 | 3 | 3 | 3 | Extra points for trick shots. |
| `EnableAfkKick` | bool | true / false | true | true | true | true | Kick (never ban) ducks that stand still round after round. |
| `AfkWarnRounds` | int | 1 - 10 | 2 | 2 | 2 | 2 | Idle rounds before the warning. |
| `AfkKickRounds` | int | 2 - 20 | 4 | 4 | 4 | 4 | Idle rounds before the kick. |
| `AfkKickMinSeconds` | int | 30 - 600 | 120 | 120 | 120 | 120 | And at least this long idle. |
| `LagLimitMs` | int | 250 - 500 | 250 | 250 | 250 | 350 | Ping where the lag monitor starts warning. |
| `EnableTeamArmorBalance` | bool | true / false | true | true | true | true | Teams: armour for the short-handed side. |
| `SkipVotePercent` | int | 30 - 90 | 50 | 50 | 50 | 50 | Share of the room a skip/restart vote needs. |
| `KickVotePercent` | int | 50 - 90 | 65 | 65 | 65 | 65 | Share of the room a kick vote needs. |

## Shop and loadouts

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `EnableItemShop` | bool | true / false | true | true | true | true | @buy spawns an item next to you mid-round. |
| `BuyCooldownSeconds` | int | 0 - 300 | 30 | 30 | 30 | 30 | Seconds between @buy purchases. |
| `BuyPriceOverrides` | priceMap | each 50 - 20000 | - | - | - | - | Item name -> price for @buy. |
| `EnableLoadouts` | bool | true / false | true | true | true | true | @l1-@l5, @l make and @l0. |
| `LoadoutPriceOverrides` | priceMap | each 50 - 20000 | - | - | - | - | Item name -> price inside a loadout. |
| `EquipmentPriceOverrides` | priceMap | each 50 - 20000 | - | - | - | - | Armour/holster name -> price. |
| `LoadoutTapePremium` | int | 0 - 2000 | 150 | 150 | 150 | 150 | What taping two items together costs. |
| `LoadoutHolsterPrice` | int | 50 - 5000 | 400 | 400 | 400 | 400 | Holster price. |
| `LoadoutPowerHolsterPrice` | int | 50 - 5000 | 800 | 800 | 800 | 800 | Power holster price. |
| `ExtraAmmoPercent` | int | 0 - 500 | 50 | 50 | 50 | 50 | Extra-ammo upgrade, % of the item price. |
| `InfiniteAmmoPercent` | int | 50 - 1000 | 200 | 200 | 200 | 200 | Infinite-ammo upgrade, % of the item price. |
| `LoadoutDelaySeconds` | int | 0 - 30 | 5 | 5 | 5 | 5 | Seconds after GO before loadouts can be bought. |

## Betting

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `EnableRoundBetting` | bool | true / false | true | true | true | true | Dead ducks bet on the final two. |
| `BettingMinBet` | int | 10 - 500 | 10 | 10 | 10 | 10 | Smallest bet. |
| `BettingMaxBet` | int | 10 - 500 | 500 | 500 | 500 | 500 | Largest bet. |
| `EnableHouseBets` | bool | true / false | true | true | true | true | Farmbot offers priced bets of his own. |
| `HouseBetWindowSeconds` | int | 15 - 60 | 20 | 20 | 20 | 20 | How long a bet offer stays open. |

## Farmbot

| Setting | Type | Range | ffa | 24p | teams | vanilla | What it does |
|---|---|---|---|---|---|---|---|
| `ChatBudgetMatchPerMinute` | int | 0 - 10 | 6 | 6 | 6 | 6 | Non-essential farmbot lines a minute during a round. |
| `ChatBudgetLobbyPerMinute` | int | 0 - 10 | 5 | 5 | 5 | 5 | ...in the lobby. |
| `ChatBudgetIntermissionPerMinute` | int | 0 - 12 | 8 | 8 | 8 | 8 | ...at the scoreboard. |
| `MaxKillCommentaryPerMatch` | int | 0 - 6 | 3 | 3 | 3 | 2 | AI kill callouts per match. |
| `EnableStoryLedger` | bool | true / false | true | true | true | true | Running rivalries and story recaps. |
| `EnableBookOfFrames` | bool | true / false | true | true | true | true | Tech callouts and @tech answers. |

## Always set for community lobbies

Whatever your file says:

- `EnableFfaRating` = `false`
- `Is1v1Server` = `false`
- `DevPassword` = `false`
- `EnableModeSwitch` = `true`
- `EnableStreaming` = `false`
- `BluesEarnPercent` = `50`

Community lobbies are unrated, and blues are earned at half the normal rate, so a
lobby can't be built to farm rating or money.

## Locked

- Credentials and links: webhooks, YouTube keys, DevPassword, script paths.
- What kind of server it is: Is1v1Server, stats reporting, Discord posting, streaming.
- Anything that creates blues: challenge rewards, daily streaks, bounty payouts, tips, the guest tab, weekly payouts, give caps.
- Ratings: community lobbies are always unrated.
- Host plumbing: logging, keepalive, lobby watcher, restart rules, mode-switch rules.
