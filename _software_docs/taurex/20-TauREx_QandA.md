---
title: "TauREx Q and A"
permalink: /software/taurex/QandA
last_modified_at: 2018-10-25
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

Here we have collected some of the most frequently asked questions on the software. 

1. Q: What is the difference between `default.par` and our customised `.par` file? 
   
   A: To run TauREx one would need to provide a lot of parameters and minor settings. Many of them will stay the same between different operations. To relieve us from specifying everything each time, the default.par file holds the default settings of TauREx. Your customised `.par` file, the one you used to input into TauREx, will the parameters or settings that you wish TauREx to use instead of the default ones. For any unspecified parameters or settings in your own `.par` file, TauREx will then look into the `default.par` file for the default settings.  
