"""
Generate manuscript figures for the CARA/OSD-120 × Virtual Root paper.
  Fig 2 : OSD-120 PIN3/PIN7 (and PIN1/4, AUX1) flight-vs-ground log2FC by condition.
  Fig 3 : auxin model, ground (1 g, pin37=1) vs spaceflight (µG, Col-0 Dark pin37=0.59).
Fig 1 (gravity series) is produced by ../../virtual-root gravity_series.py.
Outputs -> figures/.
"""
import os, csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

HERE = os.path.dirname(__file__)
FIG = os.path.abspath(os.path.join(HERE, "..", "..", "figures")); os.makedirs(FIG, exist_ok=True)
CSV = os.path.abspath(os.path.join(HERE, "..", "..", "results", "OSD120_auxin_machinery_flight_vs_ground.csv"))

# ---------- Figure 2: PIN/AUX1 fold-changes ----------
rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
conds = ["Col-0 Dark", "Col-0 Light", "Col-0 PhyD Dark", "Col-0 PhyD Light", "WS Dark", "WS Light"]
def cond(r): return f"{r['ecotype']} {r['treatment']}"
genes = ["PIN1", "PIN3", "PIN4", "PIN7", "AUX1"]
M = np.full((len(genes), len(conds)), np.nan)
for r in rows:
    if r["gene"] in genes and cond(r) in conds:
        M[genes.index(r["gene"]), conds.index(cond(r))] = float(r["log2FC_flight_vs_ground"])
fig, ax = plt.subplots(figsize=(8.2, 4.6))
x = np.arange(len(conds)); w = 0.15
for i, gname in enumerate(genes):
    ax.bar(x + (i - 2) * w, M[i], w, label=gname)
ax.axhline(0, color="0.4", lw=0.8)
ax.set_xticks(x); ax.set_xticklabels(conds, rotation=25, ha="right", fontsize=9)
ax.set_ylabel("log2 fold-change (flight / ground)")
ax.set_title("OSD-120: auxin-carrier response to spaceflight")
ax.legend(ncol=5, fontsize=8, loc="lower center")
ax.annotate("PIN3/PIN7 suppressed\n(dark-grown Col-0)", (0, -0.8), fontsize=8, color="#b33",
            ha="center", va="top")
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig2_auxin_carriers.png"), dpi=140)
print("saved fig2_auxin_carriers.png")

# ---------- Figure 3: auxin model, ground vs spaceflight ----------
R, C, c0 = 52, 17, 8; r_qc, r_mer, CAP = 46, 30, 4.7
rows_ = np.arange(R)[:, None].repeat(C, 1); rad = np.abs(np.arange(C) - c0)[None, :].repeat(R, 0)
active = np.zeros((R, C), bool)
for r in range(R):
    for c in range(C):
        rd = abs(c - c0); active[r, c] = rd <= 4 if r < r_qc else rd <= np.sqrt(max(0.0, CAP**2 - (r - r_qc)**2))
stele = rad <= 1; endo = rad == 2; cortex = rad == 3; epi = rad == 4; tip = rows_ >= r_qc
qc = active & (rows_ == r_qc) & (rad <= 1); col = active & (rows_ > r_qc) & (rad <= 2); lrc = active & (rows_ >= r_qc - 2) & (rad >= 3)
L = 10.0; gg = 1 / L; dt = 0.04; k = 0.0012; EF_BASE, EF_PIN, IN_BASE, IN_AUX1 = 1., 16., 20., 42.
S_shoot, P_qc, P_col, P_base = 0.30, 0.025, 0.012, 0.005; cc = np.arange(C)[None, :]
def run(pin37, steps=48000):
    eu = np.full((R, C), EF_BASE); ed = eu.copy(); el = eu.copy(); er = eu.copy()
    rootward = ((stele | endo) & ~tip) | (cortex & (rows_ >= r_mer) & ~tip)
    shootward = (cortex & (rows_ < r_mer)) | (epi & (rows_ < r_mer)) | (epi & tip) | lrc
    ed[rootward] = EF_PIN; eu[shootward] = EF_PIN
    inw = epi & (rows_ >= r_mer); er[inw & (cc < c0)] = EF_PIN; el[inw & (cc > c0)] = EF_PIN
    cp = EF_PIN * pin37
    for arr in (eu, ed, el, er): arr[col] = cp
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
        da[:, :-1] += gg*(pin_in[:, :-1]*Wv - er[:, :-1]*a[:, :-1])*bV
        da[:, 1:]  += gg*(pin_in[:, 1:]*Wv - el[:, 1:]*a[:, 1:])*bV
        da[:-1, :] += gg*(pin_in[:-1, :]*Wh - ed[:-1, :]*a[:-1, :])*bH
        da[1:, :]  += gg*(pin_in[1:, :]*Wh - eu[1:, :]*a[1:, :])*bH
        da[active & ~aL] -= gg*el[active & ~aL]*a[active & ~aL]; da[active & ~aR] -= gg*er[active & ~aR]*a[active & ~aR]
        da[active & ~aU] -= gg*eu[active & ~aU]*a[active & ~aU]; da[active & ~aD] -= gg*ed[active & ~aD]*a[active & ~aD]
        a += dt*da; a[~active] = 0.
    return a
def confine(a):
    center = a[r_qc-1:, :][ (np.abs(cc-c0)<=1) & active ][r_qc-1:].sum() if False else \
             a[(rows_>=r_qc-1) & (np.abs(rad)<=1) & active].sum()
    cap = a[lrc].sum(); return center / (cap + 1e-9)
ag = run(1.0); au = run(0.59)
vmax = max(np.nanmax(np.where(active, ag, np.nan)), np.nanmax(np.where(active, au, np.nan)))
fig, ax = plt.subplots(1, 2, figsize=(5.2, 5.6))
for a_, name, axx in [(ag, f"Ground (1 g)\nPIN3/7 = 100%", ax[0]), (au, f"Spaceflight (µG)\nPIN3/7 = 59%", ax[1])]:
    axx.imshow(np.where(active, a_, np.nan), cmap="magma", origin="upper", aspect="equal",
               norm=PowerNorm(0.45, vmin=0, vmax=vmax))
    axx.set_title(f"{name}\nQC:cap = {confine(a_):.2f}", fontsize=9); axx.set_xticks([]); axx.set_yticks([])
ax[0].set_ylabel("shoot → tip", fontsize=9)
fig.suptitle("Model: spaceflight PIN3/7 loss confines auxin to the QC", fontsize=11)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig3_model_ground_vs_flight.png"), dpi=140)
print(f"saved fig3_model_ground_vs_flight.png  (ground QC:cap={confine(ag):.2f}, flight={confine(au):.2f})")

# ---------- Figure 3c: QC confinement vs PIN3/7 level (dose-response) ----------
ps = [1.0, 0.85, 0.7, 0.59, 0.45, 0.3, 0.15]
cs = [confine(run(p, steps=40000)) for p in ps]
fig, ax = plt.subplots(figsize=(5.8, 4.0))
ax.plot(ps, cs, "-o", color="#2e7d32")
ax.axvline(0.59, color="#d1495b", ls="--")
ax.annotate("Col-0 Dark\n(measured)", (0.59, cs[3]), (0.59, cs[3] + 0.04), color="#d1495b", fontsize=8, ha="center")
ax.set_xlabel("columella PIN3/7 level  (1 = ground, lower = spaceflight)")
ax.set_ylabel("QC : lateral-cap auxin ratio")
ax.set_title("Lower PIN3/7 confines auxin to the QC")
ax.invert_xaxis(); ax.grid(alpha=0.25)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig3c_confinement_curve.png"), dpi=140)
print("saved fig3c_confinement_curve.png")
