# Python Style

One of the reasons Python has exploded in popularity is its *readability*. Python has **style** built-in to its design, forcing you to indent certain parts of your code and using many language elements that make *pythonic* code read almost like plain English. For example, the following code is valid python and you can probably guess what it does even if you've never read Python before:

```{code-block} python
if number in list:
    list.remove(number)
```

**How do I write clear, pythonic code?**

The Python community has published several *style guidelines* which give best practices for making your code easier to read and easier to run.

This section summarizes a few core best practices for making your code readable so that future you (and your future collaborators) can understand how and why you designed your code the way you did.

## The Zen of Python

The following poem by Tim Peters summarizes some of the central tenets of Python style. It is so revered that it has been in every version of Python since 2004 (read more [here](https://www.python.org/dev/peps/pep-0020/)).

You can print **The Zen of Python** to the screen if you type `import this` in any Python prompt. Don't worry if it reads like a riddle right now - I encourage you to re-read it at different points in your Python learning journey!

```{code-block} python
import this
```

> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.  
> Complex is better than complicated.  
> Flat is better than nested.  
> Sparse is better than dense.  
> Readability counts.  
> Special cases aren't special enough to break the rules.  
> Although practicality beats purity.  
> Errors should never pass silently.  
> Unless explicitly silenced.  
> In the face of ambiguity, refuse the temptation to guess.  
> There should be one-- and preferably only one --obvious way to do it.  
> Although that way may not be obvious at first unless you're Dutch.  
> Now is better than never.  
> Although never is often better than *right* now.  
> If the implementation is hard to explain, it's a bad idea.  
> If the implementation is easy to explain, it may be a good idea.  
> Namespaces are one honking great idea -- let's do more of those!  

## Official style guide (PEP8)

PEP 8 ([link](https://www.python.org/dev/peps/pep-0008/)) is a guide written by the creator of Python, Guido van Rossum, and is updated by the Python community. It specifies best practices for how long your lines should be, how to write clearer equations, and how to name your variables and functions.

Here are some examples of completely working Python code that adheres to and breaks the PEP8 standard:

```{code-block} python
# Whitespace around operators (but not parentheses)
# Use space to indicate order of operations "2*2 + 4"
y=exp( 2-x,(4 * z+7) )  # Not PEP8
y = exp(2 - x, 4*z + 7)  # PEP8

# Max line length: 79
# Variables use underscores, not camelCase
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]  # Not PEP8
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]  # PEP8
```



A core part of programming style is **consistency**. Some of the PEP8 style guidelines seem arbitrary or pedantic, but having one set of best practices allows all Python code to look similar. Once you are learn to read PEP8-compliant code, it makes all future PEP8 code so much easier to read because you know what to expect.

The same is true for both *future you* and *your collaborators*. One of Python's guiding principles is that **code is read much more often than it is written**. Therefore, taking some time to practice good *style* (e.g. by using the PEP8 guidelines wherever possible) will help you when you inevitably need to come back and read, update, and debug your code.

## Comments
 
Always write code for your future self who is sleep-deprived, has completely forgotten how it looks after 6 months of not coding, and is trying to run it right before a big deadline. **Future you** is the #1 person who benefits from writing understandable code. A big part of this is adding good, descriptive **comments**. 

Every programming language provides a way to add *comments*, some text in your code which is completely ignore by the computer running it, but can be critical for future you to remember how that code works.

Good comments can take seconds to write and save you hours of trying to remember how a piece of code works. .
 
## Python Comments

A comment in Python is ignored when the code is actually run.

```bash
# Single line comments use the pound symbol
```

PEP8 recommends two spaces before and 1 space after the `#` for comments following a line of code

```bash
print('Hello World')  # Everything after the pound is ignored
```

If the line exceeds 79 characters, PEP8 recommends putting them on their own line (or lines if they remain too long).

```bash
# I have a comment that would be longer than 79 characters on the next line
print('Hello World')

# I could have also split it up onto multiple lines
# each one starting with the "#" symbol
```

## Tips for Writing Good Comments

Comments should always **add** to the readability of your code. If they are long or confusing themselves, this may suggest that your code is too complicated as is and may need to be split into more steps or [functions](python_functions).

**When commenting, DO:**

- Be concise
- Add them to describe parts of your code which you found tricky (if you found it tricky now, imagine sleep-deprived future you trying to understand it)
- Organize high level sections of your code using comments to keep track of the organization.
- Consider simplifying complex parts of your code rather than commenting it.

It can also be helpful to sketch out your code in comments before you start. This can help you figure out the high level flow of the code before you get bogged down in too many coding details.

**When commenting, DON'T:**

- Be too vague. Explain your code like you remember nothing
- Be too specific. If it is obvious what a line does, no need to repeat it in the comment.
- Repeat exactly what the code says. For example:

```bash
y = exponential(x)  # takes the exponential of x
print(y)  # prints y
```

It is possible to *overcomment*. If it is clear what a line does (good variable and function names help with this!), then it doesn't need a comment. Adding additional information where it is unnecessary creates a wall of text, making your code harder to read. Try to save comments for when you can't immediately see what one or more line do just by looking at them.

How often you should comment is **highly individual** and will likely shift as you get better at reading and understanding code. It is better to err on the side of commenting more when starting out. **The only wrong number of comments is 0!**

## DRY - Do Not Repeat Yourself

The **D**o not **R**epeat **Y**ourself (**DRY**) principle encourages us to not repeat lines of code.

We shouldn't repeat ourselves according to the **DRY** principle.

Whenever possible, **DRY** say to.... you get the point.

Instead of copy and pasting code multiple times in our programs, DRY encourages us to write code once and re-use it.

**Why write DRY code?**

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

## Tips for Writing Dry Code

Most programming languages have common built-in concepts that make it easy to re-use code. You will learn how to use these in Python in the upcoming sections:

**Functions**

A function is a reusable block of code that performs a specific task. Having functions for mundane tasks can make your code more readable and maintainable.

For example, say we have a 5-line code block that computes the location of an object given its x, y, z position and speed. Now say we need to do this computation one hundred times in our code. That's 500 lines of code!

Now say we put that 5-line code block in a function called `get_location(x, y, z, speed)`. Now we only need to call `get_location()` one hundred times. We reduced our program from 500 lines to 100 by using a function!

**Loops**

A loop is a way to repeat a set of instructions to repeat a set of instructions to repeat a set of instructions multiple times.

In our example above, we needed to `get_location()` one hundred times. If instead we used a *loop*, we could do those 100 repeats in only a couple lines:

```bash
for i in range(100):  # i.e. do the following 100 times
    get_location(x, y, z, speed)
```

Now our 100 line program is only 2 lines! Now imagine we wanted to `get_location()` 1 thousand times. Or 1 million times! Loops can significantly reduce repeated code by *doing the repetition for us*!

## Summary

**Style** and **readability** are central aspects of programming in Python. There is a single set of generally accepted style guidelines called [PEP8](https://www.python.org/dev/peps/pep-0008/) which should be followed whenever possible (sometimes it isn't possible and that's ok!). Commenting code is a good habit to build and commenting effectively takes practice! When in doubt, write for the future you who doesn't remember anything about your code. DRY (Don't Repeat Yourself) programming is a way to think about code that will make programming less work overall. If you find yourself copy / pasting code, think DRY and see if a [function](python_functions) or [loop](python_loops) could help you cut down on repetition.

