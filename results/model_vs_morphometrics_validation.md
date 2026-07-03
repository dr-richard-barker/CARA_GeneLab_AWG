# Validating the model against measured spaceflight root morphometrics

**Question.** Do the model's root predictions match what spaceflight *Arabidopsis* roots actually do?

**Answer.** The model's **central** prediction is **robustly confirmed**; its secondary
**short-fat** prediction is **not** — the real, calibration-robust spaceflight phenotype is a
**loss of directional organisation** (root-angle dispersion ↑), not a change in root shape.

---

## Why this uses CARA's own images, not another mission

There is **no matched external control** for a spaceflight experiment, and other flights are **not
fair comparisons**: e.g. APEX-03-2/TAGES-ISA used **different flight hardware** (higher light,
somewhat better airflow) than CARA, so a different root phenotype is expected on physical grounds
alone. The published CARA root-length analysis also **pools light and dark**, which hides the
light-dependence that is the whole point of CARA — which is exactly why the images were
**re-measured** here with light and dark separated. So we validate against **the CARA/ABRS/OSD-121
images themselves**, re-analysed in the sibling repo
[`image-analysis-software-and-R-codes`](https://github.com/dr-richard-barker/image-analysis-software-and-R-codes)
(RootNav RSML physiology, OSD-121 seedling morphometrics, ABRS time-lapse angles).

## Result 1 — directional organisation is lost in flight (model's core prediction) ✅

The model says microgravity collapses the *directional* auxin asymmetry: the QC auxin maximum
stays symmetric with **no lateral bias**, so roots keep growing but **lose a consistent direction**.
Three independent readouts confirm this:

| Dataset | Readout | Flight | Ground | Stats |
|---|---|--:|--:|---|
| **OSD-121** (13 flight / 13 ground dishes) | root-angle dispersion (°) | **51.2** | **45.3** | **p < 1e-4** (Welch *t* = 7.6) |
| **ABRS** time-lapse (1 plate/condition, 11 d) | angle dispersion (°) | 59.1 | 57.7 | descriptive (direction only) |
| **ABRS** | mean \|angle from vertical\| (°) | 51.7 | 48.7 | descriptive |
| **18-way skew** (ground RSML) | remove organising vector (agar→phytogel) → dispersed, non-handed growth | — | — | agar skew 7.2° vs 5.7°, p=0.003; handedness p<1e-4 |

The 18-way-skew assay is the mechanistic bridge: removing the organising vector — **either** the
agar-surface interaction **or** gravity — moves roots along the same *organised/handed ↔
dispersed/wandering* axis. Microgravity is the gravity-removal case, and OSD-121 quantifies it
(dispersion ↑, p<1e-4). **This is the model's headline result and it is validated.**

## Result 2 — the "short-fat" prediction is not supported 🔴

CARA roots re-measured by RootNav (RSML), flight vs ground **within each genotype × light** — the
light/dark split the published paper lacked (`RACARA_root_physio.ipynb`):

| Genotype × light | Length FLT→GR | Δlen | **Diameter** FLT→GR | Δdiam |
|---|---|--:|---|--:|
| WS · light | 3.367 → 3.508 | −4 % | 0.048 → 0.053 | **thinner** |
| WS · dark | 3.380 → 3.780 | −11 % | 0.047 → 0.049 | thinner |
| PhyD · light | 3.176 → 3.213 | −1 % | 0.071 → 0.055 | **fatter** |
| PhyD · dark | 3.080 → 3.441 | −10 % | 0.048 → 0.059 | thinner |
| Col · light | 2.361 → 3.063 | −23 % | 0.051 → 0.050 | ~equal |
| Col · dark | 3.304 → 3.605 | −8 % | 0.047 → 0.055 | thinner |

- **Length:** flight roots are **modestly shorter in all six conditions** (−1 % to −23 %). So the
  "shorter" half is a **consistent trend** (means only here; formal ANOVA in the CARA `methods/`).
- **Diameter:** flight roots are **thinner in 4/6, fatter in only 1** (PhyD-light), ~equal in 1.
  The **"fatter / radial swelling" prediction is not supported** — roots get *smaller*, not
  *short-and-fat*. Any aspect-ratio change is **genotype × light-dependent**, not a uniform
  short-fat shift.
- **Calibration caveat (decisive for OSD-121):** the apparent "~20 % smaller in flight" was largely
  a **magnification artifact** (flight 10.6 vs ground 11.9 px/mm); in calibrated mm² the plant-area
  difference **vanished** (404 vs 393 mm², **p = 0.30**), confirmed by the dish-diameter self-check.
  So even the "shorter" signal must be read cautiously — it is small and calibration-sensitive.

## Scorecard

| Model prediction | Verdict | Evidence |
|---|---|---|
| µG → symmetric auxin, **no lateral direction** → roots lose directional alignment | **Confirmed** ✅ | OSD-121 dispersion ↑ p<1e-4; ABRS same direction; 18-way-skew analogy |
| Suppressed columella PIN3/7 → auxin confined to QC | Plausible, indirect 🟡 | real OSD-120 FC (dark Col-0); no in-flight auxin imaging |
| Spaceflight root **shorter** | Weak / calibration-sensitive 🟠 | RootNav: −1…−23 % (all 6, means); OSD-121 area p=0.30 after calibration |
| Spaceflight root **fatter** (radial swelling; Fig 5 L/W 99→41) | **Not supported** 🔴 | RootNav diameter thinner in 4/6; fatter only PhyD-light |
| Gravity dose–response 0/10/21/36/41 % (µG→2 g) | Untested prediction ⚪ | only 1 g vs µG flown |

## Bottom line
The model earns its keep on the **directional** phenotype — microgravity removes the lateral auxin
bias and roots **disorganise** (dispersion ↑, robustly, OSD-121). The **short-fat** framing (Figs
4–5) should be treated as an **illustrative mechanism, not a validated result**: the direct
morphometry shows at most a modest, calibration-sensitive shortening and **no consistent
widening**. The strongest, most testable claim to carry into the manuscript is
**loss of directional organisation**, with the size/shape story reported honestly as unresolved and
genotype × light-dependent.

## Data sources
- RootNav physiology: `RACARA_root_physio.ipynb` (image-analysis repo).
- OSD-121 morphometrics + calibration: `docs/OSD121_MORPHOMETRIC_FINDINGS.md`, `scripts/python/seedling_morphometrics.py`.
- ABRS angles: `docs/ABRS_ANGLE_FINDINGS.md`, `scripts/python/abrs_angle_analysis.py`, `ABRS_NASA_Roots_TimeLapse/`.
- Cross-experiment synthesis: `docs/CROSS_EXPERIMENT_SYNTHESIS.md`.
- Ground skew baseline: `18_way_skew/*.rsml`, `docs/SKEW_ANALYSIS_FINDINGS.md`.
