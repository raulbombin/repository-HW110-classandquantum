import numpy as np
import matplotlib.pyplot as plt
import pathlib

# This script pltos the absorption curve for  HYDROGEN

# Functions for plotting sticking
def read_sticking(folder,ener):
    file1=folder+"flux-abs-H-"+ener+"eV.dat"
    with open(file1) as f:
        absorp = np.loadtxt(f,skiprows=0)  
    return  absorp

def plot_ref_abs(ini,fin,ener):
    flux_abs=read_sticking(folder,ener)
    plt.plot(flux_abs[ini:fin,0],flux_abs[ini:fin,3],markersize=psize, linewidth=lw ,marker ="^",color="blue")
    plt.plot(flux_abs[ini:fin,0],1.-flux_abs[ini:fin,3],markersize=psize, linewidth=lw ,marker ="^",color="green")


# Data folder
folder="data-PabssvsEin-H/"
#Import classical probabilities


data_file=folder+"Pabs_vs_Ein_classical.dat"
with open(data_file) as f:
    prob_class = np.loadtxt(f,skiprows=0)

# Normalize probabilities to one
prob_class[:,1:4]=prob_class[:,1:4]/100.


# Import Quantum probability 

psize=0
lw=1.5
fs=18

plt.figure(figsize=(6.47,4))

ener="0.010"
ini=1
fin=-1
plot_ref_abs(ini,fin,ener)


ener="0.025"
ini=1
fin=-1
plot_ref_abs(ini,fin,ener)


ener="0.050"
ini=100
fin=-50
plot_ref_abs(ini,fin,ener)

ener="0.0625"
ini=50
fin=-200
plot_ref_abs(ini,fin,ener)

ener="0.075"
ini=120
fin=-120
plot_ref_abs(ini,fin,ener)

ener="0.087"
ini=100
fin=-75
plot_ref_abs(ini,fin,ener)

ener="0.10"
ini=150
fin=-160
plot_ref_abs(ini,fin,ener)

ener="0.15"
ini=59
fin=-160
plot_ref_abs(ini,fin,ener)

ener="0.182"
ini=110
fin=-160
plot_ref_abs(ini,fin,ener)

ener="0.225"
ini=100
fin=-140
plot_ref_abs(ini,fin,ener)

ener="0.265"
ini=120
fin=-140
plot_ref_abs(ini,fin,ener)

ener="0.30"
ini=190
fin=-125
plot_ref_abs(ini,fin,ener)

ener="0.375"
ini=165
fin=-120
plot_ref_abs(ini,fin,ener)

ener="0.45"
ini=165
fin=-100
plot_ref_abs(ini,fin,ener)

ener="0.525"
ini=145
fin=-130
plot_ref_abs(ini,fin,ener)

ener="0.60"
ini=100
fin=-180
plot_ref_abs(ini,fin,ener)

ener="0.70"
ini=150
fin=-120
plot_ref_abs(ini,fin,ener)

ener="0.80"
ini=150
fin=-100
plot_ref_abs(ini,fin,ener)

ener="0.90"
ini=150
fin=-100
plot_ref_abs(ini,fin,ener)

ener="1.00"
ini=100
fin=-120
plot_ref_abs(ini,fin,ener)

ener="1.10"
ini=100
fin=-1
plot_ref_abs(ini,fin,ener)

plt.plot(prob_class[:,0], prob_class[:,1],linewidth=2*lw, markersize=0, linestyle="dashed",marker="o",color="darkblue",label="Sticking")
plt.plot(prob_class[:,0], prob_class[:,2], linewidth=2*lw,markersize=0, linestyle="dotted",marker="o",color="darkgreen",label="Reflection")


plt.xscale("log")
# plt.yscale("log")
plt.xlim(0.010,1.2)
plt.ylim(0.00,1.0)
# plt.legend(loc="best",fontsize=fs)
plt.tight_layout()
plt.tick_params(axis='both',which='both',direction='inout',top=True,bottom=True,left=True,right=True,width=1.5,size=3)
plt.ylabel("Probability", fontsize=fs)
plt.xlabel(r"$E_{\rm in}$ (eV)", fontsize=fs)
plt.xticks(size=fs)
plt.yticks(size=fs)
plt.tight_layout()

plt.tight_layout()
plt.savefig('stick-H-vs-ener.pdf')
plt.show()


