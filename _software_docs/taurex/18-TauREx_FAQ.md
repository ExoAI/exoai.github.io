---
title: "TauREx FAQ"
permalink: /software/taurex/FAQ
last_modified_at: 2018-10-22
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

Under Construction.

Here we mark down some of the most frequently asked questions from the community and our recommended solution to them.

## Compiling Issues

1. Q: fatal error: stdio.h: No such file or directory

   A: For Mac OS users: You will need to update Xcode, In a Terminal please type:
```
xcode-select install
```

Caution: For users who have recently upgraded to Mac OS Mojave, if the above solution doesn't work, one could try the following commend:

```
open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg
```