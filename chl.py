import requests

url = 'https://example.com/table.csv'

response = requests.get(url)

with open('table.csv', 'w') as f:
  f.write(response.text)

import pandas as pd

# Read the table from the csv file
df = pd.read_csv('table.csv', parse_dates=['date'])

# Create a new table with the mean chl for each location by date
mean_chl = df.groupby(['date', 'location'])['chl'].mean()

# Reset the index to make the date and location columns appear as separate columns
mean_chl = mean_chl.reset_index()

import matplotlib.pyplot as plt

# Plot mean chl by date
mean_chl.plot(x='date', y='chl')
plt.show()
