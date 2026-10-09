# Reference Deck Analysis: Animation and Structure (Stage A)

Paytitude · Paytm UPI Growth Challenge, Track B · Round 2 · 9 October 2026

## 0. What this analysis is based on

**The reference `.pptx` was not attached.** The workspace has only `Team_Mythos_Slide_by_Slide_Storytelling_Animation_Analysis.md`, a written analysis of the 7-slide Team Mythos (ISB) Accenture B-School Challenge deck. So I couldn't:

- unzip `ppt/slides/slideN.xml`;
- read `<p:transition>`, `<p:timing>`, `presetID`/`presetClass`, durations, delays, `spid` targets or `bldP` builds;
- find `!!` Morph pairs.

Everything below comes from the written analysis. Figures that need the XML (exact durations, click counts, transition type) are marked **[not determinable]**. Where I had to fill a gap, the design default I chose is marked **[default]**. If you attach the `.pptx`, I'll replace sections 1 and 4 with parsed values. The script is ready (`lxml` over every slide's XML).

---

## 1. Animation inventory, as described

| Ref slide | Role | Transition | Effects described, in narrative order | Effect families | Morph pairs |
| --- | --- | --- | --- | --- | --- |
| 1 | Thesis cover | [not determinable] | Click-controlled elements; embedded video with a play command | Media play, entrance | [not determinable] |
| 2 | Business contradiction | [not determinable] | Central image as the anchor. Four metric clusters revealed with staggered delays: quality, then scale, then CX deficit, then **falling rank and share last** | Fade, directional Wipe, **Wheel** (one), staggered delays | — |
| 3 | Root-cause diagnosis | [not determinable] | Journey built around the dealer. Broken handoffs surfaced. Diagnostic questions and counts revealed. **The headline changes from its first state to its final state** ("improved each step. The journey still breaks.") | Fade, Wipe, **colour emphasis**, motion, scale. Dense | — |
| 4 | Operating model | [not determinable] | The four controls in order (context, owner, decision, outcome). Then the rules, AI and human layers. **The governance line lands last** | Fade, scale, motion, colour emphasis, Wipe. Dense | — |
| 5 | Product proof (UI) | [not determinable] | Dashboard, then the unresolved item highlighted, then the owner and deadline, then the manager's view, then the **return to "Priya"** | Fade, colour emphasis, scale, motion, Wipe, media | [not determinable] |
| 6 | Scale roadmap | [not determinable] | Five maturity stages built **left to right** | Sequential Wipe and Fade, colour emphasis, motion, scale | — |
| 7 | Decision and value | [not determinable] | ₹750 cr envelope, then the ₹690 cr kept, then the ₹60 cr redirected, then what pauses, then 420 outlets, then the value split, then ROIC and margin, then **the Priya callback**. The heaviest slide | Fade (many), motion, scale, Wipe, colour emphasis, video play/pause | — |

**Per-slide intensity, as described:** slides 3, 4 and 7 are the heaviest (diagnosis, solution logic, value). Slides 2, 5 and 6 are medium. Slide 1 is media-led. Click counts are [not determinable]. From the described sequences, the logical beats are about 4 on slide 2, 5 on slides 3 to 6, and 8 on slide 7.

---

## 2. Animation grammar: 9 rules derived for our deck

1. **The assertion headline is static. The evidence builds underneath it.** The audience reads the conclusion first and watches the proof assemble. One exception, borrowed from ref slide 3: on the diagnosis slide, the *resolving line* appears last, after the diagram has built.
2. **Build in reading order.** Left to right for journeys, roadmaps and timelines (ref 6). Top to bottom for stacked bands and funnels. Centre outward for anchor-and-satellite layouts (ref 2).
3. **The consequence comes last.** On every slide, the click with the most weight is the final one (ref 2 ends on market share; ref 7 ends on the human callback).
4. **One idea per click.** A click reveals one coherent cluster: a node, a leg, a row group or a metric cluster. Never individual labels (the analysis warns against "animating every label").
5. **Few effect families, used consistently.** **Fade** is the default entrance. **Wipe** (directional) is reserved for things that flow, such as arrows, journey legs and timeline bars. **Colour emphasis** marks the cause or target (at most one per slide). **Scale/zoom** is for a single hero number. No fly-ins, bounces or spins.
6. **Spend motion on four moments only:** the hook (our slide 2), the diagnosis (slides 3 to 4), the product proof (slides 6 to 8), and the decision and value (slides 14 to 15). Other slides use light builds (2 or 3 clicks) or none.
7. **The human thread returns at the close.** The ref deck introduces Priya and brings her back on the final slide. Our equivalent is the merchant on slide 2's split screen, who returns on slide 15 with Paytm on both phones.
8. **The final state is complete.** Every animated object ends visible, and there are no exit effects that would hide content in a static export. So the PDF shows the finished slide.
9. **Timings [default, since the reference durations aren't determinable]:** entrance 0.4–0.5 s, wipes 0.5–0.6 s, stagger 0.15–0.2 s for "after previous", emphasis 0.5 s, one Fade transition at 0.5 s, Morph 1.0 s.

---

## 3. Structural grammar

| Dimension | Reference deck | Implication for our 15 slides |
| --- | --- | --- |
| **Narrative arc** | Contradiction, then diagnosis, then operating principle, then product proof, then scale pathway, then investment decision, then human callback | Maps one to one onto our beats (section 5 below). Slides 10 to 13 add the validation, feasibility, GTM and pilot that Round 2 requires |
| **Opening** | The cover carries the thesis, not just the event name | Our cover headline is the thesis: *Settle & Pay: making Paytm the place merchants spend the money they see arrive* |
| **Dividers** | None (7 slides) | No dividers inside the 15. One "Annexures" divider after slide 15 |
| **Dark/light rhythm** | All dark (black canvas, white uppercase headlines, purple accent, red for risk) | **Proposal:** a hybrid. Dark navy for the four story moments (cover, 2, 6, 15) plus the annexure divider. Light for evidence and analysis slides, which keeps dense tables legible in the PDF the judges read. Our accent is cyan; red is used only for crossed-out paths and risks |
| **Headline style** | Short, assertive, uppercase, about 4 to 10 words | Our headlines are longer assertions (the brief fixes them). Kept in sentence case at 26–28 pt, two lines at most. Uppercase is used only for small eyebrow labels |
| **Density** | Medium to high. Four metric clusters, or one diagram plus a short governance line | Target 60–110 words per content slide plus footer. The executive summary and the feasibility matrix may reach about 140 |
| **Visual types** | Anchor image plus satellites; circular system diagram; control model; realistic UI mock-up; left-to-right maturity roadmap; budget allocation | Split-screen phones (2); 2-column comparison plus tree (3); numbered journey (4, 7); 2×2 (5); mechanism (6); phone mock-ups (8); table plus loop (9); results panel (10); matrix (11); funnel (12); timeline plus gates (13); waterfall plus sensitivity (14); risk table plus roadmap plus callback (15) |
| **Hand-offs** | Each slide answers the question the previous one raised | Each headline ends on the question the next slide answers (storyboard, Stage B) |
| **Closing callback** | The financial close returns to Priya and the opening thesis | Slide 15 brings back slide 2's split screen with "Paytm on both phones", restating the thesis as the outcome |
| **Footer** | Small, restrained footer and number | "Track B · Paytitude", the slide number, sources, and status chips at 9–10 pt |

---

## 4. What we can and can't reproduce (python-pptx plus lxml XML injection)

| Effect | Reproducible? | How | Renders in |
| --- | --- | --- | --- |
| Fade transition | Yes, reliably | `<p:transition spd="med"><p:fade/></p:transition>` | PowerPoint, LibreOffice, Keynote |
| **Morph** transition | Yes, with care | `mc:AlternateContent` → `mc:Choice Requires="p159"` → `<p159:morph option="byObject"/>`, with a `<p:fade/>` fallback. Shapes share `!!name` across the paired slides | **PowerPoint 2019/365 only.** Other apps show the Fade fallback |
| Entrance Fade (`presetID 10`) | Yes | `<p:timing>` with `clickEffect` / `withEffect` / `afterEffect` nodes, `animEffect filter="fade"` | PowerPoint; mostly LibreOffice |
| Entrance Wipe (`presetID 22`, from left: subtype 8) | Yes | `animEffect filter="wipe(left)"` | PowerPoint; mostly LibreOffice |
| Entrance Zoom (`presetID 53`) | Yes | `animScale` plus Fade | PowerPoint |
| Emphasis colour pulse | Partly | Emphasis Pulse (`presetID 26`, `emph`) is reliable. Full colour-change (`presetID 19`, `animClr`) is fragile | PowerPoint |
| Wheel entrance | Possible, not used | Not needed; it's a single decorative effect in the ref | — |
| Motion paths | Possible, not used | `animMotion`. Avoided: brittle, and they add little for our content | — |
| Embedded video | Not used | No source video. Media-dependent openings are a risk the analysis itself flags | — |
| Headline first-state/final-state swap | Yes | Two text boxes: the final line fades in last. The first state needs no exit effect | PowerPoint; the PDF shows both, so I use a *resolving line* under the diagram rather than a swap |

**Integrity plan.** After injection, re-open every slide with python-pptx, check the XML namespaces, and round-trip through LibreOffice headless. Any effect that breaks the file is removed and logged. PDF export via LibreOffice ignores animation and renders final states.

---

## 5. Proposal: mapping the grammar onto our 15 slides

I propose we keep the brief's 15-slide order. It already follows the reference arc. **Contradiction** is slide 2 (money in on Paytm, money out on another app). **Diagnosis** runs across slides 3 to 5 (app switching, not adoption; the four-step journey; the segment where the step is largest). The **operating principle** is slide 6 (two compliant legs, one flow). **Product proof** is slides 7 to 8 (before and after, re-using slide 4's journey shapes, then concept screens). The Round 2 **validation, feasibility, GTM and pilot** block is slides 10 to 13. The **decision and economics** are slides 14 to 15, ending with the slide 2 split screen returning with Paytm on both phones, as the ref deck's Priya callback does.

Motion concentrates on four moments: slide 2 (3 clicks), slides 3 to 4 (tree and step counter), slides 6 to 8 (leg-by-leg mechanism, the four-step collapse on slide 7, screens in sequence), and slides 14 to 15 (waterfall, then sensitivity; the split-screen callback, then gates). Evidence slides (5, 9 to 13) get 2 or 3 light Fade or Wipe builds, and the executive summary bands appear automatically with a 0.2 s stagger. Headlines never animate. Fade is the standard transition. Dark navy marks the story moments (cover, 2, 6, 15); light slides carry the evidence.

**One technical constraint changes the brief's two Morph moments.** PowerPoint Morph only pairs *consecutive* slides, so slide 4 can't Morph into slide 7, and slide 2 can't Morph into slide 15, without extra slides in between, which would break the 15-slide count. My recommendation:

- **Slide 7:** open on the four-step "before" row, styled exactly like slide 4 so it reads as the same journey. Then, on click, the four `!!step` shapes collapse into the single "after" flow (a scale-and-fade build). The "before" row stays visible in faded form, so both journeys are in the PDF, as Guideline 2 requires.
- **Slide 15:** re-state slide 2's split screen in miniature (same shapes, colours and names). On click, the right phone's app label and screen cross-fade from "Other app" to "Paytm".
- **True Morph is still used where slides are adjacent:** 7→8 (the after-flow phone grows into the three concept screens) and 14→15 (shared title and footer geometry). It degrades to Fade outside PowerPoint 2019/365.
