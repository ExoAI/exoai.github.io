---
title: "Issues on TauREx"
permalink: /software/taurex/issues
last_modified_at: 2018-10-31
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

Here we mark down some of the frequently happened issues from the community and our recommended solution to them. Please contact us if the provided solution failed to solve your issue.

## Compiling Issues

This session includes error messages that may arise when compiling c++ packages, i.e. when using the command:
```
sh compile.sh
```

1. Q: I received warnings when I was compiling the .cpp files, should I worry?
   
   A: As long as you have the corresponding .so files, then everything should be okay.


2. Q: fatal error: stdio.h: No such file or directory

   A: For Mac OS users: this issue may arise if your xcode is not up-to-date, please open the terminal and type:
   ```
   xcode-select install
   ```
   For users who have recently upgraded to Mac OS Mojave, if the above solution doesn't work, one could try the following command:
   ```
   open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg
   ```
3. Q: OSError: dlopen(./library/xxxx.so, 10): image not found

   A: This error arises when TauREx cannot find the necessary compiled `.so` file from the library. A likely cause for this error is simply that the `.so` does not exist. 
   
   A possible solution is to go into the `compile.sh` and un-comment the line where `.so` file was located, and run the following command after saving the changes:
   
   ```sh compile.sh```
   
## TauREx execution Issues

This session includes error messages or problems that may arise during the operation of TauREx.

1. Q: I received this error message: KeyError[‘nest_map’]
   
   A: This generally arises you are running TauREx using the MCMC sampling routine. The recommended sampler for TauREx is MultiNest Sampling. In your .par files please do the following:
   ```
   [Downhill]
   run = False
   [MultiNest]
   run = True
   ```