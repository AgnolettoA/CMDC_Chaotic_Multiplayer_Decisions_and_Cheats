# Chaotic MP Decisions and Cheats

A Hearts of Iron IV multiplayer meme mod that adds a **player-only, one-pick-only** secret advantage draft using hidden ideas/spirits. No map/history changes.

## Features
- One main decision category: **Secret Advantages**.
- Human players only (`is_ai = no`), AI cannot see/use (`ai_will_do = 0`).
- Each country can pick exactly one advantage (`secret_cheat_chosen` country flag locks the rest).
- Effects are delivered through hidden ideas (`visible = { always = no }`, `removal_cost = -1`).
- Child Miners path unlocks a second category with repeatable state-targeted resource decisions.
- Biggus Dickus and Steiner events spawn meme commanders.
- Rage Quit Offensive includes a permanent downside + optional 90-day war-time activation modifier.

## Installation

### Local mod install
1. Copy the `hoi4_mod/` folder to your HOI4 mod workspace (e.g. `Documents/Paradox Interactive/Hearts of Iron IV/mod/chaotic_mp_decisions_and_cheats`).
2. Create a launcher `.mod` file pointing to the folder path.
3. Ensure `descriptor.mod` is present inside the mod folder.
4. Enable the mod in the Paradox Launcher playset.

### Workshop install
1. Subscribe on Steam Workshop (after publishing this repo build).
2. Enable in launcher.
3. Place it near the top of your load order if another mod edits decisions/ideas heavily.

## MP usage flow
1. Host loads mod and starts lobby.
2. All players pick countries.
3. **Draft decisions before the game starts / before first unpause**.
4. Teams can either:
   - have every country lock in one role pick immediately, **or**
   - keep 1-2 reserve countries unpicked for a short moment, scout likely enemy faction composition, then choose counter-picks.
5. If Child Miners was picked, use the dedicated category later for 70-day contracts (random owned-core payout on completion).

## Quick draft table guide

### Civs / Economy
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Mexican Builders | “We built the factory, rebuilt the factory, improved the factory, and then rebuilt it again just to be sure.” | Build/rebuild turbo: construction +75%, repair +200%, building damage taken -40% | USSR, USA, GER | Best for bombing recovery, forts, and infra races. |
| Italian Mafia | “The people love us. They said so. Repeatedly. In writing.” | Internal control/PP spike: stability +30%, PP gain +0.75, resistance target -40%, compliance gain +40% | ITA, GER, JAP | Strong if you plan heavy occupation and snowball governance. |
| Orange President | “We shall declare war on Tuesday. Or Wednesday. Possibly both. It will be the best war. Very tidy.” | Faster justifies + war footing: justify time -60%, war support +40%, trade opinion -35%, factories/trade 8 | USA, aggressive minors | Leans into early war timings; trade diplomacy gets worse. |
| Child Miners Unlimited™ | “The ore simply appeared one morning. No one remembers digging. Best not to ask.” | Resource scaling + contracts: resources factor +50%; unlocks 70-day random-core contracts (Steel +40, Oil +40, Aluminum +20, Tungsten +10, Chromium +20, Rubber +20) | Resource-starved nations | Bank PP and patch specific resource bottlenecks in core states. |
| Speedrun Any% | “Why wait for history when you can fast-forward it with a hammer?” | Hyper-justify with internal strain: justify time -80%, wargoal tension gate -50%, planning speed +100%, stability -30%, war support -20% | Minors, early rush majors | Win tempo early; make sure your internal stability can absorb the downside. |

### Production
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Chinese Workers | “The machines are humming. The workers are humming. No one knows the tune.” | Pure industrial scaling: factory output +75%, efficiency gain +75% | GER, SOV, USA | Great baseline pick for long MP sessions. |
| Unlimited Budget Glitch | “We have solved economics. The solution was ‘more.’” | Massive output with economy tax: factory output +150%, efficiency cap +100%, building speed +100%, local resources -75%, consumer goods +20% | USA, GER, SOV | Pair with imports/synthetics; avoid if you cannot cover resource deficits. |
| Amazon Prime Logistics | “Supplies arrive before they are requested. Sometimes before they exist.” | Supply god mode: supply consumption -50%, supply grace +48, attrition -50%, air supply +300% | USSR, JAP, CHI | Dominates low-infra fronts and deep operations. |

### Naval
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Pooping Ships | “The dockyards are making a terrible noise and ships keep falling out.” | Fleet throughput spike: dockyard output +75%, refit speed +200%, naval speed +25% | UK, USA, JAP | Best for fast refit cycles and fast-response fleets. |
| Bonnie Blue — She Swallows All | “There are no convoys. There never were convoys. There is only sea.” | Sea denial package: convoy raiding +200%, sub attack +75%, naval detection +50%, naval strike attack +50% | UK, ITA, JAP | Focus on convoy lanes and layered naval-air interdiction. |

### Air Controller
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Indian Street Food | “Our bombers are lightly seasoned. Your cities are extremely so.” | Strategic bomber bruiser: strategic bomber attack +200%, air defense +150% | UK, USA | Enables durable strat-bomb pressure campaigns. |
| Red Baron WiFi Extenders | “We do not chase planes. We simply arrive wherever they thought they were safe.” | Fighter dominance: air attack +100%, air range +75%, air superiority combat bonus +30% | GER, UK, USA | Reliable air trade winner across large air zones. |
| Chinese Balloons | “We can see your house from here. We cannot hit it, but we can absolutely see it.” | Mission reach meme: air range +400%, air attack -80%, air defense -80%, air accidents +50% | USA, USSR | Use for reach/coverage, not for direct fighter dueling. |

### Army
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Biggus Dickus | “He has a wife, you know… but more importantly, he has a breakthrough.” | Command snowball: command power gain +3.00, max command power +1000, army XP gain +200%; spawns skill-10 commander with stacked traits | Any major | Converts good micro into massive breakthrough tempo. |
| Steiner at the Rescue | “This time Steiner will attack. And possibly continue attacking.” | Mobile warfare enabler: spawns custom commander (7/9/7/8/6 + custom trait), adds permanent country speed +20% | GER (best), any major | Excellent for armor exploitation and encirclement pacing. |
| Lag Switch Activated | “You advance? No. We are very comfortably entrenched and refusing.” | Hold-line specialist: entrench speed +200%, max entrench +100%, defense +50%, speed -60%, breakthrough -40% | FRA, CHI, USSR | Pick for static fronts where movement is less important. |
| Call an Ambulance… But Not For Me | “We charge heroically. The outcome is someone else’s concern.” | Extreme offense tradeoff: breakthrough +150%, division attack +50%, defense -50%, org loss while moving +40% | GER, SOV | Use in short shock offensives, avoid prolonged reactive defense. |
| Rage Quit Offensive | “We shall win gloriously in 90 days… or blame the weather.” | Baseline + burst: permanent attack +50% + war support -30%; optional activation gives 90d attack +150% and breakthrough +100% | Any timing-push country | Save activation for decisive campaign windows while at war. |

### Research / Intel
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| ADHD Researchers | “We attempted to invent a spoon and accidentally built a jet engine.” | Broad tech acceleration: research speed +150%, research bonus factor +50%, doctrine cost -30% | USA, GER, SOV | Best long-game universal tech pick. |
| USB Time Traveler | “We opened a small glowing device labeled ‘Do Not Touch.’ We touched it.” | Timeline skip package: special project speed +250%, research speed +100%, ahead penalty -50%, reactor output +150%, rocket site output +150% | GER, USA, USSR | Hard spikes key tech timings; especially strong in late tech races. |
| CIA Spies | “We have placed a listening device inside your listening device.” | Intel supremacy: operative slots +8, intel network gain +100%, encryption +4, decryption +4 | UK, USA, GER | Great when your faction coordinates coordinated intel and ciphers. |

### Child Miners tuning note (new system)
- Requested yearly targets: Steel 200, Oil 200, Aluminum 100, Tungsten 50, Chromium 100, Rubber 100.
- Implemented per-contract payload = **one fifth** of those yearly targets over **70 days**:
  - Steel +40, Oil +40, Aluminum +20, Tungsten +10, Chromium +20, Rubber +20.
- Practical throughput with strict 70-day cooldown per resource line is about **365/70 = 5.21 cycles/year** max, so effective cap is approximately:
  - Steel ~208/yr, Oil ~208/yr, Aluminum ~104/yr, Tungsten ~52/yr, Chromium ~104/yr, Rubber ~104/yr.
- Cost model note: HOI4 decisions do not natively spend an exact fixed "1 civilian factory" token; this mod simulates it by applying a temporary 70-day civilian assignment modifier (`child_miners_assigned_civ`) each time you fire a resource contract.

## Suggested draft rules (optional)
- No duplicate picks within the same faction.
- Encourage role distribution (econ / navy / air / army / intel).
- Ban obviously abusive pairings in smaller lobbies if desired.

## Compatibility notes
- No map/history edits.
- Decision and idea-heavy overhaul mods may conflict.
- Some modifiers are build/DLC dependent (`special_project_speed_factor`, `ahead_of_time_penalty`, `air_supply_factor`, `generate_wargoal_tension`). If a key is unsupported in your version, check:
  - `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log`
  - then replace unsupported keys with equivalents for your patch.

## Troubleshooting
- If decisions do not appear: verify mod enabled and that player nation is not AI.
- If loc keys appear raw: confirm file is UTF-8 BOM encoded (`secret_cheats_l_english.yml`).
- If a modifier fails silently: inspect `error.log` for unknown effect/modifier names.

## Repository layout
- `hoi4_mod/common/decisions/secret_cheats.txt`
- `hoi4_mod/common/ideas/secret_cheats_ideas.txt`
- `hoi4_mod/common/modifiers/secret_cheats_modifiers.txt`
- `hoi4_mod/common/traits/secret_cheats_traits.txt`
- `hoi4_mod/events/secret_cheats_events.txt`
- `hoi4_mod/localisation/english/secret_cheats_l_english.yml`
- `hoi4_mod/descriptor.mod`
- `workshop_description.md`
- `lobby_draft_guide.md`
- `CHANGELOG.md`
