---
title: "TauREx Parallelisation"
permalink: /software/taurex/parallel
last_modified_at: 2018-08-05
toc: false
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

TauREx can be run in parallel, both in generating forward models only and in retrieval

### Forward Model

The forward model parallel mode uses the python internal threading module and should not require any further software installation.

To run `create_spectrum.py` in parallel mode, add the `--nthreads [NCORES]` flag. Where `[NCORES]` is the number of cores available.

```python
python create_spectrum.py -p [PARAMETER FILE] --nthreads [NCORES]
```

### Retrieval Model

To run TauREx in parallel mode during retrieval, the following requirements need to be met:

- `mpi4py` must be installed and working
- `MultiNest` was compiled with `mpich` or `openmpi` libraries

Should these requirements be met, it is simple to run TauREx in parallel using:

```python
mpirun -np [NCORES] python taurex.py -p [PARAMETER FILE]
```
