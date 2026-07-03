# Validating the auxin→growth model against measured spaceflight root morphometrics

**Question.** Do the model's root-shape predictions (Figs 3–5) match what spaceflight
*Arabidopsis* roots actually do?

**Short answer.** The model's **central** prediction — microgravity collapses the *directional*
auxin asymmetry (symmetric QC maximum, no lower-side bias) — is **consistent** with the measured
phenotype (persistent, genotype-dependent **skewing** and **increased directional variance** in
flight). The model's **secondary** "short, fat, hypoxic root" prediction (Figs 4–5) is **not
corroborated** by the available morphometrics: measured primary-root **length** is largely
unchanged flight-vs-ground, and root **diameter/width was never measured**, so the modelled
aspect-ratio change (L/W ≈ 99 → 41) is currently **untestable** and should be treated as an
illustrative hypothesis, not a validated result.

---

## What morphometric data actually exist

- **CARA / OSD-120 is transcriptome-only.** All 851 files in OSDR OSD-120 are RNA-seq (raw/
  trimmed FASTQ, trimming reports, the GeneLab DE table). There is **no imaging or morphometric
  measurement table** in the study — so there is nothing *within* CARA to regress the model against.
- The closest quantitative spaceflight root morphometrics from the same group (Paul & Ferl, U.
  Florida) come from the sibling flight **APEX-03-2 / TAGES-ISA**
  ([Califar et al. 2020, *Front. Plant Sci.* 11:239](https://doi.org/10.3389/fpls.2020.00239)),
  which shares **Col-0 and WS** with CARA (and adds the skewing mutants *spr1*, *sku5*; it does
  **not** include CARA's *phyD*). We use it as the best available external morphometric reference,
  clearly attributed — it is **not** "CARA's own" morphometrics.

## Measured numbers (Califar et al. 2020, APEX-03-2, FLT vs GC)

| Trait | Genotype | Result (flight vs ground) |
|---|---|---|
| Primary root length, 4 d & 8 d | **Col-0** | **No significant difference** (8 d FLT trend shorter, *p* = 0.0152, above the *p* < 0.0125 threshold) |
| Primary root length | **spr1** | No significant difference (equivalent) |
| Primary root length, 8 d | **WS** | **Significantly shorter in flight** (*p* = 0.000209) |
| Primary root length | **sku5** | No significant difference |
| Skewing / directional angle | **Col-0** | Slight leftward skew **with increased variance** in flight |
| Skewing / directional angle | **spr1** | **Enhanced leftward skew in flight** (*p* = 0.00385) |
| Directional variance | all genotypes | **Greater variance in spaceflight** samples |
| Root **diameter / width** | all | **Not measured** |
| Germination | **sku5** | Reduced in flight (77 % GC → 48 % FLT, *p* = 0.0018) |

Key quote: *"There were no statistically significant differences in the primary root length
between GC and FLT in either Col-0 or spr1 4 d or 8 d plants."*

## Model prediction vs measurement — scorecard

| Model prediction | Source | Measured | Verdict |
|---|---|---|---|
| µG → **symmetric** tip auxin, **no lateral direction** (loss of a consistent gravitropic setpoint) | Fig 1, manuscript §2.1 | Skewing persists without gravity; **genotype-dependent**; **↑ directional variance** in flight | **Consistent** ✅ |
| Suppressed columella PIN3/7 → auxin **confined toward QC** | Figs 2–3 (real OSD-120 FC) | PIN3/7 suppression is real (dark Col-0); no imaging to see the auxin field directly | **Plausible, indirect** 🟡 |
| Spaceflight root **shorter** (hypoxic) | Fig 5 length curve | Col-0/spr1 **n.s.**; WS 8 d shorter only | **Weak / mostly not supported** 🔴 |
| Spaceflight root **fatter** (radial swelling), L/W ≈ 99 → 41 | Figs 4–5 | Diameter **never measured** | **Untestable** ⚪ |
| Gravity dose–response 0/10/21/36/41 % (µG→2 g) | Fig 1b | Only 1 g vs µG flown; partial-g not tested | **Untested prediction** ⚪ |

## Interpretation

1. **The core result validates.** The measured spaceflight phenotype is *directional*: roots
   still grow and skew, but **lose a consistent direction** and become **more variable** — exactly
   what "a symmetric auxin maximum with no lateral bias" predicts. This is the strongest,
   data-supported claim and should lead the narrative.
2. **The short-fat story is a hypothesis, not a CARA result.** The dramatic shortening + radial
   swelling in Figs 4–5 comes from general spaceflight/hypoxia biology, **not** from CARA/APEX
   measurements (which show near-normal length and no width data). The absolute L/W numbers are set
   by an illustrative anisotropy parameter (`alpha`) and a display width-scale, so they are **not
   calibrated** to any measurement.
3. **What would actually test it.** Root **diameter/width** and length from the CARA plate images
   (or a dedicated RSML/RootNav re-measure), and partial-g centrifuge/RPM runs for the Fig 1b
   dose–response.

## Actions taken from this validation
- Manuscript §2.4 reframed: short-fat is a **prediction from hypoxia biology**, explicitly flagged
  as **not corroborated by CARA/APEX morphometrics**; the skewing/variance match added as the
  validated result.
- Fig 5 caption + `hypoxic-root-modelling.md`: L/W numbers labelled **illustrative, uncalibrated**.
- README progress updated with this validation and its honest verdict.
