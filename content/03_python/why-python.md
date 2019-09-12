# Programming in Python

Programming is a dialogue between you and your computer. With the right words - and a little persuasion - you can tell your computer to do more work in an instant than you could do in a lifetime. Programming is possibly the most in-demand skill in 2019, and has become ubiquitous in the sciences due to the enormous datasets, statistical analyses and complex simulations enabled by the recent explosion in computing power. In this chapter, we will explore the Python programming language and learn some fundamentals that will have you writing correct and efficient programs in no time.

## Why Python?

Python has quickly risen in popularity among programmers and scientists alike. It is relatively young language compared to heavy-hitters like **C** and **JAVA**, but is has become the [third most popular programming language](https://www.tiobe.com/tiobe-index/). One reason Python has become so popular is that it is *relatively easy to read and learn*. Python was designed to put **style** and **readability** first, making it easier for beginners to pick up and for experts to prototype programs quickly.

Python makes a great learning-language for beginners because once you know the basic syntax (vocabulary), many programs you write will read almost word-for-word as you would describe them in plain English. This is not to say that learning the ins-and-outs of Python or any programming language is easy. Like any language, Python takes a lot of practice - and learning from mistakes! - to master.

Two other reasons we use Python is because it is **open-source** and **well supported**. A large community has grown around developing excellent **open-source** (free and easily modified) tools for Python. Many well-tested packages for scientific analysis, image processing, and machine learning have been written specifically for Python and are freely available for the public. 

In later chapters, we will explore how to find, install, and manage Python packages to take advantage of the huge body of open source tools that you can use to save time and effort in your research.

### But isn't it slow?

Python often gets a bad rap compared to C, Java and FORTRAN (compiled or partially-compiled languages) because it is an **interpreted language**. This means each line of code is run one at a time rather than having a whole program being **compiled** into a highly optimized machine-code before being run.

The challenge with using compiled languages is that the efficiency gains often requires a deep understanding of how compilers work (e.g. a computer science degree) and require the use of less legible, less intuitive programming languages (which make errors harder to spot and code harder to modify). It is infinitely better to have a *slower and correct* program than a *speedy, but broken* program.

Additionally, speed is rarely a problem in practice because Python is very flexible. If you ever need to make your program faster, you can run compiled programs written in other languages (e.g. C) without ever leaving Python. A more likely scenario is that there is already an open source Python package which makes parts of your program run in C without you even knowing it (e.g. `numpy` arrays are very fast because they use C under the hood, but you only need to know Python to use them).

## Stylish code

This chapter will also give a brief introduction to programming style which are a set of best-practices to keep in mind whenever you write code. Have good style will make your programs easier to debug and re-usable later, making future you much happier.
