import numpy as np
import matplotlib.pyplot as plt

# Let's plot quantumd sticking vs time
lw=1
lw2=1
ps=200
ms=1
ms2=5
fs=16

nmarkers=40
nmarkers2=10

# Import data

def read_stick_vs_time(folder,isotope,Ener):
    file1=folder+"Pref-quantum-"+isotope+"-Ein"+Ener+"eV.dat"
    with open(file1) as f:
        reflex = np.loadtxt(f,skiprows=0)
    reflex[:,0]=reflex[:,0]*0.001 #time to ps
    return reflex

def read_stick_vs_time_classical(folder,isotope,Ener):
    # Open files
    file1=folder+"Pref-classical-"+isotope+"-Ein"+Ener+"eV.dat"
    with open(file1) as f:
        prop = np.loadtxt(f,skiprows=0)
    prop[:,2:5]=prop[:,2:5]/100. # change percentages to propbabilities
    prop[:,0]=prop[:,0] # time in ps
    return prop

# Read data
folder="data-Prefvstime/"
# Read Quantum data

isotope="H"
Ener="0.050"
reflexE005 = read_stick_vs_time(folder,isotope,Ener)
Ener="0.800"
reflexE080 = read_stick_vs_time(folder,isotope,Ener)

isotope="D"
Ener="0.050"
reflexE005D = read_stick_vs_time(folder,isotope,Ener)
Ener="0.800"
reflexE080D = read_stick_vs_time(folder,isotope,Ener)


isotope="T"
Ener="0.050"
reflexE005T = read_stick_vs_time(folder,isotope,Ener)
Ener="0.800"
reflexE080T = read_stick_vs_time(folder,isotope,Ener)

# Read classical data  data

isotope="H"
Ener="0.050"
stickclasE005 = read_stick_vs_time_classical(folder,isotope,Ener)
Ener="0.800"
stickclasE080 = read_stick_vs_time_classical(folder,isotope,Ener)


isotope="D"
Ener="0.050"
stickclasE005D = read_stick_vs_time_classical(folder,isotope,Ener)
Ener="0.800"
stickclasE080D = read_stick_vs_time_classical(folder,isotope,Ener)


isotope="T"
Ener="0.050"
stickclasE005T = read_stick_vs_time_classical(folder,isotope,Ener)
Ener="0.800"
stickclasE080T = read_stick_vs_time_classical(folder,isotope,Ener)


# classical calculations start at 7 anstrons from the surface
# mctdh ones at 4.5 angstrons .--> shift time = distance /v (potential --> 0 at these distances)


# Constants
eV = 1.602176634e-19      # J
angstrom = 1e-10          # m
amu = 1.66053906660e-27   # kg

# Masses (atomic mass units)
masses_amu = {
    "H": 1.00784,
    "D": 2.01410,
    "T": 3.01605
}


def flight_times(E_meV, distance_angstrom=2.5):
    """
    Compute the flight time over a given distance.

    Parameters
    ----------
    E_meV : float
        Incident kinetic Energy in meV.
    distance_angstrom : float, optional
        Travel distance in Å (default = 2.5 Å).

    Returns
    -------
    tH, tD, tT : float
        Flight times (ps) for H, D and T.
    """

    E = E_meV * 1e-3 * eV
    distance = distance_angstrom * angstrom

    times = []

    for isotope in ("H", "D", "T"):
        m = masses_amu[isotope] * amu
        v = np.sqrt(2 * E / m)
        t = distance / v * 1e12   # ps
        times.append(t)

    return tuple(times)

# factor of two below is because it arrives to the surface and comes back
#times for 50 meV
tH1, tD1, tT1 = flight_times(50)

tH1=tH1*2
tD1=tD1*2
tT1=tT1*2

#times for 800 meV

tH2, tD2, tT2 = flight_times(800)
tH2=tH2*2
tD2=tD2*2
tT2=tT2*2


fig, ax = plt.subplots(1,2,figsize=(6, 3.7),sharey=True)
fig.subplots_adjust(wspace=0.0,hspace=0.0)


color1="ForestGreen"
color2="darkblue"
color3="red"
color4="darkblue"


E1 = 50
E2 = 800

ax[0].set_title(r"$E_{\rm in}=$" + str(E1) + " meV", fontsize=fs * 1.)
ax[1].set_title(r"$E_{\rm in}=$" + str(E2) + " meV", fontsize=fs * 1.)




# Quantum results

# Hydrogen
ax[0].plot(reflexE005[:,0]+tH1,reflexE005[:,1],markersize=ms2,markevery=nmarkers,marker="o",linewidth=lw2,color=color3,linestyle="dashed",label="H - Reflection")
ax[1].plot(reflexE080[:,0]+tH2,reflexE080[:,1],markersize=ms2,markevery=nmarkers2,marker="o",linewidth=lw2,color=color3,linestyle="dashed",label="H - Reflection")#

#Deuterium
ax[0].plot((reflexE005D[:,0]+tD1)/np.sqrt(2.),reflexE005D[:,1],markersize=ms2,markevery=nmarkers,marker="^",linewidth=lw2,color=color3,linestyle="dashed",label="D - Reflection")
ax[1].plot((reflexE080D[:,0]+tD2)/np.sqrt(2.),reflexE080D[:,1],markersize=ms2,markevery=nmarkers2,marker="^",linewidth=lw2,color=color3,linestyle="dashed",label="D - Reflection" )

#Tritium
ax[0].plot((reflexE005T[:,0]+tT1)/np.sqrt(3.),reflexE005T[:,1],markersize=ms2,markevery=nmarkers,marker="s",linewidth=lw2,color=color3,linestyle="dashed",label="T - Reflection")
ax[1].plot((reflexE080T[:,0]+tT2)/np.sqrt(3.),reflexE080T[:,1],markersize=ms2,markevery=nmarkers2,marker="s",linewidth=lw2,color=color3,linestyle="dashed",label="T - Reflection")



# Classical results
mscl=5
lwcl=0

ax[0].plot(stickclasE005[:,0],stickclasE005[:,4],markersize=mscl,marker="o",linewidth=lwcl,color=color1,label="Classical")
ax[1].plot(stickclasE080[:,0],stickclasE080[:,4],markersize=mscl,marker="o",linewidth=lwcl,color=color1,label="")
ax[0].plot(stickclasE005D[:,0]/np.sqrt(2.),stickclasE005D[:,4],markersize=mscl,marker="^",linewidth=lwcl,color=color1,label="Classical")
ax[1].plot(stickclasE080D[:,0]/np.sqrt(2.),stickclasE080D[:,4],markersize=mscl,marker="^",linewidth=lwcl,color=color1,label="")
ax[0].plot(stickclasE005T[:,0]/np.sqrt(3.),stickclasE005T[:,4],markersize=mscl,marker="s",linewidth=lwcl,color=color1,label="Classical")
ax[1].plot(stickclasE080T[:,0]/np.sqrt(3.),stickclasE080T[:,4],markersize=mscl,marker="s",linewidth=lwcl,color=color1,label="")

ax[0].set_ylabel(r"$P_{\rm ref}$",fontsize=fs)
ax[0].tick_params(left = True, labelleft=True, right=True, top=True,labelsize=fs)
ax[1].tick_params(left = True, labelleft=False,right=True, top=True,labelsize=fs)
for j in range(2):
    ax[j].set_xlabel(r"$\tau (ps)$",fontsize=fs)
    ax[j].set_ylim(0,1.0)
ax[0].set_xlim(0,3)
ax[1].set_xlim(0,1.0)

ax[0].annotate('(a)', xy=(0.1,0.92),size=fs)
ax[1].annotate('(b)', xy=(0.02,0.92),size=fs)
fig.tight_layout()


plt.savefig('sticking-vs-time.pdf')
plt.show()
