# Chapter 65 — Adolescent and Transitional Urology
*(Session 2; new source pp. 1352–1364, of which pp. 1354–1364 are new. The chapter text ends on p. 1364, followed by Selected References.)*

## What this session did
- **Reconciled the overlap (pp. 1352–1353).** Session 1 had already covered these pages in full. I checked the text against the notes and found nothing missing, so the overlap was **not duplicated**. The only open item from Session 1 was the Barriers to Transition table: its rows **3 (Institutional)** and **4 (Health system)** have now been filled in from p. 1354, and the concept line under the table has been updated to match.
- **Added the rest of the chapter (pp. 1354–1364) to `build/notes.html`,** following the source's own heading order:
  - The Practicalities (continued): Geographic Considerations; Developing a Plan / Billing; Measuring Success in Transition; Key Points.
  - Prior Male Urethral Reconstruction: surveillance, recurrent chordee, fertility (comparison table: hypospadias vs BEEC), psychosocial; Fig. 65.4.
  - Prior Female Genital Reconstruction: surveillance, sexual function, fertility and pregnancy, delivery-route table, pelvic organ prolapse; Key Points; Fig. 65.5.
  - Bladder Reconstruction and Urinary Diversion: augmentation, continent and incontinent diversion (three-category table), bladder neck reconstruction; Key Points.
  - Surveillance: SB renal surveillance (SBA guideline vs the authors' additions), creatinine vs cystatin C, CKD definition, a nephrology-referral criteria table, imaging including the "tempered" MAG3.
  - UTIs; Long-term Risks (malignancy by segment, stone management by size); Key Points.
  - Channels and Stomas (Fig. 65.6), metabolic, abdominal wall, change in reservoir function; Key Points.
  - Progression to ESRD: psychosocial, Fig. 65.7 (all nine challenges tabulated), polyuria, native nephrectomy (Fig. 65.8), peritoneal dialysis, transplant (vascular and positional planning table).
- **Trimmed the Session-1 material by about 180 words** to fit the whole-chapter budget:
  - the programmes table became a single bullet;
  - the list of failure risks was condensed;
  - three redundant bullets were removed.
- **Extended `build/cheatsheet.html` to cover the whole chapter:**
  - the "If you read nothing else" box now has 12 items;
  - six new sections;
  - seven new classic traps.
- **Rebuilt both PDFs** with the unchanged `render.py` (WeasyPrint, Carlito only, pure black). Copies are in `all-chapters/PDFs/`.

## Budgets (checked)
| Document | Words (HTML body) | Pages | Budget |
|---|---|---|---|
| Chapter Notes | 5,945 | 17 | ≤ 360 per source page: 17 pp → ≤ 6,120 (16.5 pp of text → ≤ 5,940). Actual ≈ 350 per page |
| Numbers, Gold Standards and Traps | 1,292 | 2 | 1,200–1,600 words, 2 sides |

I rendered pages 1–2 of the cheatsheet and pages 10, 12, 14 and 17 of the notes to PNG and inspected them. Tables, boxes, running heads and page numbering all render correctly. The fonts embedded are Carlito, Carlito-Bold, Carlito-Italic and Carlito-Bold-Italic only.

## Character substitution key (additions to Session 1)
- `/H11011` = "~"; `/H11005` = "="; `/H11021` = "<"; `/H11022` = ">"; `/H11349` = "≤"; `/H11350` = "≥"; `/H9252` = "β"; `/H11001` = "+". All were confirmed against the rendered page images.
- The stray "z" before "(including pain and device leakage)" on p. 1361 is a typesetting artefact.

## Source flags (errors, inconsistencies, ambiguities)
1. **"VATERL" (heading, p. 1354) and "VACTRL" (p. 1364)** are inconsistent misspellings of **VACTERL**. The notes use VACTERL.
2. **Conduit stomal complication rate, cited to the same source (Wood 2004), is given two ways:** "up to 34.4 %" (p. 1358) and "18–35 %" (p. 1361). The two figures are compatible, and both are shown.
3. **"Recurrent pyelonephrosis" (p. 1361)** is not a standard term. It probably means **pyonephrosis** (or recurrent pyelonephritis) from conduit retention. The notes say only "retention → loopogram", which avoids the term.
4. **"eGFR ≤ 30 mL/min/1.73 m² (CKD stage 4–5)" (p. 1359):** stage 4 is 15–29, so the strict threshold is < 30. This is a trivial boundary issue; the source is kept.
5. **NKF CKD definition (p. 1359):** the sentence attaches "3 or more months" only to kidney damage. The NKF requires **≥ 3 months for either criterion**. The notes are written that way.
6. **"Follow-up is recommended annually or biannually" (BEEC, p. 1355; Key Points, p. 1359):** "biannually" is ambiguous (twice a year or every two years). It is taught as "every 1–2 years".
7. **Higher decisional regret with distal (vs proximal) hypospadias (p. 1356)** is counter-intuitive but is what the text states. It is taught as stated, and there is a trap on it.
8. **"More than doubles" (hypospadias redo complication rates, p. 1354):** 10.1–37.5 % → 27.5–63.6 % is less than double at the upper end. The notes give the ranges only.
9. **Name and citation misspellings:** "Akslund" in the text vs "Asklund" in the citation (p. 1355); "Highuchi et al., 2011" for Higuchi (p. 1360); "Diaz-Gonzelez de Ferris" in the text vs "Diaz-Gonzalez" in the Fig. 65.7 legend (p. 1362).
10. **Rynja:** the text cites "Rynja et al., 2011", but the Selected References list Rynja **2009** (J Urol 182:1736). This does not affect content.
11. **"Small stones (< 1.5 cm) … via the Mitrofanoff procedure" (p. 1360):** this means via the Mitrofanoff **channel**. Rendered that way.
12. **"The AHRQ report … acknowledge" (p. 1354):** a grammatical slip, with no effect on content.
13. **Fig. 65.6 legend:** the channel is "MACE or Mitrofanoff". MACE is expanded from p. 1363 (Malone antegrade continence enema).

## Figures
- **Fig. 65.4** (BEEC phallic insufficiency with torsion; dorsal chordee), **Fig. 65.5** (26-year-old, solitary kidney, remnant ureter into the vaginal apex), **Fig. 65.6** (L-stent) and **Fig. 65.8** (native emphysematous pyelitis and reflux after transplant; nephroureterectomy) are clinical images. Each is summarised as a one-line teaching point.
- **Fig. 65.7** is a text box. It was read from the page image and all nine items are tabulated, with the source attribution kept.

## Citations removed (non-landmark, per standing rule)
Carnduff and Place; Novara; Claeys; Loftus; Peycelon and Misseri; Gray; Szymanski; Hensle; Senkul; Rynja; Thiry; Andersson; Steven; Rubenwolf; Myers; Abosena; Babu and Chandrasekharam; Castagnetti; Sinatti; Gul; Nordenvall; George; Berg; Kumar; Asklund; Ansari; Reynaud; Tack; Diseth; Holmdahl; Versteegh; Fernando; Leclair; Park; Canalichio; Couchman; Deans; Giron; Breech; Reppucci; Dy; Vilanova-Sanchez; Attini; Stec; Mathews; Nakhal; Werneburg; Kaufman; Blackburn; McDougal; Nethercliffe; Vasquez; Biers; Husmann; Couillard; O'Connor; Wood; Gillern and Bleier; Thiruchelvam; Maruf; Ahmad and Granitsiotis; Chevalier; Ardissino; Caione and Nappo; Ouyang; Chu; Dangle; Morrow; Vassalotti; Higuchi; Floyd and Stubington; Perez-Lanzac de Lorca; Harambat; Heikkila; Kogon; Medway; Parkhouse; Holmdahl; Peters; Koff; De Gennaro; Penna and Elder; Muller; Bouty; Dolan; Grunberg; Figueiredo; Tran.

**Kept by body name:** AHRQ, the Spina Bifida Association (SBA) guidelines (4th ed.) and the National Kidney Foundation (NKF). Diaz-Gonzalez de Ferris is kept as the Fig. 65.7 attribution.

**Study figures omitted as low-yield:**
- the 2011 ISHID survey percentages (collapsed to "each roughly a quarter");
- the Australian "21 % difference" in paternity (the HR 0.79 is kept);
- the BNR denominator (91/142).

## Coverage
**The whole chapter, pp. 1348–1364, is now covered.** Nothing in the text is left uncovered. The Selected References on p. 1364 are not summarised, per the standing rule.
