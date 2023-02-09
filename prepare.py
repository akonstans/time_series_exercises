import acquire as a
from matplotlib import pyplot as plt
import pandas as pd

def wrangle_store():
    
    df = a.acquire_store().drop(columns = 'Unnamed: 0')
    
    df['sale_date'] = pd.to_datetime(df['sale_date'], infer_datetime_format=True)
    df = df.set_index('sale_date').sort_index()
    
    df['month'] = df.index.month_name()
    df['day'] = df.index.day_name()
    
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df

def wrangle_power():
    
    df = a.get_power()
    
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    df = df.set_index('Date').sort_index()
    
    df['month'] = df.index.month_name()
    df['year'] = df.index.year_name()
    
    df['Wind'] = df['Wind'].fillna(value=0)
    df['Solar'] = df['Solar'].fillna(value=0)
    df['Wind+Solar'] = df['Wind+Solar'].fillna(value=0)
    
    return df

def store_distributions(df):
    
    vars_to_plot = ['sale_amount', 'item_price', 'sales_total']

    for col in vars_to_plot:
    
        df.groupby('sale_date')[vars_to_plot].sum().plot()
        
        plt.show()

def power_distributions(df):
    
    vars_to_plot = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']

    for col in vars_to_plot:
    
        df.groupby('Date')[vars_to_plot].sum().plot()
    
        plt.show()
