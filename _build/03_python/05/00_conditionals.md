---
redirect_from:
  - "/03-python/05/00-conditionals"
interact_link: content/03_python/05/00_conditionals.ipynb
kernel_name: 
has_widgets: false
title: 'Conditionals'
prev_page:
  url: /03_python/04/00_functions.html
  title: 'Functions'
next_page:
  url: /03_python/06/00_loops.html
  title: 'Loops'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Conditionals

Conditional (or, *if statements*) are ways to break up code based on certain conditions that are met. Each conditional takes a *boolean expression* and decides what to do based on whether the expression is `True` or `False`.

## If statements

If statements allow you to change the execution of your code based on whether or not a condition is met. They consist of a **condition** (the boolean expression) and a **clause** (the stuff to do if the condition is `True`).

If statements will often use **comparison operators** like `==` (is equal to) to determine whether the following code is run.

The if statement follows the following form:

```Python
if 'something' == 'something else':
    # this is the clause that is run if the condition is true
    # it will run this code
    # and everything else indented here
# This un-indented code is no longer part of the clause
# It runs regardless of whether the if block was run
```

Change the value of mynum in the following example to see what happens when an if statement is False. When mynum is not 5, is the print statement exectued?





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mynum = 5

if mynum == 5:
    print('My number is 5')

```
</div>

</div>



## if, elif, else statements

Additional clauses can be added to the if statement to modify its behaviour in other cases. 

The `elif` statement will run its clause if the previous condition(s) were not met, but this additional condition *is* met.

The `else` statement will run its clause if none of the preceeding if and elif statements have their conditions met. The else statement always comes last.

You can string together many conditions and clauses into one if, elif, else block:
```Python
if breed == 'border collie':
    size = 'medium'
elif breed == 'yorkie':
    size = 'tiny'
elif breed == 'newfoundland':
    size = 'huge'
elif breen == 'basset hound':
    size = 'small'
else:
    size = '?'
```

Experiment with running this code and changing the breed:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#Change the breed here
breed = 'border collie'

if breed == 'border collie':
    size = 'medium'
elif breed == 'yorkie':
    size = 'tiny'
elif breed == 'newfoundland':
    size = 'huge'
elif breen == 'basset hound':
    size = 'small'
else:
    size = '?'
    
#Print the value of size
print('The size of the breed is:', size)

```
</div>

</div>

