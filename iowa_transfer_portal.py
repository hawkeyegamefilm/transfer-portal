import pandas as pd

def print_divider():
    print('--------------------------------------------------------------------------------------------------------------------------')

df = pd.read_csv('data/transfer_portal_2023_2_22_2023.csv')


iowa_transfers_inbound = df[df['destination'] == 'Iowa']
iowa_transfers_outbound = df[df['origin'] == 'Iowa']
print("INBOUND TRANSFERS")
print_divider()
print(iowa_transfers_inbound.to_string())
print_divider()
print()
print("OUTBOUND TRANSFERS")
print_divider()
print(iowa_transfers_outbound.to_string())
