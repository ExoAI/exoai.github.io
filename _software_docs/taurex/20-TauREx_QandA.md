---
title: "TauREx Q and A"
permalink: /software/taurex/QandA
last_modified_at: 2018-10-31
toc: true
sidebar:
  nav: taurex_docs
author_profile: true
author: taurex
excerpt: "version 2.6"
---

Here are collected some of the most frequently asked questions on the software. 

1. Q: What is the difference between `default.par` and our customised `.par` file? 
   
   A: Please see session: <https://exoai.github.io/software/taurex/paramterfile>
   
2. Q: I would like to examine the full result of my retrieval, where should I find it?

   A: Information regarding a retrieval could be found inside your output folder's `nest_out.pickle`.
   
3. Q: How do I know if multinest is working in TauREx?

   A: There are three things you could check. 
   1. Examine the `INFO` coming out of the terminal when you run TauREx and look for the line:
      ```INFO - MultiNest library correctly loaded.```
      
      This is to ensure Multinest Library is correctly installed on your machine.
   
   2. Set `verbose = True` in the `.par` file so that there will be output whilst multinest is running. 
   3. Examine the files under `\multinest` folder. The size of the files, such as `1-.txt` and `1-live.points` should \
      increase during the exeuction. 