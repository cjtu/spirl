---
redirect_from:
  - "/05-anaconda/02/01-share-envs"
title: 'Sharing Environments'
prev_page:
  url: /05_anaconda/02/00_environments.html
  title: 'Environments'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Sharing environments

Say we want to send our conda environment to a collaborator so that they can run some code that we wrote. Or maybe we simply want a list of the packages we used to get a result to make sure we can use produce the same result in the future.

## The environment.yml

Anaconda provides us with a way to build an identical environment using a special configuration file usually called `environment.yml`. To generate this file, we use the `conda env export` command. This command simply produces a list of the packages currently installed in our active conda environment. If we pipe this output to `environment.yml`, voila! We have instructions for Anaconda to reproduce our environment.

```bash
conda env export > environment.yml
```


Now we have an `environment.yml` file that looks something like:

```yaml
name: researchenv
channels:
  - conda-forge
  - defaults
dependencies:
  - <package1>=<verion.major.minor>
  - <package2>=<verion.major.minor>
```

Now we can make a brand new environment using this `environment.yml` file.

## Deleting environments

Let's delete our `researchenv` environment with `conda remove --all`. The `--all` ensures that all packages and the environment are deleted (rather than simply deleting one package at a time from your environment).

```bash
conda remove --name researchenv --all
```

We can check that the environment is deleted by trying to activate it:

```bash
conda activate researchenv
```

Or we can list all available environments with:

```bash
conda env list
```

## Creating environments from a yml

Now we can make an identical environment with the `environment.yml` file that we saved:

```bash
conda env create -f environment.yml
conda activate researchenv
conda list
```

You should now see all of the files that we previously had in `researchenv`

## Caveats to Sharing Environments

Now that we have an `environment.yml` file, we *should* be able to send it to a collaborator, and have them run `conda env create -f environment.yml` to have a copy of our working environment.

One caveat is that certain packages depend on the operating system that the code is being run on, and Anaconda will not always be able to exactly reproduce the environment on another system. Using an `environmnet.yml` works best on the same OS that it was created on.

To make our code truly distributable and reproducible on other machines, we get into the realm of developing open source packages and publishing them to be installable with `pip` or `conda`. While this is a deep topic outside the scope of this book, there are many resources online for exploring this further if you want to share your awesome package with the community!

Now you know all you need to get started using Anaconda and managing environments for your programming projects. Everything you need to know about Anaconda environments is available [here](https://conda.io/docs/user-guide/tasks/manage-environments.html) (or like everything else, via Google search).
