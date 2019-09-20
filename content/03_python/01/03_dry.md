# DRY - Do Not Repeat Yourself

The **D**o not **R**epeat **Y**ourself principle encourages us to not repeat ourselves. We shouldn't repeat ourselves according to the **D**o not **R**epeat **Y**ourself principle.

Good DRY programmers DO NOT:

- copy and paste code

Good DRY programmers DO:

- write code once and re-use it

## Why write DRY code?

Really, DRY is all about being lazy! Re-using code makes your life easier. Programming with DRY in mind can also prevent common issues. Imagine the following scenario:

```Python
a = awesome_fucntion(0)
b = awesome_fucntion(0)
c = awesome_fucntion(0)
d = awesome_fucntion(0)
e = awesome_fucntion(0)
f = awesome_fucntion(0)
g = awesome_fucntion(0)
```

We copy and pasted our function many times (maybe in different places in the code). Later, we realize that we misspelled `awesome_function`. Now we have to go search through the code for all the times we copy and pasted that typo! Oh no!

Also, if you're keen you may notice that we are calling `awesome_function()` on the same value every time and simply storing it in different variables instead of re-using the result.

If we use the DRY principle, we would only call `a = awesome_function(0)` once and reuse the variable `a` throughout our code. This way, if we realize we made a typo - or we want to swap out `awesome_function()` for `better_function()` - we only need to fix it in one place:

```Python
a = better_function(0)
```

Whenever you write code that you think you will need to reuse, think **DRY**. Re-usable code can generally be written into a **function** (we will how to write functions in a future lesson). The function can then be called each time you want to perform that task. Now if you edit the function, your changes will propagate throughout the entire program!

DRY code is generally more readable and easier for future you to modify and understand.

## Ways to Write Dry Code

Most programming languages have common built-in concepts that make it easy to re-use code. You will learn how to use these in Python in the upcoming sections:

### Functions

A function is a reusable block of code that performs a specific task. Having functions for mundane tasks can make your code more readable and maintainable.

For example, say we have a 5-line code block that computes the location of an object given its x, y, z position and speed. Now say we need to do this computation one hundred times in our code. That's 500 lines of code!

Now say we put that 5-line code block in a function called `get_location(x, y, z, speed)`. Now we only need to call `get_location()` one hundred times. We reduced our program from 500 lines to 100 by using a function!

### Loops

A loop is a way to repeat a set of instructions to repeat a set of instructions to repeat a set of instructions multiple times.

In our example above, we needed to `get_location()` one hundred times. If instead we used a *loop*, we could do those 100 repeats in only a couple lines:

```bash
for i in range(100):  # i.e. do the following 100 times
    get_location(x, y, z, speed)
```

Now our 100 line program is only 2 lines! Now imagine we wanted to `get_location()` 1 thousand times. Or 1 million times! Loops can significantly reduce repeated code by *doing the repetition for us*!

### Think DRY

We will learn about functions and loops in future sections. As you write your first Python programs, remember to think DRY and *Do not Repeat Yourself* wherever possible.
