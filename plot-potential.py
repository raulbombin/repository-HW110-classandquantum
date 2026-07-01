import numpy as np
import matplotlib.pyplot as plt
import pathlib

from matplotlib.ticker import FixedLocator

def read_Zcuts(folder,position):
    # Open files
    file1=folder+"cutZ-"+position
    with open(file1) as f:
        cut = np.loadtxt(f,skiprows=0)

    return cut

def read_XYcuts(folder,position):
    # Open files
    file1=folder+"cutXY-"+position+".xyz"
    with open(file1) as f:
        cut = np.loadtxt(f,skiprows=0)
    return cut

def gauss(z):
    z0=4.5
    sigma=0.2
    return np.exp(-((z-z0)/(2*sigma))**2)
# Plot of Z cuts at top, hollow, L-bridge, S-brige, position minima at Z=Ztop well

ab2ang = 0.529177
angs2ab=1./0.52917725

lw2=1.5

# Read also MEP file
folder = "data-potfitcuts/"
file="MEP.dat"
file1=folder+file
with open(file1) as f:
    MEP = np.loadtxt(f,skiprows=0)
MEP[:,0:3]=MEP[:,0:3]*angs2ab 


folder = "data-potfitcuts/"
# positions can be hollow, top, LB, SB

position = "top"
cutZtop = read_Zcuts(folder, position)

position = "hollow"
cutZhollow = read_Zcuts(folder, position)

position = "SB"
cutZSB = read_Zcuts(folder, position)

position = "LB"
cutZLB = read_Zcuts(folder, position)





fs = 14

fig, axes = plt.subplots(2, 1, figsize=(5,5.5), sharex=False)

ax_top, ax_bot = axes



# =========================
# (a) LEFT: Z-cuts line plot
# =========================
ax = ax_bot

axes[0].set_aspect(0.75, adjustable='box')

ax.plot(cutZhollow[:,0]*ab2ang, cutZhollow[:,1], color="blue",  label="Hollow")
ax.plot(cutZSB[:,0]*ab2ang,     cutZSB[:,1],     color="orange", label="Short Bridge")
ax.plot(cutZLB[:,0]*ab2ang,     cutZLB[:,1],     color="black", label="Long Bridge")
ax.plot(cutZtop[:,0]*ab2ang,    cutZtop[:,1],    color="red",   label="Top")
ax.plot(MEP[:,2]*ab2ang,MEP[:,3] ,linewidth=lw2*1.5,color="Black",linestyle="dotted", label="Minimum-Energy-Path")

ax.set_xlabel(r"$\bar{z} (\mathrm{\AA})$", fontsize=fs)
ax.set_ylabel("Potential (eV)", fontsize=fs)
ax.tick_params(labelsize=fs)

ax.set_xlim(-8*ab2ang, 10*ab2ang)
ax.set_ylim(-3.2, 2)

# Gaussian
x = np.linspace(3.5, 8, 200)
y = gauss(x)
ax.plot(x, y)
ax.fill_between(x, y, color="b", alpha=0.8)

ax.arrow(4.1, 0.6, -1, 0,
         head_width=0.08, head_length=0.2,
         fc='k', ec='k')

ax.annotate("k", xy=(8, 1.2), xytext=(7.3, 1.5), fontsize=15)

#ax.grid()
ax.legend(loc=(0.08,0),fontsize=0.58*fs,frameon=False)

ax.text(0.018, 0.98, "(b)", transform=ax.transAxes,
        fontsize=fs, va="top")


# ===============================
# (b) RIGHT: XY tricontourf plot
# ===============================
ax = ax_top
#ax.set_aspect('equal', adjustable='datalim')
ax.set_aspect('equal', adjustable='box')



position = "Z1.959"
cutXYtop = read_XYcuts(folder, position)

theta = 54.11
X = cutXYtop[:, 0] + cutXYtop[:, 1]*np.cos(theta*2*np.pi/360.)
Y = cutXYtop[:, 1]*np.sin(theta*2*np.pi/360.)
Z = cutXYtop[:, 2]

# convert to Å
X *= ab2ang
Y *= ab2ang


# Explicit limits (example – adapt to your data)
ax.set_xlim(X.min(), X.max())
ax.set_ylim(Y.min(), Y.max())

#ax.set_aspect('equal')

tcf = ax.tricontourf(X, Y, Z, 20, cmap='RdGy')

ax.set_xlabel(r"$\bar{x} (\mathrm{\AA}$)", fontsize=fs)
ax.set_ylabel(r"$\bar{y} (\mathrm{\AA}$)", fontsize=fs)
ax.tick_params(labelsize=fs)
ax.yaxis.set_major_locator(FixedLocator([0, 1, 2]))

# ---- COLORBAR (figure-level, right, thin) ----
bbox = ax.get_position()   # position of right plot in figure coords

cax = fig.add_axes([
    bbox.x1 + -0.13,        # a bit to the right of the plot
    bbox.y0 + 0.30*bbox.height,
    0.015,                  # thin bar
    0.5*bbox.height        # shorter than plot
])

cbar = fig.colorbar(tcf, cax=cax)
cbar.set_label("Potential (eV)", fontsize=0.5*fs)
cbar.ax.tick_params(labelsize=0.55*fs)
cbar.ax.yaxis.set_major_locator(FixedLocator([-3,-1, 1, 3, 5]))



# Site labels


# Add label inside the circle
ax.annotate("T", color="Cyan",
    fontsize=12,fontweight="bold",
    xy=(0,0),
    xytext=(9, 5),       # pixels
    textcoords='offset points',
    ha='center',
    va='center')

ax.annotate("H", color="Cyan",
    fontsize=12,fontweight="bold",
    xy=(1.58,0.62),
    xytext=(0,0),       # pixels
    textcoords='offset points',
    ha='center',
    va='center')

ax.annotate("LB", color="Cyan",
    fontsize=12,fontweight="bold",
    xy=(1.6,0.0),
    xytext=(0,5),       # pixels
    textcoords='offset points',
    ha='center',
    va='center')

ax.annotate("SB", color="Cyan",
    fontsize=12,fontweight="bold",
    xy=(0.85,0.9),
    xytext=(0,5),       # pixels
    textcoords='offset points',
    ha='center',
    va='center')


ax.text(0.018, 0.98, "(a)", transform=ax.transAxes,
        fontsize=fs, va="top")
plt.subplots_adjust(
    top=1.00,     # remove blank space above top plot
    bottom=0.11,
    left=0.14,
    right=0.88,   # leave room for colorbar
    hspace=0.15   # tighten vertical gap
)
plt.savefig("potZcuts_XYcuts.pdf")
plt.show()
print(np.min(cutZhollow[:,1]))
