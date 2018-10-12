---
title: "Training ExoGAN"
permalink: /software/exogan/train
excerpt: "Training ExoGAN"
last_modified_at: 2018-10-12
toc: true
sidebar:
  nav: exogan_docs
author_profile: true
author:
excerpt: "version 1.0"
---

## How the training elements are structured

ExoGAN can be trained with pre-computed atmospheric spectra. The training set of 10 million transmission spectra can be found here:

<https://osf.io/6dxps/>

The training set has been split into 100 chuncks of 10000 atmospheric model each. Each element is a python dictionary containing all the information on atmospheric parameters and the spectrum.

As an Example let us take the first element of the ```chunk_0.pkgz``` file:

```python
import cPickle as pickle
import gzip
import numpy as np

def load(filename):
  """Loads a compressed object from disk
  """
  file = gzip.GzipFile(filename, 'rb')
  buffer = ""
  while 1:
    data = file.read()
    if data == "":
      break
    buffer += data
  object = pickle.loads(buffer)
  file.close()
  return object

  chunk = load('./chunck_0.pkgz')
```

Now let us select just the first atmospheric model of the ```chunck_0.pkgz``` dictionary:

```python
atmosphere = chunk[0]
```

The atmospheric spectrum can be extract from:

```python
atmosphere['data']['spectrum']
```

The related parameters can be extracted from:

```python
atmosphere['param']
```

## Training ExoGAN

The training set has been set up as default in order to load the whole training set before the training stage. Loading 10 millions of exoplanetary spectra may take several minutes. The loading part is located in the ```gan.py``` file:

```python
all_spec = glob.glob('./chunck_*.pkgz')
X = []
for i in range(len(all_spec)):
  s = load(all_spec[i])
  for j in s.keys():
    X.append(s[j])
X = np.array(X)
np.random.shuffle(X)
```

After having set up the training set, ExoGAN can be trained with exoplanetary atmospheres by running the command:

```python
python gan.py --mod train --epoch 1 --checkpoint_dir checkpoint_exogan
```

where it is possible to add a number of flags:

```
--epoch = number of epochs for the training stage; 
--learning_rate = Learning rate of for adam, default is 0.0002;
--beta1 = Momentum term of adam, default is 0.5;
--train_size = The size of train images, default is np.inf;
--batch_size = The size of batch images, default is 64;
--image_size = The size of image to use, default is 33;
--checkpoint_dir = Directory name to save the checkpoints, the default is checkpoint_test;
```

The training stage can be run in both CPU and GPU architectures.


