---
title: "TauREx Cluster:Cobweb"
permalink: /software/taurex/cobweb
last_modified_at: 2018-08-13
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

To run TauREx on cobweb, you need to set a few environment variables and set up your relevant folders

## Folders

All your data needs to be hosted in `\share\data\` as your `home` directory is relatively small.
Best create a folder there with your name where all data is hosted.

```
mkdir \share\data\[USERNAME]
```

Inside this folder, copy `TauREx`.

## Required Modules

As we are currently upgrading some of the software, this may be subject of change. Currently these modules need to be imported

- anaconda/3-4.4.0
- lapack/3.8.0
- multinest/3.10b18
- mpi/mvapich/2-2.3b
- compiler/gcc/7.2.0

To see which modules are available

```
module avail
```

to see which ones are currently loaded

```
module list
```

to load a new module

```
module load [MODULENAME]
```

similarly to unload a module

```
module unload [MODULENAME]
```

It is best if you add the module loading into your `.bashrc` file. Alternatively you can load them in your submit script.

To add them to your `.bashrc`

```
echo 'module load [MODULENAME]' > ~/.bashrc
```


## Submit Script

To run the code, you need to submit to a scheduler, who will run the program on your behalf. On cobweb we use the `torque` scheduler.
An example of a submit script to the scheduler is below. The script should have an `.sh` file name.


```
#! /bin/bash
#PBS -S /bin/bash

#################################
## Script to run Tau-REx on Cobweb
##
## DATADIR    : data directory (e.g. /share/data/taurex)
## SCRATCHDIR : temporary scratch dir. gets deleted at the end
## RUNDIR     : same as SCRATCHDIR but can include subfolders
## OUTDIR     : final results folder (DATADIR=OUTDIR usually)
##
## NP         : number of total cpus, i.e. nodes x ppn
##################################

## Name of job displayed in the queue
#PBS -N [JOBNAME]

## Queue to submit to: gpu/compute/test
#PBS -q compute

##run parameters
#PBS -l walltime=30:00:00             #Maximum runtime: HH:MM:SS
#PBS -l nodes=1:ppn=24                #NODES/CPUs required
#PBS -l mem=20gb                      #Memory requirement

##error output and path variables
#PBS -j oe
#PBS -V

##Number of total cores for mpirun command
NP=24

##setting up path
DATADIR=/share/data/ingo/repos/TauREx
cd $DATADIR

##run job
mpirun -np $NP -hostfile $PBS_NODEFILE python taurex.py -p [PARAMETER FILE] --plot
```

You need to set several parameters here:

```
#PBS -q compute
```
There are currently three queues on cobweb `compute\gpu\test`, `compute` should be your standard queue.
The `compute` queue has currently 176 cores available distributed across 6 nodes á 24 cores and 1 node á 32 cores.

```
#PBS -l walltime=05:00:00
```

This is the maximum runtime allowed. You can leave this as long as you want but please don't run too many nodes with jobs that go for days. Use Legion/Grace/DiRAC for that.

```
#PBS -l nodes=1:ppn=24
```
This sets the number of nodes required and the number of processors per node. TauREx runs best if you keep this at `nodes=1:ppn=24` as inter-node latency affects MultiNest.

```
#PBS -l mem=20gb  
```
RAM memory requirement per node. Each node has a maximum of 256 Gb of RAM memory at the moment.

## QSUB/QDEL/QSTAT

Once you have your submit script. You're ready to submit it to Cobweb. You can do this with

```
qsub [SCRIPTNAME.sh]
```

This will send it to the scheduler and you can see your job listed in the queue using

```
qstat
```

Once the required resources become available, your job will be executed.
If you need to cancel a job:

```
qdel [JOBID]
```

If you need to cancel all your jobs

```
qdel all
```
