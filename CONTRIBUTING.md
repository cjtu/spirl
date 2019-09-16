# Contributing guidelines

## Getting started

Either comment on an open issue at the [issues board](https://github.com/cjtu/spirl/issues), or get in touch with Christian at [cj.taiudovicic@gmail.com](cj.taiudovicic@gmail.com) if you'd like to contribute.

## Getting a build set up

This repository is a [jupyterbook](https://jupyter.org/jupyter-book/intro.html) that is built with [Jekyll](https://jekyllrb.com/) and published with [GitHub Pages](https://pages.github.com).

To test the site locally, you will need Ruby, bundler, and Jekyll running locally. Some helpful guides to getting set up:

- The Jupyterbook team recommends using Docker to get the necessary dependencies (guide [here](https://jupyter.org/jupyter-book/guide/05_advanced.html#Build-the-book's-site-HTML-locally))
- If that doesn't work or to get the dependencies manually, you can install Jekyll with the guide [here](https://jekyllrb.com/docs/installation/), then install the `jupyter-book` command with pip or conda as described [here](https://jupyter.org/jupyter-book/guide/01_overview.html#Install-the-command-line-interface).

## Testing the site locally

Once you have the above dependencies, you should be able to build and test the SpIRL Jupyterbook locally with the following commands. Make sure if you installed `jupyter-book` in a virtual environment, that you have activated that env!

- `make book`: Build the static `.html` site files needed to display the content
- `make serve`: Serves a local build of the website using Jekyll that you can access in a web browser using the link it gives you (probably something like `localhost:4000/spirl/00_about`). The local site will auto-update for most changes (but you will need to `make serve` again if you change the `_config.yml` or `toc.yml`)
- `make clean`: This will wipe the local site files. Sometimes your update will require you to completely re-build the book, so it can be good to run this before `make book` if things look weird. *Note*: you **must** run this before pushing your changes to GitHub (i.e. the master branch in GitHub should never have a `_site` or `_build` directory)

## Deploying the site

To deploy the site, you should have tested the updates on master locally, then run the following to build the site on the `gh-pages` branch, then push those changes to GitHub.

If this is the first time you are using the `gh-pages` branch, you will first need to:

```bash
git checkout -t origin/gh-pages
```

Now that you have a local `gh-pages` branch, you can update it with the following:

```bash
git checkout gh-pages
git rebase master
make clean
make book
git add _build
git commit -m "Build site on MM/DD/YY"
git push -f
git checkout master
```