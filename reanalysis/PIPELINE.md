# CARA (OSD-120) reanalysis pipeline — plan

Goal: turn the existing CARA write-up into a **reproducible reanalysis** that feeds a
mechanistic **auxin-transport model** ([Virtual Root](https://github.com/dr-richard-barker/virtual-root)),
producing the figures and data for an **npj Microgravity** paper + a **Zenodo** deposit.

> Status: planning scaffold. Steps marked ⬜ are to do; fill in exact accessions, versions,
> and numbers as you run them.

## 0. Dataset — confirmed from OSDR (2026-07-02)
- **OSD-120** — *"Genetic dissection of the Arabidopsis spaceflight transcriptome: Are some
  responses dispensable for the physiological adaptation of plants to spaceflight?"* (Paul,
  Ferl *et al.*), NASA OSDR. *Organism:* *Arabidopsis thaliana*. **90 samples.**
- **Two assays:** **RNA-Seq** (transcription profiling) **and Photography / image analysis** —
  the imaging supports the physiology/validation arm in the same study.
- **Factors (confirmed levels):**
  | Factor | Levels |
  |---|---|
  | **Ecotype** | Col-0 · Col-0 PhyD · Wassilewskija (WS) |
  | **Treatment** | Light · Dark |
  | **Spaceflight** | Space Flight · Ground Control |
- **API:** metadata `https://osdr.nasa.gov/osdr/data/osd/meta/120` · files `…/osdr/data/osd/files/120`.
- License: NASA OSDR public; this reanalysis is CC0.

## 1. Retrieve + verify (reproducibly)
- ⬜ Pull raw FASTQ **and** GeneLab's processed counts + metadata (ISA-Tab) from OSDR via the OSDR API / `dpapi`.
- ⬜ Record checksums, sample→factor mapping, and the OSDR processing version.

## 2. QC & preprocessing
- FastQC → **MultiQC**; adapter/quality trim (**Trim Galore** or **fastp**).
- ⬜ Flag outliers; document read depths.

## 3. Alignment & quantification
- Reference **TAIR10** (Araport11 annotation). Align **STAR**, quantify **RSEM** (or **Salmon** for tx-level), matching the GeneLab consensus RNA-seq workflow so results are comparable.
- ⬜ Alternatively start from GeneLab's normalized counts to save compute — note which.

## 4. Differential expression
- **DESeq2** with a `~ genotype + condition + light + condition:light` design (adjust to the confirmed factors).
- Contrasts of interest: **flight vs ground** within each light×genotype; **light×spaceflight interaction**.
- Outputs: per-contrast DE tables (log2FC, padj), volcano + MA plots, PCA.

## 5. Extract the auxin machinery (the model bridge)
Pull fold-changes for the transport/response genes the model uses:
- **Efflux (PIN):** PIN1, PIN2, **PIN3**, PIN4, **PIN7** — expect **PIN3/PIN7 down in flight** (the key CARA result).
- **Influx (AUX1/LAX):** AUX1, LAX1–3.
- **Perception/response:** TIR1/AFB, Aux/IAA, ARFs, and **ARR5** (cytokinin reporter, down in flight).
- ⬜ Tabulate fold-changes × condition × genotype → `results/auxin_machinery_FC.csv`.

## 6. Give it tissue resolution
OSD-120 is bulk root-tip RNA-seq, so map genes to cell types:
- Cross-reference the **root single-cell / spatiotemporal atlas** (and this repo's `results/3d-root-single-cells-data.md`) to place PIN3/PIN7 in the **columella**, AUX1/LAX in cap/columella, etc.
- ⬜ Produce a tissue × gene × fold-change matrix.

## 7. Parameterise the microgravity model
- Convert the measured **PIN3/7 columella fold-change** into the Virtual Root **`pin37`** parameter (e.g., FC of ~0.15–0.3 → `pin37 ≈ 0.15–0.3`).
- Run the model **1 g vs µG**; export the predicted auxin maps (the tool's µG preset + shareable link already do this).
- ⬜ Repeat per genotype/light to predict phenotype-specific auxin fields.

## 8. Validate
- **Imaging:** compare the predicted auxin distribution to **DII-VENUS / R2D2** patterns (see the model's DII-VENUS compare view and `SPEC.md §8`).
- **Physiology:** relate predicted QC confinement to the measured root **skewing / dwarfing / length / diameter / surface / volume** ANOVAs already in `results/`.

## 9. Functional & epigenetic context
- Reuse/refresh **GO / PPI / Metascape** enrichment (`results/Enrichment_*`, `metascape_result.xlsx`) and the **skewing loci** tables; connect to hypoxia/dwarfing.

## 10. FAIR outputs
- ⬜ All steps as scripts (R + Python), pinned environment (`renv` / `conda` / container).
- ⬜ Figure-regeneration script → the manuscript figures.
- ⬜ **Zenodo** deposit (GitHub→Zenodo release) for a DOI; cite OSD-120 and the Virtual Root DOI.

## Starter scripts (`reanalysis/scripts/`)
Runnable skeletons — point them at the OSDR counts + sample table and go:
- **`01_deseq2.R`** — DESeq2 flight-vs-ground DE within each Ecotype × Treatment → `results/de/`.
- **`02_auxin_machinery.R`** — extract PIN/AUX1/LAX/TIR1/ARR5 fold-changes (by AGI) → `results/auxin_machinery_FC.csv` + bar plot; prints **PIN3/PIN7**.
- **`03_pin37_to_model.R`** — convert the measured **PIN3/7 fold-change → the Virtual Root `pin37`** parameter and write a **shareable µG model URL** for Figure 3.

## Tooling summary
`OSDR API` · `FastQC/MultiQC` · `Trim Galore/fastp` · `STAR + RSEM` (or `Salmon`) · `DESeq2` ·
`Metascape/clusterProfiler` · [`Virtual Root`](https://github.com/dr-richard-barker/virtual-root) · `Zenodo`.
