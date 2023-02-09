import pandas as pd
import os
import new_lib as nl
from matplotlib import pyplot as plt

def get_power():
    
    if os.path.isfile('power.csv'):
        
        df = pd.read_csv('power.csv')

        return df
    
    else:
        
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        
        df.to_csv('power.csv')

        return df


def acquire_store():
    query = '''SELECT sale_date, sale_amount,
                item_brand, item_name, item_price,
                store_address, store_zipcode
                FROM sales
                LEFT JOIN items USING(item_id)
                LEFT JOIN stores USING(store_id)'''
    
    store = nl.connect('tsa_item_demand', 'store.csv', query)
        
    return store
