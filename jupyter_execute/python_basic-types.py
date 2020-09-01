# Basic Data Types (bool, int, float, str, list, tuple)

This section will introduce some of the fundamental types in Python. We will learn about:

- `bool`: the binary type
- `int`: the integer
- `float`: the floating-point (decimal) number
- `str`: the string (array) of characters
- `list`: the *mutable* array of objects
- `tuple`: the *immutable* array of objects


## Boolean

Here, we will explore the most basic data type in Python, the **boolean**. Booleans are binary data structures, representing **True** and **False** (or yes/no, on/off, 0/1, depending on the case). In Python, their type is called `bool` and they can have only one of two values, either `True` or `False`. 

We can use the `type()` function to check the type of an object in Python.

type(True)

a = False
type(a)

You may recognize the `bool` type, because we already saw it when we used the `==` equality operator in the previous chapter.

2 == 3

type(2 == 3)

**Bool vs bool**

What do you think happens if we check the equality of two `bool`s? Try it!

True == True

True == False

False == False

**Booleans as integers**

In Python `bool` types have a special property: `True` and `False` can also be treated as the integers `1` and `0`, respectively. You can include booleans in expressions and when they are converted to numbers automatically, it is called **casting**.

45 * False

True + True + True + True + True

What do you think happens when you test equality between a `bool` and `0` or `1`?

True == 1

False == 0

False == 1

This can be useful to know because as the simplest data type, booleans also use the least memory. If you need a large array of exclusively `0`s and `1`s, it will use less memory (and be the exact same), if you store those values as `bool` rather than numbers! 

## Boolean operators

There are two special operators in Python for comparing `bool`. They are `and` and `or`.

The `and` operator is `True` only when *both* of the compared `bool`s are `True`.

True and True

True and False

False and False

The `or` operator is `True` when *one* of the compared `bool`s are `True`.

True or True

True or False

False or False

Recall that Pyhton *evaluates expressions* when it comes time to compare them. Try to figure out if each of the following expressions evaluate to `True` or `False` and then run them to check!

(2 == 2) and (2 == 3)

(1 == 4) or (4 == 4)

(0 == 1) or False

## Integer (int)

The `int` type represents integers: positive and negative whole numbers and 0. 

type(42)

Unlike other languages, Python 3 integers have no fixed size. When they grow too big, they are automatically given more memory by Python, meaning integers have essentially no size limit (Note: this is not true in most other languages! Languages like C can only store `Integer`s in the range (-2147483647, 2147483647) before needing a new data type to handle them). 

a = 2
a

b = a ** 64
b

c = a ** 128
c

print(type(a), type(b), type(c))

## Floating-point numbers (float)

Decimal (or floating-point) numbers in Python belong to the `float` data type. 

type(3.2)

a = -0.11
type(a)

What do you think happens when you combine an `int` and a `float` in a mathematical expression?

2 * 3.2

4.81 / 2

8.99 * 0

Python returns a `float` whenever performing operations on a mix of `int` and `float` types.

**Integer division**

What happens if we divide two `int`s that cannot be expressed as a whole number?

4 / 3

Uh oh! Usually when we have an expression with two `int` types, the result is also an `int`, but in the case of division, two `int` can make a `float`! If we want to force division to return an `int`, we can use the *integer division* operator (`//`).

4 // 3

Integer division returns the *floor* (nearest lower integer) of the quotient. You might imagine that now we dropped the remainder, but may want to know what it is. For this we can use the **modulo** `%` operator.

4 % 3

Now we know that `4 // 3 = 1` with remainder `1` and all of the values are still type `int`!

## Comparison Operators

We already saw a host of *mathematical operators* we can apply to numbers to add, multiply, divide them, etc. We can also *compare* numerical types with handy *comparison operators*. We learned about the `==` comparison operator already. These are the most common comparison operators:

- ` == `: Equal to 
- ` != `: Not equal to 
- ` < `: Less than 
- ` > `: Greater than 
- ` <= `: Less than or equal to
- ` >= `: Greater than or equal to 

**Reminer** 

- The *single equal sign* `=` is the assignment operator for defining variables (`a = 5`). 
- The *double equal sign* is a comparison operator for checking equality (`4 == 5` would return `False`).

3 < 6

4.55 > 7.89

9 != 12.2

What do you think happens if you compare a `float` and `int` with the same value?

4.0 == 4

**Chaining comparisons**

What if we want to know if a given value is between two other values?

x = 5.5
x > 4

x < 6

We can chain comparisons in Python to write this much more simply as the following range:

4 < x < 6

0 < x < 5

## String (str)

In Python, the **string** is used to store text. Strings can be created with either single quotes `''` or double quotes `""`. The PEP8 style guideline does not specify one over the other, just recommends consistency: "Pick a rule and stick to it".

The standard way to get Python to show output as it is running is to use a `print()` statement. The `print()` function attempts to convert the *argument* in parentheses into a string and then shows the result in the shell.

first_str = 'Hello, I am a str type'
print(first_str)

type(first_str)

# Nearly anything in Python can be printed using print()
print(4.2653)

# Remember expressions are evaluated before being passed to functions
print(8*10)

# To print the expression, use quotes ("") to make it a str!
print('8*10')

## Str indexing

A particular **character** in a string can be accessed by its **index**. Python uses the square brackets `[]` to denote indices.

**Note**: Some languages start indexing at 0, and some start at 1. In Python, **indexing starts at 0**.

Python also allows you to use **negative indices** to access characters from the end of the string. The forward and backwards indices are summarized in image below:

![indexing](images/indexing.png)

For example:

mystring = 'Hello World'

#Get the 2nd character in the string
print(mystring[1])

#Get the last character
print(mystring[-1])

## Str slicing

You can also extract a range of characters from a string by taking a **slice**. Slicing in Python is again done with square brackets, but this time we need to provide a start index, a stop index, and a colon `string[start:stop]`.

**Note**: The stop index in Python is *one higher than the last character you want to slice*. E.g. if you sliced from 0 to 3, you would get the 0th, 1st, and 2nd characters (`'Hello[0:3] == 'Hel'`). The character at index 3 is not included!

If you do not provide a start index, Python assumes you want all characters from the beginning of the string to the stop index (`'Hello'[:3] == 'Hel'`). 

Likewise, if you do not provide a stop index, Python assumes you want all characters from the start index to the end of the string (`'Hello[2:] == 'llo'`).

What do you think the slice `'Hello'[:]` produces? Try it and see if you were right.

Also try indexing the string to get various letter combinations.

'Hello'[:]

Indexing and slicing are core concepts in Python that work the exact same way for other data types like the `tuple` and `list`.

## List

A `list` is a common way to store data of arbitrary type in Python (the `list` could contain `bool`, `str`, or even other `list` objects). Lists are defined with square brackets (`[]`).

# An empty list can be assigned to a variable and added to later with append
empty_list = []

# Or a list can be initialized with a few elements
fruits_list = ['apple', 'banana', 'orange', 'watermelon']

type(fruits_list)

Lists elements can be data of any type. You can even mix and match!

medley = [True, 42, 'Hello world!', 3.14159]
print(medley)
type(medley)

Lists are *ordered*, meaning they can be indexed to access their elements with square brackets, much like accessing characters in a `str`. Remember Python indexes starting at 0!

fruits_list[0]

They can also be sliced by providing a range. Remember the end index of the range is *excluded* in Python slices.

fruits_list[1:3]

Lists are also *mutable*, meaning they can change length and their elements can be modified. 

# Let's replace apple with pear (modifying an element)
fruits_list[0] = 'pear'
fruits_list

We can also add an element to the end of a list with the `.append()` method.

fruits_list.append('peach')
fruits_list

Or we can remove and return the last element from a list with `pop()`.

fruits_list.pop()

# Notice that 'peach' is no longer in the fruits list
fruits_list

To understand mutability, let's compare the list with an **immutable** array-like data type, the **Tuple**. 

## Tuples
Tuples in Python are defined with `()` parentheses.

# Tuples are defined similarly to lists, but with () instead of []
empty_tuple = ()
fruits_tuple = ('apple', 'banana', 'orange', 'watermelon')
type(fruits_tuple)

Like the `str` and `list`, the `tuple` can be indexed and sliced to access its elements.

fruits_tuple[0]

fruits_tuple[1:3]

By contrast with the `list` (which is *mutable*), we get an error if we try to change the elements of the `tuple`.

fruits_tuple[0] = 'pear'

Likewise, we cannot change the length of a `tuple` once it has been defined, so the `.append()` and `.pop()` methods do not exist.

fruits_tuple.append('peach')

fruits_tuple.pop()

**Why use a more restrictive version of a list?**

Tuples are less flexible than lists, but sometimes that is *exactly what you want*. 

Say you have a bunch of *constants* and want to make sure that they stay... constant. In this case, a tuple is a better choice to store your data. By using a tuple, you will know if any later code tries to modify your constants - because Python will throw an error! 

We will explore errors (called *exceptions*) in Python more in future sections, but we'll mention here that *exceptions are your friend*. They can tell you when your code is doing something incorrect or unexpected, and help you find exactly where it happened.

## List methods
Let's explore some useful **methods** of the **list**. We have already used the `.append()` and `.pop()` methods above. To see what methods are available, we can always use `help()`.

# Underscores denote special methods reserved by Python
# We can scroll past the __methods__ to see user methods
help(list)

Let's try out the `.index()` and `.sort()`  methods.

pets = ['dog', 'cat', 'snake', 'turtle', 'guinea pig']

# Let's find out what index cat is at
pets.index('cat')

# Now let's try sorting the list
pets.sort()
pets

Sorting a list of strings rearranges them to be in alphabetical order. Lists are not restricted to holding strings, let's see what happens when we sort a list of **Int**.

ages = [12, 24, 37, 9, 71, 42, 5]
ages.sort()
ages

Sorting can be a very useful feature for ordering your data in Python. 

A useful built-in function that can be used to find the length of an ordered data structure is `len()`. It works on lists, tuples, strings and the like.

print(len(['H', 'E', 'L', 'L', 'O']), len((1, 2, 3, 4)), len('Hello'))

## Practice

Make a list of strings with the first 4 words you think of. Call the list `words`, then `print()` it to the console.

# Define your list of words


Now use indexing to return the first letter of the third word.

*Hint*: Recall Python begins indexing at 0. Also recall that both lists and strings can be indexed

# Get the 1st letter of the 3rd word


Sort your list in reverse alphabetical order (without redfining it!), then print it. 

*Hint*: you may want to use the `help()` function on the `list.sort` method

# Sort your list in reverse alpha order then print it


Now make a tuple with the same 4 words you used above and print it to the console.

# Define a tuple with 4 words and print it


Now return the 2nd letter of the 2nd word in the tuple.

# Get the 2nd letter of the 2nd word


Now define a new tuple with the words in reverse order and print it.

*Hint*: the index `[::-1]` may be useful

# Define your new reversed tuple here then print it
