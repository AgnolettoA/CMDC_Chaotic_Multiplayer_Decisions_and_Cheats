# Chaotic MP Decisions and Cheats

A multiplayer-first HOI4 meme mod for chaotic lobbies.

## What this mod does
- Adds a **human-only** decision draft: **Secret Advantages**.
- Every player gets **exactly one pick**.
- Chosen bonus is applied through **hidden ideas** so enemies cannot see your exact choice in normal idea UI.
- AI cannot see or select these decisions.
- No map/history changes.

## MP Draft Timing (recommended)
- Decide draft plan **before game start / first unpause**.
- Two common methods:
  1. **Full-lock method:** every country picks immediately for role clarity.
  2. **Reserve-counter method:** keep 1-2 reserve countries unpicked briefly, read enemy faction setup, then lock counter picks.

## Quick table guide

### Civs
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Mexican Builders | Overnight giga-contractors | construction +75%, repair +200%, building damage -40% | USSR, USA, GER | Great anti-bombing recovery and build races. |
| Italian Mafia | Occupation with incentives | stability +30%, PP +0.75, resistance target -40%, compliance +40% | ITA, GER, JAP | Strong for conquest-heavy occupations. |
| Orange President | Diplomacy via chaos | justify -60%, war support +40%, trade opinion -35%, factories/trade 8 | USA, aggressive minors | Enables early war timing plays. |
| Child Miners Unlimited™ | Tiny labor, huge ore | resources +50%; unlocks 70d random-core contracts: Steel +40, Oil +40, Al +20, W +10, Chrom +20, Rubber +20 | Resource-starved nations | Use as staged throughput: one contract line per resource, cooldown 70d. |
| Speedrun Any% | World conquest routing | justify -80%, wargoal tension gate -50%, planning +100%, stability -30%, war support -20% | Minors, rush majors | All-in tempo at internal stability cost. |

### Production
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Chinese Workers | Assembly line overclock | factory output +75%, efficiency gain +75% | GER, SOV, USA | Safe scaling pick for long games. |
| Unlimited Budget Glitch | Treasury duplication exploit | factory output +150%, eff cap +100%, build speed +100%, local resources -75%, consumer goods +20% | USA, GER, SOV | Pair with imports/synthetics to offset deficits. |
| Amazon Prime Logistics | One-click frontline delivery | supply consumption -50%, supply grace +48, attrition -50%, air supply +300% | USSR, JAP, CHI | Excellent for deep/frontier wars. |

### Naval
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Pooping Ships | Dockyards cannot stop | dockyard output +75%, refit speed +200%, naval speed +25% | UK, USA, JAP | Fast hull throughput and refit tempo. |
| Bonnie Blue — She Swallows All | Convoys deleted | convoy raiding +200%, sub attack +75%, detection +50%, naval strike +50% | UK, ITA, JAP | Choke lanes with subs + naval bombers. |

### Air Controller
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Indian Street Food | Bombers on spice | strategic bomber attack +200%, air defense +150% | UK, USA | Durable bombing pressure. |
| Red Baron WiFi Extenders | Five bars at altitude | air attack +100%, range +75%, air superiority combat +30% | GER, UK, USA | Dominant general fighter pick. |
| Chinese Balloons | Infinite range, bad duels | range +400%, air attack -80%, air defense -80%, accidents +50% | USA, USSR | Reach tool, not a duel tool. |

### Army
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| Biggus Dickus | Gigachad general spawned | CP gain +3.00, max CP +1000, army XP +200%; spawns elite commander | Any major | Big micro and planning multiplier. |
| Steiner at the Rescue | "Steiner will attack" but real | custom commander spawn + permanent division speed +20% | GER best, any major | Peak for tank exploitation tempo. |
| Lag Switch Activated | Defensive desync doctrine | entrench speed +200%, max entrench +100%, defense +50%, speed -60%, breakthrough -40% | FRA, CHI, USSR | Hard hold line pick. |
| Call an Ambulance… But Not For Me | All-in offense | breakthrough +150%, attack +50%, defense -50%, org loss while moving +40% | GER, SOV | Shock attacks, avoid long reactive fronts. |
| Rage Quit Offensive | Permanent anger mode | permanent attack +50%, war support -30%; optional 90d burst attack +150% + breakthrough +100% | Any timing nation | Save burst for decisive wars. |

### Research
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| ADHD Researchers | Hyperfocus science | research speed +150%, research bonus +50%, doctrine cost -30% | USA, GER, SOV | Universal long-game value pick. |
| USB Time Traveler | Future docs leaked | special project +250%, research +100%, ahead penalty -50%, reactor +150%, rocket +150% | GER, USA, USSR | Ideal for key timing spikes. |

### Intel
| Decision | Meme description | Effects (summary + full values) | Suggested countries | Usage strategy tips |
|---|---|---|---|---|
| CIA Spies | Everybody is compromised | operative slots +8, intel network gain +100%, encryption +4, decryption +4 | UK, USA, GER | Best in coordinated intel factions. |

## Child Miners rate note
- One contract is one-fifth of the annual target over 70 days (close to requested yearly caps).
- Since 365/70≈5.21, practical max is slightly above nominal yearly target if cycled perfectly.
- "1 civ" is simulated through a temporary civilian-assignment modifier because HOI4 decisions do not spend exact fixed civilian factories directly.

## Compatibility
- Designed as a lightweight gameplay add-on.
- If your game version/DLC rejects certain modifier keys, check `error.log` and swap unsupported keys.
