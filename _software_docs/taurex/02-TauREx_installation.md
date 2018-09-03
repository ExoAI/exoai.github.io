---
title: "TauREx installation"
permalink: /software/taurex/installation
last_modified_at: 2018-08-05
toc: true
toc_sticky: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---


The following steps will guide you through your TauREx installation. They are very Mac centric but most of it should apply to a linux installation as well. To install things easily and smoothly for Mac, I strongly recommend to use macports or homebrew (https://www.macports.org). For ubuntu, most of the work will be the same using apt-get but the individual commands will obviously be different.

The main issue here is the installation of `multinest`. You only need to do this once for your system but it can be a bit of a hassle first time you try. There is quite a lot of documentation on the web though if you google it.

## Requirements

The main body of TauREx is written in Python 2.7/3.x. The atmospheric forward models are written in C++ and the equilibrium chemistry model is written in Fortran 90.

To run TauREx, you need a modern GCC (>4.9) or intel compiler as well as either python 2.7 or python 3.x and standard python libraries. You should be able to switch seamlessly between python versions but please note that from future versions, development will be exclusively in python 3.x.

## Installing MultiNest

Before getting to TauREx, we need to first install MultiNest.

### Downloading

To start, we need to download TauREx. It is available via GitHub:

<https://github.com/ucl-exoplanets/TauREx_public>

Either download it as `.zip` file or clone it into your directory:

```
git clone https://github.com/ucl-exoplanets/TauREx_public
```

Now download MultiNest (you will need to register to access the download page):

<https://ccpforge.cse.rl.ac.uk/gf/project/multinest/>

Make sure you download the cmake installation version. This sorts most of the makefile issues that you commonly encounter with multinest.
Unpack the .tar.gz file somewhere. The default installation directory (unless you change it) is
`/usr/local/multinest`. You can also choose a more local directory. It does not really mattter where you install it but for the sake of argument, we will assume the default from here on.

### GCC compilers

Before installing, read the *README* file in the multinest folder. This should explain quite well how to install multinest.

Before compiling multinest, I found it helpful to make sure the latest version of gcc is installed on your system (do not install 4.8 as that has a bug w.r.t. some lapack libraries). Anything above version 4.9 is fine.  

GCC5.x or above is recommended and everything will be linked to this from here on

To install gcc on a Mac using macports

```bash
sudo port install gcc5
```

now make sure this gcc is the default option

```
sudo port select --set gcc mp-gcc5
```

install cmake if you haven’t already got it

```
sudo port install cmake
```

install the OpenBLAS library (this can take an hour, not 100% sure you really need that. It depends whether you have a set of lapack libraries already installed on your system. You may want to skip this step on first try and then return to it later if needed. )

```
sudo port install openblas +gcc5
```

Install openmpi with gcc5 compiler linking

```
sudo port install openmpi +gcc5
sudo port select --set mpi openmpi-mp-fortran
```

### Compiling MultiNest

Now we get to compiling multinest itself. Go to the folder where you unpacked the multinest files into. There is a very helpful little readme file but just in case here is what you have to do:

go to the multinest directory and make a folder ‘build’
```
$ cd $MULTNEST_DIR
$ mkdir build
```
now go into the build folder and make and install multinest

```
$ cd build
$ sudo cmake ..
$ sudo make
$ sudo make install
```

Make sure that it correctly finds the gcc, gfortran (or icc, ifort) compilers, BLAS and LAPACK libraries and OpenMPI libraries. CMAKE will complain if it doesn’t.

If you have multiple compilers on your system, cmake sometimes has issues detecting the correct compiler, escpecially `gfortran` is often an issue. To force it to use a certain compiler, you can specify its `path` with

```
$ sudo cmake -D CMAKE_FC_COMPILER=[PATH_TO_EXECUTABLE]/gfortran ..
```  

If you are using a Mac, you need to soft-link the .dylib libraries to .so version. You do not need to do that on a linux system. Go to the library folder and /lib and set up soft links from .dylib to .so libraries.

These files need to have softlinks to .so endings

```
libmultinest.dylib
libmultinest.3.9.dylib
libmultinest_mpi.dylib
libmultinest_mpi.3.9.dylib
```
```
sudo ln -s libmultinest.dylib libmultinest.so
sudo ln -s libmultinest_mpi.dylib libmultines_mpi.so
```

Finally, add the multinest libraries to your LD_LIBRARY_PATH variable. Best is if you do that in your `.bashrc` or `.bash_profile` or `.profile` (whichever your system uses)

```
export LD_LIBRARY_PATH=/usr/local/multinest/lib:$LD_LIBRARY_PATH
```

## Installing python libraries

TauREx relies on mostly standard libraries and most of them are shipped in a typical Anaconda installation. I would suggest you get Anaconda here:

<https://www.anaconda.com/>

If you want to stick with your prestine macports installation, you may need to install extra packages.
The minimal set of standard libraries you need are: numpy, matplotlib, configparser, optparse

```
sudo port install py27-pymc, py27-sklearn, py27-cython, py27-configparser, py27-optparse, py27-threading, py27-subprocess, pip
```

Older versions of TauREx also require you to install pymc.

```
sudo port install py27-pymc
```

or

```
pip install pymc
```



### MPI linking (optional)

Now install the mpi linking to python with the correct links . This is important: make always sure that you are installing everything with openmpi and not mpich linking

```
sudo port install py27-mpi4py +openmpi
```

now install pymultinest using pip
```
sudo pip install pymultinest
```

## Compiling TauREx Forward models

Finally, the TauREx C++ and fortran libraries need to be compiled. In the `/library` folder

```
sh comipile.sh
```

**Optional:** if the chemical equilibrium model is required, it must be compiled separately first. In the `/library/ACE folder`

```
gfortran -shared -fPIC  -o ACE.so Md_ACE.f90 Md_Constantes.f90 Md_Types_Numeriques.f90 Md_Utilitaires.f90 Md_numerical_recipes.f90
```

That’s it. Now you should be able to run TauREx.


## Adding Input folder data

TauREx requires input data such as ktables/cross-sections/cia/mie etc. These cannot be provided on GitHub due to size. The required Input folder can be downloaded here:

<http://bit.ly/2y7XkKq>

On [this]({{baseurl}}/software/taurex/xsec) page, we explain the Input folder and what is needed in more detail.

## Downloading TauREx from Dropbox

Alternatively, you can download the full code with its Input files in place from here:

<http://bit.ly/2wmPjMV>

Remember that you still need to recompile the forward models since your system architecture is likely to be differnt.

---

## Testing TauREx

TauREx has two modes in which it can be run: Forward model and Retrieval. More detail will be given on the dedicated [pages]({{ '/software/taurex/paramterfile' | relative_url }}). For now, a simple run-through on how to test TauREx with a minimal parameter file.

### Forward model
In the forward model mode, we can create individual spectra through either the provision of a
parameter file and listed abundances or C/O and metallicity, or by providing external temperature-pressure and chemical profile files.

For a standard example, we provide example parameter files in the /tests folder.

#### For a transmisison/emission case:

```python
python create_spectrum.py -p tests/test_0_transmission/test_fm.par --plot
```

The spectrum is saved as ascii in SPECTRUM_out.dat in the Output folder specified in the parameter file.
Note these parameter files are minimal files and modify the default parameter in Parfiles/default.par. You can add as many paramters in your minimal par file
as required.

Flags:
-p : path to parameter file
--plot : creates plot of spectrum
--save_instance : saves the spectrum, together with other data (e.g. temperature-pressure profiles, transmissivity, etc) in a numpy pickle file.

To get a list of parameters that can be set on command line:

```python
python create_spectrum.py --help
```

For the emission example, use

```python
python create_spectrum.py -p tests/test_0_emission/test_fm.par --plot
```
