"""Compare the recalculated annexure workbook against model.py. Exit 1 on any mismatch."""
import sys
import openpyxl
import model as M

wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
fm, sm, uc, se, sr = (wb[n] for n in ("Funnel_Model", "Share_Metric", "Unit_Costs", "Sensitivity", "Segment_Rules"))

checks = []
for col, s in zip("BCD", ("cautious", "base", "upside")):
    f = M.F[s]
    for row, key in [(9, "eligible"), (11, "exposed"), (17, "activation"), (18, "activated"), (20, "repeat"),
                     (22, "mtu"), (26, "payments"), (29, "gmv_month")]:
        checks.append((f"Funnel_Model!{col}{row} {s} {key}", fm[f"{col}{row}"].value, f[key]))
    checks.append((f"Funnel_Model!{col}31 {s} annual crore", fm[f"{col}31"].value, f["gmv_year"] / 1e7))
    checks.append((f"Share_Metric!{col}9 {s} pool crore", sm[f"{col}9"].value, f["pool_month"] / 1e7))
    checks.append((f"Share_Metric!{col}13 {s} share exposed", sm[f"{col}13"].value, f["share_exposed"] * 100))
    checks.append((f"Share_Metric!{col}14 {s} share eligible", sm[f"{col}14"].value, f["share_eligible"] * 100))
checks += [
    ("Unit_Costs!B11 settle cost/payment", uc["B11"].value, M.SETTLE_COST_PER_PAYMENT),
    ("Unit_Costs!B24 cost/MTU no build", uc["B24"].value, M.U0["per_mtu"]),
    ("Unit_Costs!B25 cost/MTU with build", uc["B25"].value, M.U1["per_mtu"]),
    ("Unit_Costs!B26 cost/₹ no build", uc["B26"].value, M.U0["per_rupee"]),
    ("Unit_Costs!B27 cost/₹ with build", uc["B27"].value, M.U1["per_rupee"]),
    ("Unit_Costs!B31 pilot metric", uc["B31"].value, M.U0["per_mtu_per_1000"]),
    ("Funnel_Model!C32 MTU per 1000", fm["C32"].value, M.MTU_PER_1000),
]
for i, k in zip(range(5, 10), M.SENS):
    checks.append((f"Sensitivity!H{i} {k}", se[f"H{i}"].value, M.SENS[k] / 1e7))
# segment counts
checks += [("Segment_Rules!C12 Group 1", sr["C12"].value, 16), ("Segment_Rules!D12", sr["D12"].value, 7),
           ("Segment_Rules!E12", sr["E12"].value, 9), ("Segment_Rules!F12", sr["F12"].value, 0),
           ("Segment_Rules!C14 Group 3", sr["C14"].value, 18), ("Segment_Rules!D14", sr["D14"].value, 1),
           ("Segment_Rules!E14", sr["E14"].value, 4), ("Segment_Rules!F14", sr["F14"].value, 13),
           ("Segment_Rules!C21 collectors", sr["C21"].value, 42), ("Segment_Rules!C24 next/separate", sr["C24"].value, 23),
           ("Segment_Rules!C33 vendor UPI 2-3x/wk", sr["C33"].value, 41), ("Segment_Rules!C34 contradictory", sr["C34"].value, 11),
           ("Segment_Rules!C35 contra in G1", sr["C35"].value, 0), ("Segment_Rules!C30 never/rarely", sr["C30"].value, 9)]

bad = 0
for name, got, want in checks:
    ok = got is not None and abs(float(got) - float(want)) <= 1e-6 * max(1, abs(float(want)))
    bad += not ok
    print(("OK  " if ok else "FAIL"), name, got, want)
print(f"{len(checks) - bad}/{len(checks)} checks passed")
sys.exit(1 if bad else 0)
