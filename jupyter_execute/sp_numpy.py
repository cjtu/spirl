# Numpy

The basis of most scientific programming in Pyhton is the *numerical Python* library, `numpy`. NumPy gives us many tools - including a fast and efficient data type, the `numpy Array` - for working with numerical data. 

## Numpy Array

NumPy is built around the `array`. This is a data structure defined in NumPy which is *ordered* and *mutable*, must like the `list`. Although very similar to the list, the numpy array only allows *numerical* data as elements, like the `int` and `float`. Let's explore!

# Frist we need to import the numpy package. It is commonly shortened to "np"
import numpy as np 

The easiest way to define numpy arrays is to define a list or tuple, and convert it to an array with the `numpy.array()` function.

a = [0, 1, 2, 3, 4]
b = np.array(a)
print(type(a))
print(type(b))

We can index and slice numpy arrays much like lists:

print(b[0], b[1:3], b[-1])

Try running the following to get help on the NumPy array

help(np.ndarray)

Woah. That's a really long help page. Often when you are working with a new package, `help()` won't be the most convenient or easy to read way to get help. Instead, we can search for online *documentation* for the package we are using.

If you Google **numpy documentation**, you will likely see links to info about *numpy* and another package we will explore later, *scipy*. If you follow the links to **NumPy**, you should find a [NumPy user Guide](https://docs.scipy.org/doc/numpy-1.15.0/user/index.html) and from there, several pages of tutorials and documentation about the package. The [Quickstart tutorial](https://docs.scipy.org/doc/numpy-1.15.0/user/quickstart.html), will give a much more legible intro to the package.

## Numpy Attributes

NumPy arrays have some built in **attributes**, i.e. info stored in an object, accessible with `object.attribute` (note: no parentheses after).

# Let's print some attributes of our b array
print("Num dimensions:", b.ndim,
      "\nShape:", b.shape,
      "\nSize:", b.size)

A common way to define NumPy arrays with with the `arange` function.

np.arange(10)

help(np.arange)

The numpy `arange` function allows us to quickly build integer arrays. It takes `start`, `stop`, and `step` as arguments.

x = np.arange(1, 10)
y = np.arange(2, 20, 2)
print(x)
print(y)

We can apply any mathematical operation to a NumPy array, and it will apply that operation to every element in the array.

x = np.arange(-3, 4)
y = x**2
print(y)



Another way to make NumPy arrays is with the `linspace()` function. This allows us to choose the bounds of an interval and the number of points we want to divide it into. Numpy also has useful math constants like `pi` and `e` and math functions like `sin`, `cos`, `tan`.

import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)

# Linspace can be useful for adding more resolution to continuous functions
xarange = np.arange(-np.pi, np.pi)
yarange = np.cos(xarange)

xlinspace = np.linspace(-np.pi, np.pi, 1000)
ylinspace = np.cos(xlinspace)

plt.subplot(1, 2, 1)
plt.plot(xarange, yarange)

plt.subplot(1, 2, 2)
plt.plot(xlinspace, ylinspace)

If we want to plot a bell curve we can use the `np.random` module to randomly sample a normal distribution.

norm = np.random.standard_normal(100000) # Draw 1000 random points from normal distribution
hist, bins = np.histogram(norm, bins=10, density=True) # Make histogram of our samples
plt.plot(bins[1:], hist)

hist, bins = np.histogram(norm, bins=100, density=True)
plt.plot(bins[1:], hist)

This is barely scratching the surface of the `numpy` package, but should be enough to get you started. The [Quickstart tutorial](https://docs.scipy.org/doc/numpy-1.15.0/user/quickstart.html) is a great resource for more of the basics and some more advanced usage. Finally, don't forget to use the most powerful tool at our disposal: *Google*. Most programmers only have the most common syntax memorized, everything else can be found with Google!

Next we will further explore the `matplotlib` package that we briefly introduced above!