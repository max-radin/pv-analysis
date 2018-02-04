import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('openpv_all_clean_trimmed.csv')

#%%
df.groupby('state').mean()['cost_per_watt'].sort_values().plot(kind='bar')

plt.ylabel('Cost per watt ($/W)')
plt.xlabel('State')
plt.tight_layout()
plt.savefig('cost_by_state.png')