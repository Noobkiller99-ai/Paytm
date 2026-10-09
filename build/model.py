"""Single source of truth for every number in the deck.

The annexure workbook re-computes the same chain with live Excel formulas;
check_numbers.py compares the recalculated workbook against this module.
"""

DEVICE_MERCHANTS = 15_700_000  # 1.57 crore, Paytm Q1 FY27 release

# Dataset proxies (synthetic VOC workbook)
SETTLEMENT_SHARE = 23 / 42     # next-day or separate-account, of 42 Paytm collectors
FRICTION_SHARE = 16 / 23       # stated timing / transfer / staff-control friction
G1_YES, G1_MAYBE, G1_N = 7, 9, 16
NOT_ALREADY_PAYER = 9 / 16     # Group 1 never or rarely pay through Paytm

# Vendor UPI payments a month: midpoints of 2-3, 3-5, 4-6 a week (x 4.3 weeks) and daily (26)
WEEKS_PER_MONTH = 4.3
VENDOR_PAYMENTS = (2.5 * WEEKS_PER_MONTH + 4 * WEEKS_PER_MONTH + 5 * WEEKS_PER_MONTH + 26) / 4

BASELINE_OVERLAP = 0.15

SCENARIOS = {
    #            weekly-UPI share, exposure, yes-conv, maybe-conv, repeat, shift, ticket
    "cautious": dict(upi=0.35, exposure=0.25, yes=0.25, maybe=0.05, repeat=0.35, shift=0.25, ticket=2000),
    "base":     dict(upi=0.50, exposure=0.40, yes=0.40, maybe=0.10, repeat=0.50, shift=0.40, ticket=2500),
    "upside":   dict(upi=0.60, exposure=0.55, yes=0.60, maybe=0.20, repeat=0.65, shift=0.60, ticket=3500),
}

# Unit-cost assumptions
VISIT_COST = 200            # Rs per exposed merchant (range 150-300)
VISIT_COST_LOW, VISIT_COST_HIGH = 150, 300
FLOAT_RATE = 0.11           # annual
DAYS_EARLY = 1
PILOT_BUILD = 0.5e7         # Rs 0.5 crore, small build (team assumption)
FULL_BUILD = 5.0e7          # Rs 5 crore, medium-large payer flow (team assumption)
HABIT_GUARD_TARGET = 0.30


def funnel(s, settlement_share=SETTLEMENT_SHARE, act_mult=1.0, repeat_mult=1.0):
    p = SCENARIOS[s]
    eligible = DEVICE_MERCHANTS * p["upi"] * settlement_share * FRICTION_SHARE
    exposed = eligible * p["exposure"]
    activation = (p["yes"] * G1_YES + p["maybe"] * G1_MAYBE) / G1_N * act_mult
    activated = exposed * activation
    repeat = activated * p["repeat"] * repeat_mult
    mtu = repeat * NOT_ALREADY_PAYER
    payments = repeat * VENDOR_PAYMENTS * p["shift"]
    gmv_month = payments * p["ticket"] * (1 - BASELINE_OVERLAP)
    gmv_year = gmv_month * 12
    pool_month = eligible * VENDOR_PAYMENTS * p["ticket"]
    exposed_pool = exposed * VENDOR_PAYMENTS * p["ticket"]
    return dict(eligible=eligible, exposed=exposed, activation=activation, activated=activated,
                repeat=repeat, mtu=mtu, payments=payments, gmv_month=gmv_month, gmv_year=gmv_year,
                pool_month=pool_month, pool_year=pool_month * 12, exposed_pool=exposed_pool,
                share_exposed=gmv_month / exposed_pool, share_eligible=gmv_month / pool_month,
                ticket=p["ticket"])


F = {s: funnel(s) for s in SCENARIOS}
B = F["base"]

SETTLE_COST_PER_PAYMENT = SCENARIOS["base"]["ticket"] * FLOAT_RATE / 365 * DAYS_EARLY


def unit_costs(visit_cost=VISIT_COST, build=0.0, b=B):
    visits = visit_cost * b["exposed"]
    settle = SETTLE_COST_PER_PAYMENT * b["payments"] * 12
    total = visits + settle + build
    return dict(visits=visits, settle=settle, build=build, total=total,
                per_mtu=total / b["mtu"], per_rupee=total / b["gmv_year"],
                per_mtu_per_1000=visit_cost * 1000 / (b["mtu"] / b["exposed"] * 1000))


U0 = unit_costs()
U1 = unit_costs(build=PILOT_BUILD + FULL_BUILD)
MTU_PER_1000 = B["mtu"] / B["exposed"] * 1000
ITT_POINTS = B["activation"] * SCENARIOS["base"]["repeat"] * SCENARIOS["base"]["shift"]

SENS = {
    "Base case": B["gmv_year"],
    "Settlement share halved": funnel("base", settlement_share=SETTLEMENT_SHARE / 2)["gmv_year"],
    "Activation halved": funnel("base", act_mult=0.5)["gmv_year"],
    "Repeat rate halved": funnel("base", repeat_mult=0.5)["gmv_year"],
    "Gap-days-only floor": B["gmv_year"] * (1 - HABIT_GUARD_TARGET),
}


# ---------- formatting helpers (Indian units) ----------
def lakh(x, d=1):
    return f"{x / 1e5:.{d}f} lakh"


def crore(x, d=0):
    v = x / 1e7
    return f"₹{v:,.{d}f} crore"


def rs(x):
    return f"₹{x:,.0f}"


def r_cr(x):
    """Crore display rounding: nearest 10 below 10,000, nearest 100 above (240 / 2,660 / 19,400)."""
    return round(x, -1) if abs(x) < 10000 else round(x, -2)


def r3(x):
    """Round to 3 significant figures (the convention used for crore run-rates)."""
    from math import log10, floor
    if x == 0:
        return 0
    return round(x, -int(floor(log10(abs(x)))) + 2)


if __name__ == "__main__":
    for s, f in F.items():
        print(s, {k: round(v, 4) if isinstance(v, float) else v for k, v in f.items()})
    print("vendor payments", VENDOR_PAYMENTS)
    print("annual crore", {s: F[s]["gmv_year"] / 1e7 for s in F})
    print("pool month crore", B["pool_month"] / 1e7, "year lakh cr", B["pool_year"] / 1e12)
    print("share exposed", B["share_exposed"], "eligible", B["share_eligible"])
    print("unit costs no build", U0)
    print("unit costs with build", U1)
    print("MTU per 1000", MTU_PER_1000, "ITT", ITT_POINTS)
    print("settle cost/payment", SETTLE_COST_PER_PAYMENT)
    print({k: v / 1e7 for k, v in SENS.items()})
    print("visit-cost range per MTU", unit_costs(150)["per_mtu"], unit_costs(300)["per_mtu"])
