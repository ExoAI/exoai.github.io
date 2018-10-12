---
title: "ExoGAN retrieval"
permalink: /software/exogan/retrieval
excerpt: "exogan retrieval"
last_modified_at: 2018-10-12
toc: true
sidebar:
  nav: exogan_docs
author_profile: true
author:
excerpt: "version 1.0"
---

## Running ExoGAN retrieval

After training ExoGAN it returns a detailed atmospheric analysis from an input spectrum. To run an ExoGAN retrieval, run the command:

```python
python gan.py --predict --checkpointDir checkpoint_test --maskType parameters
```

with 

```
--checkpointDir = the checkpoint directory from the previous training, the default is checkpoint_test;
--outDir = output directory, the default is exogan_output
--maskType = the type of mask for which ExoGAN applies the inpainting algorithm, the default is 'parameters'
```

There are more flags which are listed in the ```gan.py```.

## The ExoGAN analysis


ExoGAN's analysis is located in the output directory specified with the ```--outDir``` flag, the default is ```exogan_output```.
Inside this directory it is possible to find:
- Input spectrum converted into ASPA;
- The masked input ASPA according to the mask choice;
- ```completed``` folder. A set of reconstructed spectra every 100 iteration steps;
- ```hats_imgs``` folder. The set of hats images every 100 iteration steps;
- ```histogram``` folder. A view of the ExoGAN prediction every 100 iteration steps;
- ```logs``` folder. Storage of zhats arrays.
- ```predictions``` folder. Tables of retrieved parameters every 100 iteration steps;
- ```spectra``` folder. Retrieved atospheric models every 100 iteration steps;

