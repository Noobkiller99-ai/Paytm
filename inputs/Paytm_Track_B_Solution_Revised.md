# Paytm Business Pay: Winning Merchants' Outgoing Business Payments

Paytm UPI Growth Challenge, Track B · Revised solution · 9 October 2026

---

## 1. Executive Summary

**The opportunity.** Merchants who collect on Paytm already pay their vendors by UPI, often several times a week, but they do it on PhonePe or Google Pay. In the 50-merchant VOC dataset, 41 pay vendors by UPI at least two to three times a week, 42 collect on Paytm, and none uses Paytm as their main business-payment app. The behaviour Paytm wants already exists. What's missing is a reason to perform it on Paytm.

**The reason.** Merchants won't switch apps for a better button: "Same steps hain toh app kyun badlu?" They will consider switching when Paytm removes a step they can't avoid elsewhere. That step is waiting for collections to settle, or moving money from the account collections land in to the account they pay from. The evidence points to a narrow, identifiable group:

| Merchant group | Merchants | Would switch: yes / maybe / no |
| --- | --- | --- |
| High potential: Paytm collector, next-day or separate-account settlement, weekly vendor UPI, a stated timing, transfer or staff-control friction | 16 of 50 | 7 / 9 / 0 |
| May try but unlikely to switch consistently | 16 of 50 | 4 / 8 / 4 |
| Little incremental value | 18 of 50 | 1 / 4 / 13 |

**The product.** Paytm Business Pay adds a **Settle & Pay** flow to Paytm for Business. In one flow, the merchant settles today's Paytm collections into their own account and pays the supplier from that account, free when the money goes to a supplier. The merchant's personal UPI app stays untouched. There's no credit, ledger or rewards in the MVP: no respondent reports high credit need, and nobody rejects the product for lacking credit.

**What public sources change.** Early settlement already exists. The Paytm for Business app offers manual "Instant Bank Settlements", and PhonePe sells "Settle Now" to selected merchants for ₹1–3 a request. So Paytm's edge is not access to unsettled money. It is three things no one offers together:
- settlement and supplier payment in one flow, in the app where merchants already watch their collections;
- the settlement free when it funds a business payment;
- the reach to tell merchants who complain about "waiting for settlement" that they don't have to.

RBI's 2025 rules for payment aggregators also shape the design. Paying a small merchant's supplier directly from collections isn't allowed, so the money must land in the merchant's own account first. The flow is built that way.

**The impact (assumption-driven, to be validated).** The base case reaches about **1.4 lakh repeat business-payment merchants** and about **78,000 incremental MTUs** by the end of year one. They add about **10 lakh extra Paytm business payments a month** and an annual run-rate of about **₹2,700 crore** in outgoing business UPI GMV. The cautious-to-upside range is wide (₹240 crore to ₹19,400 crore) because the share of Paytm merchants with next-day or separate-account settlement is not yet known. Paytm's own settlement data can resolve that before launch.

**The recommendation.** Start with a fast awareness release: surface instant settlement at the moment a merchant needs to pay a supplier, then hand off to Paytm UPI. That tests demand with almost no new build. Follow it with a randomised pilot of the full Settle & Pay flow, not a full launch. The pilot runs Settle & Pay for high-potential merchants, plus a second arm testing staff access for multi-payer shops. Two gates come first: Paytm's settlement data must confirm the size of the next-day and separate-account segment, and compliance must confirm that already-received collections can be settled free when they fund a supplier payment (Section 12).

---

## 2. Problem Statement and Growth Opportunity

**Problem statement.** Merchants who collect on Paytm make frequent outgoing business payments by UPI, yet route almost none of them through Paytm. Nothing in Paytm makes those payments easier than in the app they already use. Collections settle into a bank account, and any UPI app can pay from that account once the money arrives.

**Why it matters for Track B.** This is not a rail-adoption problem. The payments are already on UPI, and the merchant, not the supplier, chooses the app. Winning them requires one repeated decision by a merchant Paytm already serves. That decision would grow three Track B metrics:

| Metric | How Business Pay moves it |
| --- | --- |
| MTU | Merchants who collect on Paytm but have never paid through it become active Paytm transactors |
| GMV | Recurring vendor payments, several times a week per merchant, move onto Paytm |
| Frequency | Vendor payments are the most frequent business outflow, so each converted merchant adds multiple transactions a month |

**What is out of scope.** Invoice-led supplier payments that run on NEFT or RTGS because the supplier needs a bank trail. Four merchants in the dataset make planned payments this way, and forcing them onto UPI would add friction, not remove it.

---

## 3. Merchant Behaviour and VOC Insights

### 3.1 Evidence base and data audit

**Evidence status.** The workbook's Methodology Notes describe it as synthetic research for hypothesis stress-testing, deliberately including positive, ambiguous and negative cases. It is used here for structured VOC analysis, segmentation and concept stress-testing. It is not validated field research, and its counts are not market shares. Verbatims are quoted as dataset responses, not as statements by interviewed merchants.

**Audit of material issues:**

| Issue | Rows affected | Treatment |
| --- | --- | --- |
| Same-day settlement recorded, yet the merchant reports waiting for settlement before paying a supplier | 7 (V10, V11, V12, V17, V19, V35, V36) | Flagged as contradictory; excluded in the clean-sample sensitivity |
| No Paytm collection recorded, yet the merchant wants to pay from "today's collections" | 2 (V23, V40) | Flagged; kept in the "little value" group because there are no Paytm collections to pay from |
| Paytm QR collection recorded, yet the reaction or quote says the merchant doesn't collect on Paytm | 2 (V34, V42) | Flagged; excluded in the clean-sample sensitivity |
| Account-transfer pain where settlement isn't recorded as going to a separate account | 4 (V09, V30, V33, V35) | Treated as plausible: the settlement account may differ from the personal UPI account. Flagged as ambiguous |
| Secondary app identical to primary app | 2 (V11, V24) | Noted; no effect on conclusions |
| App chosen by a "manager" where no manager makes payments | 2 (V24, V29) | Noted; no effect on conclusions |
| Repeated verbatims: 15 distinct first quotes and 11 distinct second quotes across 50 rows; the most common first quote appears 8 times, the most common second quote 10 times | All | Quotes used as illustrations, never counted as independent evidence |
| 47 of 50 classed as "Small", including 10 with ₹8–20 lakh of monthly business payments | Sample mix | Medium shops (more staff, more control needs) are under-represented |
| No category has more than 5 respondents; Mumbai supplies 12 of 50 | Sample mix | No category-level conclusions; segments defined by behaviour |
| No merchant uses Paytm as the main business-payment app | Sample mix | Retention drivers of existing Paytm business payers can't be studied |

The 11 hard contradictions are the first three rows. The **clean sample** excludes them (n = 39). None of the 11 falls in the high-potential group, so the core segment finding is unchanged. One finding is materially affected, and is reported both ways below: interest in paying from collections falls from 16 of 50 to 10 of 39, because 6 of the 16 interested rows are contradictory.

### 3.2 What merchants do today

All denominators are 50 unless stated. "Paytm collectors" means the 42 merchants recorded as regularly collecting through a Paytm QR; 2 more collect on Paytm only for some customers or visitors, and 6 don't collect on Paytm at all.

| Dimension | Finding |
| --- | --- |
| Vendor UPI frequency | Daily 16; 4–6 times a week 8; 3–5 times a week 9; 2–3 times a week 8; weekly 7; rarely 2. So 41 (82%) pay vendors by UPI at least 2–3 times a week |
| Main business-payment app | PhonePe 29 (58%); Google Pay 15 (30%); bank app 6 (12%); Paytm 0 |
| Paytm for outgoing payments | Never 27 (54%); rarely 10 (20%); sometimes 13 (26%) |
| Settlement of Paytm collections (of 42 collectors) | Same day 19 (45%); next day 17 (40%); next day into a separate current account 6 (14%) |
| Who makes payments | Owner alone 22 (44%); owner plus spouse, sibling, son, staff, manager or accountant 24 (48%); accountant alone 4 (8%) |
| Who chooses the app | Owner 42 (84%); accountant 5 (10%); manager 3 (6%) |
| Payment occasion | Routine 26; routine and urgent 12; urgent only 8; planned bank payments 4 |
| Supplier credit | Cash or same day 7; 2–7 days 18; 7 days 8; 15 days 10; 15–60 days 7 |
| Cash-flow pain | Low 32 (64%); medium 13 (26%); high 5 (10%) |
| Credit need | Low 39 (78%); medium 11 (22%); high 0 |
| Would use without credit | Yes 33 (66%); maybe 17 (34%); no 0 |
| Would switch to Paytm | Yes 12 (24%); maybe 21 (42%); no 17 (34%) |

**Why merchants use their current app** (recorded reason): the supplier sends a QR on WhatsApp (6); fast for small payments (6); the local market uses it (4); PhonePe is already open and suppliers use it (4); staff already use it (3); suppliers or payment links already saved (3); habit in various forms (6); same-day settlement means no gap (2); accounting, approval or invoice processes (5); supplier insists on bank transfer (1).

### 3.3 How merchants reacted to Business Pay

| Reaction (grouped from the reaction column) | All 50 | Clean 39 | Would switch: yes / maybe / no (all 50) |
| --- | --- | --- | --- |
| Would use it to pay suppliers from today's collections or to avoid moving money between accounts | 16 | 10 | 9 / 7 / 0 |
| Values staff access with limits and owner visibility more than the app | 9 | 9 | 2 / 5 / 2 |
| Useful only for morning or urgent purchases | 4 | 1 | 1 / 2 / 1 |
| Interested only for accounting or verification | 2 | 2 | 0 / 1 / 1 |
| Would try it but keep their current app | 8 | 8 | 0 / 6 / 2 |
| Rejects it: same-day settlement, invoice-led payments, or no Paytm collections | 11 | 9 | 0 / 0 / 11 |

Stated interest is not adoption. "Yes" and "maybe" are treated as propensity signals and converted at assumed rates in the impact model (Section 10).

### 3.4 Five insights

**Insight 1: Settlement timing and destination separate interested merchants from indifferent ones.**

| Settlement (Paytm collectors) | Merchants | Would switch: yes / maybe / no | Interested in collections or staff control |
| --- | --- | --- | --- |
| Next day | 17 | 4 / 11 / 2 | 11 |
| Next day, separate current account | 6 | 3 / 3 / 0 | 4 |
| Same day (all rows) | 19 | 4 / 6 / 9 | 7 |
| Same day (clean sample) | 10 | 1 / 3 / 6 | 3 |

*Observed:* merchants settled the next day or into a separate account rarely rule out switching (2 of 23); same-day merchants often do (9 of 19, or 6 of 10 in the clean sample). *Friction:* when money settles the next day, today's sales can't pay this morning's supplier; when it settles into a separate account, it has to be moved before it can be spent. *Product implication:* lead with paying from collections and from the settlement account. *Growth opportunity:* target by settlement profile, which Paytm already holds. *Outcome to measure:* activation and repeat rates by settlement profile in the pilot.

**Insight 2: Within that group, a concrete friction is what separates "yes" from "maybe".** Of the 23 next-day or separate-account merchants, the 16 who report a timing, transfer or staff-control friction split 7 yes, 9 maybe, 0 no. The 7 with no friction split 0 yes, 5 maybe, 2 no, and all 7 say they'd try it but keep their current app. *Implication:* settlement profile alone is not enough; target the merchants who feel the friction, and lead messaging with the friction removed.

**Insight 3: Habit wins wherever there's no gap to close.** Twenty-one merchants give a parity or no-need reason as their key pain point: no switching benefit, habit, no differentiated benefit, no timing problem, relearning cost, or a supplier who requires bank transfer. Their quotes are consistent: "Same steps hain toh app kyun badlu?" and "Mera settlement same day aa jata hai, toh problem kya hai?" *Implication:* features every app has (saved suppliers, history, reminders) must be in the product, but they can't be the pitch. *Outcome to measure:* the share of Business Pay payments made when no timing or transfer gap existed (the habit guard metric).

**Insight 4: Business payments are shared, and some owners value control more than the app.** 28 merchants have someone besides the owner making payments, and all 9 who value staff limits and owner visibility are in that group. Six give the same second quote: "I don't want to change my personal UPI just to manage business spending." In the clean sample, control interest (9 of 39) is almost level with collections interest (10 of 39). *Implication:* position Business Pay as a separate place for business payments, with the personal app left alone. Test staff access as a pilot arm rather than leaving it to a later version.

**Insight 5: Credit is not the hook.** No merchant reports high credit need, nobody refuses the product without credit, and ten give the same second quote: "Loan nahi chahiye. Jo collect kiya hai, woh use karna hai." Five merchants report high cash-flow pain, but three of them report low credit need. Their pain is timing, not shortage. *Implication:* keep credit out of the MVP. Revisit only if the pilot shows payments regularly exceeding the day's collections.

### 3.5 What public sources add

The VOC dataset shows the friction; public sources show what already exists to solve it, and what the rules allow.

| Finding | Source | What it means for the solution |
| --- | --- | --- |
| Paytm's help pages give different settlement timings: "by the next working day in most cases", and elsewhere "usually settled within a few hours" | [Paytm for Business: settlement cycle](https://business.paytm.com/support/what-is-my-settlement-cycle); [settlement status](https://business.paytm.com/support/how-would-i-know-when-paytm-has-settled-my-payments-in-my-bank-account) | The real share of merchants waiting overnight is unknown publicly; Paytm's data must size it |
| The Paytm for Business app already offers "Instant Bank Settlements", with automatic or manual settlement; Paytm launched instant settlement for offline merchants in 2018 | [Google Play listing](https://play.google.com/store/apps/details?id=com.paytm.business&hl=en_US); [H2S Media, 2018](https://www.how2shout.com/news/paytm-introduces-instant-bank-settlement-for-merchants-to-improve-their-daily-cash-flows.html) | Merchants reporting a settlement gap may not know they can settle early. Part of the opportunity is awareness at the moment of need |
| The app's listing describes accepting money and refunds, not paying vendors | Google Play listing | A payer flow in Paytm for Business is new build, or a hand-off to the Paytm UPI app |
| PhonePe settles merchants by 8 am the next day; selected merchants can use "Settle Now" for ₹1–3 a request, at most once an hour, not after 11 pm | [PhonePe: settlement time](https://cms.phonepe.com/en/mx/merchant-help/settlements/can-i-change-settlement-time/); [Settle Now charges](https://cms.phonepe.com/en/mx/merchant-help/settlements/know-more-about-settlements/about-early-settlements/are-there-any-charges-raising-early-settlement-request/); [Settle Now limits](https://cms.phonepe.com/en/mx/merchant-help/on-demand-or-early-settlement/why-am-i-not-able-place-settle-now-request/) | Early settlement on its own is not a differentiator. PhonePe charges for it, limits it, and doesn't bundle it with a supplier payment |
| RBI's 2025 payment aggregator rules leave settlement timing to the merchant agreement, if timelines are disclosed | [AZB & Partners summary](https://www.azbpartners.com/bank/rbi-issues-consolidated-reserve-bank-of-india-regulation-of-payment-aggregators-directions-2025/) | Faster settlement is permissible if contracted and disclosed |
| Third-party payouts from a payment aggregator's account are allowed only for merchants above ₹40 lakh annual turnover, and only to the payee in the customer's transaction | AZB & Partners summary | Paytm can't pay a small merchant's supplier directly from collections. Money must settle into the merchant's account, and the merchant then pays by UPI |
| The earlier 2020 guidelines let payment aggregators pre-fund with their own funds; public summaries of the 2025 rules don't say whether pre-funded early settlement counts as lending | [VJM Global summary](https://www.vjmglobal.com/blog/payment-aggregators-and-payment-gateways-guidelines-on-settlement-and-escrow-account-management-and-other-instructions); [MediaNama](https://www.medianama.com/2025/09/223-explained-rbi-master-direction-payment-aggregators/) | Settle only collections already received, which avoids pre-funding. Compliance must still confirm the treatment |
| UPI works with current accounts as with savings accounts, within bank and NPCI limits | [Paytm blog](https://paytm.com/blog/payments/upi/is-upi-available-for-current-accounts-everything-you-need-to-know/) | Paying from the settlement current account is feasible, bank by bank |

---

## 4. Key Customer Segments and Jobs to Be Done

### 4.1 Segment definitions (observable criteria)

| Group | Inclusion rule | Merchants | Switch: yes / maybe / no | Rows |
| --- | --- | --- | --- | --- |
| **1. High potential** | Regular Paytm collector **and** next-day or separate-account settlement **and** vendor UPI at least weekly **and** app chosen by owner or manager **and** a stated timing, transfer or staff-control friction | **16** | **7 / 9 / 0** | V07, V09, V14, V16, V20, V24, V25, V29, V32, V33, V43, V44, V45, V47, V49, V50 |
| 2. May try, unlikely to switch consistently | Paytm collector not in Group 1 or 3: next-day settlement with no friction (7), or same-day settlement with a stated friction (9, of which 7 are contradictory rows) | 16 | 4 / 8 / 4 | V02, V04, V08, V37, V38, V41, V46; V10, V11, V12, V17, V19, V21, V30, V35, V36 |
| 3. Little incremental value | No or partial Paytm collection (8); or an accountant chooses the app (2 more); or same-day settlement with no friction (8) | 18 | 1 / 4 / 13 | V13, V15, V23, V26, V31, V39, V40, V48; V18, V27; V01, V03, V05, V06, V22, V28, V34, V42 |

Group 1 is 16 of 50 merchants, or 16 of the 42 regular Paytm collectors (38%). It contains no contradictory rows, so its composition is the same in the full and clean samples. Its profile: PhonePe 11 and Google Pay 5 as the current app; 9 interested in paying from collections, 6 in staff control, 1 in urgent purchases only; medium or high cash-flow pain for 11; urgent payments at least sometimes for 11; Paytm outgoing use never or rarely for 9, sometimes for 7.

**Why the segment is behavioural, not by industry.** Group 1 spans 11 business types, and none has more than 2 merchants. Hardware, electrical and auto-parts shops together account for 5. That is a reasonable first pilot cohort, because "the customer is waiting for the part" makes the value easy to show. But the sample is too small to claim these trades are the best market. Pilot recruitment should filter by settlement profile and friction first, and by category second.

### 4.2 Jobs to be done

| Merchant situation | Job, in the merchant's terms | What they do today | What Business Pay must do |
| --- | --- | --- | --- |
| Next-day settlement, routine daily or weekly vendors | "Pay this morning's supplier from what the shop has already taken in." | Wait for settlement or use other money; pay on PhonePe or Google Pay | Make today's collections usable for the supplier payment |
| Settlement into a separate current account | "Pay the supplier without first moving money to my personal account." | Transfer, then pay from the personal app | Pay directly from the settlement account |
| Urgent stock order | "Get the part or stock dispatched now." | Pay from whatever app and money is at hand | Do the above in the fewest possible steps, starting from a QR the supplier sent on WhatsApp |
| Several people pay for the business | "Let my staff or family pay vendors, with a limit, and let me see it immediately." | Each person pays from their own phone and app; records are scattered | Shared business-payment history with per-person limits (pilot arm B) |
| Invoice-led supplier dues | "Pay against the invoice with a bank trail." | NEFT or RTGS from the bank, often via an accountant | Nothing. Out of scope |

---

## 5. Product Proposition: Paytm Business Pay

**Proposition.** "Aaj ki collection se aaj ka supplier." Pay your supplier from what your shop has already collected on Paytm, in one flow, free, without waiting for settlement or moving money between accounts. Your personal UPI stays as it is.

| Element | Choice |
| --- | --- |
| Core behaviour | Recurring vendor payments made from Paytm for Business instead of a personal UPI app |
| Core product | **Settle & Pay**, a **Pay supplier** action on the collections screen of Paytm for Business, with saved suppliers, payee name check, and scanning a supplier QR received on WhatsApp |
| How it works | Two legs, one experience. Leg 1: Paytm settles the needed amount of collections it has already received into the merchant's own account; no UPI PIN is needed for this. Leg 2: the merchant pays the supplier by UPI from that account, with one UPI PIN. This structure follows RBI's payout rules (Section 3.5) |
| Primary differentiator | **Settlement and supplier payment in one flow, free when the money pays a supplier.** PhonePe's Settle Now costs ₹1–3 a request, is limited to selected merchants and once an hour, and ends at settlement; the merchant must then open a second app to pay |
| Secondary benefits | Settlement account set as the default paying account, so separate-account merchants never transfer (easy to copy); prompting merchants at the moment of need about settlement they may not know exists |
| What it does not claim | Exclusive access to unsettled money. Paytm and PhonePe both already offer early settlement; the edge is integration, price and reach |
| Target | Group 1 merchants (Section 4.1) |
| Excluded from MVP | Credit, a ledger or invoice manager, rewards or cashback, and invoice-led NEFT payments |

**Why free settlement is affordable.** Settling collections Paytm has already received costs operational effort, not working capital. If a merchant's collections would otherwise settle overnight, releasing ₹10,000 one day early costs at most about ₹3 of float (about 11% a year). PhonePe charging ₹1–3 for the same service shows the cost is small; giving it free when it funds a supplier payment buys Paytm a business-payment transaction.

**Design principle.** Business Pay wins only where it removes a step. It never asks the merchant to change their personal payment app, and it never presents table-stakes features (history, saved payees, reminders) as the reason to switch.

---

## 6. Core User Journey

Illustrative merchant, modelled on dataset profile V20: an auto-parts shop settled the next day into a separate current account, currently paying suppliers through Google Pay.

| Step | Today | With Business Pay |
| --- | --- | --- |
| 1. Trigger | 11 am: a customer needs a part that isn't in stock; the supplier sends his QR on WhatsApp and wants payment before dispatch | Same |
| 2. Find the money | Yesterday's collections arrive tomorrow; the owner moves money from the current account to his personal account, or uses other money | Opens Paytm for Business, where he already checks collections: "Today ₹12,400 collected · Pay supplier" |
| 3. Identify the supplier | Scans the QR in Google Pay | Scans the WhatsApp QR image; Paytm shows the name on the supplier's account |
| 4. Choose the funding | Not applicable; if he knew about manual settlement, he would trigger it in Paytm for Business, wait for the credit, then switch to Google Pay | "Settle & Pay from today's collections · ₹12,400 available · free · into current account ••4821" |
| 5. Authorise | UPI PIN | Paytm settles ₹6,800 to his current account (no PIN needed); he enters one UPI PIN for the supplier payment. The payment step waits until the settlement credit is confirmed |
| 6. Confirmation | Supplier sees a UPI credit | Supplier sees an ordinary UPI credit; the owner gets a payment reference and can share a receipt on WhatsApp |
| 7. Settlement | Normal settlement next day | Settlement notice shows "₹38,900 collected · ₹6,800 paid to suppliers · ₹32,100 settled" |
| 8. Habit loop | None | Next morning: "₹X from yesterday's collections is available for supplier payments"; weekly business-payment summary with a download for the accountant |

Amounts, names and account numbers are illustrative.

---

## 7. Competitive Differentiation

| Capability | Differentiated? | Who could copy it, and how fast |
| --- | --- | --- |
| Early settlement on its own | No | Already offered: manual instant settlement in Paytm for Business; PhonePe Settle Now at ₹1–3 a request for selected merchants |
| Settlement and supplier payment in one flow, free when it funds a supplier | **Yes, today** | PhonePe could build it for its own merchants within months, since it already has Settle Now and a payer app. It can't offer it to merchants whose collections Paytm handles. Banks can't see Paytm's unsettled collections |
| Paying from the settlement current account without a transfer | No | Any UPI app, as soon as the merchant links that current account |
| Saved suppliers, name check, WhatsApp QR scanning, history | No | Already available or trivial in every major app |
| Business-payment record and download | No | Billing and accounting software (Petpooja, Marg, Tally, Vyapar) does this better; they are channels, not payment competitors |
| Staff access with limits and owner visibility | Partly | UPI's delegated-payment feature is open to every app, with low limits; bank business apps offer approval workflows |

**Where Paytm's right to win is real.** It sits in the collections relationship: for its own merchants, only Paytm can turn unsettled collections into a supplier payment. It also has a head start in doing this as one free flow. **Where it is not.** Early settlement alone, saved payees, history and paying from a current account are table stakes or copyable. PhonePe is closer to copying the full flow than our earlier draft assumed, because it already runs Settle Now. When it responds, it can do so only for merchants whose collections it handles. The contest then becomes one over who handles the merchant's collections, which is Paytm's core business. This is a head start of months, not a permanent moat, so the pilot should start as soon as compliance clears the flow.

The main app-level alternatives are PhonePe (29 merchants) and Google Pay (15). Accounting and billing tools are not payment competitors; they are potential distribution partners later.

---

## 8. Growth Strategy Across the Challenge Pillars

Five interventions, prioritised. The first three are required for the pilot.

| # | Pillar | Target segment | Friction addressed | Mechanism | Acquisition or activation channel | Expected behaviour change | Primary metric | Key dependency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Product Strategy | Group 1 | Waiting for settlement; moving money between accounts; switching apps to pay | Settle & Pay on the collections screen: settlement into the merchant's own account, then supplier payment by UPI, free when it funds a supplier. Phase 0 surfaces existing manual settlement and hands off to Paytm UPI with the payee prefilled | In-app, on the screen merchants already open | First vendor payment made on Paytm instead of PhonePe or Google Pay | Activation: first Settle & Pay payment within 30 days of exposure | Compliance sign-off on free settlement and on settling only collections already received; payer flow in Paytm for Business (Section 12) |
| 2 | Distribution & Channels | Group 1 merchants identified from Paytm settlement data | Not knowing the feature exists | Soundbox field force visits a list built from settlement profile; the first payment is made together during the visit | Field visit plus in-app prompt | Exposure turns into a first payment | Cost per repeat merchant; exposure-to-activation rate | Settlement-data extraction; field incentives tied to repeat use, not sign-ups |
| 3 | Habit & Engagement | Activated merchants | Defaulting back to the old app | Morning prompt when yesterday's collections are available; saved suppliers and one-tap repeat; WhatsApp QR import | Push notification and the settlement notice | Routine vendor payments repeat on Paytm | Repeat rate: 2+ payments in each of months 2 and 3 | Notification permission; reliable QR parsing |
| 4 | Branding & Communication | Groups 1 and 2, including the 9 same-day-recorded merchants who still report waiting for settlement | "Same steps hain toh app kyun badlu?"; not knowing settlement can be early | Message the removed step and the price, in Hinglish: "Aaj ki collection se aaj ka supplier, bina charge" and "Personal UPI wahi rahega"; contrast with paid early settlement elsewhere without naming competitors | In-app, Soundbox field force, WhatsApp | Merchants learn they don't have to wait, and connect that to paying on Paytm | Awareness of early settlement before and after; activation lift between message variants (A/B) | Brand and legal approval of comparative claims |
| 5 | Strategic Partnerships | Separate-account merchants; later all segments | Current account not set up for payments; bills kept in other software | Settlement-bank partnerships so the current account works as the paying account; later, a Pay with Paytm action inside billing software | Bank onboarding; software integrations | Paying from the business account becomes the default | Share of separate-account merchants with the settlement account set as payer | Bank support for UPI on current accounts; partner agreements |

**Pilot arm B (multi-payer shops).** For Group 1 merchants with more than one payer, add staff access: staff request or make payments within owner-set limits, and the owner sees each payment immediately. Measure whether it lifts activation and repeat use over arm A. Build it more broadly only if it does.

---

## 9. MVP Scope and Feature Prioritisation

**Phase 0 (weeks, not months): test demand with existing capability.** On the collections screen, add "Pay a supplier from today's collections". It triggers the app's existing manual settlement, then hands off to the Paytm UPI app with the supplier prefilled. It is two apps and no new money movement, but it measures whether merchants act on the prompt and how many didn't know they could settle early.

| Priority | Capability | Why it is in or out |
| --- | --- | --- |
| Phase 0 | Settlement prompt at the moment of payment, plus hand-off to Paytm UPI | Cheapest test of demand and awareness; uses features Paytm already has |
| Must have | Pay supplier inside Paytm for Business (new payer flow) | Removes the app switch; the vehicle for every other benefit |
| Must have | Settle & Pay: settle already-received collections into the merchant's account and pay the supplier, free when it funds a supplier payment | The primary differentiator; the free price is what PhonePe's paid Settle Now doesn't match |
| Must have | Settlement current account as default paying account | Removes the transfer step for separate-account merchants |
| Must have | Payee name check, saved suppliers, WhatsApp QR import | Table stakes; 6 merchants cite "supplier sends QR on WhatsApp" as why they use their current app |
| Must have | Business-payment history, separate from personal UPI, with a weekly download | Low cost; supports the "separate place for business payments" positioning |
| Pilot arm only | Staff access with limits and owner visibility | 9 merchants value it, all in multi-payer shops; test before building fully |
| Later | Pay with Paytm inside billing software | Distribution after repeat use is proven |
| Out | Short-term credit | No high credit need; no rejection for lack of credit |
| Out | Ledger, invoice management | Billing software owns this; not a reason to switch |
| Out | Rewards or cashback | 1 merchant cites offers as a reason for their app; not economical as a switching driver |
| Out | Invoice-led NEFT supplier payments | Supplier needs a bank trail; UPI adds friction |

---

## 10. Market Sizing and Incremental Growth Model

### 10.1 Corrections to the previous model

The previous model multiplied 1.57 crore merchants by 46% (next-day or separate settlement) by 30% (stated "yes" rate), giving 21.7 lakh adopters. It then applied ₹40,000 of monthly business UPI and a 40% shift, giving about ₹41,600 crore a year. The arithmetic is correct, but the model has six flaws:

1. **Wrong denominator.** 46% was 23 of all 50 merchants; the settlement share should be measured among Paytm collectors (23 of 42, or 55%).
2. **No vendor-UPI filter.** It assumed every device merchant pays vendors by UPI.
3. **No friction filter.** It included merchants with no stated friction, who never say yes.
4. **Stated intent treated as adoption.** A "yes" in a VOC is not a transacting merchant.
5. **No exposure or repeat stage.** It went from the population straight to adoption.
6. **No incrementality.** It counted merchants already occasionally paying through Paytm as new.

### 10.2 Revised funnel

Every rate below is an assumption or a dataset proxy, and must be replaced with Paytm data or pilot results. Figures are a run-rate at the end of year one, not cumulative totals.

| Stage | Driver | Cautious | Base | Upside | Source |
| --- | --- | --- | --- | --- | --- |
| Addressable | Paytm device merchants | 1.57 crore | 1.57 crore | 1.57 crore | Paytm Q1 FY27 |
| | Share paying vendors by UPI at least weekly | 35% | 50% | 60% | Assumption (dataset sample is pre-selected for UPI payers) |
| | Share settled next day or into a separate account | 54.8% | 54.8% | 54.8% | Dataset proxy: 23 of 42 collectors; replace with Paytm settlement data |
| | Share with a stated friction | 69.6% | 69.6% | 69.6% | Dataset proxy: 16 of 23 |
| **Eligible** | | **20.9 lakh** | **29.9 lakh** | **35.9 lakh** | Result |
| Exposed in year one | Share reached by field force and in-app | 25% | 40% | 55% | Assumption |
| **Exposed** | | **5.2 lakh** | **12.0 lakh** | **19.7 lakh** | Result |
| First-time activation | Assumed conversion of stated "yes" (7 of 16) and "maybe" (9 of 16) | yes 25%, maybe 5% → 13.8% | yes 40%, maybe 10% → 23.1% | yes 60%, maybe 20% → 37.5% | Assumption applied to dataset propensity |
| **Activated** | | **0.72 lakh** | **2.77 lakh** | **7.40 lakh** | Result |
| Repeat transacting | Activated merchants with 2+ Business Pay payments in each of months 2 and 3 | 35% | 50% | 65% | Assumption |
| **Repeat merchants** | | **25,000** | **1.38 lakh** | **4.81 lakh** | Result |
| **Incremental MTU** | Repeat merchants who did not already make outgoing Paytm payments | 56% → **14,000** | 56% → **78,000** | 56% → **2.71 lakh** | Dataset proxy: 9 of 16 Group 1 merchants never or rarely pay through Paytm |
| Vendor UPI payments per merchant per month | Group 1 frequency mix | 18.9 | 18.9 | 18.9 | Dataset: midpoints of 2–3, 3–5 and 4–6 a week and daily (26 a month), equally weighted |
| Share of those payments shifted to Paytm | | 25% | 40% | 60% | Assumption |
| **Incremental Paytm business payments a month** | Repeat merchants × 18.9 × share | **1.2 lakh** | **10.4 lakh** | **54.4 lakh** | Result |
| Average vendor payment | | ₹2,000 | ₹2,500 | ₹3,500 | Assumption |
| Less baseline already on Paytm | Share of shifted value merchants already paid through Paytm | 15% | 15% | 15% | Assumption |
| **Incremental business UPI GMV a month** | | **≈ ₹20 crore** | **≈ ₹222 crore** | **≈ ₹1,620 crore** | Result |
| **Annual run-rate** | × 12 | **≈ ₹240 crore** | **≈ ₹2,660 crore** | **≈ ₹19,400 crore** | Result |

Base-case GMV per repeat merchant is about ₹18,900 a month (7.5 shifted payments of ₹2,500), comparable with the previous model's ₹16,000 (₹40,000 × 40%). The difference between the models is almost entirely the number of merchants, which is now built from eligibility, exposure, activation and repeat stages instead of stated intent.

### 10.3 What moves the answer most

| Driver | Base value | Effect if it halves |
| --- | --- | --- |
| Share settled next day or into a separate account | 54.8% (dataset proxy) | All outputs halve. This is the first number to confirm from Paytm data |
| Activation conversion | 23.1% | All outputs halve |
| Repeat rate | 50% | All outputs halve |
| Share of payments shifted | 40% | GMV and frequency halve; MTU unchanged |
| Share of eligible merchants already using manual instant settlement | Not modelled (assumed low) | If high, the timing friction is already solved for them; the remaining value is one flow instead of two apps, and activation should be lower |

The model is multiplicative, so the range between cautious and upside is wide (about 80 times on GMV). The pilot exists to replace the four drivers above with measured values.

### 10.4 Definitions

- **Incremental MTU:** a merchant who makes at least one Business Pay payment in a month, and made no outgoing Paytm business payment in the 60-day pre-pilot baseline, net of the rate at which control-group merchants become new Paytm business payers in the same period. A merchant who was already active and moves payments between Paytm products is not incremental.
- **Repeat transacting merchant:** 2 or more Business Pay payments in each of months 2 and 3 after activation.
- **Incremental business UPI GMV:** treatment-group outgoing business UPI value through Paytm, minus the control group's, per eligible merchant, multiplied by the eligible base.
- **Share shifted:** for consented merchants, Paytm's share of total outgoing business UPI value, measured from bank statements (via Account Aggregator consent) or a payment log, in treatment against control.

---

## 11. Pilot Design, Success Metrics, and Measurement

**Design.**

- **Eligible list:** built from Paytm settlement data in two cities with dense Soundbox coverage. Merchants settled next day or into a separate account, with an outgoing UPI pattern consistent with weekly vendor payments where visible.
- **Randomisation:** at field-agent territory level, to avoid contamination between neighbouring shops. Indicatively, about 3,000 merchants in treatment and 3,000 in control.
- **Arms:** arm A, Business Pay MVP, for all treatment merchants. Arm B adds staff access for treatment merchants with more than one payer.
- **Duration:** 12 weeks, after an 8-week baseline from Paytm's own transaction data.
- **Share-shift panel:** about 300 consented merchants per group, measured from bank statements or a payment log.
- **Analysis:** intention-to-treat difference-in-differences against the concurrent control group. This removes seasonality and organic growth. Results are also reported by settlement profile and by single-payer versus multi-payer shops.

**Metrics and targets.** Targets from the previous version are reviewed below; most become hypotheses to be tested, not commitments.

| Metric | Previous target | Revised target | Status | Reason |
| --- | --- | --- | --- | --- |
| Activation: exposed eligible merchants making a first Business Pay payment within 30 days | 30% | 15–25% | Hypothesis | 30% equalled the stated "yes" rate; stated intent overstates adoption |
| Repeat: activated merchants with 2+ payments in each of months 2 and 3 | 60% active in month 3 | 50% | Hypothesis | Reframed as repeat use, which defines MTU contribution |
| Frequency: Business Pay payments per repeat merchant per month | 3+ a week | 6–8 a month | Hypothesis | Base case is 7.5 shifted payments a month |
| Value: Business Pay GMV per repeat merchant per month | ₹40,000 | About ₹19,000 | Hypothesis | Base case 7.5 × ₹2,500 |
| Habit guard: share of Business Pay payments made when no timing or transfer gap existed | 30%+ | 30%+ | Keep (hypothesis) | Shows whether Paytm becomes the default or only a stopgap |
| Behaviour change: Paytm share of business UPI, treatment vs control | +25 points | +4 to +6 points across all treatment merchants (intention to treat); +30 points or more among repeat merchants | Hypothesis | 23% activation × 50% repeat × 40% shift ≈ 5 points across the whole treatment group |
| Incremental MTU per 1,000 exposed eligible merchants | Not set | About 65 (base) | Hypothesis | 23.1% × 50% × 56% |
| Payments to the wrong account; support complaints per 1,000 payments | Near zero | Near zero | **Commitment** | Trust and safety threshold, not a forecast |
| Arm B lift in repeat rate over arm A, multi-payer shops | Not set | Any significant lift | Decision rule | Determines whether staff access is built fully |
| Awareness of early settlement among eligible merchants, before and after exposure | Not set | Baseline measured; at least double after exposure | Hypothesis | Public sources show the feature exists; the dataset's settlement complaints suggest many merchants don't know |
| Phase 0 prompt-to-payment conversion | Not set | Measured, not targeted | Diagnostic | Decides whether the full Settle & Pay build is worth funding |

**Decision gates after 12 weeks.** Scale if activation is at least 15%, repeat rate at least 40%, and the intention-to-treat share lift is significant. Revise positioning if activation is fine but the habit guard is under 15%, which means the product is only being used for timing gaps. Stop if activation is under 8%.

---

## 12. Risks, Dependencies, and Feasibility Checks

**Product mechanics that need confirmation before the pilot:**

| Mechanic | What public sources indicate | Still to confirm | Owner |
| --- | --- | --- | --- |
| Releasing today's collections early | Feasible: Paytm for Business already offers manual instant settlement; PhonePe offers Settle Now; RBI's 2025 rules let the merchant agreement set settlement timing | Speed of the credit to each partner bank; daily limits; whether merchant agreements need updating | Settlement, treasury, compliance |
| Paying the supplier directly from collections | Not allowed for most target merchants: third-party payouts need ₹40 lakh+ annual turnover and must go to the customer-facing payee | None; the design avoids it by settling into the merchant's own account first | Compliance (confirm reading) |
| Early release versus credit | Settling only collections already received avoids pre-funding; public summaries of the 2025 rules don't classify pre-funded early settlement | Formal compliance view; whether any pre-funding is ever needed | Compliance, legal |
| One authorisation | Settlement needs no UPI PIN; only the supplier payment does. So one PIN is achievable if the settlement credit lands first | Settlement-to-credit time by bank; the user experience while waiting | Payments engineering |
| Paying from Paytm for Business | Current accounts work with UPI like savings accounts; the app's listing shows no payer feature today | Build the payer flow in Paytm for Business, or keep the hand-off to Paytm UPI | Engineering, partner banks |
| Free early settlement when it funds a supplier | Competitor charges ₹1–3 a request, which suggests a low unit cost | Whether conditional free pricing is acceptable, and its cost at scale | Compliance, pricing |
| Staff access (arm B) | Not researched publicly | Whether UPI's delegated-payment limits fit vendor payments, or an approval workflow is needed | Product, NPCI rules |
| Segment size | Not public; Paytm's own help pages give different timings | Share of merchants settled next day or into a separate account; share already using manual settlement | Data team |

**Business risks:**

| Risk | Signal | Mitigation |
| --- | --- | --- |
| Most Paytm merchants already settle same day into the account they pay from | Settlement data shows a small next-day and separate-account share | Shrink the target; lead with staff access for multi-payer shops |
| Habit wins even with the friction removed | Low habit-guard share; activation without repeat | Strengthen the morning prompt; restrict targeting to Group 1 |
| PhonePe responds | Adds a supplier payment to Settle Now, or makes it free, for its own merchants | Expected within months; move first with Paytm's merchants and lock in the habit before it does |
| The friction is already solved | Many eligible merchants already use manual instant settlement | Phase 0 measures this first; if so, lead with one flow instead of two apps, and with staff access |
| Early-release cost | Float cost at about 11% a year is about ₹3 per ₹10,000 per day, and lower when only already-received collections are settled | Justify against measured retention and GMV lift |
| Trust in Paytm after 2024 | Merchants hesitate to route business money through Paytm | Show the bank account the money comes from on every payment screen |
| Dataset limitations | Synthetic data; 11 contradictory rows; repeated quotes | All rates in Section 10 are proxies until replaced by pilot and Paytm data |

---

## 13. Key Hypotheses Requiring Real-Merchant Validation

| Priority | Hypothesis | Validation method | Confirmed if |
| --- | --- | --- | --- |
| P0 | A meaningful share of Paytm merchants settle next day or into a separate account | Paytm settlement data | 25% or more of device merchants |
| P0 | These merchants pay vendors by UPI on another app at least weekly | Merchant interviews with phone payment history; Paytm outflow data where visible | Most observed vendor payments are on another app |
| P0 | Merchants who report waiting for settlement don't know, or don't use, manual instant settlement | Paytm usage data on manual settlement; interview question: "Have you ever settled your Paytm collections instantly?" | Most eligible merchants have never used it |
| P0 | They feel the timing or transfer friction at the moment of paying | Interviews: last time a supplier had to be paid before money was usable | Recalled at least monthly by 40% or more |
| P0 | Paying from collections would move their next vendor payments | Concept test after reviewing their last five payments | 40% or more choose it for at least one of the five |
| P0 | They'd keep using Business Pay when no gap exists | Pilot habit-guard metric | 30% or more of payments |
| P1 | Multi-payer shops value staff access enough to adopt | Pilot arm B | Significant lift over arm A |
| P1 | Merchants trust Paytm with business payments | Interviews; pilot drop-off at the payment screen | No trust-driven drop-off pattern |
| P2 | Hardware, electrical and auto-parts shops respond best | Pilot results by category | Higher activation than average |

---

## 14. Final Recommendation and 30-Second Pitch

**Recommendation: proceed in three steps.**

1. **Data check (weeks 0–2).** Pull from Paytm's own data the share of merchants settled next day or into a separate account, and the share already using manual instant settlement.
2. **Phase 0 (weeks 2–8).** Release the settlement prompt with a hand-off to Paytm UPI to eligible merchants. It needs almost no new build, and it measures awareness and demand.
3. **Randomised pilot (from about month 3).** Run the full Settle & Pay flow, once compliance confirms settling already-received collections free when they fund a supplier payment. The pilot targets Group 1 merchants, tests staff access for multi-payer shops in a second arm, and measures incremental MTU, repeat use, GMV and share shift against a concurrent control.

Credit, ledgers and rewards stay out until the pilot shows a need. Speed matters, because PhonePe already has the parts to copy the flow for its own merchants.

**30-second pitch:**

Merchants collect on Paytm, then pay their suppliers on PhonePe or Google Pay, often several times a week. They aren't loyal to those apps; Paytm has simply never given them a reason to change. "Same steps hain toh app kyun badlu?" The reason we can give is real for one group: merchants whose Paytm money arrives tomorrow, or into a separate account, while their supplier wants paying now. Others charge to settle early, then make you open another app to pay. Paytm Business Pay does both in one flow, free when the money goes to a supplier: settle today's Paytm collections into your own account and pay the supplier from it, without a loan and without touching your personal UPI. We'll prove it fast, starting with a prompt built on features Paytm already has, then a controlled pilot that measures new transacting merchants and real share shift, not sign-ups.
