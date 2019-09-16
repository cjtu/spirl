---
redirect_from:
  - "/03-python/03/02-int-float"
interact_link: content/03_python/03/02_int-float.ipynb
kernel_name: python3
has_widgets: false
title: 'Numerical (int, float)'
prev_page:
  url: /03_python/03/01_bool.html
  title: 'Boolean (bool)'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Integer and Float

Python provides two basic numberical data types, `int` and `float`. 

## Integers (int)

The `int` type represents integers: positive and negative whole numbers and 0. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(42)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
int
```


</div>
</div>
</div>



Unlike other languages, Python 3 integers have no fixed size. When they grow too big, they are automatically given more memory by Python, meaning integers have essentially no size limit (Note: this is not true in most other languages! Languages like C can only store `Integer`s in the range (-2147483647, 2147483647) before needing a new data type to handle them). 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = 2
a

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
b = a**64
b

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
18446744073709551616
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
c = a**128
c

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
340282366920938463463374607431768211456
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(type(a), type(b), type(c))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<class 'int'> <class 'int'> <class 'int'>
```
</div>
</div>
</div>



## Floating-point numbers (float)

Decimal (or floating-point) numbers in Python belong to the `float` data type. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(3.2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
float
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = -0.11
type(a)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
float
```


</div>
</div>
</div>



What do you think happens when you combine an `int` and a `float` in a mathematical expression?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
2 * 3.2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
6.4
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
4.81 / 2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2.405
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
8.99 * 0

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.0
```


</div>
</div>
</div>



Python opts to return a `float` whenever performing operations on a mix of `int` and `float` types.

## Integer division

What happens if we divide two `int`s that cannot be expressed as a whole number?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
4 / 3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1.3333333333333333
```


</div>
</div>
</div>



Uh oh! This might be unexpected because we started with two `int` types, but now have a `float` type! If we want to force division to return an `int` in Python, we can use the *integer division* operator, `//`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
4 // 3

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



Integer division returns the *floor* (nearest lower integer) of the quotient. You might imagine that now we dropped the remainder, but may want to know what it is. For this we can use the **modulo** `%` operator.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
4 % 3

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



Now we know that `4 / 3 = 1` with a remainder of 1 and all of the values are still type `int`!



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3 < 6

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
4.55 > 7.89

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
9 != 12.2

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



What do you think happens if you compare a `float` and `int` with the same value?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
4.0 == 4

```
</div>

</div>



## Chaining comparisons

What if we want to know if a given value is between two other values?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = 5.5
x > 4

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
x < 6

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



We can chain comparisons in Python to write this much more simply as the following range:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
4 < x < 6

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
0 < x < 5

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

