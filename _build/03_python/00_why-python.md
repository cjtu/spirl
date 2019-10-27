---
redirect_from:
  - "/03-python/00-why-python"
title: 'Programming in Python'
prev_page:
  url: /02_git/03/03_more-practice.html
  title: 'More practice'
next_page:
  url: /03_python/01/00_why-style.html
  title: 'Style'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Programming in Python

Programming is a dialogue between you and your computer. With the right words - and a little persuasion - you can tell your computer to do more work in an instant than you could do in a lifetime. Programming is possibly the most in-demand skill in 2019, and has become ubiquitous in the sciences due to the enormous datasets, statistical analyses and complex simulations enabled by the recent explosion in computing power. 

In this chapter, we will explore the Python programming language and learn some fundamentals that will have you writing correct and efficient programs in no time.

## Why Python?

Python has quickly risen in popularity among programmers and scientists alike. It is relatively young language compared to **C** and **JAVA**, but is has become the [third most popular programming language](https://www.tiobe.com/tiobe-index/) as of 2019. One reason Python has become so popular is that it is *relatively easy to read and learn*. Python was designed to put **style** and **readability** first, making it easier for beginners to pick up and for experts to prototype programs quickly.

A major reason we chose Python is because of its emergence as an industry (and academic) standard. There are countless online resources - and [StackOverflow posts](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) - to help learn and troubleshoot Python. Freely available **open-source** tools are actively being made and updated for Python, allowing us to do scientific analysis, image processing, and machine learning without reinventing the wheel.

### But isn't it slow?

Python detractors give it a bad rap, saying things like "Python is slow compared to C, Java and FORTRAN (or other language of choice)". This is sometimes true because Python is an **interpreted language**, meaning each line of code is run one at a time. Programs written in C or FORTRAN are **compiled** into highly optimized machine-code before being run, meaning the same program *could* be faster.

In practice, the efficiency gains are often minor compared to the larger time investment it takes to craft programs in the compiled language of choice. If the language lacks a robust, optimized numerical data package like `numpy`, you may need to write a lot of code from scratch (most of which is likely not as optimized `numpy` package which has been developed by dozens of computer scientists).  

Another reason Python is a good choice is because it is more *legible* than many compiled languages. Being able to read and understand programs quickly reduces the chances of making errors in the code (debugging code is much more time consuming than writing it). It is infinitely better to have a *slower and correct* program than a *speedy, but broken*.

## Style

This chapter will also give a brief introduction to programming style which are a set of best-practices to keep in mind whenever you write code. Having good style will make your programs easier to debug and re-use later; future you will thank you.
