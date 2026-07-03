# CARA / OSD-120 reanalysis — FAIR structure & how to reproduce

A **F**indable, **A**ccessible, **I**nteroperable, **R**eusable layout for the reanalysis
→ manuscript → Zenodo deposit.

## Repository layout
```
CARA_GeneLab_AWG/
├── .zenodo.json            # Zenodo deposit metadata (mints the DOI on GitHub release)
├── CITATION.cff            # how to cite
├── LICENSE                 # CC0-1.0
├── reanalysis/
│   ├── PIPELINE.md         # the 10-step reproducible plan (confirmed OSD-120 design)
│   ├── environment.yml     # conda env (R/DESeq2 + Python)
│   ├── scripts/            # 01_deseq2.R · 02_auxin_machinery.R · 03_pin37_to_model.R · 04_make_figures.py
│   └── data/               # OSDR downloads (git-ignored — fetch, don't commit)
├── results/                # extracted tables + findings (OSD120_*.csv, *_findings.md)
├── figures/                # manuscript figures (fig1a/b, fig2, fig3, fig3c)
├── manuscript/             # OUTLINE.md + MANUSCRIPT.md (peer-review draft)
└── *.md                    # original CARA narrative chapters
```

## Reproduce the figures
```bash
conda env create -f reanalysis/environment.yml && conda activate cara-reanalysis

# 1. Data (from OSDR — see PIPELINE.md §0-1):
#    GLDS-120_rna_seq_differential_expression_GLbulkRNAseq.csv  (GeneLab consensus DE)
#    -> reanalysis/data/   (git-ignored)

# 2. From GeneLab's DE table (fast path):
#    extract PIN3/7 -> results/OSD120_auxin_machinery_flight_vs_ground.csv  (already provided)

# 3. Model + figures:
python reanalysis/scripts/04_make_figures.py         # fig2, fig3, fig3c -> figures/
#    fig1 (gravity series) from the Virtual Root repo: python gravity_series.py

# Optional — full DE from raw counts:
Rscript reanalysis/scripts/01_deseq2.R
Rscript reanalysis/scripts/02_auxin_machinery.R
Rscript reanalysis/scripts/03_pin37_to_model.R       # -> Virtual Root µG URL
```

## Mint the Zenodo DOI
1. Complete the ⬜ TODOs in `.zenodo.json` and `CITATION.cff` (authors, ORCIDs, acknowledgements).
2. Enable the repo in [Zenodo ↔ GitHub](https://zenodo.org/account/settings/github/).
3. Create a **GitHub Release** → Zenodo archives it and mints a versioned DOI.
4. Add the DOI badge to the top-level `README.md` and cite it + OSD-120 in the manuscript.

*Provenance:* data © NASA OSDR (public); this reanalysis, model and figures are CC0.
