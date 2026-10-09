# Build report: Paytitude R2 final submission

Paytm UPI Growth Challenge, Track B · Team Paytitude · built 9 October 2026

## 1. What was delivered

| File | What it is | Status |
| --- | --- | --- |
| `Paytitude_R2.pptx` | Live deck: cover, 15 content slides, "Annexures" divider, annexures A1–A8 (25 slides); speaker notes on every slide; Fade transitions, two Morph transitions, click builds | Passes the OOXML package validator; opens and renders in LibreOffice |
| `Paytitude_R2.pdf` | Submission PDF exported from the PPTX (25 pages, 16:9); final animation states fully visible | Rendered with LibreOffice (Carlito, metric-compatible with Calibri) |
| `Paytitude_R2_Annexure.xlsx` | 13 sheets, live formulas (231), recalculated with **0 formula errors** | 62/62 cross-checks against `build/model.py` pass |
| `storyboard.md` | Per-slide headline, message, exact on-slide text with coordinates, status chips, animation sequence, speaker notes, sources; headline sequence; compliance matrix | Generated from the deck builder, so it can't drift from the deck |
| `reference_analysis.md` | Stage A: animation and structural grammar, and how it maps onto the 15 slides | Approved at Checkpoint 1 |
| `build/` | `build_all.sh` (one-command rebuild), `model.py` (single source of truth), `build_deck.py`, `build_annexure.py`, `deckkit.py` (drawing + animation XML), `fill_validation.py`, audits | Reproducible from `inputs/` |

**Not delivered: real validation results.** No validation file existed, so slide 10 is a fully designed template with magenta placeholders (section 5).

## 2. Inputs found and missing

| Input | Status | How it was used |
| --- | --- | --- |
| `Paytm_Track_B_Solution_Revised.md` | Found, read in full | Source of truth for the product, segment, model, pilot and risks |
| `Paytm_Track_B_VOCs.xlsx` (50 VOCs, Methodology Notes) | Found, read in full | All 50 rows in `VOC_Synthetic`; every segment count recomputed by COUNTIFS and matched to the solution document (Group 1: 16, 7/9/0; Group 3: 18, 1/4/13; 23 of 42 next-day or separate; 41 of 50 pay vendors by UPI at least 2–3 times a week; 11 contradictory rows, none in Group 1) |
| `Paytitude_ExecSummary.pdf` (Round 1) | Found, read in full | Change log verified against it (section 6) |
| Round 2 guidelines PDF and problem statement PDF | Found, read in full | Compliance matrix |
| `Team_Mythos_..._Animation_Analysis.md` | Found | Stand-in for the reference deck |
| Reference deck `.pptx` | **Missing.** The Google Drive link was blocked by this environment's network policy (`docs.google.com`, `drive.google.com`) | Animation grammar derived from the written analysis instead; exact timings, click counts and Morph pairs could not be parsed |
| `Paytm_Track_B_Story_and_Slide_Architecture.md` | **Missing** | Narrative taken from the brief and the solution document |
| `Paytitude_VOC.xlsx` (Round 1 VOC workbook) | **Missing** | Round 1 VOC claims could not be checked (see the risk in section 6) |
| Notes from the real merchant conversations | **Missing** | `VOC_Real` lists the five business types named in the brief, with notes pending; slide 10 and A1 show "n = [__]" |
| Validation results (≥20 users) | **Missing** | Slide 10 template + `Validation_Log` + `fill_validation.py` |
| UI mock-up images | None | Concept screens drawn as native shapes (slides 1, 2, 8, 15) |

## 3. Reference-deck animation grammar and how it was applied

The reference .pptx was not accessible, so the grammar comes from the written analysis (`reference_analysis.md`). The rules applied:

- **Headlines never animate**: the assertion is read first, then the evidence builds.
- **Build in reading order**: left to right for journeys, legs, timelines and roadmaps; top to bottom for bands, rows and funnels; clockwise for the habit loop.
- **The consequence comes last**: the bridge line (slide 2), the resolving line (slide 3), the step counter reaching 4 (slide 4), the target quadrant (slide 5), the crossed-out path (slide 6), and the "same app" callback (slide 15).
- **Few effect families**: Fade (presetID 10) by default, Wipe (presetID 22) only for things that flow, and at most one Grow/Shrink emphasis pulse per slide (presetID 6).
- **Motion is concentrated on four moments**: the hook (slide 2), the diagnosis (slides 3–4), the product (slides 6–8) and the decision (slides 14–15). Evidence slides have 2–3 light builds; annexures are static.
- **Fade transition on every slide.** Morph is used on slide 8 (after-flow card → flow strip, `!!flow`) and slide 15 (from slide 14). Because Morph only pairs consecutive slides, the slide 4 → 7 and slide 2 → 15 callbacks are built inside slides 7 and 15 instead (agreed at Checkpoint 1).
- **Final states are complete** (no exit effects), so the PDF is fully legible.

**Animation inventory** (from the built file):

```
== Animation and transition inventory
  slide  1: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide  2: transition=fade                   clicks=0 auto=1 effects=5 presets=['entr:10']
  slide  3: transition=fade                   clicks=2 auto=0 effects=2 presets=['entr:10']
  slide  4: transition=fade                   clicks=3 auto=0 effects=6 presets=['emph:6', 'entr:10']
  slide  5: transition=fade                   clicks=4 auto=0 effects=11 presets=['entr:10', 'entr:22']
  slide  6: transition=fade                   clicks=2 auto=0 effects=5 presets=['emph:6', 'entr:10']
  slide  7: transition=fade                   clicks=3 auto=0 effects=3 presets=['entr:10', 'entr:22']
  slide  8: transition=fade                   clicks=2 auto=0 effects=3 presets=['emph:6', 'entr:10']
  slide  9: transition=morph (fade fallback)  clicks=4 auto=0 effects=7 presets=['entr:10', 'entr:22']
  slide 10: transition=fade                   clicks=3 auto=0 effects=9 presets=['entr:10']
  slide 11: transition=fade                   clicks=2 auto=0 effects=2 presets=['entr:10']
  slide 12: transition=fade                   clicks=2 auto=0 effects=8 presets=['entr:10']
  slide 13: transition=fade                   clicks=3 auto=0 effects=3 presets=['entr:10']
  slide 14: transition=fade                   clicks=2 auto=0 effects=5 presets=['entr:10', 'entr:22']
  slide 15: transition=fade                   clicks=3 auto=0 effects=4 presets=['entr:10', 'entr:22']
  slide 16: transition=morph (fade fallback)  clicks=2 auto=0 effects=3 presets=['entr:10', 'entr:22']
  slide 17: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 18: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 19: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 20: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 21: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 22: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 23: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 24: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
  slide 25: transition=fade                   clicks=0 auto=0 effects=0 presets=[]
```

**Effects that render only in PowerPoint:**
- Morph needs PowerPoint 2019 or 365; other apps use the Fade fallback.
- Grow/Shrink emphasis pulses and Wipe directions play in PowerPoint; LibreOffice and Keynote may approximate them.
- The PDF shows final states only.

Every animation target `spid` was checked against the slide's shape IDs, and the package passes the OOXML validator. **Play the deck once in PowerPoint Slide Show** before presenting; the build couldn't be tested in PowerPoint itself.

## 4. Round 2 compliance matrix

| Section | Guideline item | Where it is met |
| --- | --- | --- |
| General | Build on Round 1; same track and segment; say what changed and why | 1 (change band), 2, 5, A7 |
| Deliverables | 15-slide deck excluding cover and annexures | Slides 1–15 between cover and 'Annexures' divider |
| Deliverables | Opens with a one-slide executive summary | 1 |
| Deliverables | Optional annexures: prototypes, extra VOCs | 8, A2, A3; workbook VOC_Synthetic, VOC_Real |
| Deliverables | File names TeamName_R2.pdf and TeamName_R2_Annexure.xlsx | Paytitude_R2.pdf, Paytitude_R2_Annexure.xlsx |
| 1. Validation | Test with ≥20 target users (concept test, prototype walkthrough or trial) | 10 (template, results pending), A8, Validation_Log |
| 1. Validation | Report what users did or committed to | 10 (behaviour tiles: observed / commitment / action) |
| 1. Validation | State method, n, secondary sources, limits | 10, A1 |
| 2. Design & feasibility | User journey before and after | 4 (before), 7 (before + after), 8 (concept screens), A3 |
| 2. Design & feasibility | Paytm features used; what is new | 6, 11 |
| 2. Design & feasibility | Regulatory or partner dependencies | 6, 11, A6 |
| 2. Design & feasibility | Rough build effort (S / M / L) | 11 |
| 3. GTM & pilot | Target segment | 5, 12 |
| 3. GTM & pilot | Channels, partners, messaging | 12 |
| 3. GTM & pilot | Pilot cohort and control group | 13, A4 |
| 3. GTM & pilot | Baseline and targets | 13, 14, A4 |
| 3. GTM & pilot | What result means scale up or stop | 13, 15 |
| 3. GTM & pilot | How to scale afterwards | 13, 15 |
| 4. Business impact | Main metric: increase in Paytm share of segment UPI GMV | 14, A5, Share_Metric |
| 4. Business impact | Early indicators (activation, repeat) | 14, 12, A4 |
| 4. Business impact | Size of the opportunity | 14, A5 |
| 4. Business impact | Cost per extra active user and per ₹ of extra GMV | 14, A5, Unit_Costs |
| 4. Business impact | Whether usage holds once incentives stop; no cashback dependence | 9, 14, 13 |
| 4. Business impact | Sensitivity on 2–3 key assumptions | 14, Sensitivity |
| 4. Business impact | Key risks incl. competitor response, and mitigation | 9, 15, A6 |

## 5. Open placeholders and gaps (must be closed before submitting)

1. **Slide 10, solution validation (≥20 target users), is the biggest gap.** Everything in magenta is a placeholder: the headline, n, the four behaviour metrics, the context line, and "n = [__]" for the exploratory conversations.
   - Run the test using the guide in A8, and fill one row per merchant in `Validation_Log` from row 19.
   - Then run `python3 build/fill_validation.py Paytitude_R2_Annexure.xlsx Paytitude_R2.pptx --pdf Paytitude_R2.pdf --exploratory-n <count>`. It rewrites slide 10, the validation band on slide 1 and the A1 strip, and re-exports the PDF. (Tested on a throwaway copy with dummy rows; nothing from that test is in the deliverables.)
   - Then rewrite the slide 10 speaker notes. If the results weaken the thesis, the headline and slide 1 must say so.
2. **The exploratory conversations need notes.** The brief names five (pharmacy, café, FMCG retailer, tractor dealer, a routine vendor-UPI payer), but no notes were in the inputs. Add them to `VOC_Real` with the date, key points and verbatim.
3. **Exec summary validation band** reads "[results pending, n = __]" until step 1 is done.

## 6. Round 1 → Round 2 changes and a consistency risk

The change log (slide 1 band, A7 and `Change_Log_R1_R2`) was verified against the Round 1 PDF. Three corrections were made to the brief's version:
- **Segment:** Round 1's segment was precisely "Paytm QR / Soundbox merchants collecting over ₹1 lakh a month on UPI (≈24 lakh), starting in Andheri trade clusters". Round 2 keeps the base and re-cuts it by behaviour. Note that the base-case eligible count (29.9 lakh) is larger than Round 1's 24 lakh, because the cut is behavioural, not by collection value. So the deck says "re-cut", not "narrowed".
- **Pilot:** Round 1 already had a control group (500 Andheri merchants vs control). The change is to a 90-day, territory-randomised 3,000 vs 3,000 design with ITT share targets and gates, so the deck doesn't claim the control group is new.
- **Two further Round 1 layers were also dropped:** invoice-matched receipts with the distributor network, and due-date payments.

**Risk to resolve before submission.** Round 1 described its evidence as "VOC dataset, n=50 Andheri merchants … 50 owners in 6 trade categories … (10 in-depth) … 250 logged". The Round 2 VOC workbook is disclosed as synthetic and spans 16 cities.
- The R2 deck never presents any VOC as field research, and A7 states the Round 1 wording factually.
- Judges may still ask about the difference. Decide how to explain it (and check `Paytitude_VOC.xlsx`, which wasn't supplied) before you submit.

## 7. Headline and fact changes versus the brief

| Item | Brief | Built | Why |
| --- | --- | --- | --- |
| Slide 6 headline | "… in one compliant flow, with no loan" | "… in one flow built to fit RBI's payout rules, with no loan" | Compliance confirmation is still pending; "compliant" reads as a claim of approval (section 14 rule) |
| Slide 10 headline | From real results | Magenta placeholder | No validation data |
| Slide 14 headline | Composed from results | "Base case (projection): +1.6 points of Paytm share of segment vendor UPI in year one, ≈₹2,660 crore a year, at ≈₹3,200 per extra active merchant" | Built by formula from the model |
| Paytm settlement wording | "by the next working day in most cases"; "usually settled within a few hours" | "Usually settled to your bank within T+1 days" (Paytm for Business support); "within a few business hours or at the T+N cycle" (Paytm Payments docs) | The brief's exact quotes couldn't be found; verified wording used instead |
| NPCI app shares | Paytm ~8%, PhonePe ~46%, Google Pay ~33% | 8.0% / 45.6% / 32.3%, August 2026 (volume) | Latest month available; from a secondary report of NPCI data; confirm on npci.org.in |
| Paytm for Business listing | "collections, settlements, refunds, loans" | "collections, settlements, statements and loans" | Matches the listing text that could be verified (App Store copy) |
| RBI payout rule | Primary text | Footnoted "per legal summaries (S10, S11); primary RBI text to be confirmed" | The primary Directions text couldn't be fetched |
| Cost per extra active user | ≈₹3,000 (₹200 × 1,000 ÷ 65) | ≈₹3,200 headline (visits + free settlement ÷ incremental MTU); ₹3,080 pilot metric shown in A5 | The full formula includes settlement cost, as the brief asked |

All other facts in brief section 7.1 were verified via web search on 9 Oct 2026. Status per source is in the `Sources` sheet.

## 8. Model notes and assumptions

- **The model is a single source of truth.** `build/model.py` and `Funnel_Model` compute the same chain, and `check_numbers.py` asserts they match (62/62).
- **The ₹2,660 crore base reproduces exactly from formulas**, with no rounding fudge:
  - settlement share = 23/42 and friction share = 16/23 (live from `VOC_Synthetic`);
  - not-already-a-payer = 9/16;
  - vendor payments = (2.5 + 4 + 5) × 4.3 weeks + 26, ÷ 4 = 18.86 a month;
  - result: ₹2,661 crore, displayed as ₹2,660 crore. "₹2,700 crore" appears nowhere.
- **Display rounding:** nearest ₹10 crore below ₹10,000 crore and nearest ₹100 crore above (₹240 / ₹2,660 / ₹19,400 crore); counts to the nearest 1,000.
- **Team assumptions, not Paytm figures:**
  - pilot build ₹0.5 crore (S) and full payer flow ₹5 crore (M/L);
  - visit cost ₹200 (₹150–300) applied to **every** exposed merchant (conservative);
  - free settlement priced as a float ceiling (11%, 1 day, ₹0.75 a payment).
- **Cost per ₹ of GMV** = year-one cost ÷ annual run-rate GMV: ₹0.009 without build, ₹0.011 with. With a 50% year-one ramp it is ≈₹0.023, which is footnoted on slide 14.
- **Share metric:**
  - +3.9 pts = incremental GMV ÷ exposed-cohort vendor-UPI pool;
  - +1.6 pts = incremental GMV ÷ whole eligible pool (₹14,100 crore a month, ≈₹1.7 lakh crore a year, labelled addressable, not incremental).
- **Overlap footnote:** the GMV baseline overlap (15%) differs from the MTU exclusion (44% already sometimes pay via Paytm). This is footnoted in `Funnel_Model!C28`: "Occasional Paytm payers' shifted payments are assumed mostly new; verify in pilot."
- **Phase 0 dependency:** Phase 0 relies on manual instant settlement being available to every device merchant. It is listed as a dependency (slide 11, A6).
- **Pilot power (A4)** is indicative and marked "to validate".

## 9. Number audit (every key number vs its source)

| Slide | Number on slide | Source (cell or reference) | Status | Present |
| --- | --- | --- | --- | --- |
| 1 | 1.57 crore | S1 Paytm Q1 FY27 release | Fact | yes |
| 1 | 16 of 50, 7 yes / 9 maybe / 0 no | Segment_Rules!C12:F12 | Synthetic | yes |
| 1 | +1.6 pts | Share_Metric!C14 (1.57) | Projection | yes |
| 1 | +3.9 pts | Share_Metric!C13 (3.93) | Projection | yes |
| 1 | ₹2,660 crore | Funnel_Model!C31 (2,661) | Projection | yes |
| 1 | ₹240–19,400 crore | Funnel_Model!B31 (242), D31 (19,438) | Projection | yes |
| 1 | ₹3,200 | Unit_Costs!B24 (3,196) | Projection | yes |
| 1 | 3,000 vs 3,000 | Pilot_Design | Proposal | yes |
| 2 | 1.57 crore | S1 | Fact | yes |
| 2 | 8.0% | S2 NPCI Aug 2026 (8.03%) | Fact (secondary report) | yes |
| 2 | 45.6% | S2 (45.64%) | Fact (secondary report) | yes |
| 2 | 32.3% | S2 (32.26%) | Fact (secondary report) | yes |
| 2 | 0 of 50 | VOC_Synthetic col I (no Paytm main app) | Synthetic | yes |
| 2 | 29 use PhonePe, 15 Google Pay | VOC_Synthetic col I | Synthetic | yes |
| 3 | 41 of 50 | Segment_Rules!C33 | Synthetic | yes |
| 3 | PhonePe 29, Google Pay 15 | VOC_Synthetic col I | Synthetic | yes |
| 4 | T+1 | S4 Paytm for Business support | Fact | yes |
| 4 | ₹1–3 a request, once an hour, not after 11 pm | S6, S7 PhonePe help | Fact | yes |
| 4 | ₹12,400 | Illustrative amount | Illustrative | yes |
| 5 | 16 · Group 1 | Segment_Rules!C38 | Synthetic | yes |
| 5 | 7 yes · 9 maybe · 0 no | Segment_Rules!D38:F38 | Synthetic | yes |
| 5 | 4 yes · 3 maybe · 2 no | Segment_Rules!D40:F40 | Synthetic | yes |
| 5 | 0 yes · 5 maybe · 2 no | Segment_Rules!D39:F39 | Synthetic | yes |
| 5 | 0 yes · 2 maybe · 6 no | Segment_Rules!D41:F41 | Synthetic | yes |
| 5 | 7 of 9 rows contradictory | Segment_Rules row 40 vs contradiction flags | Synthetic (audit) | yes |
| 5 | Group 3 (18) | Segment_Rules!C14 | Synthetic | yes |
| 6 | ₹40 lakh | S10, S11 legal summaries of RBI PA Directions 2025 | Fact (primary text to confirm) | yes |
| 6 | ₹6,800 | Illustrative amount | Illustrative | yes |
| 7 | up to T+1 | S4 | Fact | yes |
| 8 | ₹9,250 | Illustrative amount | Illustrative | yes |
| 9 | ₹1–3 a request | S6 | Fact | yes |
| 10 | [__%] | Validation_Log (empty) | Placeholder | yes |
| 12 | 40% of eligible | Funnel_Model!C10 | Assumption | yes |
| 12 | 15–25% | Share_Metric early indicators | Hypothesis | yes |
| 12 | 50% | Funnel_Model!C19 | Hypothesis | yes |
| 13 | ≈3,000 | Pilot_Design | Proposal | yes |
| 13 | +4 to +6 pts | Share_Metric!C15 (4.6 before overlap) | Hypothesis | yes |
| 13 | ≥15% | Pilot_Design gates | Decision rule | yes |
| 13 | <8% | Pilot_Design gates | Decision rule | yes |
| 14 | +1.6 pts | Share_Metric!C14 | Projection | yes |
| 14 | +3.9 pts | Share_Metric!C13 | Projection | yes |
| 14 | ₹2,660 crore | Funnel_Model!C31 | Projection | yes |
| 14 | ₹1.7 lakh crore | Share_Metric!C10 (1.69) | Projection (addressable pool) | yes |
| 14 | ₹3,900 with build | Unit_Costs!B25 (3,903) | Projection | yes |
| 14 | ₹0.009 per ₹ | Unit_Costs!B26 (0.0093) | Projection | yes |
| 14 | ₹0.011 with build | Unit_Costs!B27 (0.0114) | Projection | yes |
| 14 | ≈65 MTU per 1,000 | Funnel_Model!C32 (65.0) | Projection | yes |
| 14 | ≈₹0.023 | Unit_Costs!B30 (0.0228) | Projection | yes |
| 15 | 3,000 vs 3,000 | Pilot_Design | Proposal | yes |
| 15 | 25% | Solution doc §13 P0 hypothesis threshold (G0) | Decision rule | yes |
| A5 | 20.9 L | Funnel_Model!B9 | Projection | yes |
| A5 | 29.9 L | Funnel_Model!C9 | Projection | yes |
| A5 | 35.9 L | Funnel_Model!D9 | Projection | yes |
| A5 | 12.0 L | Funnel_Model!C11 | Projection | yes |
| A5 | 23.1% | Funnel_Model!C17 | Assumption × synthetic | yes |
| A5 | 2.77 L | Funnel_Model!C18 | Projection | yes |
| A5 | 1.38 L | Funnel_Model!C20 | Projection | yes |
| A5 | 78,000 | Funnel_Model!C22 (77,799) | Projection | yes |
| A5 | 10.4 L | Funnel_Model!C26 | Projection | yes |
| A5 | ₹222 cr | Funnel_Model!C30 (221.8) | Projection | yes |
| A5 | ₹14,100 crore/month | Share_Metric!C9 (14,102) | Projection (addressable) | yes |
| A5 | ₹0.75 | Unit_Costs!B11 (0.753) | Assumption | yes |
| A5 | ₹3,080 | Unit_Costs!B31 (3,075) | Projection | yes |
| A5 | ₹2,400–4,700 | Unit_Costs!B32:B33 (2,428 / 4,734) | Projection | yes |
| A7 | ≈₹27,000 crore | Round 1 PDF (S17) | Round 1 figure (dropped) | yes |
| A7 | 500 Andheri merchants | Round 1 PDF (S17) | Round 1 figure | yes |

All 66 key numbers were found on their slides by an automated check (`build/number_audit.py`).

## 10. Claims audit

`build/audit.py` searches slide text and speaker notes for every banned claim in brief section 14:
- "interviewed 50", "will switch", forecast (outside "not a forecast"), approved, only company, can't copy, escrow, "directly from collections", "is not credit", MDR-doesn't-apply, ₹2,700 crore, and others.

**Result: 0 unexplained hits.** Every remaining mention of MDR, cashback, credit, ledger or rewards is a negation ("no cashback", "no credit") or a Round 1 history item (A7). The 50-row dataset is labelled synthetic on every slide that uses it. Projections are labelled "projection, not forecast". Compliance is always "pending".

## 11. Visual QA

- **Every one of the 25 pages was rendered to PNG and inspected.** Fixed in the process:
  - theme shadows that LibreOffice drew;
  - chips running past the slide edge on slide 1;
  - phone text wrapping on slide 2;
  - label collisions on slides 5, 9, 10 and 15 and A1;
  - an annexure table running into the footer (A7);
  - body text raised to ≥12 pt.
- **Remaining text under 12 pt is limited to:** sources and footers (9 pt); uppercase labels; status chips; concept-prototype screen text; and Hinglish English glosses (11 pt).
- **Word counts (excluding footer):** content slides run 120–260 words, with slide 1 the densest. The reference deck's density could not be measured, so the "≤ reference + 25%" check couldn't be run.

## 12. Before you submit: checklist

1. Run the ≥20-user validation, fill `Validation_Log`, and run `fill_validation.py` (section 5). Rewrite the slide 10 notes. If results weaken the thesis, update the headlines on slides 1 and 10.
2. Add the exploratory-conversation notes to `VOC_Real`, and pass `--exploratory-n`.
3. Resolve the Round 1 evidence wording question (section 6).
4. Confirm NPCI app-wise figures on npci.org.in (or update to September 2026 when published), and read the RBI PA Directions 2025 payout clause in the primary text.
5. Open the PPTX in PowerPoint 2019 or 365. Play it once in Slide Show to check the Morph on slides 8 and 15 and every click build. Then re-export the PDF from PowerPoint if you prefer genuine Calibri.
6. To check the animation grammar against the real reference deck, upload the .pptx here (or allow `docs.google.com` and `drive.google.com` in the environment's network settings) and ask for a re-check.
7. Submit `Paytitude_R2.pdf` and `Paytitude_R2_Annexure.xlsx` (file names match the guideline).
