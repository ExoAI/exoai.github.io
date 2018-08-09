---
title: TauREx Tranmission Retrieval
permalink: /software/taurex/retrieval/transmission/
last_modified_at: 2018-08-05
toc: false
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---


Retrievals can be run in transmission and emission modes (currently this version only supports transiting planets but directly imaged planets can also be modelled)

To run a retrieval on a spectrum, specify the spectrum path in the parameter file

```
[Input]
spectrum_file = [PATH TO SPECTRUM ASCII FILE]

[Output]
path = PATH_TO_OUTPUTFOLDER

[MultiNest]
run = True

#alternatively you can run PolyChord (if installed)
[PolyChord]
run = True
```

The spectrum file should have 3 to 4 columns:

wavelength (microns) | (Rp/Rs)<sup>2</sup> or Fp/Fs | Error | optional: wavelength bin width (microns)


The parameter file should contain all necessary attributes to model the spectrum. We have provided examples for 30 planets in transmission in the [Tsiaras et al. (2018)](http://iopscience.iop.org/article/10.3847/1538-3881/aaaf75) paper.
The data, parameter files and corresponding retrievals can be found [here](http://bit.ly/HSTDATA).

The `/tests` folder provides transmission and emission examples. To run the transmission retrieval case:

```python
python taurex.py -p tests/test_0_transmission/test_retrieval.par --plot
```

To run the retrieval on multiple cores in parallel, see [here]({{ '/software/taurex/parallel' | relative_url }}).

The `--plot` flag will plot a standard set of output results (posterior distributions, fitted spectrum, opacity contribution breakdown). To plot all available data (e.g. TP-profiles), plots can be
generated after the retrieval has terminated using the created `nest_out.pickle` files which contain all results and internal states of the retrieval (see [here]({{ '/software/taurex/plotting' | relative_url }}) for plotting and [here]({{ '/software/taurex/nest_out' | relative_url }}) for `nest_out.pickle`).

All parameters can be specified in the parameter file or alternatively given as flags in the command line. To print available parameters:

```python
python taurex.py --help
```
