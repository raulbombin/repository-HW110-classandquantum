import numpy as np
import matplotlib.pyplot as plt
import pathlib

#Import WF's
folder="data-WFs/"

data_file=folder+"WF00"
with open(data_file) as f:
    WF00 = np.loadtxt(f,skiprows=0)  
    
data_file=folder+"WF01"
with open(data_file) as f:
    WF01 = np.loadtxt(f,skiprows=0)  
    
data_file=folder+"WF02"
with open(data_file) as f:
    WF02 = np.loadtxt(f,skiprows=0)  
    
data_file=folder+"WF03"
with open(data_file) as f:
    WF03 = np.loadtxt(f,skiprows=0)  

data_file=folder+"WF04"
with open(data_file) as f:
    WF04 = np.loadtxt(f,skiprows=0)  
    
data_file=folder+"WF05"
with open(data_file) as f:
    WF05 = np.loadtxt(f,skiprows=0)  
    
data_file=folder+"WF06"
with open(data_file) as f:
    WF06 = np.loadtxt(f,skiprows=0)  

size = 16
bohr2angs = 0.529177

WFs = [WF00, WF01, WF02, WF03, WF04, WF05]

panel_labels = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]

# Global contour scale
# zmin = min(np.min(WF[:,2]) for WF in WFs)
# zmax = max(np.max(WF[:,2]) for WF in WFs)
zmin=-0.05
zmax=0.5

levels = np.linspace(zmin, zmax, 30)

# Fixed ticks you requested
cticks = np.arange(0, zmax, 0.1)

fig, axes = plt.subplots(
    2, 3,
    sharex=True,
    sharey=True
)

axes = axes.flatten()

for i, (ax, WF) in enumerate(zip(axes, WFs)):

    x = WF[:,0] * bohr2angs
    y = WF[:,1] * bohr2angs
    z = WF[:,2]

    cntr = ax.tricontourf(x, y, z, levels=levels,cmap="Reds",
                          vmin=zmin,     
                          vmax=zmax )     

    ax.set_aspect('equal', adjustable='box')

    ax.set_xlim(0, 5.99 * bohr2angs)
    ax.set_ylim(0, 8.47 * bohr2angs)
    ax.tick_params(labelsize=size)

    # Y labels only first column
    if i % 3 == 0:
        ax.set_ylabel(r"$\bar{y}$ (a.u)", size=size)

    # X labels only bottom row
    if i >= 3:
        ax.set_xlabel(r"$\bar{x}$ (a.u)", size=size)

    # Corner markers
    WcoordX = [0, 5.99*bohr2angs, 0, 5.99*bohr2angs, 5.99/2*bohr2angs]
    WcoordY = [0, 0, 8.47*bohr2angs, 8.47*bohr2angs, 8.47/2*bohr2angs]
    ax.scatter(WcoordX, WcoordY, color="gray", s=1200)
    
    ax.text(
    0.09, 0.96,                # position (x,y) in axes coords
    panel_labels[i],
    transform=ax.transAxes,    
    fontsize=size,
    #fontweight='bold',
    va='top'
)

#  ONE shared colorbar on LEFT spanning rows
cbar = fig.colorbar(
    cntr,
    ax=axes,
    ticks=cticks,
    location='right',   
    shrink=0.9,        
    aspect=30
)
#  Manually move it
cbar.ax.set_position([0.93, 0.250, 0.2, 0.5])
cbar.ax.tick_params(labelsize=0.8 * size)

plt.subplots_adjust(
    hspace=0.0,
    wspace=0.0
)

plt.tight_layout()
plt.show()
fig.savefig("WF_multiplot.pdf")
