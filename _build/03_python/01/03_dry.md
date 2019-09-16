---
redirect_from:
  - "/03-python/01/03-dry"
title: 'DRY programming'
prev_page:
  url: /03_python/01/02_comments.html
  title: 'Comments'
next_page:
  url: /03_python/01/04_pep8.html
  title: 'Style guide (PEP8)'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# DRY - Do Not Repeat Yourself

The do not repeat yourself principle in Python is exaclty what it sounds like. Don't re-write the same code multiple times, don't copy and paste code where you need to make changes in multiple places. Write code once and use it.

## Why write efficient code?

Really, DRY is all about being lazy! It makes your life easier. But it also prevents some common issues - for example writing multiple lines of code to do something, copy and pasting that elsewhere where you need to do the same thing. Chances are you'll change that code at some point - now you need to track down every location you have a copy of this and make the same change multiple times. This is a lot of work! It wastes time and increases the chance of making a mistake.
Instead, when code it reused it should be written into a function. This function can then be called each time you need to perform that task, and any changes easily propogate throughout the entire program. Writing code efficiently (with DRY) makes it easier for you and your future self to understand, more readable, and ensures reproducability.

## Ways to Write Dry Code

There are several easy ways to convert long code into shorte, repeatable bits. These concepts will be listed here, but you will learn how to implement these in Python in the upcoming sections.

**Loops**
A loop is a way to loop through a list of variables. You can perform a task on each variable in a list, instead of coding the task for each variable separately. The advantage of this is clear when you imaging a list with 10,000 items in it.

**Conditional Statement**
A conditional statement checks whether a certain condition (for example True of False) exists before code is executed. This allows you the ability to control the flow of your code and only perform a task when specific condtions are met.

**Functions**
A function is simply a reusable block of code that performs a specific task. It is organized so that you only need to type the name of the function and any inputs in order to perform that task. Using functions improves efficiency and allows you to write modular code - where you organize units of code into functions that can be reused (by yourself or others), without needing to understand all of the specific details.
