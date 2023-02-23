import pandas as pd

df = pd.read_csv('data/transfer_portal_2023_2_22_2023.csv')

b1g_schools = ['Indiana', 'Illinois', 'Iowa', 'Maryland','Michigan','Michigan State','Minnesota', 'Nebraska','Northwestern', 'Ohio State', 'Penn State', 'Purdue','Rutgers', 'Wisconsin']
b1g_west = ['Illinois', 'Iowa', 'Minnesota','Nebraska','Northwestern','Purdue', 'Wisconsin']
b1g_east = ['Indiana','Maryland','Michigan','Michigan State','Ohio State', 'Penn State', 'Rutgers']

for school in b1g_schools:
    outbound_count = len(df[df['origin'] == school].index)
    inbound_count = len(df[df['destination'] == school].index)

    net_count = inbound_count - outbound_count
    print(school + " net count " + str(net_count))
    avg_stars = round(df[df['destination'] == school]['stars'].sum()/inbound_count, 2)

    print('star avg: ' + str(avg_stars))


