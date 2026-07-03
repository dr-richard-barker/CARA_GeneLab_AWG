"""
The short, fat, hypoxic spaceflight root — visualisation.

In spaceflight there is no buoyancy-driven convection, so gases do not mix around the
root; water films and poor O2 diffusion cause local HYPOXIA. Hypoxia raises ethylene and
alters auxin, which reduces *axial* elongation and promotes *radial* expansion — giving the
classic short, fat root. The auxin machinery is unchanged; the growth output differs.
Here we run the same auxin-transport model on a normal (long, thin) vs a hypoxic
(short, fat) root geometry.  Output: figures/fig4_hypoxic_root.png
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

FIG = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "figures"))
os.makedirs(FIG, exist_ok=True)
L = 10.0; g = 1 / L; dt = 0.04; k = 0.0012
EF_BASE, EF_PIN, IN_BASE, IN_AUX1 = 1., 16., 20., 42.
S_shoot, P_qc, P_col, P_base = 0.30, 0.025, 0.012, 0.005

def build_run(R, HW, steps=38000):
    C = 2 * HW + 1; c0 = HW; CAP = HW + 0.7
    r_qc = R - 6; r_mer = int(R * 0.58)
    rows = np.arange(R)[:, None].repeat(C, 1); rad = np.abs(np.arange(C) - c0)[None, :].repeat(R, 0)
    active = np.zeros((R, C), bool)
    for r in range(R):
        for c in range(C):
            rd = abs(c - c0)
            active[r, c] = rd <= HW if r < r_qc else rd <= np.sqrt(max(0.0, CAP**2 - (r - r_qc)**2))
    stele = rad <= 1; endo = rad == 2; cortex = (rad >= 3) & (rad < HW); epi = rad == HW; tip = rows >= r_qc
    qc = active & (rows == r_qc) & (rad <= 1); col = active & (rows > r_qc) & (rad <= 2)
    lrc = active & (rows >= r_qc - 2) & (rad >= 3); cc = np.arange(C)[None, :]
    eu = np.full((R, C), EF_BASE); ed = eu.copy(); el = eu.copy(); er = eu.copy()
    rootward = ((stele | endo) & ~tip) | (cortex & (rows >= r_mer) & ~tip)
    shootward = (cortex & (rows < r_mer)) | (epi & (rows < r_mer)) | (epi & tip) | lrc
    ed[rootward] = EF_PIN; eu[shootward] = EF_PIN
    inw = epi & (rows >= r_mer); er[inw & (cc < c0)] = EF_PIN; el[inw & (cc > c0)] = EF_PIN
    for arr in (eu, ed, el, er): arr[col] = EF_PIN
    pin_in = np.full((R, C), IN_BASE); pin_in[epi | lrc | col | qc | (cortex & tip)] = IN_AUX1
    prod = np.where(active, P_base, 0.); prod[col] = P_col; prod[qc] = P_qc; prod[0, c0 - 1:c0 + 2] += S_shoot
    for arr in (eu, ed, el, er, pin_in, prod): arr[~active] = 0.
    a = np.where(active, 0.1, 0.)
    aL = np.zeros_like(active); aR = aL.copy(); aU = aL.copy(); aD = aL.copy()
    aL[:, 1:] = active[:, :-1]; aR[:, :-1] = active[:, 1:]; aU[1:, :] = active[:-1, :]; aD[:-1, :] = active[1:, :]
    for _ in range(steps):
        bV = active[:, :-1] & active[:, 1:]; dV = pin_in[:, :-1] + pin_in[:, 1:]
        Wv = np.where(bV, (er[:, :-1]*a[:, :-1] + el[:, 1:]*a[:, 1:]) / np.where(dV > 0, dV, 1), 0)
        bH = active[:-1, :] & active[1:, :]; dH = pin_in[:-1, :] + pin_in[1:, :]
        Wh = np.where(bH, (ed[:-1, :]*a[:-1, :] + eu[1:, :]*a[1:, :]) / np.where(dH > 0, dH, 1), 0)
        da = prod - k*a
        da[:, :-1] += g*(pin_in[:, :-1]*Wv - er[:, :-1]*a[:, :-1])*bV
        da[:, 1:]  += g*(pin_in[:, 1:]*Wv - el[:, 1:]*a[:, 1:])*bV
        da[:-1, :] += g*(pin_in[:-1, :]*Wh - ed[:-1, :]*a[:-1, :])*bH
        da[1:, :]  += g*(pin_in[1:, :]*Wh - eu[1:, :]*a[1:, :])*bH
        da[active & ~aL] -= g*el[active & ~aL]*a[active & ~aL]; da[active & ~aR] -= g*er[active & ~aR]*a[active & ~aR]
        da[active & ~aU] -= g*eu[active & ~aU]*a[active & ~aU]; da[active & ~aD] -= g*ed[active & ~aD]*a[active & ~aD]
        a += dt*da; a[~active] = 0.
    return active, a

# normal (long, thin) and hypoxic (short, fat)
n_act, n_a = build_run(R=54, HW=4)
h_act, h_a = build_run(R=32, HW=8)
vmax = max(n_a.max(), h_a.max())
maxR = 54

fig, ax = plt.subplots(figsize=(7.4, 6.4))
def draw(active, a, x0, label):
    disp = np.where(active, a, np.nan); R, C = a.shape
    ax.imshow(disp, cmap="magma", origin="upper", aspect="equal",
              norm=PowerNorm(0.45, vmin=0, vmax=vmax), extent=(x0, x0 + C, R, 0))
    ax.text(x0 + C / 2, R + 1.5, label, ha="center", va="top", fontsize=9)
draw(n_act, n_a, 0, "Normoxic (1 g)\nlong · thin")
draw(h_act, h_a, 12, "Spaceflight hypoxia\nshort · fat")
ax.annotate("no buoyant convection → water films →\nlocal hypoxia → ethylene →\nless elongation, more radial swelling",
            (20, 10), (10.5, 40), ha="center", fontsize=8, color="#2166ac",
            arrowprops=dict(arrowstyle="->", color="#2166ac"))
ax.set_xlim(-1, 24); ax.set_ylim(maxR + 5, -2); ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([]); ax.set_ylabel("shoot → tip", fontsize=9)
ax.set_title("The short, fat, hypoxic spaceflight root\n(same auxin machinery, altered growth output)", fontsize=11)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig4_hypoxic_root.png"), dpi=140)
print("saved fig4_hypoxic_root.png")
