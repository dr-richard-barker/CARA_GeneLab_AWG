# The short, fat, hypoxic spaceflight root

![Short fat hypoxic root](../figures/fig4_hypoxic_root.png)

**Figure 4.** The same auxin-transport model on a normal (long, thin) vs a hypoxic
(short, fat) root geometry. The auxin machinery — and the QC auxin maximum — is unchanged;
only the growth output differs.

## Why spaceflight roots go short and fat
On Earth, **buoyancy-driven convection** constantly mixes gases around the root, and gravity
drains water so a thin, aerated film remains. In **microgravity there is no convection**:
water is held around the root by surface tension, gas exchange collapses, and O₂ cannot
diffuse in fast enough — the root tip experiences **local hypoxia**.

Hypoxia triggers a stereotyped morphology:
- **Ethylene** accumulates (hypoxia induces its biosynthesis; poor gas exchange traps it).
- Ethylene + altered **auxin** shift growth from **axial elongation** to **radial expansion**
  (loss of growth anisotropy — cortical cells swell sideways instead of lengthening).
- The result is the classic **short, fat root**, often with reduced/agravitropic waving —
  and it overlaps the **dwarfing / skewing** phenotype seen in CARA
  (see [`hypoxia-induced-dwarfing-skew.md`](hypoxia-induced-dwarfing-skew.md)).

## How it connects to the auxin model
The auxin-transport model predicts the **auxin field** (QC maximum + reflux); it does not
itself grow the root. The short-fat phenotype is the **growth read-out** of that field under
hypoxia:
- The QC auxin maximum still forms (Fig 4, both geometries) — the tip patterning is robust.
- What changes is the **elongation-zone response**: hypoxia/ethylene blunt auxin-driven
  axial elongation and redirect it radially. Modelled here as a **geometry change** (a wider,
  shorter root) rather than a transport change — the machinery is the same, the growth differs.
- This is complementary to the PIN3/7 route (µG → auxin confined to the QC): PIN3/7 loss
  changes *where* auxin sits; hypoxia changes *how the root grows* in response to it.

## Next modelling steps
- **Couple auxin → growth:** add a simple elongation rule (axial strain ∝ auxin below a
  threshold) and an O₂/hypoxia field, so the root *develops* the short-fat shape dynamically
  rather than being drawn that way.
- **Ethylene node:** add an ethylene variable (hypoxia-induced) that damps anisotropic growth.
- **Validate:** compare predicted length/diameter/surface/volume ratios to the CARA
  physiology ANOVAs already in `results/`, and to root morphometrics (RSML / RootNav).
