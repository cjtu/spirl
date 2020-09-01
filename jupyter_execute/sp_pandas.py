# Pandas

In this tutorial we will learn to work with tables of data with the `pandas` Python package. Pandas is an industry standard analysis package for data science, so it has many features and is actively being updated and supported (full documentation [here](https://pandas.pydata.org/pandas-docs/stable/)).

## Overview

Pandas has two main data structures that it uses to store tables of data, the **Series** and the **DataFrame**. 

- The **Series** represents a single column of data
- The **DataFrame** is a collention of **Series** columns that make a table

Let's start by exploring the DataFrame in pandas!

# Pandas is commonly aliased as pd
import pandas as pd

## Creating DataFrames

In the `dict` chapter, we saw that dictionaries can be used to represent tables of data. As you may expect, DataFrames can be created directly from dictionaries!

# Daily coffee consumption over 4 weeks
coffees = {
    'Week': ['Sep 2', 'Sep 9', 'Sep 16', 'Sep 23'],
    'Monday': [2, 1, 2, 3],
    'Tuesday': [1, 2, 1, 2],
    'Wednesday': [1, 1, 2, 1],
    'Thursday': [1, 2, 1, 2],
    'Friday': [1, 1, 3, 3]
}
df = pd.DataFrame(coffees)
print(type(df))
df

We get see the column names using the `.columns` attribute.

df.columns

## Slicing and Indexing

Pandas gives a few ways to find your data in a **DataFrame**.

- `[]` raw indexing by *column* like we've seen in `dict`
- `.loc[]` **loc**ate *row* by name
- `.iloc[]` **loc**ate *row* by numerical **i**ndex

Let's try each of these on a subset of our `exoplanets` DataFrame.

df['Monday']

# try locating a row by its week
df.loc['Sep 2']

Uh oh, we didn't tell pandas which of the columns to use as our `Index`. The `Index` is an optional unique identifier of a rows, like a *name*, *ID*, or in our case, the *week*. Let's add an `Index` to our DataFrame.

df = df.set_index('Week')
df.head()

Now we can use `.loc[]` to find rows by their Index name!

df.loc['Sep 2']

Finally, we can also specify a rows from our DataFrame by its *numerical* index using `.iloc[]`.

# Get first row in the DataFrame
df.iloc[0]

## DataFrame methods

Now let's read in an example dataset to learn about a few other useful DataFrame methods.

exoplanets = pd.read_csv("https://github.com/mwaskom/seaborn-data/raw/master/planets.csv")

We can check that `pandas` read the table in as a **DataFrame**.

type(exoplanets)

The `DataFrame.info()` method can tell us about the contents of our table.

print(exoplanets.info())

In the above description, we get the total number of rows (the **RangeIndex**), and the number of non-null entries in each of the columns.

We can get a sense for what the table looks like by printing the first few rows with the `DataFrame.head(num_rows)` method. You can specify a number of rows to `.head()`, otherwise it shows the first 5 by default.

exoplanets.head()

Similarly, we can print rows from the bottom of the table with the `.tail(num_rows)` method. Here we are printing the bottom 2 rows.

exoplanets.tail(2)

## Null data

Dealing with missing data is a major strength of `pandas`. Pandas fills in missing data with a value of `NaN`, but these can be challenging to deal with because many math operations are amiguous or undefined on `NaN` values.

Let's get a list of where the values are in our DataFrame are missing with `.isnull()`. This will give a DataFrame of `bool` with whether or not each entry is null. Below, we use `.tail()` to just print the last 5 rows.


exoplanets.isnull().tail()

To get a summary of how many `NaN`s are in each column, we can use the `.sum()` method (recall that `bool` values in Python are equivalent to 0 and 1 in Python and can be summed).

exoplanets.isnull().sum()

Here we've converted each null entry to `True`, then summed each of the boolean columns. Since `False == 0`, we get a count of the `True == 1` (in this case the null valued) entries in each column.

To get rid of these null values, we have a few options. Sometimes we want to completely drop all rows with missing data and we can do this with `dropna()`.


exo = exoplanets.dropna()
exo.info()

Now we have 498 rows without missing values remaining. Let's verify this with the sum trick we saw above.

exo.isnull().sum()

If instead we want to fill the null values with some default value, we can use the `.fillna()` method.

exo_filled = exoplanets.fillna(0)
exo_filled.tail()

exo_filled.isnull().sum()

## And More

Often we want to select data from a table on some condition. Say we want all of the rows where the detection method was *microlensing*, we could do:

exoplanets[exoplanets['method'] == 'Microlensing']

Say we want all exoplanets detected between 2009 and 2011. We can do this by combining two boolean expressions with a `&`.

exoplanets[(exoplanets['year'] >= 2009) & (exoplanets['year'] <= 2011)].info()

Pandas also has a useful summary method which gives statistics on each of the columns called `.describe()`. This can be a quick way to see if the mimima, maxima and means of each column are what you expect.

exoplanets.describe()

Finally, we can plot a dataframe directly with the `.plot()` method. This method uses `pyplot` from `matplotlib` and accepts most of the same arguments that you would pass to `matplotlib.pyplot.plot()`. The conveniece of plotting directly from a DataFrame is being able to specify the names of columns as the x and y axes.

exoplanets.plot(kind='scatter', x='mass', y='orbital_period', title='Orbital Period vs Mass')

## Practice

We will read in the fuel economy dataset, **mpg** from https://github.com/mwaskom/seaborn-data below. 


mpg = pd.read_csv("https://github.com/mwaskom/seaborn-data/raw/master/mpg.csv")

1. Use the `.info()`, `.describe()`, and `.head()` methods to get acquainted with the dataset - are there null values for any columns? What is the minimum and maximum number of cylinders of cars in the dataset?
2. If any rows have null values, use `.dropna()` to remove those rows
3. Create a new variable, `mpg4` with only the 4-cylinder engine cars
4. Using the 4-cylinder car DataFrame, make a scatter plot of the *mpg* (fuel economy) vs *horsepower*
5. Plot a histogram (you can do this with `.plot(kind='hist)`) of the *mpg* for only the cars whose *origin* is "usa"

# Answer the above problems here!

