# OSD-120 PIN3/PIN7 → Virtual Root µG parameter (real numbers)

Source: **GeneLab consensus DE table** for OSD-120
(`GLDS-120_rna_seq_differential_expression_GLbulkRNAseq.csv`, downloaded from OSDR),
flight-vs-ground contrasts within each ecotype × light condition. Extracted values in
[`OSD120_auxin_machinery_flight_vs_ground.csv`](OSD120_auxin_machinery_flight_vs_ground.csv).

## PIN3 / PIN7 spaceflight response (log2 fold-change, Flight ÷ Ground)

| Condition | PIN3 (AT1G70940) | PIN7 (AT1G23080) | mean linear FC | model `pin37` |
|---|---|---|---|---|
| **Col-0 — Dark** | **−0.65** | **−0.86** | 0.59 | **0.59** |
| Col-0 — Light | −0.04 | −0.33 | 0.89 | 0.89 |
| Col-0 *PhyD* — Dark | +0.55 | +1.03 | 1.75 | 1.0 (↑) |
| Col-0 *PhyD* — Light | −0.99 | −0.63 | 0.58 | 0.58 |
| WS — Dark | +0.29 | +0.15 | 1.17 | 1.0 (↑) |
| WS — Light | −0.30 | −0.41 | 0.78 | 0.78 |

`pin37 = clamp(mean(2^log2FC_PIN3, 2^log2FC_PIN7), 0, 1)` — the columella PIN3/7 level fed
to the [Virtual Root](https://dr-richard-barker.github.io/virtual-root/) model (1 = 1 g).

## What the real data say
- **PIN3/PIN7 suppression is light- and genotype-dependent, not uniform.** The clearest
  columella-PIN suppression is **dark-grown wild-type Col-0** (PIN3 −0.65, PIN7 −0.86 →
  `pin37 ≈ 0.59`) and *phyD* in the light (`pin37 ≈ 0.58`).
- In **dark**, the *phyD* and WS backgrounds instead **raise** PIN3/PIN7 — i.e. PHYD and
  ecotype modulate the spaceflight auxin-transport response (a genetic-dissection result,
  matching the study's aim).
- The headline mechanism (**suppressed columella PIN3/7 → auxin confined to the QC**) is
  supported most strongly in **Col-0 dark** — the etiolated condition most relevant to
  seedlings germinating in spaceflight.

## Figure 3 — the microgravity model, parameterised from the data
Dark-grown Col-0 (`pin37 = 0.59`), 1 g vs µG — open / embed:

**µG (Col-0 Dark):** <https://dr-richard-barker.github.io/virtual-root/#p=16&a=42&q=0.025&k=0.0012&c=0.59&g=0&m2=0&m1=0&d=0>

**1 g reference:** <https://dr-richard-barker.github.io/virtual-root/#p=16&a=42&q=0.025&k=0.0012&c=1&g=0&m2=0&m1=0&d=0>

*Caveats:* OSD-120 is bulk root-tip RNA-seq (tissue assignment of PIN3/7 to the columella
is from prior atlases); `padj` significance and rRNA-removed vs standard tables should be
checked when finalising. This uses GeneLab's processed DE; a from-raw DESeq2 rerun
(`reanalysis/scripts/01_deseq2.R`) can confirm.
