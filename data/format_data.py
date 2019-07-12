#%% 
# Import pandas for reading/saving the data
import matplotlib.pyplot as plt
from  pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import pandas            as pd

#%%
# Load the data
file_name = "data_raw.csv"
data_raw = pd.read_csv("data/data_raw.csv")

#%% 
# Print some useful information about the data
print(data_raw.dtypes)
data_raw.head(4)
data_raw.describe()

#%% Remove null values for 'Date', 'Latitude', and 'Longitude'
data_raw = data_raw.dropna(subset=['Date', 'Latitude', 'Longitude'])

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

# Print some updated information about the database
data_raw.Date = new_dates
data_raw.head(4)
print(data_raw.dtypes)
data_raw.describe()

#%% [markdown]
# ## Before formatting the data
# The following show what the data looks like before we do any kind of 
# data conditioning.

#%%
# Plot "Miles driven on one tank" over time
plt.ylabel('Miles Driven')
plt.xlabel('Date')
plt.xticks(rotation=45, ha='right')
plt.scatter(data_raw.Date, data_raw.Miles)

#%%
# Cut longitude and latitude based on my home town
data_fmt = data_raw[data_raw.Longitude > -94]
data_fmt = data_fmt[data_fmt.Longitude < -93]
data_fmt = data_fmt[data_raw.Latitude > 41.3]
data_fmt = data_fmt[data_fmt.Latitude < 42.2]

#%% [markdown]
# ## The Final Results
# In the following plot we compare the lon,lat values for all entries (red)
# and for entries specifically around my former home town (green)

#%%
# Plot the distribution of longitude and latitude
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.scatter(data_raw.Longitude, data_raw.Latitude, color='red')
plt.scatter(data_fmt.Longitude, data_fmt.Latitude, color='green')

#%%
# Plot "Miles driven on one tank" over time after cuts
plt.ylabel('Miles Driven')
plt.xlabel('Date')
plt.xticks(rotation=45, ha='right')
plt.scatter(data_fmt.Date, data_fmt.Miles)

#%% [markdown]
# ## The final database...

#%%
print(f"Entries: {len(data_fmt)}")
data_fmt.describe()

#%%
# Save the database
data_fmt.to_pickle('data/data_formatted.pkl')
