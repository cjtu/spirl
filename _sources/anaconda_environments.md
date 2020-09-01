# Conda environments

Once you've installed Anaconda, when you open a new shell you should see the word `(base)` on the shell prompt (if not, try typing `conda --version` to make sure Anaconda installed properly and was set up). The word in parentheses is your active **conda environment**, by default this is the *base* environment.

## Why Environments?

Virtual environments allow us to install packages into a self-contained location on our computer without affecting any other parts of our system. This is particularly useful is we have multiple projects, each with their own requirements and dependencies. Sometimes the dependencies of different projects can be conflicting, and we want to be careful about installing new packages which could break code we've written for another project.

Another good reason for virtual environments is **reproducibility**. If we develop and run our programs in virtual environments, we know the exact packages which allowed us to properly run the code, and we can later share this environment with collaborators, or be confident our code will run when we return to it a year or many years later.

## Creating a New Environment

To make a conda environment, we use the command `conda create`. We need to specify a name of the environment with `-n`. We can also specify some packages we want to install right away. Try it in your shell!

```bash
conda create -n researchenv python numpy matplotlib jupyter
```

*Aside*: if you want to install all of the default Anaconda packages (e.g. the ones available in the `base` environment), you can type `conda create -n <envname> anaconda`. We very rarely need *all* of the packages that come with Anaconda, and it is generally better to use as *few dependencies as possible*. An environment with only the packages you need has less chances of dependency conflicts and is more reproducible!

Once conda processes the dependencies of the packages you specified. Are you surprised by how many dependencies it takes to make `numpy`, `matplotlib` and `jupyter` work? Good thing conda can keep track of these dependencies for us!

Once you confirm with `y`, conda will install these packages in a self-contained environment called `researchenv`.

To activate an environment, we use the `conda activate <envname>` command. To deactivate an environment, type `conda deactivate` (no envname needed in `deactivate`). Try activating your new conda environment and listing the installed packages with `conda list`.

```bash
conda activate researchenv
```

Check your command prompt to ensure your environment is active (you should see `(researchenv)` at the beginning of the line).

We can check the packages in the current environment with the `conda list` command.

```bash
conda list
```

## Using an activated environment

If we start Python from an active conda environment, we will have access to the packages installed in that environment. We can test this by running a simple one-line Python script in the command line. Try the following:

```bash
python -c "import pandas"
```

Did you see an error? This is because we haven't installed `pandas` in our conda environment. Instead let's try importing an installed module like `numpy`:

```bash
python -c "import numpy"
```

No error? That means `numpy` is available in our environment!

Now let's try deactivating our environment and see what packages the conda `base` environment provides.

```bash
conda deactivate
conda list
```

The default conda environment comes with *a lot* of packages. If you encounter long unwieldy output on the command line, you can always search it by piping (`|`) it to the `grep` bash command. Say we want to see if `pandas` is included in the `base` environment, we can write:

```bash
conda list | grep pandas
```

Now what happens if we try to import pandas with the `base` conda environment active?

```bash
python -c "import pandas"
```

No error! This example illustrates how conda environments are self-contained. Our `researchenv` does not know about any of the packages in `base`, it only has access to the ones we've installed in it. This makes it important to be aware of *which environment you have active*. If you get errors about packages that don't exist, make sure you've `conda activate`d the right environment.

Say we want to use `pandas` in our tidy, self-contained `researchenv`. First we will need to activate our environment then install it!

## Installing packages

Now let's try installing a new package. When you use the `conda install` command, it installs the package in the *currently active environment only*. Let's install `pandas` in `researchenv`.

```bash
conda activate researchenv
conda install pandas
```

Once you've confirmed and conda is finished working, let's check our list of installed packages. Remember, we can search for a word by piping output to `grep`:

```bash
conda list | grep pandas
```

Great! You now know how to make environments, activate them and install new packages!

## Finding new packages

Often we don't know what packages exist or do the things we want them to do. Sometimes a simple Google search about the program you are writing will reveal that many others have had the same problem and have already written a package to solve it!

Say we want to work with GeoSpatial data in Python and some Googling reveals the `rasterio` package. First we should check if it is available from Anaconda by Googling "conda packages", or just going straight to this [link](https://anaconda.org/anaconda/repo).

On this page we can search for packages available to be installed by Anaconda (most well-used packages are). Try searching for `rasterio` in the search box.

My search revealed two top results:

- `conda-forge/rasterio`
- `anaconda/rasterio`

## Anaconda channels

It seems `rasterio` has two versions of the package available from two different *channels* of Anaconda. The `anaconda` channel is the default, and your `conda install` command will generally install from `anaconda`. The `conda-forge` channel is a community initiative to make open-source community packages easier to access. Sometimes packages will only be available here (or in the case of `rasterio`, we can see that the `conda-forge` version has many more downloads and is probably the one we want).

We can install packages from a particular channel by using the `-c` option to `conda install`. Make sure your `researchenv` is active, then try the following:

```bash
conda install -c conda-forge rasterio
```

## Pip

Sometimes a package is not available for install from any channels of Anaconda, but it may still be available from the default Python package manager, `pip`.

The `pip install` command is similar to `conda install`, and should still install Python packages and their dependencies. The main advantage of using `conda install` over `pip install` is that `conda` is not language-specific. Packages installed with conda can have dependencies not necessarily written in Python, and conda will be able to install and keep track of those non-Python packages for for you. Pip will handle Python dependencies only.

There is no problem with using both `conda install` and `pip install` within a conda environment, though it is best practice to try stay consistent and use `conda` where possible

## Installing Packages TL;DR

First find the name of a new package you would like to install (via Google, word of mouth, the Python Package Classifieds in the newspaper, etc.)

- Search the Anaconda [package list](https://anaconda.org/anaconda/repo) for the package
- if it is only available from `anaconda` or this version has the most installs, use `conda install <name>`
- if it is only available from `conda-forge` or this version has the most installs, use `conda install -c conda-forge <name>`
- if neither is available, use `pip install <name>`

Now we have the tools we need to find and install packages into Anaconda environments! Feel free to make a new environment whenever you start a new project or want to try installing a new package without knowing if it will conflict with your current packages. Conda environments can help us keep our code packages tidy and reproducible!

In the next section we will learn to make an exact copy of our environment to share with collaborators or store for our future selves to ensure we can reproduce our results.

## Sharing environments

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
