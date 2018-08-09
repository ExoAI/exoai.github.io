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

To generate a transmission forward model, first make sure your parameter file is set to transmission

```
[General]
type = transmission
```

The forward model is then simply run with

```python
python create_spectrum.py -p [PARAMETER FILE]
```

This will create an ascii file `SPECTRUM_out.dat` in the output path specified in your parameter file (`[Output] > path`).

If you would like to plot your spectrum, add the `--plot` flag.
If you would like to save the `.pickle` instance `SPECTRUM_INSTANCE_out.pickle` containing all of the internal states (see [here]({{ '/software/taurex/nest_out' | relative_url }})), then add the flag `--save_instance`.

```python
python create_spectrum.py -p [PARAMETER FILE] --plot --save_instance
```

Documentation on additional flags can be found with

```python
python create_spectrum.py --help
```

### For C/O equilibrium chemistry models

TauREx uses the Atmospheric Chemical Equilibrium (ACE) model (Agundez et al. 2012, A&A, 548, A73) using the thermochemical data by Venot et al (2012, A&A,546,A43).

If you run the model for the first time, you may need to compile it first (see [here]({{ '/software/taurex/installation' | relative_url }}))).

To run the C/O forward model, set the following parameters:

```
[General]
ace = true

[Atmosphere]
ace_metallicity = 1  #metallicity. Change to whatever, 1 = 1x solar, 10 = 10x solar
ace_co = 0.54954     #C/O ratio
```

Below is an example:

```python
python create_spectrum.py -p tests/test_0_transmission_ace/test_fm.par --plot
```
