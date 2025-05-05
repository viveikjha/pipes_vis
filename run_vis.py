import pipes_vis as v
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
delayed = {}
delayed["massformed"] = 10.0                 # total log_10(M*/M_sun) of the galaxy, for the whole SFH
delayed["metallicity"] = 1.0                 # assumed constant metallicity, in number of times of Z_sun
delayed["tform"] = 3                         # age of universe when the population formed, Gyr
delayed["tau"] = 2                           # SFR decay timescale of the population, Gyr

init_components = {}
init_components["redshift"] = 0.04           # redshift at observation
init_components["delayed"] = delayed 
init_components["spec_lim"] = [3000,10000]   # wavelength boundaries of the main spectrum panel


# First plot
# simple_vis = v.visualizer(init_components)
# fig, axes = simple_vis.static_plot()
# plt.show()
# simple_vis = v.visualizer(init_components)
# simple_vis.GUI()
# plt.show()

def load_phot(ID):
    data = pd.read_csv('example_data/example_photometry_lowz.csv')

    # HST photometry in mujy
    flux_cols = ["f435w","f606w","f814w"]

    err_cols = [col + "_err" for col in flux_cols]

    photometry = np.c_[data.loc[0, flux_cols],
                       data.loc[0, err_cols]]

    return photometry

# get photometry filter list
filt_list = open("filters/filt_list.txt", 'r').read().split('\n')[:-1]

# simple_vis2 = v.visualizer(init_components, load_data_func=load_phot, spec_units='ergscma', phot_units='mujy', 
#                            spectrum_exists=False, photometry_exists=True, filt_list=filt_list)

# simple_vis2.GUI()
# plt.show()

burst1 = {}
burst1["massformed"] = 9                     # total log_10(M*/M_sun) of the galaxy, for the whole SFH
burst1["metallicity"] = 1.0                  # assumed constant metallicity, in number of times of Z_sun
burst1["tform"] = 2                          # age of universe when the burst happened, Gyr

burst2 = {}                                  # a second burst
burst2["massformed"] = 8.8                   # total log_10(M*/M_sun) of the galaxy, for the whole SFH
burst2["metallicity"] = 1.0                  # assumed constant metallicity, in number of times of Z_sun
burst2["tform"] = 5                          # age of universe when the burst happened, Gyr

delayed = {}
delayed["massformed"] = 10.5                 # total log_10(M*/M_sun) of the galaxy, for the whole SFH
delayed["metallicity"] = 1.0                 # assumed constant metallicity, in number of times of Z_sun
delayed["tform"] = 6                         # age of universe when the population formed, Gyr
delayed["tau"] = 1                           # SFR decay timescale of the population, Gyr

psb_wild2020 = {}                            # 2-part PSB SFH, older=exponential, younger=double power law
psb_wild2020["massformed"] = 10              # total log_10(M*/M_sun) of the galaxy, for the whole SFH
psb_wild2020["metallicity"] = 1.0            # assumed constant metallicity, in number of times of Z_sun
psb_wild2020["massformed_lims"] = [7,15]
psb_wild2020["told"] = 4                     # age of universe when the older population formed, Gyr
psb_wild2020["tau"] = 1.                     # SFR decay timescale of the older population, Gyr
psb_wild2020["tburst"] = 12                  # age of universe when the starburst happened, Gyr
psb_wild2020["alpha"] = 100                  # decline steepness of the burst, index of double power law
psb_wild2020["beta"] = 100                   # incline steepness of the burst, index of double power law
psb_wild2020["fburst"] = 0.5                 # fraction of mass formed in the burst (vs the older population)

dust = {}                                    # dust attenuation and emission, implementation identical to bagpipes
dust["type"] = "CF00"                        # Charlot & Fall (2001)
dust["eta"] = 2.0                            # additional scaling factor for dust in birth clouds (1/mu)
dust["Av"] = 1.0                             # extinction in V band (5500AA)
dust["n"] = 0.7                              # slope of the attenuation law

nebular = {}                                 # nebular emission, implementation identical to bagpipes
nebular["logU"] = -3                         # Log_10 of the ionization parameter.

init_components = {}
init_components["redshift"] = 0.04           # redshift at observation
init_components["redshift_lims"] = [0,10]
init_components["burst1"] = burst1
init_components["burst2"] = burst2
init_components["delayed"] = delayed
init_components["psb_wild2020"] = psb_wild2020
init_components["dust"] = dust
init_components["nebular"] = nebular
init_components["t_bc"] = 0.01               # duration that the birth clouds hang around, Gyr
init_components["veldisp"] = 0               # velocity dispersion, km/s
init_components["spec_lim"] = [3000,10000]   # wavelength boundaries of the main spectrum panel

complex_vis = v.visualizer(init_components, load_data_func=load_phot, spec_units='ergscma', phot_units='mujy', 
                           spectrum_exists=False, photometry_exists=True, filt_list=filt_list)
complex_vis.GUI()

plt.show()