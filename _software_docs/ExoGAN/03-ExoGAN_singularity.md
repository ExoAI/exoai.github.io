---
title: "Setting up singularity"
permalink: /software/exogan/singularity
excerpt: "How to set up the singularity docker"
last_modified_at: 2018-10-11
toc: true
sidebar:
  nav: exogan_docs
author_profile: true
author:
excerpt: "version 1.0"
---


For HPC facilities supporting `singularity` dockers, we have provided an ubuntu environment with tensorflow installed.

Singularity can be obtained [here]({https://singularity.lbl.gov}) and the pre-configured image can be downloaded [here]({https://osf.io/6dxps/}). Download the file `ubuntu.simg` which is your ubuntu docker image containing `CUDA 9.0` and `Tensorflow`.

## Setting up singularity on Cobweb

The following instructions are very UCL specific but are likely helpful in the general case.

Cobweb has two GPU nodes available with the following specifications:
- Node 1: NVIDIA - K40, 20 CPUs, 256 Gb RAM (tensorflow only supported using singularity)
- Node 2: NVIDIA - V100, 32 CPUs, 256 Gb RAM (both singularity and tensorflow module support)

To start, move the singularity image to your personal folder, e.g. `/share/data/[USER]/singularity` and navigate to the folder containing your image.

Before proceeding, make sure that you have no local copies of tensorflow installed in your `~/.local` folder. To do this, load an anaconda version

```
module load anaconda/3-4.4.0
```

if you have been using python 3.x previously or load one of the python 2 equivalent modules. Make sure you uninstall all tensorflow instances in `.local` with

```
pip uninstall tensorflow
```

Next, log into one of the GPU nodes with an interactive shell. For the V100:

```
qsub -I -q gpu -l nodes=1:v100
```

and for the K40 node:

```
qsub -I -q gpu -l nodes=1:k40
```


Now you can get on and load the following singularity module:

```
module load singularity/2.5.2
```

Navigate to the folder in which you have stored the `ubuntu.simg` image.
You can then mount the singularity image with the following command

```
singularity shell -B /share/data:/mnt --nv ubuntu.simg
```

where `-B` mounts the `/share/data` directory into the `/mnt` directory inside singularity. The `--nv` flag binds the external GPU hardware with the singularity internal CUDA libraries.

Once inside the image, you will find that your `home` diretory has been mounted and your data is mounted in `/mnt`. The image is essentially a stripped down version of an Ubuntu operating system containing both `anaconda` and `tensorflow` distributions pre-installed.

Now enter the anaconda tensorflow environment with:

```
source activate tensorflow
```
In principle you can now run ExoGAN by navigating to the folder containig ExoGAN and run the code in the interactive shell.
Once this works, we can now set up a launch script to run singularity using the Torque scheduler.

### Troubleshooting

You may find that `pylab` or other python modules are missing when running ExoGAN or similar codes. These can be easily installed inside the image using pip:

```
pip install --user matplotlib scipy numpy
```

## Running singularity using the scheduler

Whilst running ExoGAN in an interactive shell is great, the code requires significant training time. It is hence useful to use the `torque` scheduler instead. For this we need to set up two bash scripts: the launch script that gets executed inside singularity and the scheduler script that instructs the scheduler to start singularity.

### Launcher script

The following script summarises exactly the same steps as above. Place the script in the ExoGAN directory, obviously replacing the path in the script. It will get called together with singularity later. For reference we name this script `singularity_launch_gan.sh` here (but you can call it anything of course...).

```
#! /bin/bash

#load the anaconda tensorflow environment
source activate tensorflow

#navigate to GAN directory
cd /mnt/[PATH TO WHERE ExoGAN is put]

#run the code
python gan.py
```

Make sure that it is executable with

```
chmod +x singularity_launch_gan.sh
```


### Scheduler script

This is a more standard `torque` submit script. To run your code on the `V100` node:



```
#! /bin/bash
#PBS -S /bin/bash

#################################
## Script to run ExoGAN on Cobweb using singularity
##################################

## Name of job displayed in the queue
#PBS -N [JOBNAME]

## Queue to submit to: gpu/compute/test
#PBS -q gpu

##run parameters
##Maximum runtime: HH:MM:SS
#PBS -l walltime=30:00:00       
##NODES required      
#PBS -l nodes=1:v100        
##Memory requirement      
#PBS -l mem=100gb                      

##error output and path variables
#PBS -j oe
#PBS -V

##setting up path
DATADIR=[PATH TO SINGULARITY IMAGE]
cd $DATADIR

##run singularity
singularity shell -B /share/data:/mnt --nv ubuntu.simg /mnt/[PATH TO ExoGAN]/singularity_launch_gan.sh

```

To change to the NVIDIA K40 node, change the script to

```
##NODES required   
#PBS -l nodes=1:k40
```

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
