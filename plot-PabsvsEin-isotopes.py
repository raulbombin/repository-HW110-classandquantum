import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Figure
# ------------------------------------------------------------------

fs = 17
lw = 1.5
psize = 0

fig, ax = plt.subplots(3, 1, figsize=(6,5), sharex=True)

fig.subplots_adjust(wspace=0.0, hspace=0.0)

# ------------------------------------------------------------------
# Read data
# ------------------------------------------------------------------
folder="data-Pabs-isotopes/"
classical = np.loadtxt(folder+"Pabs_vs_Ein_classical.dat")

H = np.loadtxt(folder+"Pabs_vs_Ein_H_quantum.dat")
D = np.loadtxt(folder+"Pabs_vs_Ein_D_quantum.dat")
T = np.loadtxt(folder+"Pabs_vs_Ein_T_quantum.dat")

# ------------------------------------------------------------------
# Plot classical
# ------------------------------------------------------------------

for i in range(3):
    ax[i].plot(
        classical[:,0],
        classical[:,1],
        color="black",
        linestyle="dotted",
        linewidth=2*lw,
        marker="o",
        markersize=0,
        label="Bulk absorption"
    )

# ------------------------------------------------------------------
# Plot quantum
# ------------------------------------------------------------------

quantum = [H, D, T]

for i in range(3):
    ax[i].plot(
        quantum[i][:,0],
        quantum[i][:,1],
        color="blue",
        marker="^",
        linewidth=lw,
        markersize=psize
    )

# ------------------------------------------------------------------
# Vibrational thresholds
# ------------------------------------------------------------------

YMIN = 0.05
YMAX = 0.92

# Hydrogen
ener = 83/2/1000.
ener2 = 91/2/1000.
lw2 = 1.5
alph2 = 0.3

i = 0
for n in (1,3):
    e1 = ener*n
    e2 = ener2*n

    ax[i].axvline(e1,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)

    ax[i].axvline(e1+0.0162,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2+0.0122,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e1+0.0324,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2+0.0244,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)

ener = 81/2/1000.
ener2 = 88/2/1000.

for n in (1,3):
    e1 = ener*n
    e2 = ener2*n

    ax[0].axvline(e1,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)
    ax[0].axvline(e2,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)

    ax[0].axvline(e1+0.0162,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[0].axvline(e2+0.0122,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[0].axvline(e1+0.0324,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[0].axvline(e2+0.0244,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)

# Deuterium

i = 1
ener = 62.8/2./1000.
ener2 = 68.33/2./1000.

for n in (1,3):
    e1 = ener*n
    e2 = ener2*n

    ax[i].axvline(e1,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)

    ax[i].axvline(e1+0.0162/2,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2+0.0122/2,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e1+0.0324/2,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2+0.0244/2,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)

# Tritium

i = 2
ener = 52.38/2./1000.
ener2 = 58.00/2./1000.

for n in (1,3):
    e1 = ener*n
    e2 = ener2*n

    ax[i].axvline(e1,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2,ymin=YMIN,ymax=YMAX,color='red',linewidth=lw2,alpha=alph2)

    ax[i].axvline(e1+0.0162/3,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2+0.0122/3,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e1+0.0324/3,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)
    ax[i].axvline(e2+0.0244/3,ymin=YMIN,ymax=YMAX,color='green',linewidth=lw2,alpha=alph2)

# Diffraction thresholds

for ediff in (0.0122,0.0163):
    for i in (1,2,3):
        ax[i-1].axvline(
            ediff/i,
            ymin=YMIN,
            ymax=YMAX,
            color='orange',
            linewidth=lw2,
            alpha=alph2+0.3
        )

# ------------------------------------------------------------------
# Labels
# ------------------------------------------------------------------

ax[0].set_ylabel(r"$P_{\rm abs}^{\rm (H)}$",fontsize=fs)
ax[1].set_ylabel(r"$P_{\rm abs}^{\rm (D)}$",fontsize=fs)
ax[2].set_ylabel(r"$P_{\rm abs}^{\rm (T)}$",fontsize=fs)

ax[2].set_xlabel(r"$E_{\rm in}$ (eV)",fontsize=fs)

xmax = 0.5

for i in range(3):

    ax[i].set_xscale("log")
    ax[i].set_xlim(0.010, xmax)
    ax[i].set_ylim(0.00,0.99)

    ax[i].tick_params(
        axis='both',
        which='major',
        direction='inout',
        top=True,
        bottom=True,
        left=True,
        right=True,
        width=1.5,
        length=8,
        labelsize=fs
    )

    ax[i].tick_params(
        axis='both',
        which='minor',
        direction='inout',
        top=True,
        bottom=True,
        left=True,
        right=True,
        width=1.2,
        length=5
    )

ax[0].annotate("(a)",xy=(0.37,0.80),fontsize=fs)
ax[1].annotate("(b)",xy=(0.37,0.80),fontsize=fs)
ax[2].annotate("(c)",xy=(0.37,0.80),fontsize=fs)

plt.subplots_adjust(
    top=0.97,
    bottom=0.13,
    left=0.18,
    right=0.96,
    hspace=0.0,
    wspace=0.02
)

plt.savefig("stick-isotopes-log.pdf")
plt.show()
