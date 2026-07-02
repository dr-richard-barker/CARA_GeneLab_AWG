# Manuscript outline — npj Microgravity

**Working title:** *Spaceflight suppression of PIN3/PIN7 confines auxin to the quiescent
centre: integrating the CARA root transcriptome with a mechanistic auxin-transport model*

**One-line thesis:** the CARA (OSD-120) ISS transcriptome shows PIN3/PIN7 are down in
spaceflight; a cell-based auxin-transport model shows that this **confines auxin to the QC**,
mechanistically linking the flight transcriptome to the observed root-growth phenotypes.

## Abstract (≤ 150 words)
Gravity shapes root growth via PIN-mediated auxin transport. How spaceflight rewires this at
the tip is unclear. We reanalyse the CARA ISS root-tip RNA-seq (OSD-120; Col-0, *phyD*, WS;
light/dark) and find coordinated suppression of the columella carriers **PIN3/PIN7** (and
ARR5). Feeding these changes into an open, cell-based auxin-transport model
([Virtual Root](https://github.com/dr-richard-barker/virtual-root)) predicts **loss of lateral
redistribution and confinement of auxin to the quiescent centre**, consistent with the
measured skewing/dwarfing phenotypes and DII-VENUS-type patterns. The model turns a gene
list into a testable mechanism and a reusable hypothesis engine for space-plant biology.

## 1. Introduction
- Roots sense gravity via statoliths → PIN relocalisation → auxin gradient → differential growth.
- Spaceflight removes the directional cue; roots show skewing, waving, altered architecture.
- Prior CARA work: transcriptome + phenotypes, but the **mechanistic link is missing**.
- Here: reproducible reanalysis + a mechanistic model that connects the two.

## 2. Results
- **R1 — Spaceflight reprograms the root-tip transcriptome.** DE overview; light × genotype structure; PCA/volcano. *(Fig 1)*
- **R2 — The auxin transport machinery is remodelled: PIN3/PIN7 down.** Fold-changes for PIN/AUX1-LAX/ARF/ARR5, tissue-mapped to the columella. *(Fig 2)*
- **R3 — A microgravity auxin-transport model predicts QC confinement.** Set model PIN3/7 to the measured suppression → auxin shifts from lateral cap into the QC (quantified). *(Fig 3 — the µG vs 1 g maps)*
- **R4 — Predictions match imaging and physiology.** Predicted confinement vs DII-VENUS/R2D2 pattern and vs measured skewing/dwarfing/root-trait ANOVAs. *(Fig 4)*
- **R5 — Functional & epigenetic context.** GO/PPI/Metascape enrichment, skewing loci, hypoxia/dwarfing links. *(Fig 5)*

## 3. Discussion
- Mechanism: PIN3/7 loss → impaired redistribution → QC-confined auxin → altered elongation → skewing/dwarfing.
- Light × genotype (*phyD*) modulation — photomorphogenesis × gravity.
- The model as a **hypothesis engine** for space agriculture (predict interventions, target genes).
- Limitations: bulk RNA-seq tissue inference; idealised model geometry; validation is qualitative pending quantitative imaging.

## 4. Methods
Reanalysis pipeline (see [`reanalysis/PIPELINE.md`](../reanalysis/PIPELINE.md)); the
two-compartment auxin-transport model and its parameterisation (Virtual Root `SPEC.md`);
statistics.

## 5. Data & code availability
- Raw/processed data: **OSD-120 / GLDS-120** (NASA OSDR).
- Reanalysis + figures: this repo + **Zenodo DOI** (to mint on release).
- Model: [Virtual Root](https://github.com/dr-richard-barker/virtual-root) (+ its Zenodo DOI).

## Figures (main)
1. Transcriptome overview (PCA, volcano, DE counts by contrast).
2. Auxin-machinery fold-changes, tissue-mapped (PIN3/7 highlighted).
3. **Model: 1 g vs µG auxin maps** — QC confinement (from the Virtual Root µG preset).
4. Validation: model vs DII-VENUS pattern + physiology ANOVAs.
5. Functional/epigenetic context (enrichment + skewing loci).

## Author / contribution notes
⬜ Confirm authorship, CARA science-team acknowledgement, and OSDR/AWG credit.
