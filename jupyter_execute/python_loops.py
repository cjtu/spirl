# Loops

Loops are useful programming concepts that you will find in just about every lanugage because they allow us to repeat a set of instructions many times. We discuss in the [style](python_style) section how loops can help do repetitions for us, so we don't need to repeat code. 

Python has two types of loops, the **for** loop and the **while** loop. Any repeated task can be done with *either kind of loop*, but as we'll see, you might prefer to choose one type over the other in certain scenarios.

## Indentation

In Python, blocks of code are denoted by their *indentation level*. A loop will repeat only the lines which are indented, then stop once the indentation returns to normal. In the following example, the two indented lines are repeated, but the final line only runs once because it is outside the loop (back to normal indentation).

for i in (1, 2, 3):
    result = i**2
    print(result)
print("Finished!")

## For loop

A **for loop** is most often used to *iterate* through a collection of objects like a `list`, `tuple`, or `string`. At each *iteration*, we get access to the next element in the collection and can do some work on that element. 

squares = [1, 4, 9, 16, 25]
for square in squares:
    print(square)
print("We printed", len(squares), "squares")

In the above example, the `squares` list is the collection we are looping through, and `square` is a variable that Python re-defines every iteration to be the next element in `squares`.

Iteration by iteration, we get:

- On the *first* iteration, `square == 1`
- On the *second* iteration, `square == 4`
- On the *third* iteration, `square == 9`
- On the *fourth* iteration, `square == 16`
- On the *fifth* iteration, `square == 25`
- After `25`, there are no more elements in `squares`, so the loop ends and Python runs the next unindented line (the final `print()` statement)

We can choose any variable name that we'd like when define the for loop, it didn't have to be `square`.

squares = [1, 4, 9, 16, 25]
for x in squares:
    print(x)
print("We printed", len(squares), "squares")

squares = [1, 4, 9, 16, 25]
for jack_russell_terrier in squares:
    print(jack_russell_terrier)
print("We printed", len(squares), "squares")

**Aside: Good naming conventions**

As we have said before in this text and will say again: 

- good naming conventions will save you a lot of future headaches

It is good *style* to name our variables something *expressive* that reveals what they are. For example, in the `squares` list above, each element is a square number, making `square` a more logical choice for our loop variable than `jack_russell_terrier` (regardless of how much cuter our code is with dogs).

**Readability**

When we use *good naming conventions* in Python, something **magical** happens: most of the code you write will read like *plain English* (with a couple words inferred here and there).

For example, if we wanted to describe what the loop above did, we could say:

- Go through the list of squares one element at a time, and **for each square in the list, print the square**


In Python code (with *expressive names* for our list and loop variable), we can translate it to Engligh by adding very few extra words:

```Python
for square in squares:  # for [each] square in [the] squares [list],
    print(square)  # print [the] square
```

## Range

A useful built-in function that we commonly use in *for loops* is `range()`. Range is a quick way to make sequence of numbers to loop through.

r = range(5)  
print(type(r))
print(r)

It seems like `range` is its own type in Python. Let's see what happens when we loop through a `range` object:

for i in range(10): # Loop through numbers 0 to 9
    print(i)

If we want to start at another value, we can specify two arguments in `range()`, the `start` and `stop`:

for i in range(37, 42):
    print(i)

*Note*: Like when slicing, the end index is excluded from the range. This way, if you specify a range from `(37, 42)`, there are `42-37 = 5` numbers in the range, as printed above.

We can also change the spacing of the elements in our range by specifying a *third* argument to `range()`.

for i in range(0, 15, 3):
    print(i)

Often the `range()` function is useed to get *indices* to loop over, and it's convention to reserve `i`, `j`, and `k` for *index variables*. When we loop over the indices of a `list`, `tuple`, or `string`, we can then access each item one at a time with that index.

fruits = ['banana', 'apple', 'pear', 'tomato']
for i in range(4):
    print("We are on index", i)
    print(fruits[i])

We commonly want to loop through all of the elements of a collection of items, like in the code block above. To do this in general (without needing to count up all the elements to pass as a number to range), we can just pass in the `len()` of that collection. This allows us to always loop to the end of the collection, *even if its length changes*.

fruits = ['banana', 'apple', 'pear', 'tomato']
for i in range(len(fruits)):
    print(i, ":", fruits[i])
    
fruits.append('pineapple')
fruits.append('plum')
print("\nOh no! Added more fruit!\n")

for i in range(len(fruits)):
    print(i, ":", fruits[i])

## Enumerate

We will often want to loop a collection of items, but also want to know the indices of those values. To do this, we can do the following which works, but is a little messy:

vegetables = ['carrot', 'lettuce', 'zucchini']
for i in range(len(vegetables)):
    print("Index", i, ":", vegetables[i])

Alternatively, we can use the `enumerate()` function, which is a shortcut to get the *index* **and** *value* in each iteration of the loop. 

*Note*: `enumerate()` completely replaces the ugly `range(len())` and allows us to pick a good variable name for our loop variable!

for i, vegetable in enumerate(vegetables):
    print("Index", i, ":", vegetable)

## Practice for loops

1. Sort the following list of names in alphabetical order (by first name)
2. Loop through the list and 
  - print the rank of the name in alphabetical order
  - print the last name of the person at that rank

Hints: the list method, `.sort()`, and the string method `.split()` may be useful. Also your ranking should start at 1 (not 0)!

cool_scientists = ['Marie Curie', 'Jane Goodall', 'Vera Rubin', 'Mae Jemison', 
                   'Rosalind Franklin', 'Donna Strickland', 'Frances Arnold']

# Write and test your solution here



## While loops

A while loop is similar to the **for loop**, except it is defined in terms of a *end condition*, rather than a collection of elements.

While loops should be used when you need to loop *until a condition is met*, often in these cases, we do not know how many iterations we will need to complete.

capacity = 100
people = 0
while people < capacity:
    people += 10
    print("Number of people:", people)
print("We're at capacity!")

Let's unpack the example above:

- Initially, `people` (0) begins *less than* `capacity` (100), so the while condition is `True` and we enter the loop
- Each iteration, we increase `people` by 10
- After 10 iterations, `people` is *greater or equal to* capacity, so the while condition is no longer `True` and we exit the loop
- Finally we continue running the next line outside the loop (the final `print()` statement)

Although you generally want to use a **for loop** to iterate over a collection of elements, we can also accomplish the same thing with a while loop, but we have to keep track of our iterator variable manually.

dogs = ['husky', 'poodle', 'greyhound', 'boxer', 'shibe']
i = 0  # we need to define our iterator before the loop
while i < len(dogs):
    print(dogs[i])
    i = i + 1  # Don't forget to increment the iterator!
print("Much wow! Many dog!")

What do you think happens if we left out the `i = i + 1` line? Think about the `i < len(dogs)` condition. If you're brave, run the next code block:

dogs = ['husky', 'poodle', 'greyhound', 'boxer', 'shibe']
i = 0  # we need to define our iterator before the loop
while i < len(dogs):
    print(dogs[i])

With while loops, it is very important to make sure that the loop can *terminate*, that is, that the while condition will become `False` at some point. Otherwise we can get sneaky infinite loops in our code.

## Practice while loops

Say we want to see how many times we can (integer) divide a number by 2 before it is less than or equal to 1. We don't know how many times we need to divide the number when we start, but we do know when to stop. We should use a while loop!

Write the condition that allows the following code to terminate correctly:

num = 99
count = 0
while False:  # replace False with the correct condition
    num = num // 2
    count += 1
print("The base 2 log of 99 is", count)

Given the following list,

1. sort the list in alphabetical order (by first name)
2. using a **while loop**, print each name that starts with a letter before 'n'

Hint: try comparing two letters, e.g. `a < e` or `f < b`

cool_scientists = ['Marie Curie', 'Jane Goodall', 'Vera Rubin', 'Mae Jemison', 
                   'Rosalind Franklin', 'Donna Strickland', 'Frances Arnold']
# Write and test your solution here

