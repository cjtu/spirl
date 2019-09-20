---
redirect_from:
  - "/03-python/02/01-expressions"
interact_link: content/03_python/02/01_expressions.ipynb
kernel_name: python3
has_widgets: false
title: 'Syntax and Expressions'
prev_page:
  url: /03_python/02/00_basics.html
  title: 'Python Basics'
next_page:
  url: /03_python/02/02_variables.html
  title: 'Variables'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Syntax and Expressions

Programming languages are made up of **syntax** and **expressions**.

**Syntax** is the *vocabulary and grammar* of the language. These are the specific words, symbols and rules for how to combine them to convey your intent to the computer.

**Expressions** are the *sentences* of the language. All programs do *something* and expressions are how you piece together syntax to tell your program what to do.


## Expressions

At their most basic level, expressions are the same as simple *mathematical expressions*. In this way, every programming language is just a fancy calculator.

For example, to multiply two values together in Python, we use the `*` **operator**.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
2 * 3

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



In this example, the **expression** `4*5` is *evaluated* by the Python interpreter, and the result `20` is returned and shown below the cell.

Programming laguages have very specific grammatical rules. For example, in Python you cannot have the `*` operator twice in a row. Python will show a `SyntaxError`, meaning that we broke one of Python's grammatical rules.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
2 * * 3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

      File "<ipython-input-2-0f343c0fc354>", line 1
        2 * * 3
            ^
    SyntaxError: invalid syntax



```
</div>
</div>
</div>



Syntax errors are common for beginners and advanced programmers alike. When you come across one, make sure to check your program for typos. Python will even tell you the line where it came across the error (`line 1` in our single line example above), so you know where to check your syntax.

The rigid syntax of programming allows for small changes to an expression to give it a completely different meaning. For example, if we remove the space from the `* *`, we get the *exponentiation* operator, `**`. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
2 ** 3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
8
```


</div>
</div>
</div>



## Arithmetic operators

Since we work with a lot of (mainly numerical) data in science, mathematical operators are essential in just about every program you will write. In Python, these are the basic arimetic operators:

| Expression Type | Operator | Example    | Value     |
|-----------------|----------|------------|-----------|
| Addition        | `+`      | `2 + 3`    | `5`       |
| Subtraction     | `-`      | `2 - 3`    | `-1`      |
| Multiplication  | `*`      | `2 * 3`    | `6`       |
| Division        | `/`      | `7 / 3`    | `2.33334` |
| Exponentiation  | `**`     | `2 ** 0.5` | `1.41421` |



Python expressions obey the same *order of operations* (BEDMAS) as in algebra. In order Python will evaluate: 

- Brackets
- Exponents
- Multiplication and Division 
- Addition and Subtraction



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
1 + 2 * 3

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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(1 + 2) * 3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
9
```


</div>
</div>
</div>



### Integer Division and Remainders

Python also has a special operator `//` to force division to return a whole number rather than producing a decimal. It also has a **modulo** operator which gives the remainer of an integer division. Then the three division operators are:

| Expression Type  | Operator | Example    | Value     |
|----------------- |----------|------------|-----------|
| Division         | `/`      | `7 / 3`    | `2.33334` |
| Integer Division | `//`     | `7 // 3`   | `2`       |
| Remainder        | `%`      | `7 % 3`    | `1`       |




## Equality

A last basic operator we will mention here is the equality `==` operator. This operator is used to test if two *expressions* evaluate to the same value.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
2 * 2 == 4

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



Try to make the following expression evaluate to `True`, changing only the operators (and/or adding parentheses) to the left side.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3 + 1 + 2 + 4 == 16

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



Now you know some basic operators in Python and how to string them into expressions. Remember that to learn a language you need to actively explore what you're learning and try new things. For example, what do you think happens when you divide by 0? Try it (and anything else you think of) in the code block below:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
100 / 0

```
</div>

</div>

