import matplotlib.pyplot as plt
import numpy as np

def MantlePlot( rho_sil_kgm3 , R_sil_m , C2inds , Planet:dict , nTbs , wo , saveStr , lw = 1 , show=True):
    """
        Shows and saves a plot of density vs. radius in the mantle
        as implemented in PlanetProfile.m line ~1050 (as of 06/25/2021)

        Parameters:
        -----------
        rho_sil_kgm3 : 2d float numpy array of size (n,m,)
            densities of mantle [kg/m^3]
        R_sil_m : 2d float numpy array of size (n,m,)
            radii in mantle [m]
        C2inds : 2d numpy array of integers of size (n,p)
            chooses indices used for display in plot
        Planet : dictionary with keys Tb_K,Cmeasured, and Cuncerainty
            Planet["Tb_K"] : float list
                temperatures model is being made at
            Planet["Cmeasured"] : float
                moment of inetria about polar axis, normalized to MR^2
            Planet["Cuncertainty"] : float
                uncertainty in 'Cmeasured'
        nTbs : int = n
            number of temperature profiles = n (length of Tb_K)
        wo : float
            percent concentration of salt in ocean
        lw : float (optional)
            width of lines in plot
    """

    Tb_K = Planet["Tb_K"]
    Cmeasured = Planet["Cmeasured"]
    Cuncertainty = Planet["Cuncertainty"]

    # technically, C2inds should have values subtracted by 1
    # due to difference in MATLAB and python indexing
    lstr_3 = []
    for iT in range(0,nTbs):
        plt.plot(rho_sil_kgm3[iT][C2inds[iT]] , R_sil_m[iT][C2inds[iT]]*1e-3 , linewidth = lw)
        lstr_3.append( f"$T_{{b}}$: {Tb_K[iT]:0.1f} K" )

    plt.legend(lstr_3)

    plt.xlabel("$\\rho_{\\mathrm{sil}} \\, (\\mathrm{kg} \\, \\mathrm{m}^{-3}$)")
    plt.ylabel("$R_{\\mathrm{sil}} \\, (\\mathrm{km})$")
    plt.title(f"No Fe core ; $C/MR^2 = {Cmeasured} \\pm {Cuncertainty}$ ; $ W = {wo} \\, wt \\%$ ")

    plt.savefig(saveStr)

    if show:
        plt.show()