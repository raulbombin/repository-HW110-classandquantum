import numpy as np
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# units
H2eV= 27.2114  #Hartree to eV
H2meV=H2eV*1000
R2eV= 27.2114/2. #Ry to eV


# Import data
folder="data-diffraction/"


# Quantum Data H
isotope="H"
Ein="0.050"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E005 = np.loadtxt(f,skiprows=0) 
Ein="0.100"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E010 = np.loadtxt(f,skiprows=0) 
Ein="0.300"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E030 = np.loadtxt(f,skiprows=0) 

# Quantum Data D
isotope="D"
Ein="0.050"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E005_D = np.loadtxt(f,skiprows=0) 
Ein="0.100"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E010_D = np.loadtxt(f,skiprows=0) 
Ein="0.300"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E030_D = np.loadtxt(f,skiprows=0) 

# Quantum Data T
isotope="T"
Ein="0.050"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E005_T = np.loadtxt(f,skiprows=0) 
Ein="0.100"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E010_T = np.loadtxt(f,skiprows=0) 
Ein="0.300"
data_file=folder+"diffraction-quantum-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffmctdh_E030_T = np.loadtxt(f,skiprows=0) 

# Classical Data H
isotope="H"
Ein="0.050"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E005 = np.loadtxt(f,skiprows=0) 
Ein="0.100"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E010 = np.loadtxt(f,skiprows=0) 
Ein="0.300"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E030 = np.loadtxt(f,skiprows=0) 

# Quantum Data D
isotope="D"
Ein="0.050"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E005_D = np.loadtxt(f,skiprows=0) 
Ein="0.100"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E010_D = np.loadtxt(f,skiprows=0) 
Ein="0.300"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E030_D = np.loadtxt(f,skiprows=0) 

# Quantum Data T
isotope="T"
Ein="0.050"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E005_T = np.loadtxt(f,skiprows=0) 
Ein="0.100"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E010_T = np.loadtxt(f,skiprows=0) 
Ein="0.300"
data_file=folder+"diffraction-classical-"+isotope+"-Ein"+Ein+"eV.dat"
with open(data_file) as f:
    diffclas_E030_T = np.loadtxt(f,skiprows=0) 


#Normalize the diffraction spectra
def normalize(v):
    norm = np.sum(v)  
    return v / norm
# Classical: normalize column 2 (index 2)

diffclas_E005[:,2] = normalize(diffclas_E005[:,2])
diffclas_E010[:,2] = normalize(diffclas_E010[:,2])
diffclas_E030[:,2] = normalize(diffclas_E030[:,2])

diffclas_E005_D[:,2] = normalize(diffclas_E005_D[:,2])
diffclas_E010_D[:,2] = normalize(diffclas_E010_D[:,2])
diffclas_E030_D[:,2] = normalize(diffclas_E030_D[:,2])

diffclas_E005_T[:,2] = normalize(diffclas_E005_T[:,2])
diffclas_E010_T[:,2] = normalize(diffclas_E010_T[:,2])
diffclas_E030_T[:,2] = normalize(diffclas_E030_T[:,2])


# MCTDH: normalize column 1 (index 1)

diffmctdh_E005[:,1] = normalize(diffmctdh_E005[:,1])
diffmctdh_E010[:,1] = normalize(diffmctdh_E010[:,1])
diffmctdh_E030[:,1] = normalize(diffmctdh_E030[:,1])

diffmctdh_E005_D[:,1] = normalize(diffmctdh_E005_D[:,1])
diffmctdh_E010_D[:,1] = normalize(diffmctdh_E010_D[:,1])
diffmctdh_E030_D[:,1] = normalize(diffmctdh_E030_D[:,1])

diffmctdh_E005_T[:,1] = normalize(diffmctdh_E005_T[:,1])
diffmctdh_E010_T[:,1] = normalize(diffmctdh_E010_T[:,1])
diffmctdh_E030_T[:,1] = normalize(diffmctdh_E030_T[:,1])
# === Style settings ===
lw = 3
ps = 200
ms = 4
ms2 = 15
fs = 24

# === Figure setup ===
fig, ax = plt.subplots(3, 3, figsize=(15, 12), sharey=False, constrained_layout=False)
fig.subplots_adjust(left=0.05, right=0.98, top=0.9, bottom=0.1, wspace=0, hspace=0)

for i in range(3):
    for j in range(3):
        # Make axes lines thicker
        for spine in ax[j, i].spines.values():
            spine.set_linewidth(2.5)   # try 2.5–3.5 for a poster

        # Make ticks thicker too
        ax[j, i].tick_params(
            direction='inout',
            which='major',
            length=8,
            width=2.5,
            top=True,
            right=True,
            labelsize=fs
        )

        # Optional: thicker minor ticks
        ax[j, i].tick_params(
            which='minor',
            length=4,
            width=2.0
        )

E1 = 50
E2 = 100
E3 = 300

ax[0, 0].set_title(r"$E_{\rm in}=$" + str(E1) + " meV", fontsize=fs * 1.2,pad=8)
ax[0, 1].set_title(r"$E_{\rm in}=$" + str(E2) + " meV", fontsize=fs * 1.2,pad=8)
ax[0, 2].set_title(r"$E_{\rm in}=$" + str(E3) + " meV", fontsize=fs * 1.2,pad=8)

# === Helper: function to plot paired bars with proportional width ===
def plot_pair(ax, x_class, y_class, x_quant, y_quant, xlim_val, label_class, label_quant):
    k_width = 0.010  # proportional width (same apparent width across panels)
    width = k_width * xlim_val
    offset = 0.010 * xlim_val  # 1% shift between classical and quantum bars
    ax.bar(x_class - offset / 2, y_class, color="ForestGreen", width=width, label=label_class,alpha=1.0)
    ax.bar(x_quant + offset / 2, y_quant, color="Red", width=width, label=label_quant,alpha=1.0)

# === E1 data (H, D, T) ===
xlim1 = 0.0012 * E1
plot_pair(ax[0, 0], diffclas_E005[:, 1] * H2eV, diffclas_E005[:, 2],
          diffmctdh_E005[:, 0] * H2eV, diffmctdh_E005[:, 1],
          xlim1, r"H - Quasi-classical", r"H - Quantum")

plot_pair(ax[1, 0], diffclas_E005_D[:, 1] * H2eV, diffclas_E005_D[:, 2],
          diffmctdh_E005_D[:, 0] * H2eV, diffmctdh_E005_D[:, 1],
          xlim1, r"D - Quasi-classical", r"D - Quantum")

plot_pair(ax[2, 0], diffclas_E005_T[:, 1] * H2eV, diffclas_E005_T[:, 2],
          diffmctdh_E005_T[:, 0] * H2eV, diffmctdh_E005_T[:, 1],
          xlim1, r"T - Quasi-classical", r"T - Quantum")

# === E2 data (H, D, T) ===
xlim2 = 0.0011 * E2
plot_pair(ax[0, 1], diffclas_E010[:, 1] * H2eV, diffclas_E010[:, 2],
          diffmctdh_E010[:, 0] * H2eV, diffmctdh_E010[:, 1],
          xlim2, r"H - Quasi-classical", r"H - Quantum")

plot_pair(ax[1, 1], diffclas_E010_D[:, 1] * H2eV, diffclas_E010_D[:, 2],
          diffmctdh_E010_D[:, 0] * H2eV, diffmctdh_E010_D[:, 1],
          xlim2, r"D - Quasi-classical", r"D - Quantum")

plot_pair(ax[2, 1], diffclas_E010_T[:, 1] * H2eV, diffclas_E010_T[:, 2],
          diffmctdh_E010_T[:, 0] * H2eV, diffmctdh_E010_T[:, 1],
          xlim2, r"T - Quasi-classical", r"T - Quantum")

# === E3 data (H, D, T) ===
xlim3 = 0.0011 * E3
plot_pair(ax[0, 2], diffclas_E030[:, 1] * H2eV, diffclas_E030[:, 2],
          diffmctdh_E030[:, 0] * H2eV, diffmctdh_E030[:, 1],
          xlim3, r"H - Quasi-classical", r"H - Quantum")

plot_pair(ax[1, 2], diffclas_E030_D[:, 1] * H2eV, diffclas_E030_D[:, 2],
          diffmctdh_E030_D[:, 0] * H2eV, diffmctdh_E030_D[:, 1],
          xlim3, r"D - Quasi-classical", r"D - Quantum")

plot_pair(ax[2, 2], diffclas_E030_T[:, 1] * H2eV, diffclas_E030_T[:, 2],
          diffmctdh_E030_T[:, 0] * H2eV, diffmctdh_E030_T[:, 1],
          xlim3, r"T - Quasi-classical", r"T - Quantum")


# Data  for E1, H, D, T
alphval=0.2
color1="tab:red"
color2="tab:green"
ax[0,0].plot(diffclas_E005[:,1]*H2eV,diffclas_E005[:,2],markersize=ms,marker="s", alpha=alphval, color=color2,
             linewidth=lw,label=r"H - Quasi-classical")
ax[1,0].plot(diffclas_E005_D[:,1]*H2eV,diffclas_E005_D[:,2],markersize=ms,marker="s",alpha=alphval, color=color2,
             linewidth=lw,label=r"D - Quasi-classical")
ax[2,0].plot(diffclas_E005_T[:,1]*H2eV,diffclas_E005_T[:,2],markersize=ms,marker="s",alpha=alphval,color=color2,
              linewidth=lw,label=r"T - Quasi-classical")

ax[0,0].plot(diffmctdh_E005[:,0]*H2eV,diffmctdh_E005[:,1],markersize=ms,marker="s",alpha=alphval, color=color1,
             linewidth=lw,label=r"H - Quantum")
ax[1,0].plot(diffmctdh_E005_D[:,0]*H2eV,diffmctdh_E005_D[:,1],markersize=ms,marker="s",alpha=alphval, color=color1,
             linewidth=lw,label=r"D - Quantum")
ax[2,0].plot(diffmctdh_E005_T[:,0]*H2eV,diffmctdh_E005_T[:,1],markersize=ms,marker="s",alpha=alphval, color=color1,
             linewidth=lw,label=r"T- Quantum")

# Data  for E2, H, D, T
ax[0,1].plot(diffclas_E010[:,1]*H2eV,diffclas_E010[:,2],markersize=ms,marker="s",alpha=alphval,color=color2,
             linewidth=lw,label=r"H - Quasi-classical")
ax[1,1].plot(diffclas_E010_D[:,1]*H2eV,diffclas_E010_D[:,2],markersize=ms,marker="s",alpha=alphval,color=color2,
             linewidth=lw,label=r"D - Quasi-classical")
ax[2,1].plot(diffclas_E010_T[:,1]*H2eV,diffclas_E010_T[:,2],markersize=ms,marker="s",alpha=alphval,color=color2,
              linewidth=lw,label=r"T - Quasi-classical")

ax[0,1].plot(diffmctdh_E010[:,0]*H2eV,diffmctdh_E010[:,1],markersize=ms,marker="s",alpha=alphval,color=color1,
             linewidth=lw,label=r"H - Quantum")
ax[1,1].plot(diffmctdh_E010_D[:,0]*H2eV,diffmctdh_E010_D[:,1],markersize=ms,marker="s",alpha=alphval,color=color1,
             linewidth=lw,label=r"D - Quantum")
ax[2,1].plot(diffmctdh_E010_T[:,0]*H2eV,diffmctdh_E010_T[:,1],markersize=ms,marker="s",alpha=alphval,color=color1,
             linewidth=lw,label=r"T - Quantum")

# Data  for E3, H, D, T
ax[0,2].plot(diffclas_E030[:,1]*H2eV,diffclas_E030[:,2],markersize=ms,marker="s",alpha=alphval,color=color2,
             linewidth=lw,label=r"H - Quasi-classical")
ax[1,2].plot(diffclas_E030_D[:,1]*H2eV,diffclas_E030_D[:,2],markersize=ms,marker="s",alpha=alphval,color=color2,
             linewidth=lw,label=r"D - Quasi-classical")
ax[2,2].plot(diffclas_E030_T[:,1]*H2eV,diffclas_E030_T[:,2],markersize=ms,marker="s",alpha=alphval,color=color2,
              linewidth=lw,label=r"T - Quasi-classical")

ax[0,2].plot(diffmctdh_E030[:,0]*H2eV,diffmctdh_E030[:,1],markersize=ms,marker="s",alpha=alphval,color=color1,
             linewidth=lw,label=r"H - Quantum")
ax[1,2].plot(diffmctdh_E030_D[:,0]*H2eV,diffmctdh_E030_D[:,1],markersize=ms,marker="s",alpha=alphval,color=color1,
             linewidth=lw,label=r"D - Quantum")
ax[2,2].plot(diffmctdh_E030_T[:,0]*H2eV,diffmctdh_E030_T[:,1],markersize=ms,marker="s",alpha=alphval,color=color1,
             linewidth=lw,label=r"T - Quantum")


# === Axis settings ===
for j in range(0, 2):
    ax[j, 0].tick_params(left=True, labelleft=True, labelbottom=False, right=True, top=True, labelsize=fs)
    ax[j, 1].tick_params(left=True, labelleft=False, labelbottom=False, right=True, top=True, labelsize=fs)
    ax[j, 2].tick_params(left=True, labelleft=False, labelbottom=False, right=True, top=True, labelsize=fs)

ax[2, 0].tick_params(left=True, labelleft=True, right=True, top=True, labelsize=fs)
ax[2, 1].tick_params(left=True, labelleft=False, right=True, top=True, labelsize=fs)
ax[2, 2].tick_params(left=True, labelleft=False, right=True, top=True, labelsize=fs)

ax[1, 0].set_ylabel(r"scattering probability", fontsize=fs)

# === Vertical lines, limits, and labels ===
for j in range(3):
    ax[j, 0].axvline(x=E1 / 1000, color='b')
    ax[j, 1].axvline(x=E2 / 1000, color='b')
    ax[j, 2].axvline(x=E3 / 1000, color='b')

    ax[j, 0].set_xlim(-0.001,0.0695)
    ax[j, 1].set_xlim(-0.002, 0.112)
    ax[j, 2].set_xlim(-0.003, 0.33)

    for i in range(3):
        ax[2, j].set_xlabel(r"$E_{\rm XY}$ (eV)", fontsize=fs)



locy=0.57
locx1=0.061
locx2=0.099
locx3=0.299
ax[0,0].annotate('(a)', xy=(0., 0.), xytext=(locx1, locy),size=fs)
ax[0,1].annotate('(b)', xy=(0, 0.), xytext=(locx2,locy),size=fs)
ax[0,2].annotate('(c)', xy=(0, 0.), xytext=(locx3, locy),size=fs)
#locy=0.53
ax[1,0].annotate('(d)', xy=(0., 0.), xytext=(locx1, locy),size=fs)
ax[1,1].annotate('(e)', xy=(0, 0.), xytext=(locx2,locy),size=fs)
ax[1,2].annotate('(f)', xy=(0, 0.), xytext=(locx3, locy),size=fs)
#locy=0.48
ax[2,0].annotate('(g)', xy=(0., 0.), xytext=(locx1, locy),size=fs)
ax[2,1].annotate('(h)', xy=(0, 0.), xytext=(locx2,locy),size=fs)
ax[2,2].annotate('(i)', xy=(0, 0.), xytext=(locx3, locy),size=fs)


plt.subplots_adjust(
    top=0.93,     # remove blank space above top plot
    bottom=0.12,
    left=0.06,
    right=0.99,   # leave room for colorbar
    hspace=0.,  # tighten vertical gap
    wspace=0.02
)
formatter = ticker.FormatStrFormatter('%.2f')

dtick1=0.02
dtick2=0.03
dtick3=0.10
tick1=0.00
tick2=0.00
tick3=0.00

for i in range(3):
    for j in range(3):
        ax[j,i].tick_params(
            direction='inout',
            which='major',
            length=6,
            width=1.5,
            top=True,
            labelsize=fs
        )

        ax[j,i].xaxis.set_major_formatter(formatter)
        ax[j,i].yaxis.set_major_formatter(formatter)
    ax[i, 0].set_xticks(np.arange(tick1/2, 0.079, dtick1))
    ax[i, 1].set_xticks(np.arange(tick2, 0.119, dtick2))
    ax[i, 2].set_xticks(np.arange(tick3, 0.32, dtick3))
# === Y-limits and legends ===
for j in range(3):
    ax[0,j].set_ylim(0, 0.68)
    ax[1,j].set_ylim(0, 0.68)
    ax[2,j].set_ylim(0, 0.68)
    # ax[j, 0].legend(fontsize=fs, frameon=False)
fig.subplots_adjust(left=0.07, right=0.99, top=0.9, bottom=0.12, wspace=0.05, hspace=0.0)
# === Save and show ===



plt.savefig('diffraction-classical-quantum-isotopes-barsandlines.pdf')
plt.show()

