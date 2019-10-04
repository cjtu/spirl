---
redirect_from:
  - "/04-sci-programming/01/00-jupyter"
interact_link: content/04_sci-programming/01/00_jupyter.ipynb
kernel_name: python3
has_widgets: false
title: 'Jupyter'
prev_page:
  url: /04_sci-programming/00_why-sci-programming.html
  title: 'Scientific Programming'
next_page:
  url: /04_sci-programming/02/00_numpy.html
  title: 'Numpy'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Jupyter Notebooks

The **Jupyter Notebook** is an interactive document that combines text and code. They can be a great way of communicating your science in an expressive, transparent, and reproducible way like this great dive into sunspot data ([link](http://nbviewer.jupyter.org/gist/jhemann/4569783)).

In the *Anaconda* chapter, we will learn to run our own Jupyter notebook servers to create and test our own notebooks locally. For now, we can use a website called *mybinder.org* to view, edit, and practice our programming in interactive Jupyter notebooks..

You can open this page in *MyBinder* by clicking the **Interact** button above, or by clicking the following [link](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Fjupyter_tutorial.ipynb). 

We reccommend you head over to *MyBinder* before continuing this page!


## Anatomy of a Jupyter notebook

Jupyter Notebooks consist of **cells** that contain either text or Python code. 

This is a text (`Markdown`) cell. It supports basic text formatting with Markdown and can be used to descibe the code that preceeds or follows it. 

The cell below is a `Code` cell. You can quickly write and run Python in `Code` cells, and any outputs or plots will be shown directly below them.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# This is a code cell.
# Any outputs of code written here will appear directly below.
print('Hello World')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Hello World
```
</div>
</div>
</div>



## Editing blocks
You can edit any block by double clicking it to enter edit mode. Double click me to edit!



## Running cells
To run a cell, click the cell to select it, and then click the `>| Run` button above. 

Try running the block below.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("You can run me by selecting me and clicking Run")

```
</div>

</div>



## Making new cells
You can make a new cell by clicking the `+` button in the toolbar above. New cells default to the`Code` cell type. You can change the type of a cell in the dropdown menu above.

Try adding a `Markdown` cell below. Write something surrounded by asterisks (e.g. `**wow**`) and then click `>| Run` to render your new cell.



## Cool plots
Jupyter notebooks also allow you display plots and graphics inline. Try running the following two code blocks (don't worry about the code for now).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# This will install the numpy and matplotlib packages to show the following plot
import sys
!conda install --yes --prefix {sys.prefix} numpy matplotlib

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Taken from the matplotlib examples gallery: https://matplotlib.org/gallery/ (full url below)
# https://matplotlib.org/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-pym https://matplotlib.org/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)
axs[0].set_title('The coherence of two signals')

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('coherence')

# fig.tight_layout()
plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Solving environment: / ^C
failed

CondaError: KeyboardInterrupt

```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
<Figure size 640x480 with 2 Axes>
```

</div>
</div>
</div>



## Other options
Note some other buttons on the toolbar above:
- save: Saves the notebook. Your notebook will also autosave every few minutes.
- cut, copy, and paste: Duplicate or move cells.
- stop, refresh, fast-forward: These stop, restart and re-run the **kernel**.

**Kernels**: Underlying the Jupyter notebook is an **IPython** kernel which is interpreting the code and rendering the pretty graphics. Sometimes this kernel gets bogged down or crashes and needs to be restarted. Try clicking the fast-forward button (restart kernel and re-run notebook). This will clear all outputs and rerun the notebook from the top down.



## Jupyter in action
The Jupyter notebook allows for complete reproducibility of scientific analyses. Most computational science involves writing code that imports and analyzes data, and then plots some results. Once you have that code working, you can copy and paste it into a Jupyter notebook and explain the important parts of your analysis with markdown cells.

For a great example, see this Jupyter tutorial from LIGO on how to find gravitational waves (go to link and then run the notebook with Azure or mybinder): https://www.gw-openscience.org/tutorials/ 

