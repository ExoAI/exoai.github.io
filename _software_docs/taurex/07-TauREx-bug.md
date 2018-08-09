---
title: "TauREx Input Folder"
permalink: /software/taurex/bugs
last_modified_at: 2018-08-05
toc: false
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

## We're genuinely sorry...

With all evolving codes, there will be bugs an kinks... please report them should you find issues.
We are working on a bug report system. In the meantime, please report bugs as **issues** on the GitHub repository or alternative email ingo@star.ucl.ac.uk. Thank you.


## MPI4PY, PYMULTINEST, etc

If you run `TauREx` and you get the warning message:

```bash
WARNING - MPI disabled
```

your `MPI4PY` `python` library is either not installed properly or you forgot to run `TauREx` with `mpirun`:

```bash
mpirun -np [NCORES] python taurex.py -p [PARAMETER FILE] --plot
```

where `[NCORES]` is the number of cores you want to run it on.

If you see the following:

```bash
WARNING - MultiNest library is not loaded. MultiNest functionality will be disabled
WARNING - PolyChord library is not loaded. PolyChord functionality will be disabled
```

your `MultiNest` or `PolyChord` libraries are not found and `PYMULTINEST` fails. Try import them manually in a python shell

```python
python
$ import pymultinest
$ import PyPolyChord
```

If that does not work then make sure your `PATH` variables are set correctly

```
export LD_LIBRARY_PATH=[PATH_TO_MULTINEST_FOLDER]/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=[PATH_TO_POLYCHORD_FOLDER]/lib:$LD_LIBRARY_PATH
```

## Test script

If you do not want to run `TauREx` to debug these issues, there is a minimal python script below that imports these libraries in very much the same way `TauREx` does.

```python
# loading libraries
import sys
import os


#trying to initiate MPI parallelisation
try:
    from mpi4py import MPI
    MPIrank = MPI.COMM_WORLD.Get_rank()
    MPIsize = MPI.COMM_WORLD.Get_size()
    MPIimport = True
except ImportError:
    MPIimport = False

# checking for multinest library
try:
    import pymultinest
    multinest_import = True
except:
    multinest_import = False


if MPIimport:
    print('MPI imported')
else:
    print('no MPI')

if multinest_import:
    print('imported pymultinest, all is well')
else:
    print('not imported pymultinest')
```
