"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# Import the necessary libraries
import pandas as pd
import datetime
import re
import numpy as np

# Import the dataset

path = r'./data/weather_dataset.data'

# Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data = pd.read_fwf(path, widths=[3] * 3 + [6] * 12)
data['dt'] = data.apply(lambda row: datetime.datetime(1900 + int(row[0]), row[1], row[2]), axis=1)
data = data.set_index('dt', drop=True)
data = data.drop(labels=['Yr', 'Mo', 'Dy'], axis=1)

# Converting data to float
for col in data:
    isfloat = re.compile(r'\d+(?:\.\d*)')
    data[col] = data[col].str.replace(',', '.')
    data[col] = data[col].apply(
        lambda x: float(match.group()) if isinstance(x, str) and bool(match := isfloat.match(x)) else np.nan)

# Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
# By print(data.isna().sum() / len(data)) can check percent of broken values (it's small).
# Then replace it by mean over columns

isna_num = data.isna().sum()
print(f'Not a number count: \n{isna_num}\n')
print(f'Fine values: \n{isna_num * (-1) + len(data)}\n')

means = data.mean()
data = data.fillna(value=means)
# Write a function in order to fix date (this relate only to the year info) and apply it
# Done

# Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
# Done

# Compute how many values are missing for each location over the entire record
# Done

# Compute how many non-missing values there are in total
# Done

# Calculate the mean windspeeds of the windspeeds over all the locations and all the times
print(f'Means: \n{means}\n')

# Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations
# of the windspeeds at each location over all the days
loc_stats = data.describe()


# Find the average windspeed in January for each location
print(f'Average windspeed in January: \n{data[data.index.month == 1].mean()}\n')

# Downsample the record to a yearly frequency for each location
# Downsample the record to a monthly frequency for each location
# Downsample the record to a weekly frequency for each location

for name, freq in [('year', 'Y'), ('month', 'M'), ('week', 'W')]:
    print(f'Downsampled record to a {name}ly frequency: '
          f'\n {data.resample(freq).mean()}\n')


# Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each
# week (assume that the first week starts on January 2 1961) for the first 21 weeks

sample = data.loc[data.index <= datetime.datetime(1961, 1, 2) + datetime.timedelta(weeks=7)]
stats = sample.resample("W").apply(lambda x: x.describe())
stats = stats.stack()
stats = stats.reorder_levels([0, 2, 1]).reset_index(level=2)
stats = pd.pivot_table(stats, index=stats.index, columns='level_2')
stats.columns = stats.columns.get_level_values(1)
stats.columns.name = None
stats.index = pd.MultiIndex.from_tuples(stats.index, names=['date', 'location'])

print(f'Week stats: \n {stats}')
