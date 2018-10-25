---
title: "Issues on TauREx"
permalink: /software/taurex/issues
last_modified_at: 2018-10-25
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
   For users who have recently upgraded to Mac OS Mojave, if the above solution doesn't work, one could try the following commend:
   ```
   open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg
   ```

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