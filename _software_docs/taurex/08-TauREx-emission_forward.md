---
title: "TauREx Emission Forward Model"
permalink: /software/taurex/forward/emission/
last_modified_at: 2018-08-05
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

The emission forward model runs in much the same way as the [transmission]({{ '/software/taurex/forward/transmission/' | relative_url }}). The following must be set in the parameter file

```
[General]
type = emission

[Atmosphere]
tp_type = guillot/Npoint #anthing but isothermal unless you want a black body

#example guillot paramters for a hot-Jupiter
tp_guillot_T_irr = 1500
tp_guillot_kappa_ir = 1e-4
tp_guillot_kappa_v1 = 1e-7
tp_guillot_kappa_v2 = 1e-7
tp_guillot_alpha = 1.0
```
