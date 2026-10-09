"""Build Paytitude_R2.pptx: cover, 15 content slides, annexure divider and annexures A1-A8.

Usage: python3 build_deck.py <out.pptx> <storyboard.md>
"""
import sys

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

import content as C
import model as M
from deckkit import *  # noqa: F401,F403

OUT, STORYBOARD = sys.argv[1], sys.argv[2]
prs = new_presentation()
SB = []  # storyboard registry

B, U0, U1 = M.B, M.U0, M.U1
N = dict(
    eligible=M.lakh(B["eligible"]), exposed=M.lakh(B["exposed"]), activated=M.lakh(B["activated"], 2),
    repeat=M.lakh(B["repeat"], 2), mtu=f"{round(B['mtu'], -3):,.0f}", payments=M.lakh(B["payments"]),
    gmv_m=f"₹{B['gmv_month'] / 1e7:,.0f} crore", gmv_y=f"₹{M.r_cr(B['gmv_year'] / 1e7):,.0f} crore",
    gmv_c=f"₹{M.r_cr(M.F['cautious']['gmv_year'] / 1e7):,.0f}", gmv_u=f"{M.r_cr(M.F['upside']['gmv_year'] / 1e7):,.0f}",
    pool_m=f"₹{M.r3(B['pool_month'] / 1e7):,.0f} crore", pool_y=f"₹{B['pool_year'] / 1e12:.1f} lakh crore",
    sh_exp=f"{B['share_exposed'] * 100:.1f}", sh_el=f"{B['share_eligible'] * 100:.1f}",
    cpm=f"₹{round(U0['per_mtu'], -2):,.0f}", cpm_b=f"₹{round(U1['per_mtu'], -2):,.0f}",
    cpr=f"₹{U0['per_rupee']:.3f}", cpr_b=f"₹{U1['per_rupee']:.3f}",
    pilot_cpm=f"₹{round(U0['per_mtu_per_1000'], -1):,.0f}", mtu1000=f"{M.MTU_PER_1000:.0f}",
    half=f"₹{M.r_cr(M.SENS['Activation halved'] / 1e7):,.0f}", floor=f"₹{M.r_cr(M.SENS['Gap-days-only floor'] / 1e7):,.0f}",
    settle=f"₹{M.SETTLE_COST_PER_PAYMENT:.2f}",
)
assert N["gmv_y"] == "₹2,660 crore", N["gmv_y"]


def register(slide, num, role, headline, message, visual, chips, sources, anim, talk, guideline=""):
    notes(slide, talk)
    SB.append(dict(num=num, role=role, headline=headline, message=message, visual=visual, chips=chips,
                   sources=sources, anim=anim.log if anim else [], notes=talk, slide=slide, guideline=guideline))


# ================================================================== COVER
s = blank(prs, dark=True)
text(s, 0.8, 0.85, 8, 0.3, [[("PAYTM UPI GROWTH CHALLENGE  ·  TRACK B  ·  ROUND 2 FINAL SUBMISSION", dict(bold=True, color=SOFT, size=12))]], name="Eyebrow")
text(s, 0.8, 1.45, 7.7, 2.9, [[("Settle & Pay:", dict(size=52, bold=True, color=WHITE))],
                               [("making Paytm the place merchants spend the money they see arrive", dict(size=32, bold=True, color=WHITE))]],
     name="Title", line_spacing=0.95, spacing=6)
text(s, 0.8, 4.55, 7.5, 0.4, "Growing Paytm usage among merchants as UPI payers", size=18, color=SOFT, name="Subtitle")
text(s, 0.8, 5.45, 7.5, 0.95, [[("Team Paytitude", dict(size=22, bold=True, color=WHITE))], [("9 October 2026", dict(size=14, color=SOFT))]],
     name="Team", spacing=4)
ix, iy, iw = phone(s, 9.15, 0.85, 3.0, 5.75, "Paytm for Business", header_fill=NAVY2, name_prefix="cover")
text(s, ix, iy + 0.05, iw, 0.3, "Today's collections", size=11, color=GREY)
text(s, ix, iy + 0.35, iw, 0.55, "₹12,400", size=28, bold=True, color=NAVY)
for k, (a, who, t) in enumerate([("+₹350", "Ravi K.", "10:42"), ("+₹1,200", "Anita S.", "10:15"), ("+₹2,150", "UPI", "09:58"), ("+₹640", "Soundbox", "09:31")]):
    yy = iy + 1.05 + k * 0.48
    text(s, ix, yy, iw, 0.4, [[(a + "  ", dict(bold=True, color=INK)), (who, dict(color=GREY)), ("   " + t, dict(color=GREY, size=10))]], size=12)
    line(s, ix, yy + 0.42, ix + iw, yy + 0.42, color=GREY_XL, width=0.75)
text(s, ix, iy + 3.25, iw, 0.55, [[("Pay supplier", dict(bold=True, color=NAVY, size=14))]], fill=CYAN,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3, align="c", anchor="m", name="cover_cta")
text(s, ix, iy + 3.9, iw, 0.3, "Concept prototype", size=9, color=GREY, align="c")
transition(s, "fade")
register(s, "Cover", "Cover", "Settle & Pay: making Paytm the place merchants spend the money they see arrive",
         "Paytm can turn the screen where merchants see money arrive into the place they spend it.",
         "Dark navy; thesis title left; one concept phone right with the single cyan accent (Pay supplier).",
         [], "—", None,
         "Every day, merchants open Paytm to see their money arrive, then open another app to spend it. "
         "We are Team Paytitude, and our Round 2 submission is about that second moment. We stayed on Track B and on the same "
         "base of merchants we studied in Round 1: Paytm-collecting merchants who pay suppliers by UPI. What changed is how "
         "precisely we define them and how simply we solve for them. Our proposal is Settle & Pay: a Pay supplier button on the "
         "screen where the merchant already watches today's collections. It settles the money into the merchant's own account "
         "and pays the supplier by UPI in one flow. It has no loan and no cashback. In the next fifteen slides we show why the "
         "switch happens only when a step disappears, which merchants feel that step most, how the flow works within RBI's payout "
         "rules, how we will validate it, and the 90-day pilot that tells Paytm whether to scale, fix or stop.")

# ================================================================== 1 EXEC SUMMARY
H1 = ("Paytm can win merchants' supplier payments by letting them spend collections where they already see them; "
      "a 90-day pilot will prove it before scale")
s = blank(prs)
frame(s, 1, "Executive summary", H1,
      sources="Sources: Paytm Q1 FY27 release (S1); NPCI app-wise data, Aug 2026 (S2); synthetic VOC workbook (S16); model in annexure workbook (Funnel_Model, Share_Metric, Unit_Costs). Full source list: annexure A1 and 'Sources' sheet.")
bands = [
    ("PROBLEM\n& INSIGHT", [[("1.57 crore merchants collect on Paytm devices, but pay suppliers on PhonePe or Google Pay. ", dict(bold=True)),
                              ("Merchants won't switch apps for parity. They switch when a step disappears: waiting for settlement, or moving money between accounts.", {})]],
     ["fact", "synthetic"]),
    ("SOLUTION", [[("Settle & Pay ", dict(bold=True)), ("on the Paytm for Business collections screen: settle today's collections into the merchant's own account (no PIN), "
                   "then pay the supplier by UPI (one PIN). Free when it funds a supplier payment. No credit, no cashback.", {})]],
     ["concept"]),
    ("VALIDATION", [[("≥20-user prototype walkthrough with commitment asks: ", dict(bold=True)),
                     ("[results pending, n = __]", dict(bold=True, color=MAGENTA)),
                     (". Evidence so far is a 50-row synthetic dataset (hypothesis only): high-potential group 16 of 50, 7 yes / 9 maybe / 0 no.", {})]],
     ["validate", "synthetic"]),
    ("IMPACT\n& ASK", [[(f"Base case +{N['sh_el']} pts Paytm share of segment vendor-UPI value in year one ", dict(bold=True)),
                        (f"(+{N['sh_exp']} pts among exposed merchants); {N['gmv_y']} annual run-rate (range {N['gmv_c']}–{N['gmv_u']} crore); "
                         f"≈{N['cpm']} per extra active merchant. ", {}),
                        ("Ask: approve a 90-day randomised pilot, 3,000 vs 3,000 merchants.", dict(bold=True))]],
     ["projection"]),
]
band_shapes = []
for k, (lab, body, chips) in enumerate(bands):
    y = 1.82 + k * 0.94
    g = group(s, f"band{k + 1}")
    text(g, 0.6, y, 1.75, 0.84, [[(l, dict(bold=True, color=WHITE, size=12))] for l in lab.split("\n")], fill=NAVY,
         anchor="m", margin=0.12)
    text(g, 2.42, y, 8.55, 0.84, body, size=13, fill=PALE, anchor="m", margin=0.14)
    cy = y + 0.84 / 2 - (len(chips) * 0.27 - 0.05) / 2
    for c_i, c in enumerate(chips):
        chip(g, 12.73 - chip_w(c), cy + c_i * 0.27, c)
    band_shapes.append(g)
g = group(s, "changed")
text(g, 0.6, 5.62, 12.13, 0.8, [[("WHAT CHANGED SINCE ROUND 1   ", dict(bold=True, color=CYAN_D, size=11)),
                                  ("Same track and merchant base, re-cut by settlement behaviour · Supplier Pay → Settle & Pay · "
                                   "Dropped partner credit, supplier ledger, MDR framing and the ₹27,000 crore estimate · "
                                   "500-merchant Andheri pilot → 90-day randomised pilot with scale and stop gates · Detail: annexure A7", dict(size=12))]],
     line=CYAN, line_w=1.25, anchor="m", margin=0.14, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
text(s, 0.6, 6.55, 1.35, 0.25, "Evidence status:", size=10, bold=True, color=GREY, anchor="m")
xx = 1.95
for kind, lab in [("fact", "FACT (CITED)"), ("synthetic", "SYNTHETIC HYPOTHESIS"), ("projection", "PROJECTION, NOT FORECAST"),
                  ("validate", "TO VALIDATE"), ("validated", "VALIDATED (n = __)"), ("placeholder", "MAGENTA = AWAITING DATA")]:
    chip(s, xx, 6.565, kind, lab)
    xx += chip_w(kind, lab) + 0.1
transition(s, "fade")
a = Anim(s)
a.auto([fx(band_shapes[0], "fade", "after")] + [fx(b, "fade", "after", delay=200) for b in band_shapes[1:]] + [fx(g, "fade", "after", delay=200)],
       "Bands appear top to bottom automatically after the transition (Fade 0.45 s, 0.2 s stagger), then the Round 1 change band")
a.write()
register(s, 1, "Executive summary", H1,
         "Paytm can win supplier payments by removing the settlement step at the moment of payment, and should prove it with a 90-day pilot.",
         "Four horizontal bands (label block + body + status chips), a 'What changed since Round 1' band, and the evidence-status legend.",
         "Fact, Synthetic, To validate, Projection, Placeholder", "S1, S2, S16, workbook", a,
         "Here is the whole argument on one page. The problem: 1.57 crore merchants collect on Paytm devices, but their supplier payments, "
         "the business UPI they actually choose an app for, go through PhonePe or Google Pay. The insight: merchants don't switch apps for "
         "parity. They switch when a step disappears, and the step that hurts is waiting for settlement or moving money between accounts. "
         "The solution is Settle & Pay: settle today's collections into the merchant's own account and pay the supplier by UPI, in one flow, "
         "free when it funds a supplier payment, with no credit and no cashback. Validation: the twenty-user prototype test is being run now and "
         "its results go on slide ten. The only data so far is a synthetic stress-test set, which we label as such everywhere. Impact: our base "
         f"case is a {N['sh_el']}-point rise in Paytm's share of the segment's vendor UPI value, about {N['gmv_y']} a year, at roughly {N['cpm']} per extra "
         "active merchant, inside a very wide range. That range is why our ask is a 90-day randomised pilot rather than a launch. The band at the "
         "bottom shows what we changed since Round 1 and why.",
         guideline="Deliverable: one-slide executive summary; Round 1 continuity")

# ================================================================== 2 PROBLEM: SPLIT SCREEN
H2 = "Paytm owns the moment merchants' money arrives, and hands the moment they spend it to another app"
s = blank(prs, dark=True)
frame(s, 2, "The problem", H2, dark=True,
      sources="Sources: S1 Paytm Q1 FY27 release; S2 NPCI app-wise volume share, Aug 2026 (secondary report; confirm on npci.org.in); S3 Paytm for Business app listing; S16 synthetic VOC dataset. Screens are illustrative.")


def split_phone(container, x, header, fill, rows, name, cta=None, cta_fill=CYAN, foot=None, cta_color=WHITE):
    ix, iy, iw = phone(container, x, 1.95, 2.6, 3.85, header, header_fill=fill, name_prefix=name)
    for k, r in enumerate(rows):
        text(container, ix, iy + k * 0.42, iw, 0.4, [r] if isinstance(r, list) else r, size=12)
    if cta:
        text(container, ix, iy + 2.45, iw, 0.45, [[(cta, dict(bold=True, color=cta_color, size=12))]],
             fill=cta_fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3, align="c", anchor="m")
    if foot:
        text(container, ix, iy + 2.95, iw, 0.3, foot, size=10, color=GREY, align="c")


gL = group(s, "!!phoneL")
split_phone(gL, 0.75, "Paytm for Business", NAVY2,
            [[("Today's collections", dict(color=GREY, size=11))], [("₹12,400", dict(bold=True, size=22, color=NAVY))], "",
             [("+₹1,200 ", dict(bold=True)), ("Anita S.", dict(color=GREY))], [("+₹350 ", dict(bold=True)), ("Ravi K.", dict(color=GREY))]],
            "pL", cta="Settles next working day", cta_fill=GREY_XL, cta_color=GREY)
text(s, 0.75, 5.88, 2.6, 0.3, [[("MONEY IN  ·  PAYTM", dict(bold=True, color=CYAN, size=12))]], align="c", name="labelL")
gR = group(s, "!!phoneR")
split_phone(gR, 4.45, "Another UPI app", "4A5568",
            [[("Pay", dict(color=GREY, size=11))], [("Sharma Traders", dict(bold=True, size=14, color=INK))],
             [("₹6,800", dict(bold=True, size=22, color=INK))], [("From personal a/c ••2210", dict(color=GREY, size=11))], ""],
            "pR", cta="Enter UPI PIN", cta_fill="4A5568")
text(gR, 4.0, 5.88, 3.5, 0.3, [[("MONEY OUT  ·  PHONEPE OR GOOGLE PAY", dict(bold=True, color=WHITE, size=12))]], align="c")
arr = line(gR, 3.45, 3.85, 4.35, 3.85, color=SOFT, width=2, arrow=True)
bridge = text(s, 0.6, 6.25, 6.6, 0.45, [[("Same merchant. Same money. Different app.", dict(bold=True, color=CYAN, size=18))]], align="c",
              name="bridge")
tiles = [("1.57 crore", "merchants pay for Paytm payment devices (Q1 FY27)", "fact"),
         ("8.0%", "Paytm's share of UPI volume, vs PhonePe 45.6% and Google Pay 32.3% (NPCI, Aug 2026)", "fact"),
         ("Collect only", "Paytm for Business lists collections, settlements, statements and loans; no supplier payments (app listing)", "fact"),
         ("0 of 50", "synthetic merchants use Paytm as their main business-payment app; 29 use PhonePe, 15 Google Pay", "synthetic")]
for k, (big, desc, kind) in enumerate(tiles):
    y = 1.95 + k * 1.02
    box(s, 7.75, y, 4.98, 0.9, fill=NAVY2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
    text(s, 7.9, y + 0.08, 1.75, 0.5, [[(big, dict(bold=True, color=CYAN, size=22 if len(big) < 9 else 17))]], anchor="m")
    chip(s, 7.95, y + 0.62, kind, size=8, h=0.19)
    text(s, 9.65, y + 0.04, 2.98, 0.82, desc, size=12, color=WHITE, anchor="m")
transition(s, "fade")
a = Anim(s)
a.click([fx(gR, "fade")], "Right phone (money out on another app) fades in")
a.click([fx(bridge, "fade")], "Bridging line: 'Same merchant. Same money. Different app.'")
a.write()
register(s, 2, "Problem: contradiction", H2,
         "The merchant's money arrives on Paytm but is spent on another app.",
         "Split screen: two phones (money in on Paytm, money out on another app) with an arrow between; four fact tiles on the right.",
         "Fact ×3, Synthetic ×1", "S1, S2, S3, S16", a,
         "Start with one merchant and one rupee. On the left, the merchant opens Paytm for Business and watches today's collections arrive: "
         "twelve thousand four hundred rupees. Paytm owns that moment. 1.57 crore merchants now pay for Paytm devices, and every Soundbox "
         "announcement reinforces it. [click] But when the supplier wants six thousand eight hundred rupees, the merchant opens a different app. "
         "Paytm for Business is built to collect: its listing shows collections, settlements, statements and loans, but no supplier payments. "
         "So the outgoing business payment, the one where the merchant chooses the app, goes to PhonePe or Google Pay. That is part of why Paytm "
         "sits at about eight per cent of UPI volume while PhonePe has forty-six and Google Pay thirty-two. In our synthetic stress-test data, "
         "not one of fifty merchants used Paytm as their main business-payment app. [click] Same merchant. Same money. Different app. The rest "
         "of the deck is about closing that gap.",
         guideline="Problem; Round 1 continuity (same segment)")

# ================================================================== 3 ROOT CAUSE
H3 = "The habit Paytm wants already exists. Merchants won't switch for a better button, only when a step disappears"
s = blank(prs)
frame(s, 3, "The problem · root cause", H3,
      sources="Source: S16 synthetic VOC dataset (counts of 50 rows; illustrative, not market prevalence). Quotes are dataset responses, not interviewed merchants.")
text(s, 0.6, 1.85, 5.1, 0.3, [[("APP SWITCHING, NOT UPI ADOPTION", dict(bold=True, color=GREY, size=11))]])
gA = group(s, "colA")
text(gA, 0.6, 2.2, 2.45, 3.55, [[("UPI adoption", dict(bold=True, size=15, color=GREY))], "",
                                 "Teach merchants to pay by UPI", "", "Get suppliers to accept UPI", "", "Move payments off cash and NEFT", "",
                                 [("Not the problem", dict(bold=True, color=GREY))]],
     size=12, color=GREY, fill=GREY_XL, margin=0.16, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06, spacing=0)
text(gA, 3.2, 2.2, 2.5, 3.55, [[("App switching", dict(bold=True, size=15, color=NAVY))], "",
                                [("41 of 50", dict(bold=True)), " already pay vendors by UPI at least 2–3 times a week"], "",
                                "The merchant, not the supplier, picks the app: any UPI app pays any QR", "",
                                [("Habit to beat: ", dict(bold=True)), "PhonePe 29, Google Pay 15 of 50"], "",
                                [("The problem", dict(bold=True, color=CYAN_D))]],
     size=12, color=INK, fill=PALE, line=CYAN, line_w=1.5, margin=0.16, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06, spacing=0)
chip(s, 3.32, 5.85, "synthetic")
# root cause tree
sym = text(s, 7.2, 1.85, 4.4, 0.55, "Paytm collectors pay suppliers on another app", size=13, bold=True, color=INK, fill="D5DCE4",
           align="c", anchor="m", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2, name="symptom")
gNav = group(s, "causes_navy")
line(gNav, 9.4, 2.4, 7.65, 2.75, color=GREY_L, width=1.25)
text(gNav, 6.1, 2.78, 3.1, 0.3, [[("WHAT KEEPS THEM WHERE THEY ARE", dict(bold=True, color=NAVY, size=10))]])
for k, t in enumerate(["Same steps on every app (parity)", "Habit and staff familiarity", "Supplier's QR on WhatsApp opens in the current app"]):
    text(gNav, 6.1, 3.12 + k * 0.6, 3.1, 0.52, t, size=12, color=WHITE, fill=NAVY, anchor="m", margin=0.1,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
gCy = group(s, "causes_cyan")
line(gCy, 9.4, 2.4, 11.15, 2.75, color=CYAN, width=1.5)
text(gCy, 9.55, 2.78, 3.18, 0.3, [[("STEPS PAYTM CAN REMOVE", dict(bold=True, color=CYAN_D, size=10))]])
cy_boxes = []
for k, t in enumerate(["Waiting for collections to settle before paying", "Moving money from the settlement account to the paying account"]):
    cy_boxes.append(text(gCy, 9.55, 3.12 + k * 0.9, 3.18, 0.8, t, size=12, bold=True, color=NAVY, fill=CYAN, anchor="m", margin=0.1,
                         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12))
for k, (q, src) in enumerate([("“Same steps hain toh app kyun badlu?”", "If the steps are the same, why change apps?"),
                              ("“Subah supplier ko paisa chahiye, collection baad mein settle hota hai.”", "The supplier wants money in the morning; collections settle later.")]):
    text(s, 6.1 + k * 3.35, 5.05, 3.25, 0.85, [[(q, dict(italic=True, bold=True, color=NAVY, size=12))], [(src, dict(color=GREY, size=10))]],
         fill=GREY_XL, margin=0.1, anchor="m", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
text(s, 6.1, 5.93, 6.6, 0.25, "Synthetic-dataset verbatims: illustrations only, never counted as evidence", size=9, color=GREY, italic=True)
resolve = text(s, 0.6, 6.3, 12.13, 0.45, [[("Remove a step, and merchants have a reason to switch. Match a step, and they don't.",
                                             dict(bold=True, color=NAVY, size=17))]], align="c", name="resolve")
transition(s, "fade")
a = Anim(s)
a.click([fx(sym, "fade"), fx(gNav, "fade", "after")], "Symptom, then the three navy causes that keep merchants on their current app")
a.click([fx(gCy, "fade"), fx(cy_boxes[0], "pulse", "after"), fx(cy_boxes[1], "pulse", "with")],
        "The two cyan causes Paytm can remove, with one emphasis pulse")
a.click([fx(resolve, "fade")], "Resolving line")
a.write()
register(s, 3, "Problem: root cause", H3,
         "This is app switching, not UPI adoption, and only removing a step gives merchants a reason to switch.",
         "Left: two-column comparison (UPI adoption vs app switching). Right: root-cause tree, symptom grey, causes navy, removable causes cyan; two labelled synthetic verbatims; resolving line.",
         "Synthetic", "S16", a,
         "The first thing to get right is what kind of problem this is. It is not UPI adoption. In our stress-test data, forty-one of fifty "
         "merchants already pay vendors by UPI at least two or three times a week. And because any UPI app can pay any QR, the merchant, not "
         "the supplier, decides which app gets the payment. So Paytm is competing with a habit, mostly PhonePe and Google Pay. [click] Why do "
         "merchants stay where they are? Because every app has the same steps, staff already know the app, and the supplier's QR arrives on "
         "WhatsApp and opens in whatever app is already there. 'Same steps hain toh app kyun badlu?' Parity features can't beat that. [click] "
         "But two causes are different, because Paytm can remove them: waiting for collections to settle before paying the supplier, and "
         "moving money from the settlement account to the account the merchant pays from. [click] That is the design rule for everything that "
         "follows. Remove a step, and merchants have a reason to switch. Match a step, and they don't.",
         guideline="Problem diagnosis; Round 1 continuity")

# ================================================================== 4 TODAY'S JOURNEY
H4 = "Paying a supplier from today's sales takes up to four steps across two apps"
s = blank(prs)
frame(s, 4, "The problem · today's journey", H4,
      sources="Sources: S4 Paytm for Business support (settlement timing); S5 Paytm Payments docs; S3 app listing (manual instant settlement); S6, S7 PhonePe merchant help (Settle Now). Amounts illustrative.")
steps = [("1", "Check collections", "Open Paytm for Business: ₹12,400 collected today.", "Paytm for Business", NAVY),
         ("2", "Settle or wait", "Trigger manual instant settlement, if the merchant knows it exists, or wait for T+1.", "Paytm for Business", NAVY),
         ("3", "Transfer, if accounts differ", "Move money from the settlement current account to the account the UPI app pays from.", "Other UPI app", "4A5568"),
         ("4", "Switch app and pay", "Open PhonePe or Google Pay, scan the supplier's QR, enter the UPI PIN.", "Other UPI app", "4A5568")]
step_groups, arrows = [], []
for k, (n, t, d, app, col) in enumerate(steps):
    x = 0.6 + k * 2.62
    g = group(s, f"!!step{n}")
    box(g, x, 1.95, 2.25, 2.7, fill=PALE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    text(g, x + 0.15, 2.08, 0.5, 0.5, [[(n, dict(bold=True, color=NAVY, size=18))]], fill=CYAN, shape=MSO_SHAPE.OVAL, align="c", anchor="m", margin=0)
    text(g, x + 0.75, 2.17, 1.4, 0.32, [[(app, dict(bold=True, color=WHITE, size=9))]], fill=col, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
         radius=0.5, align="c", anchor="m", margin=0.02)
    text(g, x + 0.15, 2.72, 1.98, 0.62, t, size=15, bold=True, color=NAVY)
    text(g, x + 0.15, 3.35, 1.98, 1.25, d, size=12, color=INK)
    step_groups.append(g)
    if k < 3:
        arrows.append(line(s, x + 2.28, 3.3, x + 2.59, 3.3, color=GREY, width=1.75, arrow=True))
counters = []
for k, (big, small) in enumerate([("1", "step · 1 app"), ("2", "steps · 1 app + a wait"), ("3", "steps · 2 apps"), ("4", "steps · 2 apps")]):
    counters.append(text(s, 11.12, 1.95, 1.61, 2.7, [[(big, dict(bold=True, color=CYAN_D, size=66))], [(small, dict(bold=True, color=NAVY, size=13))]],
                         fill=WHITE, line=GREY_L, align="c", anchor="m", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08, name=f"counter{k + 1}"))
text(s, 0.6, 4.95, 6.0, 1.75, [[("PAYTM'S OWN SETTLEMENT TIMING", dict(bold=True, color=GREY, size=10))],
                                [("“Usually settled to your bank within T+1 days”", dict(bold=True, color=NAVY, size=13)), (" (Paytm for Business support)", dict(color=GREY, size=11))],
                                [("“Within a few business hours or at the T+N cycle”", dict(bold=True, color=NAVY, size=13)), (" (Paytm Payments docs)", dict(color=GREY, size=11))],
                                [("Manual instant settlement exists, but the merchant still pays from another app.", dict(size=12))]],
     fill=GREY_XL, margin=0.15, spacing=3, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
chip(s, 5.55, 5.05, "fact")
text(s, 6.85, 4.95, 5.88, 1.75, [[("COMPETITOR EARLY SETTLEMENT STOPS AT STEP 2", dict(bold=True, color=GREY, size=10))],
                                  [("PhonePe 'Settle Now': ", dict(bold=True, color=NAVY, size=13)),
                                   ("₹1–3 a request, once an hour, not after 11 pm, for selected merchants only.", dict(size=13))],
                                  [("Then the merchant still opens another screen to pay the supplier. Nobody joins settlement and payment.", dict(size=12))]],
     fill=GREY_XL, margin=0.15, spacing=3, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
chip(s, 12.0, 5.05, "fact")
transition(s, "fade")
a = Anim(s)
for k in range(4):
    eff = [fx(step_groups[k], "fade")]
    if k > 0:
        eff.insert(0, fx(arrows[k - 1], "wipe-left", dur=300))
    eff.append(fx(counters[k], "fade", "with", dur=300))
    a.click(eff, f"Step {k + 1} appears; the step counter shows {k + 1}")
a.write()
register(s, 4, "Problem: friction", H4,
         "Paying a supplier from today's collections takes up to four steps across two apps, and nobody joins settlement and payment.",
         "Numbered horizontal journey (4 cards with app tags, arrows) with a step counter; two fact callouts on settlement timing and PhonePe Settle Now.",
         "Fact", "S3, S4, S5, S6, S7", a,
         "Here is what that step looks like today, for a merchant whose collections settle the next day or into a separate current account. "
         "[click] Step one: open Paytm for Business and see twelve thousand four hundred rupees collected. [click] Step two: settle it. Paytm does "
         "offer manual instant settlement, but in our stress-test data many merchants complaining about the wait don't seem to know it exists. "
         "The default, in Paytm's own words, is 'usually within T+1 days'. So the merchant either triggers settlement or waits. [click] Step "
         "three: if the money lands in a current account that the UPI app doesn't pay from, move it. [click] Step four: switch to PhonePe or "
         "Google Pay, scan the supplier's QR and enter the PIN. Four steps, two apps, and sometimes a wait. Note the competitor: PhonePe charges "
         "one to three rupees for Settle Now, once an hour, not after eleven at night, and only for selected merchants. And then its merchant "
         "still has to pay from another screen. Nobody joins the two halves of this journey.",
         guideline="Design: user journey before (Guideline 2)")

# ================================================================== 5 SEGMENT
H5 = "Start with merchants whose money arrives late or lands elsewhere; Paytm can find them in its own data"
s = blank(prs)
frame(s, 5, "Target segment", H5,
      sources="Source: S16 synthetic VOC dataset, 40 of 42 regular Paytm collectors (2 accountant-led excluded); counts per quadrant computed in annexure workbook 'Segment_Rules'. Illustrates the hypothesis, not market prevalence.")
text(s, 0.6, 1.9, 0.75, 1.95, [[("Friction", dict(bold=True, color=NAVY, size=12))], [("stated", dict(color=GREY, size=11))]], anchor="m")
text(s, 0.6, 3.95, 0.75, 1.95, [[("No", dict(bold=True, color=NAVY, size=12))], [("friction", dict(color=GREY, size=11))]], anchor="m")
text(s, 1.4, 5.98, 2.95, 0.3, "Same-day settlement", size=12, bold=True, color=NAVY, align="c")
text(s, 4.45, 5.98, 2.95, 0.3, "Next day, or into a separate account", size=12, bold=True, color=NAVY, align="c")
text(s, 1.4, 6.3, 6.0, 0.25, "SETTLEMENT PROFILE OF PAYTM COLLECTIONS  →", size=9, bold=True, color=GREY, align="c")


def quad(container, x, y, title, n, split, note, fill=GREY_XL, fg=INK, name=None):
    return text(container, x, y, 2.95, 1.95, [[(title, dict(bold=True, size=11, color=fg))], [(n, dict(bold=True, size=24, color=fg))],
                                               [(split, dict(bold=True, size=12, color=fg))], [(note, dict(size=12, color=fg))]],
                fill=fill, margin=0.14, spacing=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05, name=name)


q_tl = quad(s, 1.4, 1.9, "SAME DAY + FRICTION", "9", "4 yes · 3 maybe · 2 no", "7 of 9 rows contradictory: same-day yet 'waiting for settlement'", name="q_tl")
q_bl = quad(s, 1.4, 3.95, "SAME DAY + NO FRICTION", "8", "0 yes · 2 maybe · 6 no", "“Mera settlement same day aa jata hai, toh problem kya hai?”", name="q_bl")
q_br = quad(s, 4.45, 3.95, "NEXT DAY / SEPARATE + NO FRICTION", "7", "0 yes · 5 maybe · 2 no", "All 7: 'would try it, but keep my current app'", name="q_br")
gT = group(s, "q_target")
quad(gT, 4.45, 1.9, "NEXT DAY / SEPARATE + FRICTION", "16 · Group 1", "7 yes · 9 maybe · 0 no", "No 'no' at all: the target quadrant", fill=CYAN, fg=NAVY)
text(gT, 6.2, 3.55, 1.1, 0.26, [[("TARGET", dict(bold=True, color=WHITE, size=9))]], fill=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5, align="c", anchor="m", margin=0.02)
chip(s, 6.05, 6.3, "synthetic")
# right panel
text(s, 7.75, 1.9, 4.98, 2.05, [[("SEGMENT RULES (ALL FIVE)", dict(bold=True, color=GREY, size=10))],
                                 "1  Collects on a Paytm QR or Soundbox", "2  Settles next day, or into a separate current account",
                                 "3  Pays vendors by UPI at least weekly", "4  Owner or manager chooses the app",
                                 "5  States a timing, transfer or staff-control friction"],
     size=12, color=INK, fill=PALE, margin=0.14, spacing=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
gC = group(s, "contrast")
box(gC, 7.75, 4.08, 4.98, 1.25, fill=WHITE, line=GREY_L, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
text(gC, 7.9, 4.13, 4.7, 0.28, [[("WOULD SWITCH: YES / MAYBE / NO", dict(bold=True, color=GREY, size=10))]])
for k, (lab, yes, maybe, no) in enumerate([("Group 1 (16)", 7, 9, 0), ("Group 3 (18)", 1, 4, 13)]):
    yy = 4.48 + k * 0.4
    text(gC, 7.9, yy, 1.25, 0.32, lab, size=12, bold=True, color=NAVY, anchor="m")
    xx, scale = 9.15, 3.4 / 18
    for v, col, fg in [(yes, NAVY, WHITE), (maybe, CYAN, NAVY), (no, GREY_L, INK)]:
        if v:
            text(gC, xx, yy, v * scale, 0.32, [[(str(v), dict(bold=True, color=fg, size=11))]], fill=col, align="c", anchor="m", margin=0)
            xx += v * scale
chip(gC, 11.6, 4.14, "synthetic", size=8, h=0.19)
text(s, 7.75, 5.45, 4.98, 1.25, [[("HOW PAYTM FINDS THEM: INTERNAL DATA REQUEST", dict(bold=True, color=GREY, size=10))],
                                  "Settlement cycle and destination account per device merchant; share already using manual instant settlement; outgoing UPI pattern where visible"],
     size=12, color=INK, fill=GREY_XL, margin=0.14, spacing=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
chip(s, 11.6, 5.52, "validate", size=8, h=0.19)
transition(s, "fade")
a = Anim(s)
a.click([fx(q_bl, "fade"), fx(q_tl, "fade", "after", delay=100), fx(q_br, "fade", "after", delay=100)], "Three non-target quadrants appear")
a.click([fx(gT, "fade"), fx(gT, "pulse", "after")], "Target quadrant (Group 1) highlighted, one pulse")
a.write()
register(s, 5, "Segment", H5,
         "Target merchants with next-day or separate-account settlement and a stated friction; Paytm can find them from its own settlement data.",
         "2×2 matrix (settlement profile × stated friction) with synthetic counts and switch splits, target quadrant in cyan; right panel with the five rules, Group 1 vs Group 3 bars, and the internal data request.",
         "Synthetic, To validate", "S16; workbook Segment_Rules", a,
         "Who should Paytm start with? Not everyone. We sort Paytm collectors on two things Paytm can observe or ask: when and where their "
         "collections settle, and whether they state a real friction. [click] Three quadrants are weak. Same-day merchants with no friction "
         "mostly say no: 'my settlement comes the same day, so what's the problem?' Next-day merchants without a friction say they'd try it but "
         "keep their current app. The same-day-with-friction box looks interesting, but seven of its nine rows are contradictory in the dataset, "
         "so we don't build on it. [click] The target is the top-right quadrant: money arrives the next day or lands in a separate account, and "
         "the merchant feels it. Sixteen of fifty rows; seven yes, nine maybe, and not a single no. Compare Group 3: one yes, thirteen no. These "
         "are synthetic counts, so they show the logic, not the market size. The good news is that the first two rules are already in Paytm's "
         "settlement data. Our first data request is the share of device merchants on next-day or separate-account settlement, and how many "
         "already use manual instant settlement.",
         guideline="GTM: target segment; Round 1 continuity (segment narrowed by behaviour)")

# ================================================================== 6 MECHANISM
H6 = "Settle & Pay turns today's collections into a supplier payment in one flow built to fit RBI's payout rules, with no loan"
s = blank(prs, dark=True)
frame(s, 6, "The solution", H6, dark=True,
      sources="RBI (Regulation of Payment Aggregators) Directions, 15 Sep 2025 (S9). Payout restriction per legal summaries (S10, S11); primary RBI text to be confirmed. Compliance confirmation of free conditional settlement pending. Amounts illustrative.")


def node(container, x, title, big, sub, fill=NAVY2, name=None):
    return text(container, x, 2.2, 3.0, 1.75, [[(title, dict(bold=True, color=SOFT, size=11))], [(big, dict(bold=True, color=WHITE, size=20))],
                                                [(sub, dict(color=WHITE, size=12))]],
                fill=fill, line=NAVY3, margin=0.16, spacing=3, anchor="m", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08, name=name)


nA = node(s, 0.6, "PAYTM COLLECTIONS", "₹12,400 today", "Already received from customers, not yet settled", name="nodeA")
gL1 = group(s, "leg1")
line(gL1, 3.68, 3.07, 5.07, 3.07, color=CYAN, width=4, arrow=True)
text(gL1, 3.55, 2.22, 1.65, 0.75, [[("LEG 1", dict(bold=True, color=CYAN, size=11))], [("Settle ₹6,800", dict(bold=True, color=WHITE, size=13))]], align="c")
text(gL1, 3.55, 3.2, 1.65, 0.75, [[("No PIN · free when", dict(color=SOFT, size=12))], [("it funds a supplier", dict(color=SOFT, size=12))]], align="c")
node(gL1, 5.15, "MERCHANT'S OWN ACCOUNT", "Current a/c ••4821", "Money is the merchant's before it moves on")
gL2 = group(s, "leg2")
line(gL2, 8.23, 3.07, 9.62, 3.07, color=CYAN, width=4, arrow=True)
text(gL2, 8.1, 2.22, 1.65, 0.75, [[("LEG 2", dict(bold=True, color=CYAN, size=11))], [("Pay by UPI", dict(bold=True, color=WHITE, size=13))]], align="c")
text(gL2, 8.1, 3.2, 1.65, 0.75, [[("One UPI PIN", dict(color=SOFT, size=12))], [("ordinary UPI credit", dict(color=SOFT, size=12))]], align="c")
node(gL2, 9.7, "SUPPLIER", "Sharma Traders", "Sees a normal UPI payment")
gX = group(s, "crossed")
line(gX, 2.1, 3.97, 2.1, 4.55, color=RED, width=2, dash=True)
line(gX, 2.1, 4.55, 11.2, 4.55, color=RED, width=2, dash=True)
line(gX, 11.2, 4.55, 11.2, 4.0, color=RED, width=2, dash=True, arrow=True)
text(gX, 6.35, 4.3, 0.5, 0.5, [[("✕", dict(bold=True, color=WHITE, size=18))]], fill=RED, shape=MSO_SHAPE.OVAL, align="c", anchor="m", margin=0)
text(gX, 2.3, 4.68, 8.7, 0.62, [[("Not this: Paytm paying the supplier straight from collections. ", dict(bold=True, color="FF8A80", size=12)),
                                  ("RBI's 2025 rules allow third-party payouts only for merchants above ₹40 lakh turnover, and only to the customer-facing payee.",
                                   dict(color=WHITE, size=12))]], align="c")
pills = ["Free when it funds a supplier payment", "Settles only collections already received: designed to avoid pre-funding; compliance confirmation pending",
         "No credit · no cashback · personal UPI untouched"]
pw = [3.05, 5.6, 3.2]
xx = 0.6
for t, w in zip(pills, pw):
    text(s, xx, 5.75, w, 0.85, [[(t, dict(bold=True, color=NAVY if t.startswith("Free") else WHITE, size=12))]],
         fill=CYAN if t.startswith("Free") else NAVY2, line=None if t.startswith("Free") else NAVY3, align="c", anchor="m", margin=0.12,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2)
    xx += w + 0.14
transition(s, "fade")
a = Anim(s)
a.click([fx(gL1, "wipe-left", dur=700)], "Leg 1 wipes left to right: settle into the merchant's own account")
a.click([fx(gL2, "wipe-left", dur=700)], "Leg 2 wipes left to right: merchant pays supplier by UPI")
a.click([fx(gX, "fade")], "Crossed-out direct-payout path appears")
a.write()
register(s, 6, "Solution: mechanism", H6,
         "Settle & Pay is one flow with two legs: settle received collections into the merchant's own account, then pay the supplier by UPI.",
         "Three-node mechanism diagram (collections → merchant's own account → supplier), built one leg per click; crossed-out red direct path below; three principle pills.",
         "Footnoted regulation; compliance pending", "S9, S10, S11", a,
         "This is the product. On the left are collections Paytm has already received for the merchant today: twelve thousand four hundred "
         "rupees. [click] Leg one: Paytm settles exactly what the supplier needs, six thousand eight hundred rupees, into the merchant's own "
         "current account. No PIN is needed for a settlement, and it is free when it funds a supplier payment. [click] Leg two: the merchant "
         "pays the supplier by UPI from that account with one PIN. The supplier sees an ordinary UPI credit. [click] Notice what we do not do. "
         "Paytm does not pay the supplier straight out of collections. Under RBI's 2025 payment aggregator directions, as summarised by two law "
         "firms, third-party payouts are only for merchants above forty lakh turnover, and only to the customer-facing payee. Most of our "
         "merchants don't qualify, so the money always becomes the merchant's first. Because we only settle money already received, the "
         "design avoids pre-funding; compliance still has to confirm that treatment and the conditional free pricing. And there is no loan, "
         "no cashback, and the merchant's personal UPI stays untouched.",
         guideline="Design: Paytm features used; regulatory dependencies")

# ================================================================== 7 BEFORE / AFTER
H7 = "Four steps across two apps become one flow and one PIN"
s = blank(prs)
frame(s, 7, "Design · before and after", H7,
      sources="Before: slide 4 journey. After: concept flow (light pilot build hands off to the Paytm UPI app with the supplier prefilled; the full in-app flow follows the scale gate). Settlement-to-credit time by bank is to be validated.")
text(s, 0.6, 2.0, 1.2, 1.2, [[("BEFORE", dict(bold=True, color=GREY, size=14))], [("4 steps", dict(bold=True, color=INK, size=12))],
                               [("2 apps · a wait", dict(color=INK, size=12))]], anchor="m")
before = [("1", "Check collections"), ("2", "Settle or wait"), ("3", "Transfer, if accounts differ"), ("4", "Switch app and pay")]
for k, (n, t) in enumerate(before):
    x = 1.9 + k * 2.72
    g = group(s, f"!!step{n}")
    box(g, x, 2.0, 2.45, 1.2, fill=GREY_XL, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
    text(g, x + 0.12, 2.1, 0.42, 0.42, [[(n, dict(bold=True, color=WHITE, size=14))]], fill=GREY, shape=MSO_SHAPE.OVAL, align="c", anchor="m", margin=0)
    text(g, x + 0.12, 2.56, 2.2, 0.6, t, size=15, bold=True, color=GREY)
    if k < 3:
        line(s, x + 2.48, 2.6, x + 2.69, 2.6, color=GREY_L, width=1.5, arrow=True)
text(s, 0.6, 3.7, 1.2, 1.5, [[("AFTER", dict(bold=True, color=CYAN_D, size=14))], [("1 flow", dict(bold=True, color=INK, size=12))],
                              [("1 app · 1 PIN", dict(color=INK, size=12))]], anchor="m", name="afterLabel")
gF = group(s, "!!flow")
box(gF, 1.9, 3.7, 10.83, 1.5, fill=PALE, line=CYAN, line_w=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
sub = [("Tap 'Pay supplier'", "on the collections screen the merchant already has open"),
       ("Pick or scan the supplier", "payee name check, then 'Settle & Pay from today's collections · free'"),
       ("Enter one UPI PIN", "settlement lands in the merchant's own account, then the supplier is paid")]
for k, (t, d) in enumerate(sub):
    x = 2.1 + k * 3.55
    text(gF, x, 3.88, 0.42, 0.42, [[(str(k + 1), dict(bold=True, color=NAVY, size=14))]], fill=CYAN, shape=MSO_SHAPE.OVAL, align="c", anchor="m", margin=0)
    text(gF, x + 0.52, 3.84, 2.75, 1.3, [[(t, dict(bold=True, color=NAVY, size=15))], [(d, dict(size=13, color=INK))]], spacing=2)
    if k < 2:
        line(gF, x + 3.3, 4.09, x + 3.5, 4.09, color=CYAN_D, width=1.5, arrow=True)
gM = group(s, "metrics")
for k, (lab, b4, af, chipk) in enumerate([("Apps", "2", "1", None), ("Steps", "4", "1 flow, 3 taps", None),
                                          ("Wait for settlement", "up to T+1", "seconds to minutes", "validate")]):
    x = 0.6 + k * 4.1
    text(gM, x, 5.65, 3.95, 0.85, [[(lab.upper(), dict(bold=True, color=GREY, size=10))],
                                    [(b4, dict(bold=True, color=GREY, size=16)), ("  →  ", dict(color=GREY, size=16)), (af, dict(bold=True, color=NAVY, size=16))]],
         fill=GREY_XL, margin=0.14, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
    if chipk:
        chip(gM, x + 2.75, 5.72, chipk, size=8, h=0.19)
transition(s, "fade")
a = Anim(s)
a.click([fx(gF, "fade", dur=600), fx(gF, "pulse", "after")], "The single after-flow appears beneath the greyed four-step row, one pulse")
a.click([fx(gM, "fade")], "Before → after metrics")
a.write()
register(s, 7, "Design: before/after", H7,
         "The four-step, two-app journey becomes one flow with one PIN.",
         "Before row: slide 4's four steps, greyed (same !!step names). After row: one wide flow card with three sub-steps (named !!flow, Morphs into slide 8's strip). Three before→after metric pills.",
         "To validate (settlement credit time)", "Slide 4 sources; concept", a,
         "Here is the same journey, before and after. The top row is today: four steps, two apps, and a wait. [click] The bottom row is "
         "Settle & Pay. The merchant taps 'Pay supplier' on the collections screen they already have open. They pick or scan the supplier, "
         "see the verified name, and choose 'Settle & Pay from today's collections, free'. Then one UPI PIN. Behind that PIN, Paytm settles "
         "the amount into the merchant's own account and the payment goes out once the credit is confirmed. [click] Two apps become one. Four "
         "steps become one flow of three taps. And the wait for settlement drops from up to a working day to seconds or minutes, which we still "
         "have to confirm bank by bank. One honest caveat: the pilot's light build reaches the same outcome with a hand-off to the Paytm UPI "
         "app, supplier prefilled. The fully in-app flow comes only after the scale gate.",
         guideline="Design: before and after journey, both in full (Guideline 2)")

# ================================================================== 8 CONCEPT SCREENS
H8 = "The merchant never leaves the screen where the money arrives"
s = blank(prs)
frame(s, 8, "Design · concept prototype", H8,
      sources="Concept prototype drawn for this submission: fictional names, amounts and account numbers; not Paytm's live interface. Payee name check, QR scan and notifications reuse existing Paytm capabilities.")
gS = group(s, "!!flow")
text(gS, 0.6, 1.72, 9.4, 0.36, [[("One flow, three screens:  ", dict(bold=True, color=NAVY, size=12)),
                                  ("collections  →  funding choice  →  confirmation, plus a next-morning prompt", dict(color=INK, size=12))]],
     fill=PALE, line=CYAN, line_w=1.25, anchor="m", margin=0.12, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3)
chip(s, 10.2, 1.79, "concept")
phones = []
# phone 1
g1 = group(s, "screen1")
ix, iy, iw = phone(g1, 0.7, 2.25, 2.75, 3.95, "Paytm for Business", header_fill=NAVY, name_prefix="s1")
text(g1, ix, iy, iw, 0.25, "Today's collections", size=10, color=GREY)
text(g1, ix, iy + 0.22, iw, 0.45, "₹12,400", size=22, bold=True, color=NAVY)
for k, (amt, who) in enumerate([("+₹1,200", "Anita S."), ("+₹350", "Ravi K."), ("+₹2,150", "UPI")]):
    text(g1, ix, iy + 0.78 + k * 0.36, iw, 0.32, [[(amt + "  ", dict(bold=True)), (who, dict(color=GREY))]], size=11)
text(g1, ix, iy + 1.95, iw, 0.45, [[("Pay supplier", dict(bold=True, color=NAVY, size=13))]], fill=CYAN, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
     radius=0.3, align="c", anchor="m")
text(g1, ix, iy + 2.48, iw, 0.4, "Settlement: next working day", size=9, color=GREY, align="c")
phones.append(g1)
# phone 2
g2 = group(s, "screen2")
ix, iy, iw = phone(g2, 3.95, 2.25, 2.75, 3.95, "Pay supplier", header_fill=NAVY, name_prefix="s2")
text(g2, ix, iy, iw, 0.3, "Sharma Traders", size=13, bold=True, color=INK)
text(g2, ix, iy + 0.28, iw, 0.25, "✓ Name verified: SHARMA TRADERS", size=9, bold=True, color=GREEN)
text(g2, ix, iy + 0.52, iw, 0.42, "₹6,800", size=20, bold=True, color=INK)
text(g2, ix, iy + 1.0, iw, 0.85, [[("Settle & Pay from today's collections", dict(bold=True, color=NAVY, size=10))],
                                   [("₹12,400 available · free", dict(color=INK, size=10))], [("Into current a/c ••4821", dict(color=GREY, size=9))]],
     fill=PALE, line=CYAN, line_w=1.75, margin=0.07, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
text(g2, ix, iy + 1.93, iw, 0.32, "Pay from bank balance", size=10, color=GREY, fill=GREY_XL, margin=0.07, anchor="m",
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
text(g2, ix, iy + 2.35, iw, 0.45, [[("Pay with UPI PIN", dict(bold=True, color=WHITE, size=12))]], fill=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
     radius=0.3, align="c", anchor="m")
phones.append(g2)
# phone 3
g3 = group(s, "screen3")
ix, iy, iw = phone(g3, 7.2, 2.25, 2.75, 3.95, "Payment successful", header_fill=GREEN, name_prefix="s3")
text(g3, ix + iw / 2 - 0.27, iy + 0.02, 0.54, 0.54, [[("✓", dict(bold=True, color=WHITE, size=18))]], fill=GREEN, shape=MSO_SHAPE.OVAL, align="c", anchor="m", margin=0)
text(g3, ix, iy + 0.62, iw, 0.5, [[("₹6,800 paid to", dict(bold=True, size=12, color=INK))], [("Sharma Traders", dict(bold=True, size=12, color=INK))]], align="c")
text(g3, ix, iy + 1.12, iw, 0.25, "UPI ref 6281 4402 1193", size=9, color=GREY, align="c")
text(g3, ix, iy + 1.42, iw, 0.85, [[("Today", dict(bold=True, color=NAVY, size=10))], [("₹38,900 collected", dict(size=10))],
                                    [("₹6,800 paid to suppliers", dict(size=10, bold=True, color=CYAN_D))], [("₹32,100 to settle", dict(size=10))]],
     fill=PALE, margin=0.07, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
text(g3, ix, iy + 2.38, iw, 0.42, [[("Share receipt on WhatsApp", dict(bold=True, color=NAVY, size=11))]], line=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
     radius=0.3, align="c", anchor="m")
phones.append(g3)
caps = ["1 · Pay supplier sits where the money arrives", "2 · Funding choice, with payee name check", "3 · Confirmation with a settlement summary"]
cap_shapes = []
for k, c in enumerate(caps):
    cap_shapes.append(text(s, 0.7 + k * 3.25, 6.27, 2.75, 0.5, c, size=12, bold=True, color=NAVY, align="c"))
gN = group(s, "notification")
text(gN, 10.35, 2.25, 2.38, 1.65, [[("Paytm for Business · 8:05 am", dict(bold=True, color=GREY, size=9))],
                                    [("₹9,250 from yesterday's collections is ready for supplier payments. Tap to pay.", dict(bold=True, color=INK, size=12))]],
     fill=WHITE, line=GREY_L, margin=0.12, spacing=3, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
text(gN, 10.35, 4.0, 2.38, 0.8, "4 · Next morning: the prompt that restarts the habit", size=12, bold=True, color=NAVY, align="c")
transition(s, "morph")
a = Anim(s)
for k in range(3):
    a.click([fx(phones[k], "fade"), fx(cap_shapes[k], "fade", "with")], f"Screen {k + 1} enters (left to right)")
a.click([fx(gN, "wipe-down", dur=500)], "Morning notification slides in last")
a.write()
register(s, 8, "Design: prototype", H8,
         "The whole job happens on the screen where the merchant already watches money arrive.",
         "Three phone mock-ups (collections, funding choice with name check, confirmation with settlement summary) plus a morning notification; labelled concept prototype.",
         "Concept prototype", "Concept; existing Paytm capabilities", a,
         "This is what it looks like. The transition you just saw is the after-flow collapsing into this strip: one flow, three screens. "
         "[click] Screen one is the collections screen merchants already open many times a day. The only new element is the Pay supplier "
         "button. [click] Screen two is the funding choice. The merchant has scanned the supplier's QR from WhatsApp; Paytm shows the verified "
         "name before anything moves. The default is 'Settle & Pay from today's collections: twelve thousand four hundred available, free, "
         "into current account ending forty-eight twenty-one'. Paying from the bank balance stays available. Then one PIN. [click] Screen "
         "three confirms the payment and, importantly, shows the settlement summary: collected, paid to suppliers, still to settle. The "
         "merchant sees one ledger of their own money. [click] And the next morning, the notification that restarts the habit: yesterday's "
         "collections are ready for supplier payments. Everything here is a concept prototype with fictional names; it is what we put in "
         "front of merchants in the validation test.",
         guideline="Optional annexure: prototype (concept screens)")

# ================================================================== 9 WHY IT LASTS
H9 = "No cashback needed: merchants switch because a step disappears, and stay because the trigger repeats daily"
s = blank(prs)
frame(s, 9, "Solution · why it lasts", H9,
      sources="Sources: S3, S6, S7 (existing early settlement at Paytm and PhonePe); S14 (UPI on current accounts). Switching and staying are design hypotheses, tested by the pilot's activation, repeat and habit-guard metrics.")
cols_x, cols_w = [0.6, 3.55, 4.95], [2.9, 1.35, 2.5]
hdr = group(s, "thead")
for t, x, w in zip(["Capability", "Differentiated?", "Who can copy it"], cols_x, cols_w):
    text(hdr, x, 1.9, w, 0.38, [[(t, dict(bold=True, color=WHITE, size=12))]], fill=NAVY, anchor="m", margin=0.08)
rows9 = [("Early settlement on its own", "No", "Already offered by Paytm and by PhonePe (₹1–3 a request)", False),
         ("Settlement + supplier payment in one flow, free when it funds a supplier", "Yes, today", "PhonePe, within months, but only for merchants whose collections it handles", True),
         ("Paying from the settlement current account", "No", "Any UPI app, once the account is linked", False),
         ("Saved suppliers, name check, history", "No", "Every major app has them: must-haves, not the pitch", False)]
row_groups = []
for k, (cap, dif, who, hl) in enumerate(rows9):
    y = 2.32 + k * 0.82
    g = group(s, f"trow{k + 1}")
    fill = PALE2 if hl else (GREY_XL if k % 2 == 0 else WHITE)
    for t, x, w, b, colr in [(cap, cols_x[0], cols_w[0], hl, NAVY if hl else INK), (dif, cols_x[1], cols_w[1], True, CYAN_D if hl else GREY),
                              (who, cols_x[2], cols_w[2], False, INK)]:
        text(g, x, y, w, 0.78, [[(t, dict(bold=b, color=colr, size=12))]], fill=fill, anchor="m", margin=0.08,
             line=CYAN if hl else None, line_w=1.25)
    row_groups.append(g)
# habit loop
cx, cy, r = 10.3, 3.85, 1.2
text(s, 7.85, 1.85, 4.88, 0.3, [[("DAILY HABIT LOOP  ·  NO REWARD NEEDED", dict(bold=True, color=GREY, size=10))]], align="c")
box(s, cx - r, cy - r, 2 * r, 2 * r, line=CYAN, line_w=3, shape=MSO_SHAPE.OVAL)
text(s, cx - 0.32, cy - 0.2, 0.64, 0.4, [[("daily", dict(bold=True, color=CYAN_D, size=11))]], align="c", anchor="m", margin=0)
loop = [("1 · Morning prompt", "yesterday's collections are ready", cx - 1.15, cy - r - 0.39, 2.3),
        ("2 · Pay", "one flow, one PIN", cx + r - 0.85, cy - 0.39, 1.7),
        ("3 · Record", "settlement notice: 'paid to suppliers'", cx - 1.15, cy + r - 0.39, 2.3),
        ("4 · Repeat", "saved supplier, one tap", cx - r - 0.85, cy - 0.39, 1.7)]
loop_shapes = []
for k, (t, d, x, y, w) in enumerate(loop):
    loop_shapes.append(text(s, x, y, w, 0.78, [[(t, dict(bold=True, color=NAVY, size=12))], [(d, dict(color=INK, size=12))]],
                            fill=WHITE, line=NAVY, line_w=1.25, align="c", anchor="m", margin=0.06, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
                            radius=0.15, name=f"loop{k + 1}"))
comp = text(s, 0.6, 5.75, 12.13, 0.95, [[("Competitor response: ", dict(bold=True, color=NAVY, size=13)),
                                          ("PhonePe can copy the flow for merchants whose collections it handles, not for Paytm's. The contest then becomes "
                                           "who handles the merchant's collections, which is Paytm's core business. A head start of months, not a permanent moat: start the pilot as soon as compliance clears it.", dict(size=13))]],
            fill=GREY_XL, margin=0.16, anchor="m", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1, name="competitor")
transition(s, "fade")
a = Anim(s)
a.click([fx(row_groups[0], "fade")] + [fx(g, "fade", "after", delay=100) for g in row_groups[1:]], "Differentiation rows build top to bottom")
a.click([fx(loop_shapes[0], "fade")] + [fx(sh, "fade", "after", delay=100) for sh in loop_shapes[1:]], "Habit-loop nodes appear clockwise")
a.click([fx(comp, "fade")], "Competitor-response line")
a.write()
register(s, 9, "Solution: differentiation and habit", H9,
         "The edge is one free flow at the moment of need, and a daily trigger keeps it without cashback.",
         "Differentiation table built from shapes (row 2 highlighted) and a four-node habit loop on a cyan ring; competitor-response strip.",
         "Fact (sources); hypothesis", "S3, S6, S7, S14", a,
         "Why would this hold without cashback? Start with what is not different. [click] Early settlement on its own is table stakes: Paytm "
         "has it, PhonePe sells it. Paying from a current account, saved suppliers, name checks and history are in every app. We build them "
         "because merchants expect them, but they are not the pitch. What is different today is settlement and supplier payment in one flow, "
         "free when it funds a supplier, at the moment the merchant needs it. [click] And the trigger repeats every day. Each morning, "
         "yesterday's collections are ready: that is the prompt. The merchant pays in one flow, the settlement notice records it, and the "
         "saved supplier makes the next payment one tap. No reward is needed because the trigger is the merchant's own business rhythm. "
         "[click] Can PhonePe copy it? Yes, within months, but only for merchants whose collections PhonePe handles. For Paytm's merchants, "
         "only Paytm holds the unsettled collections. That turns the contest into one about who handles collections, which is Paytm's core "
         "business. It is a head start, not a moat, so speed matters.",
         guideline="Business impact: cashback dependence; competitor response")

# ================================================================== 10 VALIDATION (TEMPLATE)
H10 = "[Assertion from the ≥20-user test, e.g. '__ of __ target merchants completed the Settle & Pay task unaided; __% committed to move a named supplier payment']"
s = blank(prs)
frame(s, 10, "Solution validation · awaiting results", H10, title_color=MAGENTA, title_size=24,
      sources="Method and recruitment per annexure A8; results recompute from the 'Validation_Log' sheet via fill_validation.py. Secondary sources: S3–S7 (settlement), S9–S11 (regulation). Magenta = to be filled from real results; nothing on this slide is invented.")
[setattr(sh, "name", "VAL_title") for sh in s.shapes if sh.name == "Title"]
gMeth = group(s, "methods")
text(gMeth, 0.6, 1.85, 1.15, 0.36, [[("METHOD", dict(bold=True, color=GREY, size=10))]], anchor="m")
xx = 1.7
for t in ["Prototype walkthrough", "Concept test on last 5 vendor payments", "Commitment asks"]:
    w = text_width(t, 12, True) + 0.3
    text(gMeth, xx, 1.85, w, 0.36, [[(t, dict(bold=True, color=NAVY, size=12))]], line=NAVY, align="c", anchor="m",
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5, margin=0.04)
    xx += w + 0.12
text(s, 9.4, 1.82, 3.33, 0.42, [[("n = [__] ", dict(bold=True, color=MAGENTA, size=16)), ("target merchants (≥20)", dict(color=INK, size=12))]],
     line=MAGENTA, dash=True, anchor="m", align="c", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3, name="VAL_n")
text(s, 0.6, 2.32, 12.13, 0.32, [[("Recruited: ", dict(bold=True, color=NAVY)), ("owner or app-chooser · collects on Paytm · pays vendors by UPI weekly · settlement profile recorded · "
                                   "every answer marked observed or stated", {})]], size=12, name="VAL_recruit")
tiles10 = [("VAL_t1", "completed the prototype task unaided", "OBSERVED"), ("VAL_t2", "named a specific supplier payment they would move", "COMMITMENT"),
           ("VAL_t3", "agreed to a follow-up trial in 7 days", "COMMITMENT"), ("VAL_t4", "enabled instant settlement in the session", "ACTION")]
gT10 = group(s, "behaviour")
for k, (nm, lab, tag) in enumerate(tiles10):
    x = 0.6 + k * 3.07
    text(gT10, x, 2.8, 2.95, 1.55, [[(tag, dict(bold=True, color=GREY, size=9))], [("[__%]", dict(bold=True, color=MAGENTA, size=32))], [(lab, dict(color=INK, size=12))]],
         line=MAGENTA, dash=True, margin=0.14, spacing=1, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08, name=nm)
gLim = group(s, "limits")
text(gLim, 0.6, 4.5, 6.6, 1.25, [[("CONTEXT", dict(bold=True, color=GREY, size=10))],
                                  [("Used instant settlement in the last month: ", dict(size=12)), ("[__%]", dict(bold=True, color=MAGENTA, size=12))],
                                  [("Settlement: ", dict(size=12)), ("[__ same day / __ next day / __ separate account]", dict(bold=True, color=MAGENTA, size=12))],
                                  [("Top objections: ", dict(size=12)), ("[Trust __ · Habit __ · Supplier __ · Staff __]", dict(bold=True, color=MAGENTA, size=12))]],
     fill=GREY_XL, margin=0.14, spacing=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06, name="VAL_ctx")
text(gLim, 7.35, 4.5, 5.38, 1.25, [[("LIMITS OF THIS EVIDENCE", dict(bold=True, color=GREY, size=10))],
                                    "Small, non-random sample from our own networks", "Concept prototype: no live money movement",
                                    "Stated answers marked; only observed actions count as 'did'"],
     size=12, fill=GREY_XL, margin=0.14, spacing=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06, name="VAL_limits")
text(s, 0.6, 5.88, 12.13, 0.82, [[("SEPARATE FROM THE ≥20-USER TEST (CONTEXT ONLY)   ", dict(bold=True, color=GREY, size=10))],
                                  [("50-row VOC dataset: ", dict(bold=True, size=12)), ("synthetic, for hypothesis stress-testing only, not field research. ", dict(size=12)),
                                   ("Exploratory merchant conversations: ", dict(bold=True, size=12)), ("genuine, exploratory, ", dict(size=12)),
                                   ("n = [__]", dict(bold=True, color=MAGENTA, size=12)),
                                   (" (pharmacy, café, FMCG retailer, tractor dealer, a routine vendor-UPI payer).", dict(size=12))]],
     fill=PALE, margin=0.14, spacing=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06, name="VAL_context_evidence")
transition(s, "fade")
a = Anim(s)
a.click([fx(gT10, "fade")], "Behaviour metrics (did / committed)")
a.click([fx(gLim, "fade")], "Context and limits boxes")
a.write()
register(s, 10, "Validation", H10 + "  (TEMPLATE: to be written from real results)",
         "Report what ≥20 target merchants did or committed to, with method, n, sources and limits (results pending).",
         "Results panel: method chips, n box, four behaviour tiles, context and limits boxes, and a separated context strip; magenta placeholders throughout.",
         "Placeholder (magenta), Synthetic, Genuine", "Validation_Log; S3–S7, S9–S11", a,
         "[Rewrite this talk track once results are in.] This slide reports our solution validation, and today it is deliberately a template. "
         "We will not show results we don't have. The method: a prototype walkthrough of the three screens you just saw, a concept test where "
         "each merchant looks at their own last five vendor payments and says which they would make with Settle & Pay, and three commitment "
         "asks. We recruit owners or whoever chooses the payment app, who collect on Paytm and pay vendors by UPI weekly, and we record their "
         "settlement profile. [click] We report behaviour, not liking: the share who completed the task unaided, the share who named a specific "
         "supplier payment they would move, the share who agreed to a follow-up trial, and the share who switched on instant settlement in the "
         "session. [click] We also show context, how many already used instant settlement and the top objections, and the limits: a small, "
         "non-random sample and a prototype without real money movement. The synthetic dataset and our exploratory conversations sit below, "
         "clearly separated from this test.",
         guideline="Solution validation: method, n ≥20, did/committed, secondary sources, limits")

# ================================================================== 11 FEASIBILITY
H11 = "Every leg exists today; the work is joining them, rated small to large, with four open dependencies"
s = blank(prs)
frame(s, 11, "Design & feasibility", H11,
      sources="Sources: S3 app listing (instant settlement; no payer feature); S13 instant settlement since 2018; S14 UPI on current accounts; S10, S11 RBI payout rule. Effort: S = weeks, M = 1–3 months, L = 3+ months (team estimate). Owners are proposed functions.")
cols11 = [("Component", 2.3), ("Exists today in Paytm", 2.45), ("New build", 2.75), ("Open dependency", 2.7), ("Effort", 0.75), ("Owner", 1.18)]
xs = [0.6]
for _, w in cols11[:-1]:
    xs.append(xs[-1] + w)
gH = group(s, "mhead")
for (t, w), x in zip(cols11, xs):
    text(gH, x, 1.85, w - 0.04, 0.36, [[(t, dict(bold=True, color=WHITE, size=12))]], fill=NAVY, anchor="m", margin=0.06)
rows11 = [("Collections screen", "Paytm for Business collections and alerts", "'Pay supplier' button and prompt", "—", "S", "Merchant app"),
          ("Early settlement", "Manual instant settlement in the app", "Settle the exact amount; waive the fee when it funds a supplier", "◆ Compliance: conditional free pricing; received funds only", "S", "Settlement, compliance"),
          ("Supplier payment", "UPI payer flow, name check, QR scan in Paytm UPI app", "Pilot: hand-off, payee prefilled. Scale: payer flow inside Paytm for Business", "◆ Banks: UPI on settlement current accounts", "S → M/L", "Payments eng."),
          ("One-PIN sequencing", "Settlement needs no UPI PIN", "Wait for the settlement credit, then pay", "◆ Settlement-to-credit time by bank", "M", "Payments eng."),
          ("Eligible list", "Settlement cycle and account data", "Extraction; territory randomisation", "◆ Instant settlement live for all device merchants?", "S", "Data, field ops"),
          ("Habit loop", "Push notifications, settlement notices", "Morning prompt; 'paid to suppliers' line", "—", "S", "Growth"),
          ("Staff access (arm B)", "—", "Per-person limits, owner visibility", "NPCI delegated-payment limits", "M", "Product")]
mrows = []
for i, row in enumerate(rows11):
    y = 2.25 + i * 0.6
    g = group(s, f"mrow{i + 1}")
    for j, ((_, w), x, v) in enumerate(zip(cols11, xs, row)):
        dep = v.startswith("◆")
        colr = RED if dep else (NAVY if j == 0 else INK)
        txt = [[(v, dict(bold=(j in (0, 4)) or dep, color=colr, size=12))]]
        text(g, x, y, w - 0.04, 0.57, txt, fill=GREY_XL if i % 2 == 0 else WHITE, anchor="m", margin=0.06,
             align="c" if j == 4 else "l")
    mrows.append(g)
summ = text(s, 0.6, 6.5, 12.13, 0.38, [[("Pilot build: S (weeks)   ·   Scale build: M–L, the full in-app payer flow, only after the scale gate   ·   ", dict(bold=True, color=NAVY, size=12)),
                                        ("◆ = one of four open dependencies", dict(bold=True, color=RED, size=12))]],
            fill=PALE, anchor="m", align="c", margin=0.08, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3, name="feas_summary")
transition(s, "fade")
a = Anim(s)
a.click([fx(mrows[0], "fade")] + [fx(g, "fade", "after", delay=60, dur=300) for g in mrows[1:]], "Matrix rows build component by component")
a.click([fx(summ, "fade")], "Build-effort summary with the four open dependencies")
a.write()
register(s, 11, "Feasibility", H11,
         "Settle & Pay reuses existing Paytm pieces; the new work is joining them, with four dependencies to clear.",
         "Feasibility matrix built from shapes: component × exists / new / dependency (red ◆) / effort / owner; summary bar.",
         "Fact (sources), team estimates", "S3, S10, S11, S13, S14", a,
         "Is it buildable? Almost every piece exists. [click] The collections screen exists; we add a button. Manual instant settlement exists "
         "and has since 2018; we settle the exact amount and waive the fee when it funds a supplier. Paytm already runs a UPI payer app with "
         "name checks and QR scanning; for the pilot we hand off to it with the supplier prefilled, and only after the scale gate do we build "
         "the payer flow inside Paytm for Business. The new engineering is the one-PIN sequencing, waiting for the settlement credit before "
         "the payment goes out, and the morning prompt. Staff access for multi-payer shops is a pilot arm, not core scope. [click] So the "
         "pilot build is small, weeks not months; the scale build is medium to large. The real work is four dependencies, marked in red: "
         "compliance on conditional free settlement, partner banks supporting UPI on settlement current accounts, settlement-to-credit time by "
         "bank, and whether manual instant settlement is live for every eligible device merchant.",
         guideline="Design & feasibility: features used, new build, dependencies, effort (Guideline 2)")

# ================================================================== 12 GTM
H12 = "Paytm can reach, activate and retain this segment through channels it already controls"
s = blank(prs)
frame(s, 12, "Go-to-market", H12,
      sources="Targets are hypotheses from the model (annexure A5) and will be replaced by pilot results. Messages are draft Hinglish lines; comparative claims need brand and legal approval.")
text(s, 0.6, 1.82, 12.13, 0.5, [[("SEGMENT  ", dict(bold=True, color=CYAN_D, size=11)),
                                  ("Group 1 merchants found in Paytm settlement data: next-day or separate-account settlement, weekly vendor UPI, a stated friction. "
                                   "Start in two cities with dense Soundbox coverage.", dict(size=12))]], fill=PALE, anchor="m", margin=0.12,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2)
hx = [3.25, 6.35, 9.65]
for t, x, w in zip(["CHANNEL AND PARTNER", "MESSAGE", "METRIC (HYPOTHESIS)"], hx, [2.95, 3.15, 3.08]):
    text(s, x, 2.45, w, 0.28, [[(t, dict(bold=True, color=GREY, size=10))]])
stages = [("ACQUIRE", 2.55, "Soundbox field force visits a list built from settlement data; banner on the collections screen",
           "“Aaj ki collection se aaj ka supplier, bina charge.”", "Today's collections, today's supplier, no charge", "Exposure: 40% of eligible in year one"),
          ("ACTIVATE", 2.2, "First payment made together during the visit; prompt at the moment of payment",
           "“Personal UPI wahi rahega.”", "Your personal UPI stays as it is", "First Settle & Pay payment within 30 days: 15–25%"),
          ("RETAIN", 1.85, "Morning push on yesterday's collections; settlement notice; WhatsApp receipt",
           "“₹9,250 kal ki collection se supplier ke liye ready.”", "Yesterday's collections are ready for suppliers", "2+ payments in months 2 and 3: 50%; habit guard ≥30%")]
stage_groups = []
for k, (st, w, ch, msg, eng, met) in enumerate(stages):
    y = 2.8 + k * 1.02
    g = group(s, f"stage{k + 1}")
    x0 = 0.6 + (2.55 - w) / 2
    text(g, x0, y, w, 0.92, [[(st, dict(bold=True, color=WHITE if k else NAVY, size=14))]], fill=[CYAN, NAVY3, NAVY][k], align="c", anchor="m",
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
    text(g, hx[0], y, 2.95, 0.92, ch, size=12, fill=GREY_XL, anchor="m", margin=0.1)
    text(g, hx[1], y, 3.15, 0.92, [[(msg, dict(bold=True, italic=True, color=NAVY, size=12))], [(eng, dict(color=GREY, size=11))]], fill=GREY_XL, anchor="m", margin=0.1)
    text(g, hx[2], y, 3.08, 0.92, [[(met, dict(bold=True, color=INK, size=12))]], fill=PALE, anchor="m", margin=0.1)
    stage_groups.append(g)
text(s, 0.6, 5.98, 12.13, 0.72, [[("PARTNERS AND RULES  ", dict(bold=True, color=CYAN_D, size=11)),
                                  ("Settlement banks for UPI on current accounts now; billing software (Petpooja, Marg, Vyapar, Tally) as later channels. "
                                   "Field incentives paid on repeat use, not sign-ups. No cashback in any message.", dict(size=12))]],
     fill=PALE, anchor="m", margin=0.12, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.15)
transition(s, "fade")
a = Anim(s)
for k in range(3):
    a.click([fx(stage_groups[k], "fade")], f"Funnel stage {k + 1} ({stages[k][0].title()}) with channel, message and metric")
a.write()
register(s, 12, "GTM", H12,
         "Paytm can reach, activate and retain the segment with its own field force, screens and notifications.",
         "Three-stage funnel (acquire, activate, retain) with channel/partner, Hinglish message and metric per stage; segment line above and partner line below.",
         "Projection / hypothesis targets", "Model; draft messaging", a,
         "Go-to-market uses channels Paytm already controls. The segment comes straight from settlement data, starting in two cities with dense "
         "Soundbox coverage. [click] Acquire: the Soundbox field force visits a list built from that data, and the collections screen carries a "
         "banner. The message names the removed step and the price: 'Aaj ki collection se aaj ka supplier, bina charge.' Our base case assumes "
         "forty per cent of eligible merchants are reached in year one. [click] Activate: the first payment is made together during the visit, "
         "and the prompt appears at the moment of payment. The message answers the biggest worry: 'Personal UPI wahi rahega', your personal "
         "UPI stays as it is. Target: fifteen to twenty-five per cent make a first payment within thirty days. [click] Retain: the morning push, "
         "the settlement notice and the WhatsApp receipt. Target: half of activated merchants pay twice or more in each of months two and "
         "three. Partners are settlement banks now and billing software later, and field incentives pay on repeat use, never on sign-ups.",
         guideline="GTM: segment, channels, partners, messaging")

# ================================================================== 13 PILOT
H13 = "A 90-day randomised pilot will tell Paytm whether to scale, fix or stop"
s = blank(prs)
frame(s, 13, "90-day pilot", H13,
      sources="Full design: annexure A4 and workbook 'Pilot_Design'. Targets are hypotheses; gates are decision rules. AA = Account Aggregator consented bank-statement panel. ITT = intention to treat.")
segs = [("DAYS 0–14", "Set up", 14, NAVY), ("DAYS 15–30", "Live + field visits", 16, CYAN_D), ("DAYS 31–60", "Habit: visits end, repeat measured", 30, NAVY3),
        ("DAYS 61–90", "Durability: optional price-reversion sub-arm", 30, NAVY)]
xx, seg_shapes = 0.6, []
for k, (d, t, days, col) in enumerate(segs):
    w = 12.13 * days / 90
    seg_shapes.append(text(s, xx, 1.85, w - 0.04, 0.72, [[(d, dict(bold=True, color=WHITE, size=11))], [(t, dict(color=WHITE, size=12))]],
                           fill=col, margin=0.08, anchor="m", name=f"seg{k + 1}"))
    xx += w
text(s, 0.6, 2.62, 12.13, 0.5, [[("Days 0–14: ", dict(bold=True, color=NAVY)), ("pull settlement data, build the eligible list, randomise by field-agent territory, pull a 60-day baseline, "
                                  "recruit the AA panel, ship the light build (prompt, fee waiver, hand-off to Paytm UPI).", {})]], size=12, name="setup_detail")
# schematic
gSc = group(s, "schematic")
text(gSc, 0.6, 3.3, 5.9, 0.5, "Eligible list, two cities: next-day or separate-account settlement", size=12, bold=True, color=NAVY, fill=PALE,
     anchor="m", align="c", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2)
line(gSc, 3.55, 3.8, 3.55, 4.0, color=GREY, width=1.5, arrow=True)
text(gSc, 1.6, 4.02, 3.9, 0.4, "Randomise by field-agent territory", size=12, bold=True, color=WHITE, fill=NAVY, anchor="m", align="c",
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3)
line(gSc, 2.6, 4.42, 1.95, 4.62, color=GREY, width=1.5, arrow=True)
line(gSc, 4.5, 4.42, 5.15, 4.62, color=GREY, width=1.5, arrow=True)
text(gSc, 0.6, 4.65, 2.9, 1.2, [[("Treatment ≈3,000", dict(bold=True, color=NAVY, size=13))], [("Arm A: Settle & Pay, light build", dict(size=12))],
                                 [("Arm B: + staff access, multi-payer shops", dict(size=12))]], fill=PALE2, margin=0.1, spacing=2,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
text(gSc, 3.6, 4.65, 2.9, 1.2, [[("Control ≈3,000", dict(bold=True, color=NAVY, size=13))], [("No prompt, no fee waiver", dict(size=12))],
                                 [("Same baseline and metrics", dict(size=12))]], fill=GREY_XL, margin=0.1, spacing=2,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
text(gSc, 0.6, 5.95, 5.9, 0.78, [[("Main metric: ", dict(bold=True, color=NAVY)), ("ITT change in Paytm share of business UPI value, treatment vs control; target +4 to +6 pts. ", {}),
                                  ("Baseline: ", dict(bold=True, color=NAVY)), ("60-day pre-period; AA panel ≈300 per arm.", {})]], size=12, margin=0.04)
# gates
gG = group(s, "gates")
gate_rows = [("SCALE", GREEN, "Activation ≥15%, repeat ≥40% and a significant ITT share lift",
              "Full in-app payer flow (M/L) → all eligible merchants via settlement data → Soundbox waves by city → bank partners"),
             ("REVISE", AMBER, "Activation fine, habit guard <15% (gap-only use)",
              "Reposition on one flow and staff access; strengthen the morning prompt; re-test"),
             ("STOP", RED, "Activation <8%", "Stop; keep the settlement-awareness learning")]
text(gG, 6.85, 3.3, 5.88, 0.32, [[("DECISION GATES AT DAY 90", dict(bold=True, color=GREY, size=10))]])
for k, (g_, col, rule, then) in enumerate(gate_rows):
    y = 3.65 + k * 0.93
    text(gG, 6.85, y, 1.05, 0.85, [[(g_, dict(bold=True, color=WHITE if g_ != "REVISE" else INK, size=12))]], fill=col, align="c", anchor="m",
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
    text(gG, 7.98, y, 4.75, 0.85, [[(rule, dict(bold=True, color=INK, size=12))], [("→ " + then, dict(color=GREY, size=12))]], fill=GREY_XL,
         anchor="m", margin=0.1)
text(gG, 6.85, 6.45, 5.88, 0.3, [[("Safety commitment: ", dict(bold=True, color=NAVY)), ("wrong-payee payments near zero.", {})]], size=12)
transition(s, "fade")
a = Anim(s)
a.click([fx(seg_shapes[0], "wipe-left", dur=400)] + [fx(sh, "wipe-left", "after", dur=400) for sh in seg_shapes[1:]], "Timeline segments wipe left to right")
a.click([fx(gG, "fade")], "Decision-gate table")
a.write()
register(s, 13, "90-day pilot", H13,
         "A territory-randomised 90-day pilot with a control group, baseline, targets and gates decides scale, fix or stop.",
         "Timeline (days 0–90, proportional segments), experiment schematic (eligible → randomise → treatment arms A/B vs control), decision-gate table.",
         "Hypothesis targets; decision rules", "Pilot_Design", a,
         "The pilot is how Paytm buys certainty cheaply. [click] Days zero to fourteen: pull settlement data, build the eligible list, randomise "
         "by field-agent territory so neighbouring shops don't contaminate each other, pull a sixty-day baseline, and ship the light build. "
         "Days fifteen to thirty: the treatment group goes live and gets field visits. Days thirty-one to sixty: the visits stop, so repeat use "
         "is measured without a person in the shop. Days sixty-one to ninety: durability, including an optional sub-arm where free settlement "
         "goes back to standard pricing. About three thousand merchants in treatment, three thousand in control; arm B adds staff access for "
         "multi-payer shops. The main metric is the intention-to-treat change in Paytm's share of business UPI value, measured on a consented "
         "Account Aggregator panel of about three hundred merchants per arm; target, four to six points. [click] The gates are fixed in "
         "advance. Scale if activation is at least fifteen per cent, repeat at least forty, and the share lift is significant. Revise if "
         "activation is fine but the habit guard is under fifteen per cent. Stop if activation is under eight.",
         guideline="GTM & pilot: cohort, control, baseline, targets, scale/stop, how to scale")

# ================================================================== 14 IMPACT
H14 = (f"Base case (projection): +{N['sh_el']} points of Paytm share of segment vendor UPI in year one, ≈{N['gmv_y']} a year, "
       f"at ≈{N['cpm']} per extra active merchant")
s = blank(prs)
frame(s, 14, "Business impact", H14,
      sources=f"Projection, not forecast: annexure workbook Funnel_Model, Share_Metric, Unit_Costs, Sensitivity. Cost per ₹ = year-one cost ÷ annual run-rate GMV; with a 50% year-one ramp it is ≈₹{U1['total'] / (B['gmv_year'] * 0.5):.3f}. Pool = addressable vendor UPI, not incremental Paytm GMV.")
text(s, 0.6, 1.85, 4.1, 0.3, [[("BASE-CASE FUNNEL, MERCHANTS (LAKH)", dict(bold=True, color=GREY, size=10))]])
chip(s, 3.6, 1.88, "projection", size=8, h=0.19)
funnel = bar_chart(s, 0.45, 2.15, 4.35, 2.6, ["Eligible", "Exposed", "Activated", "Repeat", "Incremental MTU"],
                   [round(B[k] / 1e5, 1) if B[k] >= 1e6 else round(B[k] / 1e5, 2) for k in ("eligible", "exposed", "activated", "repeat", "mtu")],
                   [GREY_L, GREY_L, NAVY3, NAVY, CYAN], '0.0#', "funnel_chart", max_val=36)
text(s, 0.6, 4.85, 4.1, 1.05, [[("EARLY INDICATORS (PILOT TARGETS)", dict(bold=True, color=GREY, size=10))],
                                [("Activation 15–25% · repeat 50% · 6–8 payments a month · habit guard ≥30% · ≈" + N["mtu1000"] + " MTU per 1,000 exposed", dict(size=12))]],
     fill=GREY_XL, margin=0.12, spacing=2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
gK = group(s, "kpis")
kpis = [(f"+{N['sh_el']} pts", "MAIN METRIC", f"Paytm share of segment vendor-UPI value, end of year one (+{N['sh_exp']} pts across exposed merchants)"),
        (N["gmv_y"], "OPPORTUNITY", f"annual run-rate; range {N['gmv_c']}–{N['gmv_u']} crore, from a {N['pool_y']}-a-year addressable pool"),
        (N["cpm"], "UNIT COST", f"per incremental MTU ({N['cpm_b']} with build); {N['cpr']} per ₹ of GMV ({N['cpr_b']} with build)")]
for k, (big, lab, d) in enumerate(kpis):
    y = 1.85 + k * 1.37
    text(gK, 5.0, y, 3.75, 1.27, [[(lab, dict(bold=True, color=GREY, size=9))], [(big, dict(bold=True, color=NAVY if k else CYAN_D, size=24))], [(d, dict(size=12, color=INK))]],
         fill=PALE if k == 0 else WHITE, line=CYAN if k == 0 else GREY_L, line_w=1.5 if k == 0 else 0.75, margin=0.12,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
text(s, 9.05, 1.85, 3.68, 0.3, [[("SENSITIVITY: ANNUAL RUN-RATE, ₹ CRORE", dict(bold=True, color=GREY, size=10))]])
sens_cats = ["Base case", "Gap-days-only floor", "Settlement share ½", "Activation ½", "Repeat rate ½"]
sens_vals = [M.r_cr(M.SENS[k] / 1e7) for k in ("Base case", "Gap-days-only floor", "Settlement share halved", "Activation halved", "Repeat rate halved")]
sens = bar_chart(s, 8.9, 2.15, 3.95, 2.6, sens_cats, sens_vals, [NAVY, NAVY3, CYAN, CYAN, CYAN], '#,##0', "sens_chart", max_val=3500, cat_size=10)
text(s, 9.05, 4.85, 3.68, 1.05, [[("Each halving halves every output; the floor assumes only gap-day payments move (habit guard 30%).", dict(size=12))]],
     fill=GREY_XL, margin=0.12, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06, name="sens_note")
dur_ = text(s, 0.6, 6.05, 12.13, 0.7, [[("HOLDS WITHOUT INCENTIVES?  ", dict(bold=True, color=CYAN_D, size=11)),
                                         ("No cashback: free settlement is permanent pricing, not a promotion. The pilot tests (a) repeat after field visits end, days 31–90; "
                                          "(b) the habit-guard share; (c) an optional price-reversion sub-arm, days 61–90.", dict(size=12))]],
            fill=PALE, anchor="m", margin=0.12, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.15, name="durability")
transition(s, "fade")
a = Anim(s)
a.click([fx(funnel, "wipe-left", dur=700)], "Funnel bars build left to right")
a.click([fx(gK, "fade")], "Main metric, opportunity and unit-cost tiles")
a.click([fx(sens, "wipe-left", dur=700), fx(dur_, "fade", "after")], "Sensitivity bars, then the durability line")
a.write()
register(s, 14, "Business impact", H14,
         f"The base case adds {N['sh_el']} points of segment share and {N['gmv_y']} a year at about {N['cpm']} per extra active merchant, within a wide range driven by three assumptions.",
         "Native bar chart (funnel) left; three KPI tiles centre; native sensitivity bar chart right; early indicators and durability strips.",
         "Projection", "Workbook: Funnel_Model, Share_Metric, Unit_Costs, Sensitivity", a,
         f"What is it worth? Everything here is a projection, not a forecast. [click] The funnel: about {N['eligible']} eligible merchants, "
         f"{N['exposed']} reached in year one, about {N['activated']} activating, {N['repeat']} repeating, and about {N['mtu']} who are new Paytm "
         f"business payers, net of those who already sometimes pay through Paytm. [click] The main metric: Paytm's share of the segment's vendor "
         f"UPI value rises by about {N['sh_el']} points by the end of year one, or {N['sh_exp']} points across the merchants we actually reach. "
         f"That is about {N['gmv_y']} a year of incremental GMV, out of a {N['pool_y']} pool that we treat as addressable, not as ours. It costs "
         f"about {N['cpm']} per incremental active merchant, mostly field visits, or under a paisa per rupee of GMV. [click] The range is wide, "
         f"{N['gmv_c']} to {N['gmv_u']} crore, because three assumptions multiply: the settlement share, activation and repeat. Halve any one and "
         f"every output halves. If only payments made on settlement-gap days move, we keep about {N['floor']} crore. And durability is designed in: "
         "no cashback, and three pilot tests of whether use holds once the visits and the free price stop.",
         guideline="Business impact: main metric, early indicators, opportunity, unit costs, durability, sensitivity")

# ================================================================== 15 DECISION
H15 = "Approve the 90-day pilot; scale only on the gates. Competitors can copy the feature, but not for Paytm's merchants"
s = blank(prs, dark=True)
frame(s, 15, "Risks and decision", H15, dark=True,
      sources="Full registers: annexure A6. Gate thresholds: workbook 'Pilot_Design'. Owners are proposed functions, not confirmed people. Screens illustrative.")
text(s, 0.6, 1.85, 6.4, 0.3, [[("TOP RISKS AND HOW WE REDUCE THEM", dict(bold=True, color=CYAN, size=10))]])
risks15 = [("Segment smaller than the proxy", "Size it from settlement data in days 0–14; shrink the target or lead with staff access"),
           ("Habit wins even without the step", "Morning prompt; habit-guard metric; 'revise' gate below 15%"),
           ("PhonePe copies, or makes Settle Now free", "Only for its own merchants; move first and lock in the habit"),
           ("Compliance reads free settlement differently", "Settle received funds only; confirm before launch; fallback: priced settlement + hand-off")]
for k, (r_, m_) in enumerate(risks15):
    y = 2.18 + k * 0.66
    text(s, 0.6, y, 2.75, 0.6, r_, size=12, bold=True, color=WHITE, fill=NAVY2, anchor="m", margin=0.1)
    text(s, 3.4, y, 3.6, 0.6, m_, size=12, color=SOFT, fill=NAVY2, anchor="m", margin=0.1)
gRm = group(s, "roadmap")
text(gRm, 0.6, 4.9, 6.4, 0.3, [[("ROADMAP AND GATES", dict(bold=True, color=CYAN, size=10))]])
line(gRm, 0.8, 5.75, 6.8, 5.75, color=SOFT, width=2)
stops = [(0.8, "Weeks 0–2", "Data + compliance check"), (2.8, "Days 0–90", "Pilot, 3,000 vs 3,000"), (4.8, "Months 4–12", "Full payer flow, city waves")]
for x, t1, t2 in stops:
    box(gRm, x - 0.08, 5.67, 0.16, 0.16, fill=CYAN, shape=MSO_SHAPE.OVAL)
    text(gRm, x - 0.05, 5.98, 1.95, 0.55, [[(t1, dict(bold=True, color=WHITE, size=12))], [(t2, dict(color=SOFT, size=12))]])
for x, g_, cond, w in [(2.3, "G0", "segment ≥25% + compliance", 2.3), (4.4, "G1", "scale / revise / stop", 1.8), (6.5, "G2", "lift holds", 1.3)]:
    box(gRm, x - 0.17, 5.58, 0.34, 0.34, fill=AMBER, shape=MSO_SHAPE.DIAMOND)
    text(gRm, x - w / 2, 5.22, w, 0.3, [[(g_ + "  ", dict(bold=True, color=AMBER, size=11)), (cond, dict(color=WHITE, size=11))]], align="c", anchor="b")
text(gRm, 0.6, 6.6, 6.4, 0.28, [[("Owners: ", dict(bold=True, color=WHITE)), ("data team · compliance · merchant product · field ops", dict(color=SOFT))]], size=12)
# callback split-screen
text(s, 7.5, 1.85, 5.23, 0.3, [[("THE SAME MERCHANT, AFTER", dict(bold=True, color=CYAN, size=10))]], align="c")


def mini_phone(container, x, header, fill, big, small, name):
    ix, iy, iw = phone(container, x, 2.2, 2.2, 3.0, header, header_fill=fill, name_prefix=name)
    text(container, ix, iy + 0.1, iw, 0.45, big, size=18, bold=True, color=NAVY, align="c")
    text(container, ix, iy + 0.62, iw, 0.7, small, size=11, color=GREY, align="c")


gCL = group(s, "!!phoneL_end")
mini_phone(gCL, 7.85, "Paytm for Business", NAVY2, "₹12,400", "collected today", "cL")
text(gCL, 7.85, 5.28, 2.2, 0.3, [[("MONEY IN · PAYTM", dict(bold=True, color=CYAN, size=11))]], align="c")
gCR0 = group(s, "phoneR_before")
mini_phone(gCR0, 10.35, "Another UPI app", "4A5568", "₹6,800", "to Sharma Traders", "cR0")
gCR = group(s, "!!phoneR_end")
mini_phone(gCR, 10.35, "Paytm for Business", NAVY2, "₹6,800", "to Sharma Traders, from today's collections", "cR")
text(gCR, 10.35, 5.28, 2.2, 0.3, [[("MONEY OUT · PAYTM", dict(bold=True, color=CYAN, size=11))]], align="c")
same = text(s, 7.5, 5.7, 5.23, 0.4, [[("Same merchant. Same money. Same app.", dict(bold=True, color=CYAN, size=16))]], align="c", name="same_app")
ask = text(s, 7.5, 6.15, 5.23, 0.6, [[("The ask: ", dict(bold=True, color=NAVY, size=13)), ("approve the 90-day pilot, 3,000 vs 3,000 merchants in two cities", dict(color=NAVY, size=13))]],
           fill=CYAN, align="c", anchor="m", margin=0.1, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3, name="ask")
transition(s, "morph")
a = Anim(s)
a.click([fx(gCR, "fade", dur=700), fx(same, "fade", "after")], "Right phone cross-fades from 'Another UPI app' to Paytm (callback to slide 2); 'Same app' line")
a.click([fx(gRm, "wipe-left", dur=800)], "Roadmap with diamond gates wipes left to right")
a.write()
register(s, 15, "Risks and decision", H15,
         "Approve the pilot and scale only on evidence; competitors can copy the feature but not for Paytm's merchants.",
         "Compact risk table (4 risks with mitigations); roadmap with three diamond gates and owners; slide 2's split screen returns with Paytm on both phones; the ask.",
         "Decision rules", "A6; Pilot_Design", a,
         "So what should Paytm decide today? Not a launch. A 90-day pilot, with the gates fixed before it starts. The risks are real, and each "
         "has a response. The segment may be smaller than our proxy, so we size it from settlement data in the first two weeks. Habit may win "
         "even when the step is gone, which is why the habit-guard metric and the 'revise' gate exist. PhonePe can copy the feature, and we "
         "expect it to, but only for merchants whose collections it handles. And compliance may read free conditional settlement differently, "
         "so we settle only received funds and confirm before launch. [click] Remember the merchant from slide two: money in on Paytm, money out "
         "somewhere else. With Settle & Pay, both phones are Paytm. Same merchant, same money, same app. [click] The roadmap: two weeks of data "
         "and compliance checks to gate zero, which needs at least a quarter of device merchants on next-day or separate-account settlement, the ninety-day pilot to gate one, and only then the full payer flow and city waves. The ask is "
         "simple: approve the pilot, three thousand against three thousand merchants in two cities.",
         guideline="Risks incl. competitor response; mitigation; how to scale; decision")

# ================================================================== ANNEXURE DIVIDER
s = blank(prs, dark=True)
text(s, 0.8, 1.2, 8, 0.35, [[("NOT PART OF THE 15-SLIDE DECK", dict(bold=True, color=SOFT, size=12))]], name="Eyebrow")
text(s, 0.8, 1.65, 8, 1.1, "Annexures", size=54, bold=True, color=WHITE, name="Title")
annex_list = [("A1", "Evidence status and methodology"), ("A2", "Full VOC and segment tables"), ("A3", "Full prototype flow and edge cases"),
              ("A4", "Pilot measurement methodology and metric definitions"), ("A5", "Financial model and unit-cost detail"),
              ("A6", "Dependency and risk registers"), ("A7", "Round 1 to Round 2 change log"), ("A8", "Validation interview guide")]
for k, (aid, t) in enumerate(annex_list):
    col, row = k // 4, k % 4
    text(s, 0.8 + col * 6.0, 3.25 + row * 0.62, 5.8, 0.5, [[(aid + "   ", dict(bold=True, color=CYAN, size=16)), (t, dict(color=WHITE, size=16))]], anchor="m")
text(s, 0.8, 6.0, 11.5, 0.6, "Companion workbook: Paytitude_R2_Annexure.xlsx (live formulas; Validation_Log ready for the ≥20-user results)", size=13, color=SOFT)
text(s, 0.6, 7.0, 1.7, 0.3, "Track B · Paytitude", size=9, bold=True, color=SOFT)
transition(s, "fade")
register(s, "Divider", "Annexure divider", "Annexures", "Supporting detail; not part of the 15 slides.", "Dark divider listing A1–A8.", [], "—", None,
         "The annexures carry the evidence, model and design detail behind every number. They are not part of the fifteen-slide deck.")


def annex(aid, title, sources):
    s = blank(prs)
    frame(s, aid, f"Annexure {aid}", title, sources=sources, title_size=24)
    transition(s, "fade")
    return s


# ---------------------------------------------------------------- A1
s = annex("A1", "Evidence status: what is fact, what is synthetic, what is still to be validated",
          "Full source list with URLs and verification status: workbook 'Sources'. Disclosure quoted verbatim from Paytm_Track_B_VOCs.xlsx, 'Methodology Notes'.")
cards = [
    ("synthetic", "SYNTHETIC DATASET (50 ROWS)", [
        [("“This is synthetic research for hypothesis stress-testing, not customer evidence.”", dict(italic=True, bold=True, color=NAVY))],
        "16 cities (Mumbai 12); 47 of 50 'small'; no category above 5 rows",
        "Audit: 11 hard contradictions (V10, V11, V12, V17, V19, V23, V34, V35, V36, V40, V42); none in Group 1; clean sample n = 39",
        "15 distinct first quotes across 50 rows: quotes illustrate, never count",
        [("Used for: ", dict(bold=True)), "segment logic and model proxies only"]]),
    ("genuine", "EXPLORATORY CONVERSATIONS", [
        [("n = [__]", dict(bold=True, color=MAGENTA)), " genuine, exploratory conversations"],
        "Pharmacy, café, FMCG retailer, tractor dealer, and a merchant who routinely pays vendors by UPI",
        "Notes and verbatims to be added to workbook 'VOC_Real'",
        [("Not validation: ", dict(bold=True)), "too few and not structured for the ≥20-user test"]]),
    ("fact", "SECONDARY SOURCES", [
        "Paytm Q1 FY27 release: 1.57 crore device merchants (S1)",
        "NPCI app-wise share, Aug 2026, via secondary report (S2)",
        "Paytm for Business listing and support pages (S3–S5)",
        "PhonePe Settle Now help pages (S6–S8)",
        "RBI PA Directions 2025 press release and legal summaries (S9–S12)"]),
]
for k, (kind, t, lines_) in enumerate(cards):
    x = 0.6 + k * 4.1
    text(s, x, 1.85, 3.93, 3.95, [[(t, dict(bold=True, color=GREY, size=10))]] + [l if isinstance(l, list) else [(l, {})] for l in lines_],
         size=13, fill=GREY_XL, margin=0.15, spacing=5, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
    chip(s, x + 0.15, 5.45, kind)
text(s, 0.6, 5.95, 12.13, 0.75, [[("VALIDATION (≥20 TARGET USERS): ", dict(bold=True, color=MAGENTA, size=12)),
                                  ("not yet run at the time of this build. Interview guide in A8; 'Validation_Log' sheet and fill_validation.py recompute slide 10 and re-export the PDF.", dict(size=12))]],
     line=MAGENTA, dash=True, anchor="m", margin=0.14, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
register(s, "A1", "Annexure", "Evidence status and methodology", "Separates synthetic, genuine exploratory and secondary evidence, and states the validation gap.",
         "Three evidence cards with status chips; validation status strip.", ["synthetic", "genuine", "fact"], "S1–S12, S16", None,
         "Annexure A1 lists every type of evidence we use and its status.")

# ---------------------------------------------------------------- A2
s = annex("A2", "Full VOC and segment tables (synthetic dataset)",
          "Source: S16, computed live in workbook 'Segment_Rules' (COUNTIFS over 'VOC_Synthetic'). SYNTHETIC: illustrates the hypothesis; counts are not market shares.")
native_table(s, 0.6, 1.85, 7.1, [1.1, 3.7, 0.95, 1.35], [
    ["Group", "Inclusion rule", "Merchants", "Yes / maybe / no"],
    ["1 · High potential", "Paytm collector; next-day or separate-account settlement; vendor UPI ≥ weekly; owner or manager chooses; stated friction", "16", "7 / 9 / 0"],
    ["2 · May try", "Paytm collector not in 1 or 3: next-day with no friction (7) or same-day with friction (9, of which 7 contradictory)", "16", "4 / 8 / 4"],
    ["3 · Little value", "No or partial Paytm collection (8); accountant chooses (2); same-day, no friction (8)", "18", "1 / 4 / 13"],
], size=12, row_h=0.68, name="a2_groups", bold_first_col=True)
native_table(s, 7.95, 1.85, 4.78, [2.4, 1.0, 1.38], [
    ["Settlement (42 Paytm collectors)", "Merchants", "Yes / maybe / no"],
    ["Same day", "19", "4 / 6 / 9"],
    ["Next day", "17", "4 / 11 / 2"],
    ["Next day, separate current account", "6", "3 / 3 / 0"],
], size=12, row_h=0.5, name="a2_settle")
native_table(s, 0.6, 4.75, 12.13, [6.2, 1.2, 1.3, 1.85, 1.58], [
    ["Reaction to the concept (grouped)", "All 50", "Clean 39", "Yes / maybe / no", "Status"],
    ["Would pay suppliers from today's collections, or avoid moving money between accounts", "16", "10", "9 / 7 / 0", "Synthetic"],
    ["Values staff access with limits and owner visibility more than the app", "9", "9", "2 / 5 / 2", "Synthetic"],
    ["Would try it but keep their current app", "8", "8", "0 / 6 / 2", "Synthetic"],
    ["Rejects: same-day settlement, invoice-led payments, or no Paytm collections", "11", "9", "0 / 0 / 11", "Synthetic"],
], size=12, row_h=0.36, name="a2_reactions")
register(s, "A2", "Annexure", "Full VOC and segment tables", "Shows group rules, settlement split and reactions, with the clean-sample view.",
         "Three native tables.", ["synthetic"], "S16; Segment_Rules", None, "Annexure A2: full segment tables from the synthetic dataset.")

# ---------------------------------------------------------------- A3
s = annex("A3", "Full prototype flow, including the three edge cases",
          "Concept prototype; fictional names and amounts. Settlement-to-credit timeout and limits are to be set with payments engineering and partner banks.")
happy = ["Collections screen: tap 'Pay supplier'", "Scan WhatsApp QR or pick saved supplier", "Name check shown before any money moves",
         "Choose 'Settle & Pay · free' (or bank balance)", "One UPI PIN; pay only after settlement credit is confirmed", "Receipt + settlement summary; WhatsApp share"]
for k, t in enumerate(happy):
    x = 0.6 + k * 2.03
    text(s, x, 1.85, 1.93, 1.15, [[(str(k + 1), dict(bold=True, color=CYAN_D, size=16))], [(t, dict(size=12, color=INK))]], fill=PALE, margin=0.1,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
edges = [("Settlement delay", "Credit not confirmed within the timeout",
          ["Supplier is never debited before the credit lands", "Screen: 'Waiting for ₹6,800 to reach ••4821'", "Options: wait, pay from bank balance, or cancel", "Settlement still completes; nothing is lost"]),
         ("Insufficient collections", "Supplier amount > collections available",
          ["Show '₹4,100 available from today's collections'", "Offer: settle ₹4,100 + pay the rest from bank balance", "No credit, no overdraft, no pre-funding", "Log frequency: if common, revisit credit after the pilot"]),
         ("Wrong payee", "Name doesn't match or QR looks altered",
          ["Verified account name shown before the PIN", "Mismatch warning against the saved supplier", "First payment to a new payee needs an extra confirm", "After payment: UPI dispute flow and support; track per 1,000"])]
for k, (t, trig, pts) in enumerate(edges):
    x = 0.6 + k * 4.1
    text(s, x, 3.25, 3.93, 3.3, [[(f"EDGE CASE {k + 1}", dict(bold=True, color=GREY, size=10))], [(t, dict(bold=True, color=NAVY, size=16))],
                                  [(trig, dict(italic=True, color=GREY, size=13))]] + [[("•  " + p, dict(size=13))] for p in pts],
         fill=GREY_XL, margin=0.15, spacing=4, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
register(s, "A3", "Annexure", "Full prototype flow and edge cases", "Happy path plus settlement delay, insufficient collections and wrong payee.",
         "Six-step happy path; three edge-case cards.", ["concept"], "Concept", None, "Annexure A3: the full flow and how it fails safely.")

# ---------------------------------------------------------------- A4
s = annex("A4", "Pilot measurement: design, definitions and how the result is read",
          "Power: indicative only; to be recomputed from baseline variance and the territory design effect before launch. Definitions as in the solution document, section 10.4.")
native_table(s, 0.6, 1.85, 12.13, [2.55, 6.35, 1.75, 1.48], [
    ["Metric", "Definition", "Source", "Target"],
    ["Main: share lift (ITT)", "Paytm share of total outgoing business UPI value, treatment minus control, change vs 60-day baseline (difference-in-differences), all assigned merchants", "AA panel ≈300/arm", "+4 to +6 pts"],
    ["Incremental MTU", "≥1 Settle & Pay payment in a month and no outgoing Paytm business payment in the baseline, net of the control group's rate", "Paytm data", "≈65 per 1,000"],
    ["Activation", "Exposed eligible merchants making a first Settle & Pay payment within 30 days", "Paytm data", "15–25%"],
    ["Repeat", "Activated merchants with 2+ Settle & Pay payments in each of months 2 and 3", "Paytm data", "50% (gate 40%)"],
    ["Habit guard", "Share of Settle & Pay payments made when no settlement or transfer gap existed", "Paytm data", "≥30% (revise <15%)"],
    ["Durability", "Repeat in days 31–90 after visits end; price-reversion sub-arm usage, days 61–90", "Paytm data", "Measured"],
    ["Safety", "Wrong-payee payments and support complaints per 1,000 payments", "Support logs", "Near zero"],
], size=12, row_h=0.52, name="a4_metrics", bold_first_col=True)
text(s, 0.6, 6.12, 12.13, 0.72, [[("Reading the result: ", dict(bold=True, color=NAVY)),
                                  ("randomise by field-agent territory to avoid spill-over; analyse intention to treat; report by settlement profile and single- vs multi-payer shops. "
                                   "Indicatively, 300 per arm detects a 4–6 pt share difference at 80% power if per-merchant share SD is 17–25 pts, before design effect.", {})]],
     size=12, fill=GREY_XL, margin=0.14, anchor="m", shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
chip(s, 11.45, 6.02, "validate", size=8, h=0.19)
register(s, "A4", "Annexure", "Pilot measurement methodology", "Defines every pilot metric and how results are read.",
         "Metric definition table; analysis note.", ["validate"], "Solution doc §10.4, §11", None, "Annexure A4: pilot metrics and definitions.")

# ---------------------------------------------------------------- A5
s = annex("A5", "Financial model and unit-cost detail (projection, not forecast)",
          "All values computed by live formulas in the workbook (Funnel_Model, Share_Metric, Unit_Costs). Inputs are assumptions or synthetic proxies; build costs are team assumptions, not Paytm figures.")
F = M.F
fmt_l = lambda v, d=1: f"{v / 1e5:.{d}f} L"
native_table(s, 0.6, 1.85, 7.2, [3.0, 1.4, 1.4, 1.4], [
    ["Stage (run-rate, end of year one)", "Cautious", "Base", "Upside"],
    ["Eligible merchants", fmt_l(F['cautious']['eligible']), fmt_l(B['eligible']), fmt_l(F['upside']['eligible'])],
    ["Exposed", fmt_l(F['cautious']['exposed']), fmt_l(B['exposed']), fmt_l(F['upside']['exposed'])],
    ["Activation rate", f"{F['cautious']['activation']:.1%}", f"{B['activation']:.1%}", f"{F['upside']['activation']:.1%}"],
    ["Activated", fmt_l(F['cautious']['activated'], 2), fmt_l(B['activated'], 2), fmt_l(F['upside']['activated'], 2)],
    ["Repeat merchants", f"{round(F['cautious']['repeat'], -3):,.0f}", fmt_l(B['repeat'], 2), fmt_l(F['upside']['repeat'], 2)],
    ["Incremental MTU", f"{round(F['cautious']['mtu'], -3):,.0f}", f"{round(B['mtu'], -3):,.0f}", fmt_l(F['upside']['mtu'], 2)],
    ["Extra payments a month", fmt_l(F['cautious']['payments']), fmt_l(B['payments']), fmt_l(F['upside']['payments'])],
    ["Incremental GMV a month", f"₹{F['cautious']['gmv_month'] / 1e7:,.0f} cr", f"₹{B['gmv_month'] / 1e7:,.0f} cr", f"₹{M.r3(F['upside']['gmv_month'] / 1e7):,.0f} cr"],
    ["Annual run-rate", f"₹{M.r_cr(F['cautious']['gmv_year'] / 1e7):,.0f} cr", f"₹{M.r_cr(B['gmv_year'] / 1e7):,.0f} cr", f"₹{M.r_cr(F['upside']['gmv_year'] / 1e7):,.0f} cr"],
    ["Share lift, whole segment", f"+{F['cautious']['share_eligible'] * 100:.1f} pts", f"+{B['share_eligible'] * 100:.1f} pts", f"+{F['upside']['share_eligible'] * 100:.1f} pts"],
], size=12, row_h=0.4, name="a5_funnel", bold_first_col=True)
native_table(s, 8.05, 1.85, 4.68, [3.08, 1.6], [
    ["Unit cost (base)", "Value"],
    ["Visit cost per exposed merchant", "₹200 (₹150–300)"],
    ["Free settlement per payment (ceiling)", N["settle"]],
    ["Pilot build / full payer flow", "₹0.5 cr / ₹5 cr"],
    ["Cost per incremental MTU", f"{N['cpm']} / {N['cpm_b']}*"],
    ["Visit-cost range per MTU", f"₹{round(M.unit_costs(150)['per_mtu'], -2):,.0f}–{round(M.unit_costs(300)['per_mtu'], -2):,.0f}"],
    ["Cost per ₹ of GMV", f"{N['cpr']} / {N['cpr_b']}*"],
    ["Pilot metric: ₹200 × 1,000 ÷ 65", N["pilot_cpm"]],
    ["Segment pool (addressable)", f"{N['pool_m']}/month"],
], size=12, row_h=0.4, name="a5_units", bold_first_col=False)
text(s, 8.05, 5.5, 4.68, 0.3, "* without / with build cost", size=10, color=GREY, italic=True)
text(s, 0.6, 6.35, 12.13, 0.4, "Drivers: weekly vendor UPI 35/50/60%; settlement share 54.8% (23/42); friction 69.6% (16/23); exposure 25/40/55%; repeat 35/50/65%; not already a Paytm payer 56% (9/16); 18.9 payments a month; shift 25/40/60%; ticket ₹2,000/2,500/3,500; baseline overlap 15%.",
     size=10, color=GREY)
register(s, "A5", "Annexure", "Financial model and unit-cost detail", "Shows the full funnel, share metric and unit costs for all scenarios.",
         "Two native tables plus drivers line.", ["projection"], "Workbook", None, "Annexure A5: the model behind slide 14.")

# ---------------------------------------------------------------- A6
s = annex("A6", "Dependency and risk registers",
          "Full registers with sources and build effort: workbook 'Dependencies_Risks'. Owners are proposed functions.")
native_table(s, 0.6, 1.85, 12.13, [3.5, 5.3, 2.4, 0.93], [
    ["Dependency", "Still to confirm", "Owner", "Effort"],
    ["Early release of collections", "Credit speed per bank; daily limits; merchant-agreement update", "Settlement, treasury", "S"],
    ["Early release vs credit", "Formal compliance view; is any pre-funding ever needed?", "Compliance, legal", "—"],
    ["Free settlement for supplier payments", "Is conditional free pricing acceptable? Cost at scale", "Compliance, pricing", "S"],
    ["One authorisation", "Settlement-to-credit time by bank; the waiting experience", "Payments eng.", "M"],
    ["Payer flow in Paytm for Business", "Build in-app, or keep the hand-off to Paytm UPI", "Engineering, banks", "S / M–L"],
    ["Instant settlement for all device merchants", "Live for every eligible merchant today? (Phase 0)", "Merchant product", "S"],
    ["Staff access (arm B)", "Do UPI delegated-payment limits fit vendor payments?", "Product, NPCI rules", "M"],
], size=12, row_h=0.39, name="a6_deps", bold_first_col=True)
native_table(s, 0.6, 5.15, 12.13, [3.5, 8.63], [
    ["Risk", "Mitigation"],
    ["Segment smaller than the proxy", "Size it from settlement data in days 0–14; shrink the target; lead with staff access"],
    ["Habit wins even without the step", "Morning prompt; habit-guard metric; 'revise' gate below 15%"],
    ["PhonePe responds", "Only for its own merchants; move first and lock in the habit"],
], size=12, row_h=0.36, name="a6_risks", bold_first_col=True)
register(s, "A6", "Annexure", "Dependency and risk registers", "Lists what must be confirmed, by whom, and how each risk is reduced.",
         "Two native tables.", [], "Workbook", None, "Annexure A6: dependencies and risks.")

# ---------------------------------------------------------------- A7
s = annex("A7", "What changed from Round 1 to Round 2, and why",
          "Round 1 column verified against Paytitude_ExecSummary.pdf (25 Sep 2026). Same track (B) and the same merchant base.")
native_table(s, 0.6, 1.85, 12.13, [1.6, 3.65, 3.75, 3.13], [
    ["Area", "Round 1 (Paytitude_ExecSummary.pdf)", "Round 2", "Why"],
    ["Problem framing", "'Owns the counter, not the payout'; 0.4% MDR pushes payouts to NEFT and cash", "Owns money in, not money out; no MDR argument", "Fee isn't why merchants pick an app; MDR argument legally fragile"],
    ["Segment", "Paytm QR / Soundbox merchants, >₹1 lakh a month UPI (≈24 lakh), Andheri", "Same base, re-cut: settlement timing, weekly vendor UPI, stated friction", "Removing a step only matters where the step exists"],
    ["Solution", "Supplier Pay: settlement-account pay, invoice receipts, due-date credit, Supplier Khata", "Settle & Pay: settle received collections to own account, pay by UPI", "Settlement plus payment in one flow is Paytm's edge"],
    ["Credit", "30-day partner-lender credit", "Dropped", "No credit need in the evidence; thin economics"],
    ["Ledger", "Supplier Khata; invoice-matched receipts", "Dropped from the MVP", "Billing software already owns this"],
    ["Impact", "≈₹27,000 crore a year; +1–2 lakh payers", f"{N['gmv_y']} base ({N['gmv_c']}–{N['gmv_u']} crore); ≈{N['mtu']} MTU", "₹27,000 crore rested on simulated data and planned payments"],
    ["Pilot", "500 Andheri merchants vs control; 30% share by month 12", "90 days, territory-randomised, 3,000 vs 3,000; ITT +4–6 pts; gates", "Prove incrementality before scale"],
    ["Evidence", "'VOC dataset, n=50 Andheri merchants'", "Synthetic set disclosed as such; ≥20-user validation added", "Keep hypothesis and evidence separate"],
], size=12, row_h=0.5, name="a7_changes", bold_first_col=True)
register(s, "A7", "Annexure", "Round 1 to Round 2 change log", "States every change since Round 1 and the reason.", "Native table.", [],
         "S17", None, "Annexure A7: what changed since Round 1 and why.")

# ---------------------------------------------------------------- A8
s = annex("A8", "Validation interview guide (≥20 target merchants)",
          "One row per merchant in workbook 'Validation_Log'. Only observed actions and explicit commitments count as 'did or committed'.")
native_table(s, 0.6, 1.85, 12.13, [3.1, 9.03], [
    ["Step", "What we do and record"],
    ["Screener (all true)", "Owner or app-chooser; collects on a Paytm QR or Soundbox; pays a vendor by UPI weekly; settlement profile recorded"],
    ["1 · Last five payments", "Open the phone's UPI history together: app, amount, payee, time, paying account (observed, not estimated)"],
    ["2 · Settlement reality", "When did yesterday's collections reach the bank? Ever settled instantly in Paytm for Business (last 30 days)?"],
    ["3 · Friction moment", "Last time a supplier had to be paid before the money was usable: date and workaround"],
    ["4 · Prototype task", "'Pay Sharma Traders ₹6,800 from today's collections': unaided completion Y/N, time, errors (observed)"],
    ["5 · Choice on real payments", "Of the last five payments, which would they make with Settle & Pay? (count of five)"],
    ["6 · Commitment asks", "Name an upcoming supplier payment to move · agree to a 7-day follow-up · enable instant settlement now"],
    ["7 · Objections", "'What would stop you tomorrow?' coded: trust, habit, supplier, staff, account set-up, other"],
    ["Recording rules", "Each answer marked observed or stated; no incentives tied to answers; anonymised; one row per merchant"],
], size=12, row_h=0.44, name="a8_guide", bold_first_col=True)
register(s, "A8", "Annexure", "Validation interview guide", "Screener, observed tasks and commitment asks for the ≥20-user test.", "Native table.", [],
         "Solution doc §13", None, "Annexure A8: the guide for the validation test.")

strip_theme_effects(prs)
prs.save(OUT)
print("saved", OUT, "slides:", len(prs.slides))

# ================================================================== storyboard
import storyboard  # noqa: E402
storyboard.write(SB, STORYBOARD, N)
