---
title: "TauREx Parameter Files"
permalink: /software/taurex/paramterfile
last_modified_at: 2018-08-05
toc: true
toc_sticky: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

The parameter file is the main way of running TauREx. Two parameter files exist

- `default.par`, found in `Parfiles` folder
- a custom user-defined file

The `default.par` sets all parameter defaults of the code and should not be touched.  
The user-defined file will only include the parameters that differ from the default and is hence much smaller and easier to use.

Examples of user-defined parameter files can be found at:

Type | TauREx directory
--- | ---
Retrieval | `tests/test_0_transmission/test_retrieval.par` `tests/test_0_emission/test_retrieval.par`
Forward model only | `tests/test_0_transmission/test_fm.par` `tests/test_0_emission/test_fm.par`

### Essentials

In the tables below, we will outline the essential parameters (you will find more with explanations in `default.par`). The parameters are grouped into classes, e.g. `[General]` or `[Planet]`, `[Atmosphere]`, etc. Classes must be respected, otherwise parameters will not be recognised by TauREx.
Some parameters will only be used by the forward model generator `create_spectrum.py` whilst some will only be used during the retrieval by `taurex.py`, we denote these with FM and R usage tags respectively in the following sections.

### General

`[General]` handles the general setup parameters.

Parameter | Value | Explanation | Usage (FM/R only)
--- | --- | --- | ---
verbose | True/False | verbose or not |
type | transmission/emission | transmission or emission forward/retrieval model  |
ace | True/False | equilibrium chemistry mode |
manual_waverange | True/False | Sets a manual wavelength range | FM
wavemin | float | minimum wavelength in microns if manual_waverange = True | FM
wavemax | float | maximum wavelength in microns if manual_waverange = True | FM
lightcurve_fitting | True/False | Retrieves on lightcurves (not yet supported) |


### Input

`[Input]` handles all file and data input paths.

Parameter | Value | Explanation | Usage (FM/R only)
--- | --- | --- | ---
spectrum_file | PATH / False | Observed spectrum to be fitted (Format: wavelength (micron), (Rp/R*)^2, error[, bin width (micron)]) | R
opacity_method | xsec_sampled/xsec_highres/ktables | Opacity method, absorption cross-sections or correlated k-coefficients |
xsec_path | PATH | path to cross section folder |
ktab_path | PATH | path to ktable folder |
cia_path | PATH | path to collision induced absorption coefficients |
mie_path | PATH | path to Mie scattering coefficients |
star_path | PATH | path to Phoenix stellar models |


### Output

`[Output]` handles the output paths.

[Output]

Parameter | Value | Explanation | Usage (FM/R only)
--- | --- | --- | ---
path | PATH | main output path where forward models and retrievals will be saved |
sigma_spectrum | True/False | calculates in post-processing the uncertainty bound on the best-fit spectrum | R
sigma_spectrum_frac | float | fraction of total samples from which to calculate the one sigma spectrum (default = 0.1) | R


### Star

`[Star]` handles the stellar parameters.

Parameter | Value | Unit| Explanation | Usage (FM/R only)
--- | --- | --- | --- | ---
radius | float |R<sub>sun</sub> | Stellar radius |
temp | float | K | Stellar temperature |
use_blackbody | True/False | | Uses blackbody instead of Phoenix spectra (default = False) |
unocculted_spots | True/False || Models the effect of unocculted star spots and faculae |
use_spot_bb | True/False || Use blackbody for star spots instead of Phoenix (default = False) |
spot_fill | float || Spot filling factor |


### Planet

`[Planet]` handles the planet bulk parameters.

Parameter | Value | Unit| Explanation | Usage (FM/R only)
--- | --- | --- | --- | ---
radius | float | R<sub>J</sub> | Planet radius |
mass | float | M<sub>J</sub> | Planet mass |

### Atmosphere

`[Atmosphere]` handles all parameters pertaining to modelling the planetary atmosphere. We will discuss the various temperature-pressure profile parameterisations in detail [here]({{ '/software/taurex/forward/emission/' | relative_url }}).

Parameter | Value | Unit| Explanation | Usage (FM/R only)
--- | --- | --- | --- | ---
nlayers | int | | number of atmospheric layers (default = 100) |
max_pressure| float |Pa | maximum atmospheric pressure (default = 1e6) |
min_pressure| float |Pa | minimum atmospheric pressure (default = 1e-4) |
tp_type| isothermal/guillot/Npoint/3point/rodgers | | type of temp-pres. profile parameteristation |
tp_iso_temp | float | K | isothermal temperature |
tp_guillot_T_irr | float | K | 2-stream approx. parameter |
tp_guillot_kappa_ir |float || 2-stream approx. parameter |
tp_guillot_kappa_v1 = |float || 2-stream approx. parameter |
tp_guillot_kappa_v2 = |float || 2-stream approx. parameter |
tp_guillot_alpha = |float || 2-stream approx. parameter |
tp_Npoint_T_list | list of floats |K| Npoint temp.-pres. profile parameter |
tp_Npoint_P_list | list of floats |Pa| Npoint temp.-pres. profile parameter |
tp_Npoint_smooth | int | | Npoint temp.-pres. profile parameter |
tp_Npoint_T_list | list of floats |K| Npoint temp.-pres. profile parameter |
tp_Npoint_P_list | list of floats |Pa| Npoint temp.-pres. profile parameter |
tp_Npoint_smooth | int | | Npoint temp.-pres. profile parameter |
tp_3point_T_surf |float |K| 3point  temp.-pres. profile parameter |
tp_3point_P_1 = |float |Pa | 3point  temp.-pres. profile parameter |
tp_3point_T_1 = |float |K| 3point  temp.-pres. profile parameter |
tp_3point_P_2 = |float |Pa | 3point  temp.-pres. profile parameter |
tp_3point_T_2 = |float |K| 3point  temp.-pres. profile parameter |
tp_3point_smooth = |float || 3point  temp.-pres. profile parameter |
tp_corr_length | int | |Rodgers 2000 temp.-pres. profile parameter |
active_gases  | list || Active gasses, e.g. H2O, CH4, CO |
active_gases_mixratios | list || Active gasses mixing ratios | FM
N2_mixratio | float || N<sub>2</sub> mixing ratio | FM, R depending
He_H2_ratio | float || He to H<sub>2</sub> ratio (default is 0.85 H2, 0.15 He) |
rayleigh | True/False || include Rayleigh scattering |
cia | True/False || include collision induced absorption |
cia_pairs | list| | Collision induced absorption pairs default = H2-H2, H2-He |
mie | True/False || Include Mie scattering |
mie_type | flat/lee/bh || flat: assumes grey haze, lee: Use fromalism from Lee et al. 2013, ApJ, 778, 97, bh: Use formalism from Bohren and Huffman (1983) appendix A |
mie_dist_type |cloud/haze || Mie scattering particle distribution for bh model: cloud/haze |
mie_r | float | microns |Mie scattering cloud particle size |
mie_f | float || Mie scattering cloud mixing ratio |
mie_q | float || Mie scattering cloud composition for lee model |
mie_topP | float |Pa| Mie upper atmospheric pressure bound (PA). Set to -1 to assume top of atmosphere |
mie_bottomP |float Pa || Mie bottom atmospheric pressure bound (PA). Set to -1 to assume top of atmosphere|
clouds | True/False | | Include grey cloud opacity |
clouds_pressure | float | Pa | Grey cloud top pressure |
ace_metallicity | float | Fe/H (solar) | Equilibrium chemistry model atmospheric metallicity |
ace_co |float || Equilibrium chemistry model C/O ratio |


### Fitting
`[Fitting]` handles which parameters should be fitted and sets their upper and lower bounds.

Parameter | Value | Unit| Explanation
--- | --- | --- | --- | ---
ace | True/False || Use equilibrium chemistry model
mixratio_log | True/False || fit mixing ratios in log space
fit_active_gases | True/False ||Fit the active gases mixing ratios, defined in `[Planet]` > active_gases. Bounds set in mixratio_bounds
fit_N2_mixratio | True/False || Fit the mixing ratio of N2, defined in `[Planet]` > N2_mixratio. Bounds set in mixratio_bounds
fit_He_H2_ratio | True/False || Fit the He/H2 content ratio, defined in `[Planet]` > H2_He_ratio
fit_temp | True/False || Fit temperature profile
fit_radius | True/False || Fit planetary radius
fit_mass | True/False || Fit planetary mass
fit_unocc_spots | True/False || Fit unocculted starspots & faculae
fit_spot_temp | True/False || Fit starspot temperature
fit_faculae_temp | True/False || Fit faculae temperature
fit_spot_fill_factor | True/False || Fit star spot filling factor
fit_faculae_fill_factor | True/False || Fit star faculae filling factor
spot_temp_bounds| True/False |K|Spot temperature bound. Symmetric bound around analytic spot temperature
faculae_temp_bounds| True/False |K|Spot temperature bound. Symmetric bound around analytic faculae temperature
spot_fill_factor | float list || Spot fill factor bound. Lower and upper bounds as fraction of stellar surface
faculae_fill_factor |float || Faculae fill factor bound. Symmetric bound around analytic fill factor as fraction of stellar surface
fit_mie_scattering |True/False || Fit Mie scattering slope
fit_mie_composition |True/False || Fit Mie cloud composition. Only applicable if mie_type = lee
fit_mie_radius |True/False || Fit Mie particle size
mie_r_bounds | float list | microns | Mie scattering particle size bound
mie_f_bounds| float list || Mie scattering, cloud mixing ratio bound
mie_q_bounds |float list || Mie scattering, composition parameter bound
fit_mie_Ptop |True/False || Mie scattering fitting top pressure
mie_ptop_bounds |float list ||Mie top pressure bounds min-max (Pa). Set to -1 to assume top/bottom atmosphere
fit_mie_Pbottom |True/False ||Mie scattering fitting bottom pressure
mie_pbottom_bounds|float list || Mie bottom pressure bounds min-max (Pa). Set to -1 to assume top/bottom atmosphere
fit_clouds_pressure|True/False || Fit grey cloud top pressure
fit_ace_metallicity|True/False || Fit equilibrium chemistry metallicity
fit_ace_co|True/False || Fit equilibrium chemistry C/O ratio
fit_normal_factor |True/False || Fit lightcurve normalisation factor
Nfactor_num |all/int|| Fit number of normalisation factors
fit_orbital_elements |True/False || fitting oribital elements
inclination_bounds | float list |deg.| orbital inclination bounds
sma_over_rs_bounds | float list || sma over Rs bounds
mixratio_bounds | float list || upper and lower bounds for active gases mixing ratios (in linear space).IMPORTANT: never set mixratio_bounds to zero, otherwise log conversion (mixratio_log = True) will break
He_H2_ratio_bounds | float list || He to H2 ratio. Fitted in log space. Do not set bounds to zero
N2_mixratio_bounds| float list || Mixing ratio bounds for N2 inactive gas
radius_bounds | float list |R<sub>J</sub>|Upper and lower bounds of the radius (but see also radius_bounds_factor)
radius_bounds_factor | float ||If you set radius_bounds_factor = 0.1, and Planet->radius = 1, the radius bounderies will be 0.9 - 1.0. This parameter overrides radius_bounds. You can set this to None or False, and then radius_bounds will be used.
mass_bounds| float list |M<sub>J</sub>| Planet mass prior bounds if fit_mass = True
clouds_pressure_bounds| float list | Pa | Grey cloud top pressure bounds
tp_iso_bounds | float list |K | isothermal temperature bounds
tp_guillot_T_surf_bounds | float list |K | 2-stream approx. temp.-pres. bounds
tp_guillot_kappa_ir_bounds | float list || 2-stream approx. temp.-pres. bounds
tp_guillot_kappa_v1_bounds | float list || 2-stream approx. temp.-pres. bounds
tp_guillot_kappa_v2_bounds | float list || 2-stream approx. temp.-pres. bounds
tp_guillot_alpha_bounds  | float list || 2-stream approx. temp.-pres. bounds
tp_3point_T_surf_bounds | float list |K | 3point temp.-pres. bounds
tp_3point_P_1_bounds | float list |Pa | 3point temp.-pres. bounds
tp_3point_T_1_bounds | float list |K | 3point temp.-pres. bounds
tp_3point_P_2_bounds | float list |Pa | 3point temp.-pres. bounds
tp_3point_T_2_bounds | float list |Pa | 3point temp.-pres. bounds
ace_metallicity_bounds | float list || Equilibrium chemistry metallicity bounds
ace_co_bounds | float list || Equilibrium chemistry C/O ratio bounds

### Downhill
`[Downhill]` handles fitting routine based on simple minimisation. Usually not suggested.

Parameter | Value | Unit| Explanation
--- | --- | --- | --- | ---
run | True/False || run downhill minimisation
type | ascii || type of minimisation to use: Nelder-Mead, Powell, CG, BFGS, Newton-CG, L-BFGS-B, TNC, COBYLA, SLSQP, dogleg, trust-ncg. See scipy.optimize.minimize documentation
options |dictionary || additional minimisation options, e.g.: {‘verbose’:False}

### MultiNest
`[MultiNest]` handles sampling routine based on the MultiNest library. This is the standard.

Parameter | Value | Unit| Explanation
--- | --- | --- | ---
run | True/False || Run MultiNest
resume | True/False || resume from previous run
verbose | True/False || run in verbose
nest_path | PATH || sampling chains director
sampling_eff | ascii || sampling efficiency mode (default=parameter)
n_live_points | int || number of live points
max_iter | int || maximum no. of iterations (0=inf)
multimodes | True/False || search for multiple modes
nclust_par | int || parameters on which to cluster, e.g. if nclust_par = 3, it will cluster on the first 3 parameters only. If ncluster_par = -1 it clusters on all parameters.
max_modes | int || maximum number of modes
const_eff | int || run in constant efficiency mode
evidence_tolerance | float || set log likelihood tolerance. If change is smaller, multinest will have converged
mode_tolerance | float || set mode tolerance
imp_sampling | True/False || Run with importance sampling
out_filename | PATH || output path (default=default)


### PolyChord

`[PolyChord]` handles the PolyChord sampling parameters

Parameter | Value | Unit| Explanation
--- | --- | --- | ---
run | True/False || Run PolyChord
resume | True/False || resume from previous run
nlive_pdim | int || number of life points per sampling dimension (total points = nlive * nDim)
nrepeats | int || number of repeats per sample (decreases correlation in evidence).
path | PATH || sampling chains directory
file_root | ascii || root file prefix
clustering | True/False || attempt clustering of likelihood
precision | float || Likelihood convergence precision
out_filename | PATH || output path (default=default)
