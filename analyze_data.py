import pandas
import matplotlib.pyplot as plt

# Load data
df = pandas.read_csv('openpv_all_clean_trimmed.csv')
df['state'] = df['state'].str.strip()

#%% Plot cost per watt by state
df.groupby('state').mean()['cost_per_watt'].sort_values().plot(kind='bar')
plt.ylabel('Cost per watt ($/W)')
plt.xlabel('State')
plt.tight_layout()
plt.savefig('cost_by_state.png')

#%% Plot change in number of installations from 2016 to 2017

# Convert date strings to datetime objects
df['date_installed'] = pandas.to_datetime(df['date_installed'],format='%m/%d/%Y')

# Find rows in given date ranges
mask_2016 = (df['date_installed'] > '12/31/15') & (df['date_installed'] < '1/1/17')
mask_2017 = (df['date_installed'] > '12/31/16') & (df['date_installed'] < '1/1/18')
df2 = df.loc[:,['state','size_kw']]

# Find total number of installations by state for 2016 and 2017
tot_2016 = df2[mask_2016].groupby('state')['size_kw'].size()
tot_2017 = df2[mask_2017].groupby('state')['size_kw'].size()

# Calculate difference between 2016 and 2017
diff = (tot_2017-tot_2016).dropna()

# Plot results
diff.sort_values().plot(kind='bar')
plt.xlabel('State')
plt.ylabel('Change in number of PV installations from 2016 to 2017')
plt.tight_layout()
plt.savefig('growth_by_state.png')