# Advanced Data Types (set, dict)

In this section, we will explore some more advanced data structures that Python provides.

The **set** is a unique collection of items which work much like mathematical sets.

The **dictionary** is a key-value store of data, which is one of the most efficient and flexible data structures in Python.

We will start this section off with the `set`!


## Set

The `set` is a data type in Python which stores only unique elements in no particular order. In this way, the set works much like a *mathematical set*, and even has methods that perform set operations. 

## Defining a set

Sets in Python are defined with curly braces `{}` in Python. 

pets = {'dog', 'cat', 'hamster', 'fish', 'snake'}
type(pets)

The `set` is not concerned with duplicate items, in fact it doesn't matter how many copies of an item you pass to a set, that item will only be included once!

my_favorite_animals = {'dog', 'dog', 'dog', 'dog', 'cat'}
print(my_favorite_animals)

Sets also **not ordered** meaning they do not always print in the same order that items were added. Two sets are equal as long as they contain the same objects, regardless of the order they were added.

a = {0, 1, 2}
b = {2, 0, 1}
a == b

**When would I use a set over a list?**

You may want to quickly see how many unique items you have. For example, say our shopping cart is poorly organized and we want to see if we got all the different items on our grocery list.

cart = {'apple', 'pear', 'tofu', 'milk', 'apple', 'apple', 'orange', 'rice', 
        'pasta', 'pear', 'milk', 'pear', 'grapes', 'orange', 'apple'}
print(cart)
print("We bought {} different items".format(len(cart)))

```{note}
Sets can only contain **immutable** objects like the `int`, `float`, `str`, and `tuple`. The types are called "hashable" in Python. If you try to pass a **mutable** object like a `list`, you will get the following `TypeError`:
```

set_of_list = {[1, 2, 3]}

**Convert to set**

To quickly see the unique elements of a list or tuple, we can convert it to a set with the built-in `set()` function. The following example will show how useful this can be.

my_list = [3, 2, 0, 3, 3, 3, 0]
my_set = set(my_list)
print(my_set)

## Set methods


In the help info for `set`, we might notice that we can use mathematical set operations like `union()` and `difference()`.

help(set)

Going back to our shopping list example, say you list and cart look like:

grocery_list = {'milk', 'eggs', 'tomato', 'apple', 'pasta'}
cart = {'apple', 'apple', 'tomato', 'chocolate', 'milk', 'eggs', 'eggs', 'tomato', 'apple', 'chips', 'tomato', 'milk'}

We can quickly see what items in the cart are missing from the list using `set1.different(set2)`.

grocery_list.difference(cart)

The difference operation can also be achieved with the minus (`-`) sign.

grocery_list - cart

If we do the set difference the other way, we can see what items snuck into our cart that weren't on our grocery list....

cart - grocery_list

If we want to see what all of the unique items in both sets, we can use the `.union()` or `|` operator.

grocery_list.union(cart)

grocery_list | cart

We can also use the `.intersection()` method or `&` operator to see the overlap between sets (the items in our cart that actually were on the grocery list).

grocery_list.intersection(cart)

grocery_list & cart

Great, hopefully the unordered `set` makes a little more sense now. We are now ready to learn one of the most useful data types in Python, the Dictionary (`dict`).

## Dictionary (dict)

The dictionary is similar to the set in that it is an **unordered** collection of **unique** items. Dictionaries very efficiently store **key-value** pairs of data. 

## Keys and Values

In dictionaries, we need to provide a *name* or **key** to store our data. This **key** is how we will find our data later. Dictionary keys must be immutable (i.e. *hashable*), most commonly an `int` or `string`.

The **value** is any object we would like to store in the dictionary at the specified key. The value can be of any type, making the `dict` object extremely flexible.

The `dict`, like the `set`, is defined with `{}` curly braces, but each element must be colon `:` separated key-value pair (**key** `:` **value**).

# Postition of letters in the alphabet
alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':7}
type(alphabet)

To access a *value* in a dict, you must supply the *key*.

print(alphabet['a'])
print(alphabet['e'])

Uh oh, `'e'` is the 5th letter of the alphabet, not the 7th! We can fix it by re-assigning the key to a new value:

alphabet['e'] = 5
print(alphabet['e'])

To delete an item in a dictionary, we can use the `.pop()` method. This also returns the value, so you can remove and use the value if you would like.

e_position = alphabet.pop('e')
print("E is the {}th letter in the alphabet".format(e_position))

# Now e is no longer in the dictionary
print(alphabet['e'])

## Dict for tabular data

Say we have a table (rows and columns) of data. Generally, our table has a header of column names (e.g. *keys* that we can access each column by), and a column of *values*. The sounds awfully similar to a `dict`, and indeed, Dictionaries can be a convenient way of representing tabular data in Python.

Say we have a table of number of coffees consumed each day in the weeks leading up to a proposal deadline:

| Week | Monday | Tuesday | Wednesday | Thursday | Friday |
| - | - | - | - | - | - |
| Sep 2 | 2 | 1 | 1 | 1 | 2 | 0 |
| Sep 9 | 1 | 2 | 1 | 2 | 1 | 2 |
| Sep 16 | 2 | 1 | 2 | 1 | 2 | 2 |
| Sep 23 | 3 | 2 | 1 | 2 | 3 | 4 |

We can represent this as a `dict`, where the days of the week are the **keys** and the list of coffees each week are the **values**

coffees = {
    'Week': ['Sep 2', 'Sep 9', 'Sep 16', 'Sep 23'],
    'Monday': [2, 1, 2, 3],
    'Tuesday': [1, 2, 1, 2],
    'Wednesday': [1, 1, 2, 1],
    'Thursday': [1, 2, 1, 2],
    'Friday': [1, 1, 3, 3]
}

Now we can conveniently access our coffee consumption on any given day over the four weeks by specifying the day as our key.

coffees['Wednesday']

If we want to compare all of the coffees consumed on Monday vs Friday:

print(sum(coffees['Monday']), sum(coffees['Friday']))

Or if we want to know how many coffees we consumed on Thursday of week 3:

coffees['Thursday'][2]

And if we want to get fancy, we can use a loop over the weeks and a loop over the days of the week to get the total coffees each week leading up to our deadline.

for i, week in enumerate(coffees['Week']):
    total = 0
    for day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
        total += coffees[day][i]
    print("I drank {} coffees in week {}".format(total, week))

## Dictionary Practice

# Dict of day of the week to shoe sizes sold
shoe_dict = {'Monday' : [7, 8, 9, 6, 7, 7, 9, 7, 8],
             'Tuesday' : [7, 6, 7, 8, 9, 6, 7, 7, 9], 
             'Wednesday' : [6, 7, 7, 9],
             'Thursday' : [7, 7, 6, 7, 9, 8, 6, 7, 13],
             'Friday' : [13, 7, 6, 7, 8, 9, 6, 7, 7],
             'Saturday' : [7, 7, 9, 7, 8, 10],
             'Sunday': [7, 7, 9, 7, 8, 10]}
shoe_dict['Thursday']

# return True if all of the same shoe shoe sizes and number of each were sold on saturday and sunday
# in the same order


# return True if all of the same shoe sizes (regardless of number) were sold on monday and tuesday
# hint: compare two sets


# return True if all of the same shoe sizes and number of each were sold on thursday and friday
# regardless of the order they were sold in
# hint: compare two sorted lists
