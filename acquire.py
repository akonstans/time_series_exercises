import pandas as pd
import os

def get_power():
    
    if os.path.isfile('power.csv'):
        
        df = pd.read_csv('power.csv')

        return df
    
    else:
        
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        
        df.to_csv('power.csv')

        return df