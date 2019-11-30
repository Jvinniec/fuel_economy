[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jvinniec/fuel_economy/master)

# Fuel Economy
This repository serves as a place where I can use a sample of data that I collected over a few years on the fuel efficiency of my car. This repository serves as a sandbox for trying out different methods for analyzing the actual underlying data in the CSV file under data.

The following tools are used:
* [Pandas](https://pandas.pydata.org/)
* [Jupyter notebook](https://jupyter.org/)
* [Scikit-learn](https://scikit-learn.org/stable/index.html)
* [TensorFlow](https://www.tensorflow.org/)

# What is covered
There are a few directories that highlight specific topics of investigation. If you're looking for a cohesive story, I advise reading them in order.

## [data](data/)
Raw and formatted data as well as the script used to convert raw data into formatted data using **Pandas**. No actual investigation of the data is done in this directory. Rather it is where I inspect and clean the data into a useable state for importing elsewhere.

## [visualization](visualization/)
Visualizations of the underlying data with **matplotlib**.

## [miles_per_gallon](miles_per_gallon/)
Investigating whether or not it is possible to predict MPG for my car using scikit-learn and TensorFlow.

## [price_per_gallon](price_per_gallon/)
Investigating whether or not it is possible to predict price per gallon for my car using scikit-learn and TensorFlow.

# A note on file names
Note that each file also contains information about the specific tools it is highlighting:

* `_skl.ipynb`: **scikit-learn** machine-learning modules.
* `_tf.ipynb`: **TensorFlow**'s deep-learning framework for prediction.