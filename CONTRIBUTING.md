# Contributing guidelines

Contributing to the SPIRL textbook can be a great way to practice your Git-fu and help make this textbook even more useful! Found a typo? Have an idea for a new tutorial? Consider contributing!

## Getting started

A good place to learn how to get started with Git and contributing to repositories like this one on GitHub is... in the SPIRL textbook! Check out the [Git chapter](https://cjtu.github.io/spirl/git_about.html) and particularly the [Practicing Git IRL](https://cjtu.github.io/spirl/git_practice.html) section which will get you up to speed on contributing on GitHub.

## Getting a build set up

The folks at the [Executable Book Project](https://executablebooks.org/en/latest/) have done a great job of making the [JupyterBook](https://jupyterbook.org/intro.html) a textbook / website that you can set up on your local computer in only 6 steps. All you need is a GitHub account and to have [Anaconda installed](https://cjtu.github.io/spirl/anaconda_installing.html). Then:

0. **Fork** the [spirl](https://github.com/cjtu/spirl) repository.
0. **Clone** your fork locally (see [here](https://cjtu.github.io/spirl/git_remotes.html) for a refresher).
0. **Install** the conda environment by entering to the `spirl` directory you cloned and running `conda env create`.
0. **Activate** the conda environment with `conda activate spirl`.
0. **Build** the textbook with `jupyter-book build spirl`.
0. **Open** the textbook in a web browser by putting the path to the `index.html` as the url (e.g. `file:///home/user/spirl/spirl/_build/html/index.html`).

Now you should see a full copy of the local textbook in your browser! You can edit any of the files in the content folder (`./spirl/spirl`), rebuild the site with `jupyter-book build spirl`, and see your changes exactly how they will look on the main site.

## Changing a file

Every page of the SPIRL textbook is either a MarkDown file (`.md`) or Jupyter notebook (`.ipynb`) found in the `./spirl/spirl` directory.

The book supports all standard MarkDown syntax plus the extras available in the MyST flavor of MarkDown (docs [here](https://myst-parser.readthedocs.io/en/latest/)). For an overview of other special types of content you can add, see the JupyterBook docs [here](https://jupyterbook.org/content/myst.html).

Jupyter notebooks will made interactive automatically through the Binder link at the top of the page. **Note**: this link will not work on your local build but will become active on the website once your changes have been added to the main repository. Any cell output that is saved in the Jupyter notebook will appear in the text - if you don't want a certain cell to show its output, make sure to clear it before committing the file.

When you are ready to preview your changes locally, follow steps 4-6 above. Continue to edit and rebuild until you are happy with your changes.

## Adding a new page

The structure of the SPIRL textbook is defined in the table of contents file, `_toc.yml`. This file defines the high level chapters and the order of the pages in each chapter with a links to each page in the spirl content folder. No extension on file names is necessary (e.g. `./spirl/spirl/chapter_page.md` can be specified as `file: chapter_page`).

Pages are named with the convention `chapter_page-name`, where `chapter` is a one word description of the chapter and `page-name` describes the page concisely (one word when possible, hyphenated if necessary).

Check the [issue board](https://github.com/cjtu/spirl/issues) for planned content pages (they may also be listed in `spirl/todo`) to make sure nobody else is working on them already. Feel free to comment to take on a new page or open a new issue with a new page idea. If you would like to add a new chapter, please first open an issue and discuss your idea with the maintainers.

## Contributing your changes

When you have built your changes locally and proofread your content on the local version of the website, you can push your changes to your fork and open a pull request! You will receive feedback on your PR and may need to update and commit new changes which will be added to your PR automatically. When all of the changes look good, your PR will be merged and the site will be built automatically. You can check the [Actions](https://github.com/cjtu/spirl/actions) page to check the progress of your accepted PR. If all of the Actions have green checkmarks, your changes are live and you can see them at [cjtu.github.io/spirl](https://cjtugithub.io/spirl)! Thanks for helping make this resource even better!

## I want to make my own JupyterBook

The JupyterBook docs are quite good and available [here](https://jupyterbook.org/start/overview.html). SPIRL is currently deployed using GitHub pages, a free static website hosting service provided by GitHub (learn more [here](https://pages.github.com/)). You can register your own domain url or use the default `username.github.io` provided for free by GitHub. Although it took a little more setup, you can also set up a GitHub Action to automatically deploy your website on every new commit by using the Action [here](https://github.com/peaceiris/actions-gh-pages). Check out the SPIRL GitHub Pages actions configuration file at [gh-pages.yml](https://github.com/cjtu/spirl/blob/master/.github/workflows/gh-pages.yml) for reference.
