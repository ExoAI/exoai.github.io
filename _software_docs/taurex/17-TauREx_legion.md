---
title: "TauREx Cluster:LEGION/GRACE"
permalink: /software/taurex/legion
last_modified_at: 2018-08-13
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

Running TauREx on the UCL HPC facilities (Legion/Grace/Myriad/Thomas/Aristotle) is slightly different than running on [cobweb]({{ '/software/taurex/cobweb' | relative_url }}).


Fortunately, all UCL HPC systems work in the same way, so you can easily transfer your setup between, say, Legion and Grace. They have extensive documentation and user examples [here](https://wiki.rc.ucl.ac.uk/wiki/Category:User_Guide). We will only discuss Legion and Grace here.
There are differences between Legion and Grace. Legion is a very heterogeneous system allowing small (<10 core) jobs, whilst Grace has a minimum requirement of 32 cores per job. For a breakdown of the specifications, see [here](https://wiki.rc.ucl.ac.uk/wiki/RC_Systems#Thomas_technical_specs).

## Folders

Legion has a `home` and `Scratch` directory. During runtime, you must be in `Scratch` as `home` becomes read-only. So in `Scratch`, set up your TauREx folder.

## Modules

This is ever changing. What works for now are the following combinations of modules:

```
module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load compilers/gnu/4.9.2
module load mpi/openmpi/1.10.1/gnu-4.9.2

module load python3/3.6
module load mpi4py/2.0.0/python3
```

Note that you must unload the default intel libraries to get `mpi4py` loaded. Best add these to your `.bashrc`.


## Installing MultiNest

After loading the above modules, installing MultiNest is relatively easy on Legion. Follow the instructions [here]({{ '/software/taurex/installation' | relative_url }}) and make sure you export your library path (best add to `.bashrc` as well):

```
export LD_LIBRARY_PATH=[PATH TO MULTINEST]/lib:$LD_LIBRARY_PATH
```

## Submit Script

The submit script works differently to cobweb. Here's an example:

```
#! /bin/bash -l
#$ -S /bin/bash
#$ -N [JOBNAME]        #name of job in queue
#$ -V
#$ -l h_rt=5:00:00     #maximum walltime
#$ -l mem=10G          #maximum memory
#$ -l tmpfs=10G        #maximum disk size
#$ -pe mpi 16          #number of cores
#$ -wd [PATH]          #path to working directory

#environment variables
export MPLBACKEND="pdf"

gerun python taurex.py -p [PARAMETERFILE] --plot
```

Note that `gerun` replaces all instances of `mpirun` on Legion. You can now submit and monitor progress in much the same way as on cobweb.
