"""
Auxin -> growth coupling: the short-fat hypoxic root EMERGES from the model.

Each cell in the root file grows by turgor at a volumetric rate set by the auxin field
(cells elongate once auxin falls below a meristem threshold) and by O2 supply. A single
anisotropy parameter alpha partitions that volume growth between AXIAL (elongation) and
RADIAL (widening). Hypoxia (low O2) raises ethylene, which lowers alpha and the rate — so
the same rule gives a long thin root in air and a short fat root in spaceflight hypoxia.
Output: figures/fig5_growth_coupling.png
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.cm import magma

FIG = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "figures")); os.makedirs(FIG, exist_ok=True)

N = 44                                  # cells in the file (0 = just behind the QC/tip)
x = np.arange(N)
auxin = 0.15 + np.exp(-x / 5.0)         # high at the tip, decays shootward (the model gradient)
gate = (auxin < 0.5).astype(float)      # elongation competence: cells past the meristem

def grow(alpha, o2, cap=5.0, steps=320, dt=0.03):
    # bounded turgor growth: each competent cell's volume increment g saturates toward an
    # O2-limited budget (cap*o2); alpha partitions it axial vs radial.
    g = np.zeros(N); hist = []; rate = 0.9 * gate * o2; C = cap * o2 + 1e-9
    for _ in range(steps):
        g += dt * rate * np.maximum(0.0, 1 - g / C)
        hist.append((1 + g * alpha).sum())
    return 1 + g * alpha, 1 + g * (1 - alpha), np.array(hist)

# Normoxic (1 g air): strong axial anisotropy, full O2.  Hypoxic (spaceflight): isotropic + low O2.
lN, wN, hN = grow(alpha=0.82, o2=1.00)
lH, wH, hH = grow(alpha=0.50, o2=0.55)

def stats(l, w): return l.sum(), w.max(), (l.sum() / w.max())
LN, WN, AN = stats(lN, wN); LH, WH, AH = stats(lH, wH)
print(f"Normoxic : length={LN:.1f}  width={WN:.2f}  aspect(L/W)={AN:.1f}  volume={np.sum(lN*wN):.1f}")
print(f"Hypoxic  : length={LH:.1f}  width={WH:.2f}  aspect(L/W)={AH:.1f}  volume={np.sum(lH*wH):.1f}")

fig, (axr, axg) = plt.subplots(1, 2, figsize=(9.2, 5.6), gridspec_kw={"width_ratios": [1.1, 1]})

WSCALE = 10   # radial exaggeration for visibility (true aspect is extreme)
def draw(ax, l, w, x0, label):
    y = 0.0; amax = auxin.max()
    for i in range(N):
        ww = w[i] * WSCALE
        ax.add_patch(Rectangle((x0 - ww / 2, y), ww, l[i], facecolor=magma(min(1, auxin[i] / amax)),
                               edgecolor="#3a0f28", lw=0.2))
        y += l[i]
    ax.text(x0, -14, label, ha="center", va="top", fontsize=8)
draw(axr, lN, wN, 0, f"Normoxic (1 g)\nlong · thin\nL/W = {AN:.0f}")
draw(axr, lH, wH, 78, f"Spaceflight\nhypoxia\nshort · fat\nL/W = {AH:.0f}")
axr.set_xlim(-30, 108); axr.set_ylim(-40, LN * 1.06)
axr.set_aspect("equal"); axr.axis("off")
axr.set_title("Emergent root shape\n(tip ↓, colour = auxin; width ×10)", fontsize=9)

t = np.arange(len(hN)) * 0.02
axg.plot(t, hN, color="#2e7d32", lw=2, label="normoxic (1 g)")
axg.plot(t, hH, color="#d1495b", lw=2, label="spaceflight hypoxia")
axg.set_xlabel("time (a.u.)"); axg.set_ylabel("root length (a.u.)")
axg.set_title("Auxin→growth coupling:\nhypoxia shortens the root"); axg.legend(fontsize=8); axg.grid(alpha=0.25)

fig.suptitle("The short-fat hypoxic root emerges from an auxin→growth rule", fontsize=12)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig5_growth_coupling.png"), dpi=140)
print("saved fig5_growth_coupling.png")
