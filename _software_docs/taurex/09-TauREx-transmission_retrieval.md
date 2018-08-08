---
title: TauREx Tranmission Retrieval
permalink: /software/taurex/retrieval/transmission/
last_modified_at: 2018-08-05
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---


Retrievals can be run in transmission and emission modes (currently this version only supports transiting planets but directly imaged planets can also be modeled)

To run a retrieval on a spectrum, specify the spectrum path in the parameter file

```
[Input]
spectrum_file = PATH_TO_SPECTRUM
```

The spectrum file should have 3 to 4 columns: wavelength (microns), (Rp/Rs)^2 or Fp/Fs, Error, wavelength bin width (microns, optional)
The parameter file should contain all necessary attributes to model the spectrum. We have provided examples for 30 planets in transmission in the Tsiaras et al. (2017, arXiv: ) paper.
The data, parameter files and corresponding retrievals can be found here: http://bit.ly/HSTDATA

The /tests folder provides transmission and emission examples. To run the tranmission retrieval case:

```python
python taurex.py -p tests/test_0_transmission/test_retrieval.par --plot
```

The --plot flag will plot a standard set of output results (posterior distirbutions, fitted spectrum, opacity contribution breakdown). To plot all available data (e.g. TP-profiles), plots can be
generated after the retrieval has terminated using the created nest_out.pickle files. All parameters can be specified in the parameter file or given as flags in the command line. To print available paramters:

```python
python taurex.py --help
```

To generate all available plots:

```python
python tools/taurex_plots.py --db_dir tests/tests_0_transmission/ --plot_all
```

where --db_dir is the directory containing the nest_out.pickle file. For the data structure of the nest_out.pickle file and the data contained within, we refer you to the documentation in the *Documentation* folder.
