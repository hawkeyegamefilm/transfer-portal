import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('data/transfer_portal_2023_05_03.csv')
df['date'] = pd.DatetimeIndex(df.transferDate).normalize()
s = df.groupby('date').date.agg('count').to_frame('cnt').reset_index().sort_values('date', ascending=False)

s2 = s.iloc[:-12]
print(s2.to_string())
fig,ax = plt.subplots()
ax.plot_date(s2.date, s2.cnt, linestyle='--')

ax.annotate('Dec 5, 2022', (mdates.date2num(s2.loc[79].date), s2.loc[79].cnt), xytext=(40, 1),
            textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))

ax.annotate('April 15, 2023', (mdates.date2num(s2.loc[174].date), s2.loc[174].cnt), xytext=(40, 1),
            textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))

fig.autofmt_xdate()
plt.title('NCAA Transfer Portal Activity for 2022-2023 cycle')
plt.ylabel('Transfer portal entries')
plt.xlabel('Date')
plt.show()
