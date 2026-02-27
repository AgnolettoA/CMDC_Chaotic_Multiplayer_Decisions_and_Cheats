# simulation of civilian factories growth

from dataclasses import dataclass
from math import floor

# =========================
# Constants (edit these)
# =========================
START_CIVS = 34  # civilian factories available for building at day 0
PRODUCTION_SPEED_BUILDINGS_FACTOR = 1.5  # +20% => 0.20, -10% => -0.10
YEARS = 8  # simulate this many years
DAYS_PER_YEAR = 365  # HOI4 uses 365-day years in many mechanics; keep it simple

# Game-ish constants
CIV_TO_BUILD_POWER = 5.0      # each civ contributes 5 construction
CIV_COST = 10800.0            # construction cost of a civilian factory

# Quarter ends (day indices, inclusive) within a year
QUARTER_ENDS = (91, 182, 273, 365)  # approx; 365 is end-of-year


# =========================
# Model
# =========================
@dataclass
class SimConfig:
    start_civs: int
    prod_speed_factor: float
    years: int


def simulate_civ_builds(cfg: SimConfig):
    total_days = cfg.years * DAYS_PER_YEAR
    civs = cfg.start_civs

    # progress towards current civ (in "cost" units)
    progress = 0.0

    # multiplier from production_speed_buildings_factor
    speed_mult = 1.0 + cfg.prod_speed_factor
    if speed_mult < 0:
        raise ValueError("production_speed_buildings_factor makes speed multiplier negative.")

    # store results at quarter boundaries
    # key: (year, quarter) -> civ count
    results = {}

    def record_if_quarter_end(day_index_1based: int):
        # day_index_1based: 1..N
        year = (day_index_1based - 1) // DAYS_PER_YEAR + 1
        day_in_year = (day_index_1based - 1) % DAYS_PER_YEAR + 1

        # check if this is a quarter end
        for q, q_end in enumerate(QUARTER_ENDS, start=1):
            if day_in_year == q_end:
                results[(year, q)] = civs

    for day in range(1, total_days + 1):
        # construction gained this day
        daily_build_power = civs * CIV_TO_BUILD_POWER * speed_mult
        progress += daily_build_power

        # if we finished 1+ civs today, apply completions
        # (rare to finish >1 in one day, but handle it safely)
        if progress >= CIV_COST:
            completed = int(progress // CIV_COST)
            civs += completed
            progress -= completed * CIV_COST

        record_if_quarter_end(day)

    return results


def print_quarter_table(results, years: int):
    print("Civs by quarter end")
    print("-" * 40)
    print(f"{'Year':>4}  {'Q1':>6}  {'Q2':>6}  {'Q3':>6}  {'Q4':>6}")
    print("-" * 40)

    for y in range(1, years + 1):
        row = []
        for q in range(1, 5):
            row.append(results.get((y, q), None))
        # If a quarter wasn't simulated (e.g. short sim), show blank
        row_fmt = [("" if v is None else str(v)) for v in row]
        print(f"{y:>4}  {row_fmt[0]:>6}  {row_fmt[1]:>6}  {row_fmt[2]:>6}  {row_fmt[3]:>6}")


if __name__ == "__main__":
    cfg = SimConfig(
        start_civs=START_CIVS,
        prod_speed_factor=PRODUCTION_SPEED_BUILDINGS_FACTOR,
        years=YEARS
    )
    results = simulate_civ_builds(cfg)
    print_quarter_table(results, cfg.years)