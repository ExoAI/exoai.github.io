---
title: "TauREx Emission Retrieval"
permalink: /software/taurex/retrieval/emission/
last_modified_at: 2018-08-05
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

The emission retrieval runs in the same way as transmission. There are some notable changes in the parameter file

We strongly suggest to use the `tp_type = guillot` profile based on

`Line et al. 2012, ApJ, 749,93 (equation 19)` <br />
`Guillot 2010, A&A, 520, A27 (equation 49)`

Other profiles such as by Rodgers are also available:

`Introduced in Rodgers (2000): Inverse Methods for Atmospheric Sounding (equation 3.26)`

The corresponding changes to the parameter file are:

```
[General]
type = Emission

[Input]
spectrum_file = [PATH TO SPECTRUM ASCII FILE]

[Atmosphere]
tp_type = guillot     #the standard temperature-pressure profile used

[Fitting]
fit_temp = True       #you likely want to fit the temp-pressure profile

tp_guillot_T_surf_bounds = 1300, 2500
tp_guillot_kappa_ir_bounds = 1e-10, 1
tp_guillot_kappa_v1_bounds =  1e-10, 1
tp_guillot_kappa_v2_bounds =  1e-10, 1
tp_guillot_alpha_bounds = 0.5, 1.

[MultiNest]
run = True

#alternatively you can run PolyChord (if installed)
[PolyChord]
run = True
```

The `/tests` folder provides transmission and emission examples. To run the emission retrieval case:

```python
python taurex.py -p tests/test_0_emission/test_retrieval.par --plot
```
