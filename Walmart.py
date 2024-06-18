import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('shipment_database.db')
cursor = conn.cursor()

# Load CSV files from the data folder
spreadsheet_0 = pd.read_csv('data/shipping_data_0.csv')
spreadsheet_1 = pd.read_csv('data/shipping_data_1.csv')
spreadsheet_2 = pd.read_csv('data/shipping_data_2.csv')

# Insert spreadsheet_0 into the database
spreadsheet_0.to_sql('spreadsheet_0', conn, if_exists='replace', index=False)

for _,row in spreadsheet_1.iterrows():
    shipping_id = row['shipment_identifier']
    product_name = row['product']
    # quantity= spreadsheet_0.loc[spreadsheet_0['shipment_identifier'] == 'shipment_identifier','product_quantity'].values[0]

for _, row in spreadsheet_2.iterrows():
    shipping_id = row['shipment_identifier']
    origin = row['origin_warehouse']
    destination = row['destination_store']

conn.commit()
conn.close()
print("Success")