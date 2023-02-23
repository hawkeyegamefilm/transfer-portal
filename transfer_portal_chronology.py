import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('data/transfer_portal_2023_2_22_2023.csv')
df['date'] = pd.DatetimeIndex(df.transferDate).normalize()
s = df.groupby('date').date.agg('count').to_frame('cnt').reset_index().sort_values('date', ascending=False)

s2 = s.iloc[:-12]
print(s2.to_string())
fig,ax = plt.subplots()
ax.plot_date(s2.date, s2.cnt, linestyle='--')

ax.annotate('Dec 5', (mdates.date2num(s2.loc[80].date), s2.loc[80].cnt), xytext=(100, 25),
            textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))

fig.autofmt_xdate()
plt.title('NCAA Transfer Portal Activity for 2022-2023 cycle')
plt.ylabel('Transfer portal entries')
plt.xlabel('Date')
plt.show()
