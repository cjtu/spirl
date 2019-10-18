---
redirect_from:
  - "/03-python/07/01-set"
interact_link: content/03_python/07/01_set.ipynb
kernel_name: 
has_widgets: false
title: 'Set (set)'
prev_page:
  url: /03_python/07/00_data-structs.html
  title: 'Advanced Data Types'
next_page:
  url: /03_python/07/02_dict.html
  title: 'Dictionary (dict)'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Sets

The **set** is a data type in Python which stores only unique elements in no particular order. In this way, the set works much like a *mathematical set*, and even has methods that perform set operations. 

## Defining a set

Sets in Python are defined with curly braces `{}`, and each element is separated by a comma, like with lists and tuples. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pets = {'dog', 'cat', 'hamster', 'fish', 'snake'}
mammals = {'human', 'dog', 'cat', 'hamster', 'whale'}
scales = {'snake', 'alligator', 'pangolin', 'snake', 'fish'}
non_animals = {42, 'galaxy', None, False, ('Microsoft', 'Apple', 'Google')}

```
</div>

</div>



In the above example, we can see that the `set` doesn't care what type our elements are, we can even mix types in a single set (like with the tuple and list). 

You may have notices that we specified `'snake'` twice in the `scales` set. Let's print that set:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(scales)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'pangolin', 'alligator', 'snake', 'fish'}
```
</div>
</div>
</div>



You may also notice that the `scales` set is now in a different order (or it may be in the same order by coincidence). This is because sets are *unordered*, meaning they cannot be indexed like the `string`, `tuple` and `list`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
scales[2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-94b10e62ca53> in <module>
    ----> 1 scales[2]
    

    TypeError: 'set' object is not subscriptable


```
</div>
</div>
</div>



Since sets only hold unique objects, it doesn't matter how many times we specify an element, it will only be recorded once! This makes sets a bad way to keep track of a coin-flip contest.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
results = {'heads', 'tails', 'tails', 'tails', 'heads', 'tails', 'heads', 
           'tails','heads', 'tails', 'heads', 'tails'}
print(results)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'tails', 'heads'}
```
</div>
</div>
</div>



But it does make sets a great way to quickly see how many different items are in our poorly organized shopping cart.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cart = {'apple', 'pear', 'tofu', 'milk', 'apple', 'apple', 'orange', 'rice', 
        'pasta', 'pear', 'milk', 'pear', 'grapes', 'orange', 'apple'}
print(cart)
print("We bought {} different items".format(len(cart)))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'pasta', 'grapes', 'pear', 'apple', 'milk', 'orange', 'rice', 'tofu'}
We bought 8 different items
```
</div>
</div>
</div>



## Hashable types

The exception to our brash statement that the "set doesn't care what type our elements are" is for types that Python claims are *unhashable*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
broken_set = {[1, 2, 3]}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-6464f2ba00fd> in <module>
    ----> 1 broken_set = {[1, 2, 3]}
    

    TypeError: unhashable type: 'list'


```
</div>
</div>
</div>



Here, the error tells us that the `list` type is *unhashable*. This is because lists are *mutable*, meaning that can be changed later. Make sure when you're using sets that you use immutable types like `int`, `float`, `string` and `tuple`. 



## Converting to set

To quickly see the unique elements of a list or tuple, we can convert it to a set with the built-in `set()` function. The following example will show how useful this can be.

Say a shoe store sells the many different sizes of shoes on a given day and their bookkeeping is simply a list of the sizes sold. We want to see which sizes aren't selling, so we use the `count()` method to find which shoe sizes are missing.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# A shoe stores sells shoes of the following sizes on a certain day
shoe_sizes = [7, 8, 9, 6, 7, 7, 9, 7, 8, 10, 13, 7, 6, 7, 8, 9, 6, 7, 
              7, 9, 7, 8, 10, 13, 7, 6, 7, 8, 9, 6, 7, 7, 9, 7, 14, 5,
              8, 10, 13, 7, 6, 7, 8, 9, 6, 7, 7, 9, 7, 8, 10, 13, 7, 6,
              7, 8, 9, 6, 7, 7, 9, 7, 8, 10, 13, 7, 6, 7, 8, 9, 6, 7, 7, 
              9, 7, 8, 10, 13, 7, 6]

# We can print how many of each shoe was sold with count
print(shoe_sizes.count(6),
      shoe_sizes.count(7),
      shoe_sizes.count(8),
      shoe_sizes.count(9),
      shoe_sizes.count(10),
      shoe_sizes.count(11),
      shoe_sizes.count(12),
      shoe_sizes.count(13))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
12 30 12 12 6 0 0 6
```
</div>
</div>
</div>



Since we only care about the shoes that are not selling for this example, we can simply use a set!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sold_sizes = set(shoe_sizes)
print(sold_sizes)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{5, 6, 7, 8, 9, 10, 13, 14}
```
</div>
</div>
</div>



This `shoe_set` shows the 8 sizes that were sold that day. Now we want to see which of our sizes were *not* sold. There's a set method for that!

Remember, you can always use the `help()` function to see methods of an object in Python



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(set)

```
</div>

</div>



## Set methods



In the help info, we might notice that we can use set operations like `union()` and `difference()` on our set. Let's use the set difference to see which shoes were not sold on a give day.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
all_sizes = {6, 7, 8, 9, 10, 11, 12, 13}
not_sold = all_sizes.difference(sold_sizes)
print(not_sold)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{11, 12}
```
</div>
</div>
</div>



Sets also allow us to use math operators to compare sets, so the following is the exact same as above



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(all_sizes - sold_sizes)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{11, 12}
```
</div>
</div>
</div>



Now we know that size 11 and size 12 were the only shoe sizes not sold.


Let's return to our animal sets from the start of this chapter. Say we want to add to a set. We can do this with the `add()` method.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pets = {'dog', 'cat', 'hamster', 'fish', 'snake'}
mammals = {'human', 'dog', 'cat', 'hamster', 'whale'}
scales = {'snake', 'alligator', 'pangolin', 'snake', 'fish'}

mammals.add('koala')
print(mammals)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'hamster', 'cat', 'whale', 'dog', 'human', 'koala'}
```
</div>
</div>
</div>



If we want to take the unions of two sets, we can use `union()` or `|`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
all_animals = pets | mammals | scales
print(all_animals)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'fish', 'alligator', 'snake', 'hamster', 'pangolin', 'cat', 'whale', 'dog', 'human', 'koala'}
```
</div>
</div>
</div>



We can also take the set intersection (`.intersection()` or `&`), to see the overlap between sets.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mammalian_pets = pets & mammals
print(mammalian_pets)

scaly_pets = pets & scales
print(scaly_pets)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'cat', 'hamster', 'dog'}
{'fish', 'snake'}
```
</div>
</div>
</div>



Great now that you know the basics of the `set`, our first unordered and unique data type in Python, we will explore the Dictionary (`dict`) which is a very useful and conceptually similar data structure in Python.

