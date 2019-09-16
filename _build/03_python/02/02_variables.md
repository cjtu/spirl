---
redirect_from:
  - "/03-python/02/02-variables"
interact_link: content/03_python/02/02_variables.ipynb
kernel_name: python3
has_widgets: false
title: 'Variables'
prev_page:
  url: /03_python/02/01_expressions.html
  title: 'Syntax and Expressions'
next_page:
  url: /03_python/02/03_calls.html
  title: 'Calls'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Variables

So far, the expressions we have seen have all been evaluated on one line, with the result shown right away. Often we want to store the result of an expression to use later. We can store the result of an expression in a **variable**. 

A variable is created in Python with an **assignment** statement involving the `=` sign (not to be confused with the equality operator `==`).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = 10

```
</div>

</div>



Here, the variable `a` was *assigned* the value `10`. Now, if we use `a` in future, it will refer to the value we stored in it.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(a)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
10
```
</div>
</div>
</div>



You can use your newly minted variables in expressions too!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
b = 12 + a
print(b)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
22
```
</div>
</div>
</div>



Variables can be re-assigned at will, but be careful - there's no undo on assignment statements!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
c = 1
c = 5
print(c)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
5
```
</div>
</div>
</div>



## Allowed variable names

There are a couple rules for naming variables in Python. They must:

- begin with a letter (though they can contain letters and numbers)
- cannot use spaces (often spaces are replaced with `_` underscores)
- cannot contain special characters



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a2 = 2
b_0_e = 3
ch$1 = 17

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

      File "<ipython-input-5-d85f68312c1b>", line 3
        ch$1 = 17
          ^
    SyntaxError: invalid syntax



```
</div>
</div>
</div>



## Naming conventions

Although variable names like `i_1_1i_III` are technically *allowed* in Python, they may not be that *useful*. When writing code, we want to be as **expressive** as possible so that it is legible later. For example, if our variable is used to track the number of apples we have, a good name could be `apples`, or perhaps `num_apples`. 


PEP8 also gives some stylistic guidelines for naming variables in Python.

> [Variable] names should be lowercase, with words separated by underscores as necessary to improve readability

This is slightly different to other languages that prefer the use of `mixedCase` variable names.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
doNotNameVariableLikeThis = 0
use_underscores_instead = 1

```
</div>

</div>



## Possible pitfalls

In Python, expressions are *evaluated* as soon as you assign them to a variable. That means that future updates to a variable won't change any other variables defined in reference to it. 

For example, what do you think will happen when you run the following code? Try it!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
apples = 4
oranges = 3
total_fruit = apples + oranges
apples = 8
oranges = 11
print(total_fruit)

```
</div>

</div>



### Protected names

In Python, there are a few variable and function names that are used by the language and shouldn't be used as variable names. For example, if you want to count the number of times your publication has been printed, you may be inclined to use the variable name `print`. But `print` is the name of a built-in function in Python. What do you think will happen if you run the following?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print = 2 + 3 + 4 + 5
print

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
14
```


</div>
</div>
</div>



Python allows you to use the variable name `print`, but this could be disasterous later when you try to use the `print` function because now you've redefined it!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(1 + 2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-520716ea4f3c> in <module>
    ----> 1 print(1 + 2)
    

    TypeError: 'int' object is not callable


```
</div>
</div>
</div>



Most code editors help avoid mistakes like this by highlighting laguage-specific protected names like so:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print
type
help
int
enumerate

```
</div>

</div>



Code editors will not highlight your defined names thouhgh, so make sure to use decriptive names to reduce chances of accidentally overwriting your `a` or `tmp` variables!

