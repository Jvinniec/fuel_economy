#%% [markdown]
# # Prepparing the data
# This notebook is intended to describe how I've collected the data and shows the
# preliminary process of getting it into the format I will use for the rest of
# the notebooks in this series. By the end, we should be left with a Pandas
# dataframe that we can easily save and use in the future.
#
# ## Data Collection
# The data that I will be looking at here was collected over about 4 years. It
# consists of all the information about my personal vehicle's fuel economy. The
# car in question was a 2012 Chevy Cruze (Eco), that I had obtained secondhand.
# The data was collected and stored in a `Google Sheet` for the purposes of easily
# plotting quick results and the ability to access it from pretty much anywhere
# I had an internet connection. I could also export the data as a CSV file for 
# easy loading into a Pandas dataframe. That being said, let's show how we do that!

#%% 
# Import pandas for reading/saving the data
import pandas            as pd

# Load the data
file_name = "data_raw.csv"
data_raw = pd.read_csv("data/data_raw.csv")

#%% [markdown]
# And we now have the raw data in a Pandas dataframe, which we can use to do all
# kinds of fun things. First, let's try to do some basic probing of the data to
# see what types each column has been imported as whatnot

#%%
# Print information about what datatype each column is
data_raw.dtypes
#%%
# Print the first four rows of the data
data_raw.head(4)
#%%
# Print some summary statistics about each column
data_raw.describe()

#%% [markdown]
# Looking at the `count` values for each row, it's clear that there are some
# rows that don't have values for specific parameters (prepresented by `NaN`).
# This happens when an imported cell in the sheet was empty. Specifically, we 
# can see that there are quite a few 'Latitude' and 'Longitude' columns that 
# are empty because I didn't start keeping track of location until about 2014. 
# Ultimately we want to use the data to make some predictions, so we need to
# remove any NaN values in these columns. Because we also want to plot with 
# respect to time, we'll also remove any entries for which we don't have `Date` 
# information.

#%% Remove null values for 'Date', 'Latitude', and 'Longitude'
data_raw = data_raw.dropna(subset=['Date', 'Latitude', 'Longitude'])
data_raw.describe()

#%% [markdown]
# Awesome! But we have another problem: The `Date` column isn't in a datetime
# format that can be easily used. So, let's just go ahead and put those in the
# appropriate format (i.e. we need to convert from a string of the form 
# `DD/MM/YYYY` to a pandas.datetime object)

#%% Format the 'Date' column
# Convert entries into datetime format
new_dates = []
for d,date in enumerate(data_raw.Date):
    # Typically we should make sure here that the data is the expected format
    # But I'm not going to worry about that for this simple sample
    date_arr = date.split('/')
    dat = pd.datetime(int(date_arr[2]), 
                      int(date_arr[0]), 
                      int(date_arr[1]))
    new_dates.append(dat)

# Update the Date column
data_raw.Date = new_dates

# Print some updated information about the dataframe
data_raw.dtypes

#%% [markdown]
# ## Formatting the data
# The following show what the data looks like before we do any kind of 
# data conditioning.

#%%
# Load matplotlib for plotting
import matplotlib.pyplot as     plt
from   pandas.plotting   import register_matplotlib_converters
register_matplotlib_converters()

# Plot "Miles driven on one tank" over time
plt.ylabel('Miles Driven')
plt.xlabel('Date')
plt.xticks(rotation=45, ha='right')
scat = plt.scatter(data_raw.Date, data_raw.Miles)

#%% [markdown]
# We can see quite a few of the values are relatively large or small for `Miles 
# Driven` (i.e. outliers). These values are taken from times when I was driving
# large distances (most likely for vacations and whatnot). So it appears we need
# to make a selection on the geographic position in order to select only those
# near my home town. Let's do that now:

#%%
# Cut longitude and latitude based on my home town
data_fmt = data_raw[(data_raw.Longitude > -94.0) &
                    (data_raw.Longitude < -93.0) &
                    (data_raw.Latitude  >  41.3) &
                    (data_raw.Latitude  <  42.2)]

#%% [markdown]
# ## The Final Results
# In the following plot we compare the lon,lat values for all entries (red)
# and for entries specifically around my former home town (green)

#%%
# Plot the distribution of longitude and latitude
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.scatter(data_raw.Longitude, data_raw.Latitude, 
            color='red', label='All Data')
plt.scatter(data_fmt.Longitude, data_fmt.Latitude, 
            color='green', label='Hometown')
leg = plt.legend()

#%%
# Plot "Miles driven on one tank" over time after cuts
plt.ylabel('Miles Driven')
plt.xlabel('Date')
plt.xticks(rotation=45, ha='right')
scat = plt.scatter(data_fmt.Date, data_fmt.Miles)

#%% [markdown]
# ## The final dataframe...

#%%
print(f'Entries: {len(data_fmt)}')
data_fmt.describe()

#%%
# Save the dataframe
data_fmt.to_pickle('data/data_formatted.pkl')

#%% [markdown]
# ## Summary
# So we've now loaded the data, done a VERY preliminary exploration to see what
# kind of information we have and removed the most obvious information that will
# not be useful to achieve what we want to do with that data.
