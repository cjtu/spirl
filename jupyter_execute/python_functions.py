# Methods
Classes have special functions defined only for their own members called class methods, or simply **methods**. Methods are called on an object by following that object with `.methodname()`. We saw methods like `.isround()` in action above. Built-in classes like `str` have methods too!

# The upper() method changes all characters in a string to uppercase
introduction = 'Hi, my name is...'
introduction.upper()

# The isdigit() method checks if all characters in a string are digits
'12345'.isdigit()

Using the `help()` function on a class shows all methods available to instances of that class. The `__methods__` are private methods used internally by Python. Skip down to `capitalize(...)` to see the methods available to us.

help(str)

# The capitalize method capitalizes the fist letter of the str
'united states'.capitalize()

# Functions
Functions are like methods but are independent of a specific class. Any objects that they act on must be passed in as arguments. Let's break down the anatomy of a function.

```Python
def funcname(arg1, arg2):
    """Docstring"""
    # Do stuff here
    return output
```

All functions start with a `def` or **define** statement, followed by the name of the function and a list of arguments in parentheses. 

Below the `def` statement is the **docstring** in triple quotes `""" """`. Docstrings are important for humans (including you) who need to read / use your code. The docstring explains what the function does, what arguments the function needs to work properly, and can even suggest example usage. The docsting is what is shown when you call `help(funcname)` on your function.

As we saw with the if blocks, Python uses indentation to organize code. All code indented in the function definition will be run when the function is called. 

Finally, if your function produces an output, it must be **returned** with a `return` statement. This signals the end of the function. Python will pick up where it left off before running the function.

Let's work through an example. Say we encounter the following function `stuff()`. We may not know what it does initially if we don't know where it is defined. Let's try calling `help()`.

def stuff(a):
    return a**2
help(stuff)

Hmm. Not very descriptive. And the name of the function is not exactly helpful. I guess we need to try some examples to figure it out.

stuff('hello?')

Well it didn't like the `str`, so let's try an `int` instead.

stuff(1)

Now we're getting somewhere, maybe `stuff` returns the number it is given!

stuff(2)

There goes that idea. But this looks like it could be pattern.

print(stuff(1),stuff(2),stuff(3),stuff(4),stuff(5))

Cool it looks like `stuff` takes the square of the number it is given! Now to do the same trial and error with the function `allxsonthelistorunderbutnotboth(x1, x2, x3, x4, x5, x6, list1, list2)`. Uhh...

That was an example of writing a function with poor *style*. The function worked as intended, but was frustrating to use if you didn't remember what `stuff()` did. I hope this highlights the importance of readable code. Python comes built-in with features like the **docstring** to avoid situations like the one above. Python won't force you to use docstrings, but it is highly encouraged to get into the habit, especially if you are working with others. And if not for others, do it for future you who won't remember what `stuff()` is in 6 months.

So how do we improve our `stuff()` function for squaring numbers? The first step is giving it a self-evident name, e.g. `square(num)`. Next, we can add a docstring with a description `"""Return the square of num"""`. Finally, we can describe the parameters, return values and provide a couple examples of how to use it. Altogether, it might look like this.

def square(num):
    """Return the square of num.
    
    Parameters
    ----------
    num: int, float
        The number to square.
        
    Returns
    -------
    int, float
        The square of num.
        
    Examples
    --------
    >>> square(2)
    4
    >>> square(2.5)
    6.25
    """
    return num**2

Say we encounter `square()` in the wild and want to know how to use it. Now we can call `help(square)` and see a nicely formatted docstring.

help(square)

We can even try the examples it provides to ensure the function is working properly.

print(square(2), square(2.5))

Much less frustrating! 

*Style* is an aspect of writing code that is often overlooked in sciences. Just like writing good `git commit` messages, it is very important to write code in a way that future you and future collaborators will be able to read and use.

Another aspect of style is knowing when to break your code down into functions that perform small tasks. This is one of the hardest, but most useful programming skills to master. If you can define function(s) for complex / repetitive code and give those functions good names and good docstrings, you are on your way to writing readable, re-usable code!

Your turn!

## Breaking code down into functions
The following example is long and repetitive. See if you can define functions to shorten and simplify the code, and get the same result.

In this example, we want to see if 3 people like apples, oranges, and are above the age of 20. The data is formatted as such:

person = 'likesapples likesoranges age'
```Python
person1 = 'yes yes 13'
person2 = 'yes nah 21'
person3 = 'nah nah 80'
```

We want to `print('It's a match!')` if all 3 people like apples and oranges and are older than 20. Otherwise, `print('It's not a match!')`.

person1 = 'yes yes 42'
person2 = 'yes yes 64'
person3 = 'yes yes 80'

# Uncomment these three for an example of not a match
# person1 = 'yes yes 13'
# person2 = 'yes nah 21'
# person3 = 'nah nah 80'

if person1[0:3] == 'yes' and person1[4:7] == 'yes' and int(person1[8:]) > 20:
    if person2[0:3] == 'yes' and person2[4:7] == 'yes' and int(person2[8:]) > 20:
        if person3[0:3] == 'yes' and person3[4:7] == 'yes' and int(person3[8:]) > 20:
            print("It's a match!")
        else:
            print("It's not a match!")
    else:
        print("It's not a match!")
else:
    print("It's not a match!")

# Put your function version of the above code here
# Don't forget the docstrings!




There are many possible ways to break up code into functions. How specific you make your functions depends on your particular use case. If you want to see my solution, you can copy and paste it from [here](https://github.com/cjtu/sci_coding/tree/master/lessons/lesson3/data/function_solution.py) and compare with yours!


Great job! You made it to the end of the crash course on objects, methods and functions (oh my). Next, we will be working with `Lists and Tuples`.