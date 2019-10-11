---
redirect_from:
  - "/05-anaconda/00-why-anaconda"
title: 'Anaconda'
prev_page:
  url: /04_sci-programming/05/00_pandas.html
  title: 'Pandas'
next_page:
  url: /05_anaconda/01/00_installing.html
  title: 'Installing Anaconda'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Anaconda Package Manager

As we have seen by now, there are a range of package available for Python that can be installed and used, and there are likely several packages specific to your research that make use of the common ones we covered here.

Installing many code packages which can depend on other code packages can sometimes be a headache - especially if you run into a scenario like:

- install package A, version 1.0
- package B requires package A, version 1.0
- install package B
- package C requires package A, version 2.0
- upgrade package A
- install package C

Figuring out which packages depend on which other packages can get unwieldy very quickly, especially when we may want to have dozens of packages with dozens of dependencies all work nicely together.

Luckily, a tool was created to deal with this messiness: [Anaconda](https://www.anaconda.com/). Originally just a Python package manager, Anaconda now comes with many tools that are useful for analyzing data in Python.

In this section, we will cover how to get started using Anaconda, how to use install new Python packages, and how to use *conda environments* to organize your installed packages and reduce the chances of having messy dependency conflicts.
