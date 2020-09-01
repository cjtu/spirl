# Matplotlib

Matplotlib is the standard library in Python used for plotting. It can be really powerful and offers a lot of customization, but with that can come frustration and an initial learning curve. Plotting something requires interacting different levels. Often you can use high level coommands like plot this array but sometimes it is necessary to interact at a low-level or use very specific commands like change the color of this pixel. Matplotlib does a great job of allowing you to interact at a high level most of the time to easily make plots, while leaving the freedom to make changes at a lower level when necessary. 

Today, we are going to focus on learning to use the built in functions within matplotlib to make a variety of plot types. Matplotlib has a number of usefule modules, but we will focus on the most commonly used **pyplot**. Pyplot is a collection of functions which allow matplotlib to be run like MATLAB. This is sufficient for most plot types you will need to make.

First, we import the pyplot module. We alias this as **plt** to make calling all of the plotting functions easer (less typing)! **plt** is an extremely common alias for matplotlib and most code you see will use this.

%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np

The %matplotlib notebook command just tells Jupyter to automatically display the plots we generate. This is not needed when making plots outside of a Jupyter notebook.

We'll start by making a simple plot and taking a closer look at each part.

x = np.linspace(0,10) #array with values from 0 to 10
plt.plot(x, x, label='Line') #Plot a line
plt.plot(x, x**2, label='x Squared') # Plot x^2

plt.title('This is the Title')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

## Parts of the Figure

**Figure**
The entire plot is called a figure. It is an object that keeps track of all parts of the figure including the axes and any number of special artists (ie: title, legend, labels, etc. The figure also keeps track of the canvas, but for now we will ignore this. When using matplotlib any interaction with the canvas should happen under the hood, making it virtually invisible.

**Axes**
The axes part of a figure contains all of the information for both axis of a 2D plot (ie: axis labels, tick mark spacing and numbering, the title, etc). You can have multiple axis on a figure, as you will see below, but each axes can only be on one figure. The attributes of the axes can be controlled with a set of methods, such as set_xlabel(), set_ylabel(), set_title(), and many more. 


**Axis**
The axis is the object containing the information for each axis on your plot. Two or more of these are combined with some extra information to make the axes. The axis can set graph limits, set tickmarks and labels and change the visual properties of an individual axis (for example making thicker tick marks, or moving the tick marks inside the plot). Many of the changes you want to make to an axis can be accomplished using the methods within **axes**, however there is a greater level of control over specific details here, when the need arises. 

**Artist**
Basically everything you can see on the figure is an artist (even the Figure, Axes, and Axis objects). Anything you add to a plot is also an artist, for example adding a text box or the legend. Artists are usually tied to an axes object and cannot be shared by multiple axes at once.

## Subplots

The ability to use subplots within pyplot is extremely useful. It allows you to place multiple axes options on a single figure. For example:

x = np.linspace(0,10) #array with values from 0 to 10

fig, ax = plt.subplots(2,1, figsize=(10,5))

ax[0].plot(x, x) #Plot a line
ax[1].plot(x, x**2) # Plot x^2

fig.suptitle('This is the Main Title')
ax[0].set_title('X vs X')
ax[1].set_title('X Squared')
ax[1].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[1].set_ylabel('Y')

Here, we have two **axes**. In the plt.subplots(2,1) function we specify that we want the figure to have 2 axis vertically and only one horizontally. Changing this to plt.subplots(1,2) would render the plots next to one another.

We also use a slightly different coding style here (with subplots) than in the first example. To set all of the axis labes and titles we use the methods for each **axes**. The top plot is axis 1, accessed using `ax[0]` and the bottom with `ax[1]`.