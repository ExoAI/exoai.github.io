---
title: "ExoGAN Guide"
permalink: /software/exogan/installation
excerpt: "How to install and run the ExoGAN code"
last_modified_at: 2018-10-11
toc: false
sidebar:
  nav: exogan_docs
author_profile: true
author: 
excerpt: "version 1.0"
---

ExoGAN is written in Tensorflow (v. 1.8) with additional standard python packages.

#Installing Tensorflow

Tensorflow is easy to install on most systems though we do find GPU support to be difficult to install and highly architecture dependent. Hene we will not provide a general installation manual here but refer you to the tensorflow website.

<https://www.tensorflow.org/install/>

If possible, we strongly suggest to run tensorflow in `docker` container (avaialable on the tensorflow website). If your cluster supports containers, it is a much easier way to port your code and handle difficult GPU dependencies.

We have also created a `singularity` container for use on clusters supporting singularity (<https://singularity.lbl.gov>). For the singularity image description, please see [here]({{ '/software/exogan/singularity' | relative_url }}).

#Installing python packages

We recommend using anaconda as python distribution but python packages can easily be installed using pip

```
pip install scipy numpy matplotlib argparse
```
