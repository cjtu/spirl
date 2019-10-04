---
redirect_from:
  - "/03-python/07/02-dict"
interact_link: content/03_python/07/02_dict.ipynb
kernel_name: python3
has_widgets: false
title: 'Dictionary (dict)'
prev_page:
  url: /03_python/07/01_set.html
  title: 'Set (set)'
next_page:
  url: /03_python/08/00_modules.html
  title: 'Modules'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Dictionaries

The dictionary is similar to the set in that it is *unordered* and has unique items. Dictionaries are one of the most useful types in Python because they very efficiently store **key-value** pairs of data. 

## Key and Value

In dictionaries, we need to provide a *name* or **key** to store our data. This **key** is how we will update and retrieve our data later. Dictionary keys must be *hashable*, most commonly an `int` or `string`.

The **value** is any object we would like to store in the dictionary at the specified key. The value can be of any type, making `dict` object extremely flexible.

The `dict`, like the `set`, is defined with `{}` curly braces, but each element must be colon `:` separated key-value painr (**key** `:` **value**).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Postition of letters in the alphabet
alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':7}
type(alphabet)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict
```


</div>
</div>
</div>



To access a *value* in a dict, you must supply the *key*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alphabet['a']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alphabet['e']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
7
```


</div>
</div>
</div>



Uh oh, we provided the wrong value for `'e'`. We can fix it by re-assigning the key to a new value:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alphabet['e'] = 5
alphabet['e']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
5
```


</div>
</div>
</div>



To delete an item in a dictionary, we can use the `.pop()` method. This also returns the value, so you can remove and use the value if you would like.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
e_position = alphabet.pop('e')
print("E is the {}th letter in the alphabet".format(e_position))

# Now e is no longer in the dictionary
print(alphabet['e'])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
E is the 5th letter in the alphabet
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-5-ae1a4be03e43> in <module>
          3 
          4 # Now e is no longer in the dictionary
    ----> 5 print(alphabet['e'])
    

    KeyError: 'e'


```
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
coffees = {
    'Week': ['Sep 2', 'Sep 9', 'Sep 16', 'Sep 23'],
    'Monday': [2, 1, 2, 3],
    'Tuesday': [1, 2, 1, 2],
    'Wednesday': [1, 1, 2, 1],
    'Thursday': [1, 2, 1, 2],
    'Friday': [1, 1, 3, 3]
}

```
</div>

</div>



Now we can conveniently access our coffee consumption on any given day over the four weeks by specifying the day as our key.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
coffees['Wednesday']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[1, 1, 2, 1]
```


</div>
</div>
</div>



If we want to compare all of the coffees consumed on Monday vs Friday:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(sum(coffees['Monday']), sum(coffees['Friday']))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
8 8
```
</div>
</div>
</div>



Or if we want to know how many coffees we consumed on Thursday of week 3:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
coffees['Thursday'][2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1
```


</div>
</div>
</div>



And if we want to get fancy, we can use a loop over the weeks and a loop over the days of the week to get the total coffees each week leading up to our deadline.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i, week in enumerate(coffees['Week']):
    total = 0
    for day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
        total += coffees[day][i]
    print("I drank {} coffees in week {}".format(total, week))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
I drank 6 coffees in week Sep 2
I drank 7 coffees in week Sep 9
I drank 9 coffees in week Sep 16
I drank 11 coffees in week Sep 23
```
</div>
</div>
</div>



### Dictionary Practice



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Dict of day of the week to shoe sizes sold
shoe_dict = {'Monday' : [7, 8, 9, 6, 7, 7, 9, 7, 8],
             'Tuesday' : [7, 6, 7, 8, 9, 6, 7, 7, 9], 
             'Wednesday' : [6, 7, 7, 9],
             'Thursday' : [7, 7, 6, 7, 9, 8, 6, 7, 13],
             'Friday' : [13, 7, 6, 7, 8, 9, 6, 7, 7],
             'Saturday' : [7, 7, 9, 7, 8, 10],
             'Sunday': [7, 7, 9, 7, 8, 10]}
shoe_dict['Thursday']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# return True if all of the same shoe shoe sizes and number of each were sold on saturday and sunday
# in the same order



```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# return True if all of the same shoe sizes (regardless of number) were sold on monday and tuesday
# hint: compare two sets



```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# return True if all of the same shoe sizes and number of each were sold on thursday and friday
# regarless of the order they were sold in
# hint: compare two sorted lists



```
</div>

</div>

