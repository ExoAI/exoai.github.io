---
title: "TauREx Input Folder"
permalink: /software/taurex/xsec
last_modified_at: 2018-08-05
toc: false
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

The Input folder is not shipped with the GitHub repository but must be added manually.
It can be obtained from [here](https://www.dropbox.com/sh/13y33d02vh56jh2/AABxuHdrZI83bSgoLz1Wzb2Fa?dl=0) or
[here](https://osf.io/hn8uk/) and has a permanent DOI: `DOI 10.17605/OSF.IO/HN8UK`.

It contains absorption cross sections, correlated k-coefficients, stellar spectra (for emission models), rayleigh, cia and mie coefficients.

## Layout

This is the default layout of the folder. All paths are specified in the parameter file, so the layout can vary.

```bash
Input
├── xsec                          # folder containing absorption cross sections
|  ├── xsec_sampled_R10000_0.3-15 # Resolution R = 10k set
|  └── xsec_sampled_R15000_0.3-15 # Resolution R = 15k set
|
├── ktables                    # correlated k-coefficients
|  └── R100                    # R = 100 resolution set
|
├── star_spectra               # Phoenix stellar spectra
├── rayleigh                   # Rayleigh scattering coefficients
├── mie                        # Mie scattering coefficients
└── cia                        # Collision induced absorption coefficients
   ├── HITRAN                  # obtained from HITRAN
   └── Borysow                 # obtained from Borysow

```

## Completeness

Some parts of the folder are not very complete, e.g. the number of molecules available aas ktables or cross-sections falls woefully short of what [HITRAN](http://hitran.org) and [ExoMol](http://exomol.com) have to offer. As part of this project, we are generating new cross sections and aiming for a complete set with ExoMol. If however you require cross sections immediately, please contact us (ingo@star.ucl.ac.uk) and let us know.
