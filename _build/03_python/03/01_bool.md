---
redirect_from:
  - "/03-python/03/01-bool"
interact_link: content/03_python/03/01_bool.ipynb
kernel_name: python3
has_widgets: false
title: 'Boolean (bool)'
prev_page:
  url: /03_python/03/00_types.html
  title: 'Basic Data Types'
next_page:
  url: /03_python/03/02_int-float.html
  title: 'Numerical (int, float)'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Booleans

Here, we will explore the most basic data type in Python, the **boolean**. Booleans are binary data structures, representing **True** and **False** (or yes/no, on/off, 0/1, depending on the case). In Python, their type is called `bool` and they can have only one of two values, either `True` or `False`. 

We can use the `type()` function to check the type of an object in Python.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
bool
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = False
type(a)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
bool
```


</div>
</div>
</div>



You may recognize the `bool` type, because we already saw it when we used the `==` equality operator in the previous chapter.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
2 == 3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
False
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(2 == 3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
bool
```


</div>
</div>
</div>



## Bool vs bool

What do you think happens if we check the equality of two `bool`s? Try it!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True == True

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True == False

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
False == False

```
</div>

</div>



## Casting bools
In Python `bool` types have a special property: `True` and `False` are **cast** to `1` and `0` when included in an expression.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
45 * False

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True + True + True + True + True

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



What do you think happens when you test equality between a `bool` and `0` or `1`?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True == 1

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
False == 0

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
False == 1

```
</div>

</div>



This can be useful to know because as the simplest data type, booleans also use the least memory. If you need a large array of exclusively `0`s and `1`s, it will use less memory (and be the exact same), if you store those values as `bool` rather than numbers! 

## Boolean operators

There are two special operators in Python for comparing `bool`. They are `and` and `or`.

The `and` operator is `True` only when *both* of the compared `bool`s are `True`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True and True

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True and False

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
False
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
False and False

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
False
```


</div>
</div>
</div>



The `or` operator is `True` when *one* of the compared `bool`s are `True`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True or True

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True or False

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
False or False

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
False
```


</div>
</div>
</div>



Remember that Pyhton *evaluate expressions* when it comes time to compare them. What do you think happens in each of the following cases?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(2 == 2) and (2 == 3)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(1 == 4) or (4 == 4)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(0 == 1) or False

```
</div>

</div>

