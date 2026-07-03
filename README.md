# CARA — spaceflight root transcriptome × auxin modelling

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

Reanalysis of the **CARA** *Arabidopsis* root-tip spaceflight RNA-seq (NASA OSDR **OSD-120**),
integrated with an open, cell-based auxin-transport model (the
**[Virtual Root](https://github.com/dr-richard-barker/virtual-root)**), toward an **npj
Microgravity** manuscript and a **Zenodo** deposit.

## Goal
Turn a spaceflight gene list into a **mechanism**: use a transparent auxin model to explain
how the flight transcriptome (and gravity itself) reshapes the root-tip auxin field — and the
root growth that follows.

## The story so far
- **On Earth**, gravity is *required* for the "reverse fountain": statoliths sediment → **PIN3/PIN7**
  relocalise → auxin is biased to the lower side → the root bends.
- **In microgravity** the fountain still forms but has **no direction** (symmetric auxin), and
  independently CARA/OSD-120 shows spaceflight **suppresses PIN3/PIN7** → auxin **confined to the QC**.
- **Gravity sets the asymmetry**: model predicts 0 % (µG) → 10 % (Moon) → 21 % (Mars) → 36 % (Earth) → 41 % (2 g).
- **The growth read-out** is the **[short, fat, hypoxic root](results/hypoxic-root-modelling.md)** — no convection → hypoxia → ethylene → radial swelling.

## Progress
- [x] Confirmed OSD-120 design via OSDR API (90 samples; Ecotype × Light × Spaceflight; RNA-Seq + imaging).
- [x] Extracted real **PIN3/PIN7** flight fold-changes (`results/OSD120_*`) — suppression strongest in dark Col-0.
- [x] Built the **microgravity + gravity-series** auxin model and the **µG (PIN3/7) confinement** model.
- [x] Generated manuscript **figures 1–4** (`figures/`).
- [x] **Manuscript draft** ([`manuscript/MANUSCRIPT.md`](manuscript/MANUSCRIPT.md)) + FAIR metadata (`.zenodo.json`, `CITATION.cff`).
- [x] Short-fat **hypoxic-root** visualisation + explanation (Fig 4).
- [ ] From-raw **DESeq2** rerun to confirm GeneLab's table (`reanalysis/scripts/01_deseq2.R`).
- [ ] Couple **auxin → growth** so the short-fat shape develops dynamically.
- [ ] Complete author list / ORCIDs → **mint the Zenodo DOI** (enable repo in Zenodo, then release).

## Repository map
| Path | What |
|---|---|
| [`manuscript/`](manuscript/) | `MANUSCRIPT.md` (peer-review draft) + `OUTLINE.md` |
| [`figures/`](figures/) | Fig 1 (gravity series) · Fig 2 (PIN carriers) · Fig 3 (µG confinement) · Fig 4 (hypoxic root) |
| [`reanalysis/`](reanalysis/) | `PIPELINE.md`, `environment.yml`, `scripts/`, `README.md` (FAIR + reproduce) |
| [`results/`](results/) | extracted tables, findings, enrichment, physiology ANOVAs |
| `*.md` | original CARA narrative chapters |

## Reproduce & cite
See [`reanalysis/README.md`](reanalysis/README.md) to reproduce the figures and mint the DOI.
Data © NASA OSDR (public); this reanalysis, model and figures are **CC0**. Interactive model:
<https://dr-richard-barker.github.io/virtual-root/>.
