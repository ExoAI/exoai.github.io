---
title: "TauREx Tranmission Forward Model"
permalink: /software/taurex/forward/transmission/
last_modified_at: 2018-08-05
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---


#### For C/O equilibrium chemistry models

TauREx uses the Atmospheric Chemical Equilibrium (ACE) model (Agundez et al. 2012, A&A, 548, A73) using the thermochemical data by Venot et al (2012, A&A,546,A43).
To run the C/O forward model:

```python
python create_spectrum.py -p tests/test_0_transmission_ace/test_fm.par --plot
```




#### External input files

External input files for temperature-pressure profiles and chemical abundance profiles can be provided using the following routine

```python
create_spectrum_chemprofile.py
```

We will add documentation for this mode soon. If you want to use it, please just email ingo@star.ucl.ac.uk for now.
