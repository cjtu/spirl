# Anaconda

One of the strengths of using Python for scientific programming is its myriad **packages** which allow you to install and use code developed by others in your own programs. Since Python has become ubiquitous in data science, many packages for statistical analysis, working with large data sets, and training machine learning models have been written and made available for free as open source Python packages.

## Anaconda Package Manager

[Anaconda](https://www.anaconda.com/) is a tool which simplifies the installation and management of Python packages (and now even provides some other tools used in data science). Using a package manager like Anaconda is useful because of *dependencies* and *dependency conflicts*.

## Dependencies

Whenever you write an `import <package>` statement, you have introduced a **dependency** into your code. This simply means that in order to run your code, a collaborator would first need to install the package that you imported.

Almost all packages have one or more dependencies because importing well-tested packages is often preferable to re-inventing the wheel and writing code and tests from scratch (this is true in your programming endeavors too!). Installing many code packages which can depend on other code packages can sometimes lead to headaches - especially since many Python packages are actively being developed and have different (sometimes incompatible) versions.

Take the following example, where we want to use packages B and C:

- want to install package B
  - package B depends on package A (version 1.0)
  - install package A  (version 1.0)
  - install package B
- want to install package C
  - package C depends on package A (version 2.0)
  - upgrade package A to version 2.0
  - install package C
- does package B still work?

Say the package A upgrade from version 1.0 -> version 2.0 removed or renamed some functions used in package B. Now package B might not work as intended, meaning package B and C have a **dependency conflict**. This can introduce sneaky bugs into your programs in code that you didn't even write!

## Conda to the rescue

The central tool offered in Anaconda, the `conda` package manager, helps automagically solve our dependency headaches.

In this section, we will cover how to get Anaconda, how to use `conda` to install new Python packages, and how to make *conda environments* to organize packages that we install for different projects.
