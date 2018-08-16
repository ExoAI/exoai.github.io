---
title: "TauREx Output"
permalink: /software/taurex/output
last_modified_at: 2018-08-05
toc: false
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---


Aaaah. You got to the output page... That means you must have run TauREx successfully.
Here, have some flowers:

![image-center]({{ site.url }}{{ site.baseurl }}/assets/images/flowers.png){: .align-center}


You may have wondered what the output is. In the folder specified by `[Output] > path` in the parameter file, you will find the following structure


```bash
Input
├── multinest       # folder created by MultiNest. Contains all raw fitting data
|  └── 1-stats.dat  # contains human readable summary of fits
├── polychord       # if PolyChord is run, raw fitting data is found here
├── mcmc            # obsolete (will be removed). MCMC is no longer supported
|
├── nest_out.pickle # main python pickle output file. Used for post-analysis and plotting
└── various plots   # Described in the plotting section
```

The most important file is `nest_out.pickle` as it contains all fitting information (see [here]({{ '/software/taurex/nest_out' | relative_url }})).

If you ran `taurex.py` without the `--plot` flag, you will not have generated the standard output plots. These plots can be generated later on using the `nest_out.pickle` file.
