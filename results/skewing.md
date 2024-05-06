# Skewing



GWAS interesect with differentially expressed loci from OSDR meta-analysis.&#x20;





GWAS\_tortosity\_associations&#x20;

GWAS\_root\_angle\_associations&#x20;

DGE\_37,\_38,\_120&#x20;

GDE\_37,\_251,\_321&#x20;

DGE\_37,\_38,\_120,\_217,\_321

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/Pairwise_heatmap2_Intervene-2024-05-03.png" alt=""><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>





<figure><img src="../.gitbook/assets/jVenn_chart.png" alt=""><figcaption></figcaption></figure>





Gene Ontology (GO) Categories and Descriptions with Statistical Analysis

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

## Gene Ontology (GO) Categories and Descriptions with Statistical Analysis

This section presents the results of a statistical analysis of gene ontology (GO) categories, covering Biological Processes, Molecular Functions, and Cellular Components. For each category, a description is provided alongside the count and statistical significance of observed phenomena.

### Biological Processes

1. **Organic Hydroxy Compound Metabolic Process**
   * **GO ID:** GO:1901615
   * **Count:** 4 (12.12%)
   * **Log10(P):** -3.10
   * **Log10(q):** 0.00
2. **Pyridine-containing Compound Metabolic Process**
   * **GO ID:** GO:0072524
   * **Count:** 3 (9.09%)
   * **Log10(P):** -3.03
   * **Log10(q):** 0.00

### Molecular Functions

1. **Glycosyltransferase Activity**
   * **GO ID:** GO:0016757
   * **Count:** 5 (15.15%)
   * **Log10(P):** -2.51
   * **Log10(q):** 0.00

### Cellular Components

1. **Nuclear Protein-containing Complex**
   * **GO ID:** GO:0140513
   * **Count:** 4 (12.12%)
   * **Log10(P):** -2.16
   * **Log10(q):** 0.00
2. **Membrane Protein Complex**
   * **GO ID:** GO:0098796
   * **Count:** 3 (9.09%)
   * **Log10(P):** -1.50
   * **Log10(q):** 0.00







<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>



#### Protein-protein Interaction Enrichment Analysis

For each gene list, we conducted a protein-protein interaction enrichment analysis using databases such as STRING, BioGrid, OmniPath, and InWeb\_IM. The network derived from this analysis includes a subset of proteins that have at least one physical interaction with another protein in the list. If the network consists of 3 to 500 proteins, we apply the Molecular Complex Detection (MCODE) algorithm to identify densely connected network regions. The identified MCODE networks for each gene list are presented in Figure 5. Furthermore, we conducted pathway and process enrichment analyses on each MCODE component separately. We retained the three highest-ranked terms by p-value as the functional descriptors for each component. These are depicted in the tables beneath the network illustrations in Figure 5.

<figure><img src="../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

**All lists merged Colored by Counts(Full Connection)**

| GO         | Description                                   | Log10(P) |
| ---------- | --------------------------------------------- | -------- |
| GO:0042537 | benzene-containing compound metabolic process | -4.7     |
| GO:0009723 | response to ethylene                          | -3.0     |
| GO:0046527 | glucosyltransferase activity                  | -2.9     |



'



{% embed url="https://knetminer.com/beta/knetspace/network/82664856-9a2d-4925-9b09-8952578351e1" %}
Link to interactive version
{% endembed %}

<table><thead><tr><th width="173">Category</th><th width="207">Description</th><th width="76">LogP</th><th width="476">Hits</th></tr></thead><tbody><tr><td>GO Biological Processes</td><td>organic hydroxy compound metabolic process</td><td>-3.8</td><td>HMG2|UGT74F2|UGT74F1|RSR4</td></tr><tr><td>GO Biological Processes</td><td>pyridine-containing compound metabolic process</td><td>-3.6</td><td>QPT|NADP-ME2|RSR4</td></tr><tr><td>GO Biological Processes</td><td>amino acid metabolic process</td><td>-3.2</td><td>UGT74F2|UGT74F1|OASA2|RSR4</td></tr><tr><td>GO Biological Processes</td><td>purine nucleotide metabolic process</td><td>-2.7</td><td>QPT|HMG2|NADP-ME2</td></tr><tr><td>GO Biological Processes</td><td>organophosphate metabolic process</td><td>-2.6</td><td>QPT|HMG2|NADP-ME2|RSR4</td></tr><tr><td>GO Biological Processes</td><td>purine-containing compound metabolic process</td><td>-2.6</td><td>QPT|HMG2|NADP-ME2</td></tr><tr><td>GO Biological Processes</td><td>nucleotide metabolic process</td><td>-2.5</td><td>QPT|HMG2|NADP-ME2</td></tr><tr><td>GO Biological Processes</td><td>nucleoside phosphate metabolic process</td><td>-2.5</td><td>QPT|HMG2|NADP-ME2</td></tr><tr><td>GO Molecular Functions</td><td>glycosyltransferase activity</td><td>-2.4</td><td>QPT|UGT74F2|UGT74F1|ZIP2</td></tr><tr><td>GO Biological Processes</td><td>nucleobase-containing small molecule metabolic process</td><td>-2.1</td><td>QPT|HMG2|NADP-ME2</td></tr><tr><td>WikiPathways</td><td>Seed development</td><td>-2.1</td><td>UGT74F2|UGT74F1|CSN5A</td></tr><tr><td>GO Cellular Components</td><td>membrane protein complex</td><td>-2</td><td>AP19|AGB1|TIM17-3</td></tr><tr><td>GO Biological Processes</td><td>carboxylic acid metabolic process</td><td>-2</td><td>UGT74F2|UGT74F1|OASA2|NADP-ME2</td></tr><tr><td>GO Cellular Components</td><td>nuclear protein-containing complex</td><td>-1.9</td><td><p></p><p>ESP4|CSN5A|THO2</p></td></tr></tbody></table>

<figure><img src="../.gitbook/assets/Skewing intersect with flight.png" alt=""><figcaption><p><a href="https://knetminer.com/beta/knetspace/network/82664856-9a2d-4925-9b09-8952578351e1">https://knetminer.com/beta/knetspace/network/82664856-9a2d-4925-9b09-8952578351e1</a></p></figcaption></figure>

<table><thead><tr><th width="286">Intersecting lists</th><th width="171">Loci used in Knet-1</th></tr></thead><tbody><tr><td>root_angle|5 OSDR|3 OSDR</td><td>AT3G10340</td></tr><tr><td>root_angle|5 OSDR|3 OSDR</td><td>AT2G13540</td></tr><tr><td>root_angle|5 OSDR|3 OSDR</td><td>AT5G22880</td></tr><tr><td>root_angle|5 OSDR|3 OSDR</td><td>AT5G35590</td></tr><tr><td>root_angle|5 OSDR|3 OSDR</td><td>AT5G49360</td></tr><tr><td>root_angle|5 OSDR|3 OSDR</td><td>AT1G55580</td></tr><tr><td>root_angle|5 OSDR</td><td>AT3G23100</td></tr><tr><td>tortosity|5 OSDR</td><td>AT3G05870</td></tr><tr><td>tortosity|5 OSDR</td><td>AT5G11710</td></tr><tr><td>tortosity|5 OSDR</td><td>AT5G25220</td></tr><tr><td>tortosity|5 OSDR</td><td>AT4G37580</td></tr><tr><td>tortosity|5 OSDR</td><td>AT3G56000</td></tr></tbody></table>

**Some of these loci might be invovled in the hypoxia induced skew in space flight.**&#x20;



