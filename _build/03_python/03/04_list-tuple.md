---
redirect_from:
  - "/03-python/03/04-list-tuple"
interact_link: content/03_python/03/04_list-tuple.ipynb
kernel_name: python3
has_widgets: false
title: 'List and Tuple'
prev_page:
  url: /03_python/03/03_str.html
  title: 'String (str)'
next_page:
  url: /03_python/04/00_functions.html
  title: 'Functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# List and Tuple

These two array-like types in Python are handy for storing data. Like the string, they can be indexed and sliced, but unlike the string they can contain *any object*, not just characters.



## Lists
A **List** is a common way to store a collection of objects in Python. Lists are defined with square brackets `[]` in Python.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# An empty list can be assigned to a variable and added to later
empty_list = []

# Or a list can be initialized with a few elements
fruits_list = ['apple', 'banana', 'orange', 'watermelon']

type(fruits_list)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
list
```


</div>
</div>
</div>



Lists elements can be data of any type:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
medley = [True, 42, 'Hello world!', 3.14159]
print(medley)
type(medley)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[True, 42, 'Hello world!', 3.14159]
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
list
```


</div>
</div>
</div>



Lists are *ordered*, meaning they can be indexed to access their elements, much like accessing characters in a **String**.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_list[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'apple'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_list[1:3]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['banana', 'orange']
```


</div>
</div>
</div>



Lists are also *mutable*, meaning they can change length and their elements can be modified. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Let's replace apple with pear (modifying an element)
fruits_list[0] = 'pear'
fruits_list

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['pear', 'banana', 'orange', 'watermelon']
```


</div>
</div>
</div>



We can also add an element to the end of a list with the `.append()` method.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_list.append('peach')
fruits_list

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['pear', 'banana', 'orange', 'watermelon', 'peach']
```


</div>
</div>
</div>



Or we can remove and return the last element from a list with `pop()`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_list.pop()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'peach'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Notice that 'peach' is no longer in the fruits list
fruits_list

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['pear', 'banana', 'orange', 'watermelon']
```


</div>
</div>
</div>



To understand mutability, let's compare the list with an **immutable** array-like data type, the **Tuple**. 

# Tuples
Tuples in Python are defined with `()` parentheses.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Tuples are defined similarly to lists, but with () instead of []
empty_tuple = ()
fruits_tuple = ('apple', 'banana', 'orange', 'watermelon')
fruits_tuple

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
('apple', 'banana', 'orange', 'watermelon')
```


</div>
</div>
</div>



Like the **String** and **List**, the **Tuple** can be indexed and sliced to access its elements.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_tuple[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'apple'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_tuple[1:3]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
('banana', 'orange')
```


</div>
</div>
</div>



Unlike the *mutable* list, we get an error if we try to change the elements of the **Tuple** in place.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_tuple[0] = 'pear'

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-3dbfe5bf3508> in <module>
    ----> 1 fruits_tuple[0] = 'pear'
    

    TypeError: 'tuple' object does not support item assignment


```
</div>
</div>
</div>



Likewise, we cannot change the length of a `tuple` once it has been defined, so the `.append()` and `.pop()` methods are not defined



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_tuple.append('peach')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-13-d4a14f82ed20> in <module>
    ----> 1 fruits_tuple.append('peach')
    

    AttributeError: 'tuple' object has no attribute 'append'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits_tuple.pop()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-3a9e4f529938> in <module>
    ----> 1 fruits_tuple.pop()
    

    AttributeError: 'tuple' object has no attribute 'pop'


```
</div>
</div>
</div>



### Why would I ever use an inferior version of the list?
Tuples are less flexible than lists, but sometimes that is *exactly what you want* in your program. 

Say I have a bunch of *constants* and I want to make sure that they stay... constant. In this case, a tuple is a better choice to store my data. By using a tuple, you will know if any later code tries to modify your constants - because Python will throw an error! 

We will explore errors (called *exceptions*) in Python more in future sections, but we'll mention here that *exceptions are your friend*. They can tell you when your code is doing something incorrect or unexpected, and help you find exactly where it happened.



## List methods
Let's explore some useful **methods** of the **list**. We have already used the `.append()` and `.pop()` methods above. To see what methods are available, we can always use `help()`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Underscores denote special methods reserved by Python
# We can scroll past the __methods__ to see user methods
help(list)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

```
</div>
</div>
</div>



Let's try out the `.index()` and `.sort()`  methods.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pets = ['dog', 'cat', 'snake', 'turtle', 'guinea pig']

# Let's find out what index cat is at
pets.index('cat')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Now let's try sorting the list
pets.sort()
pets

```
</div>

</div>



Sorting a list of strings rearranges them to be in alphabetical order. Lists are not restricted to holding strings, let's see what happens when we sort a list of **Int**.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ages = [12, 24, 37, 9, 71, 42, 5]
ages.sort()
ages

```
</div>

</div>



Sorting can be a very useful feature for ordering your data in Python. 

A useful built-in function that can be used to find the length of an ordered data structure is `len()`. It works on lists, tuples, strings and the like.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(len(['H', 'E', 'L', 'L', 'O']), len((1, 2, 3, 4)), len('Hello'))

```
</div>

</div>



## Practice

Make a list of strings with the first 4 words you think of. Call the list `words`, then `print()` it to the console.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Define your list of words


```
</div>

</div>



Now use indexing to return the first letter of the third word.

*Hint*: Recall Python begins indexing at 0. Also recall that both lists and strings can be indexed



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Get the 1st letter of the 3rd word


```
</div>

</div>



Sort your list in reverse alphabetical order (without redfining it!), then print it. 

*Hint*: you may want to use the `help()` function on the `list.sort` method



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Sort your list in reverse alpha order then print it


```
</div>

</div>



Now make a tuple with the same 4 words you used above and print it to the console.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Define a tuple with 4 words and print it


```
</div>

</div>



Now return the 2nd letter of the 2nd word in the tuple.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Get the 2nd letter of the 2nd word


```
</div>

</div>



Now define a new tuple with the words in reverse order and print it.

*Hint*: the index `[::-1]` may be useful



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Define your new reversed tuple here then print it


```
</div>

</div>

