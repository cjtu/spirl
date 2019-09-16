---
redirect_from:
  - "/03-python/02/03-calls"
interact_link: content/03_python/02/03_calls.ipynb
kernel_name: python3
has_widgets: false
title: 'Calls'
prev_page:
  url: /03_python/02/02_variables.html
  title: 'Variables'
next_page:
  url: /03_python/03/00_types.html
  title: 'Basic Data Types'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Call Statements

Call statements in Python are a name followed by `()` parentheses. They are used to invoke functions and methods (more on these later). For example, the absolute value function `abs`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
abs(-12)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
12
```


</div>
</div>
</div>



Expressions placed in the `()` are called **arguments**, and the type and number of arguments expected depend on the function. 


## Help!

To get a description of a function and the arguments it accepts, we can use the `help()` function:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(abs)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

```
</div>
</div>
</div>



This description tells us that `abs()` takes one argument, `x`, and returns its absolute value. Try `help(hex)` to see one of many nerdy easter eggs built into Python...



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(hex)

```
</div>

</div>



## Multiple arguments

Some functions like `max()` take multiple arguments.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
max(2, 6, 4)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
6
```


</div>
</div>
</div>



Expressions can also be passed as arguments, and they are evaluated before being passed to the function.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
max(2, 2 + 3, 4)

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



Python comes with some [built-in functions](https://docs.python.org/3/library/functions.html) such as `abs` and `max`. Soon we will learn to write our own custom Python functions that we can use to simplify tedious or repetative tasks. 

First, we will introduce some common data structures that will be appear in almost every Python program you ever write.

