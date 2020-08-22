# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:38:49 2020

@author: Igor
"""

import pandas as pd
import API_Functions

xlsx_path = ('Carteira Acoes B3.xlsx')

bought_stocks_dataframe = pd.read_excel(xlsx_path)

my_stocks_list = bought_stocks_dataframe['Codigo da Açao'].unique()

actual_stock_values = {}

def get_stocks_price():
    for stocks in my_stocks_list:
        temporary_stock_value = API_Functions.get_api_marketstack_bvmf_data(stocks)
        actual_stock_values.update({stocks:temporary_stock_value})
    return(actual_stock_values)    
    

def actual_stock_values_dataframe():
    actual_stock_values_dataframe = pd.DataFrame()
    actual_stock_values_dataframe['Ticker'] = my_stocks_list
    actual_stocks_value_list = []
    for stocks in my_stocks_list:
        actual_stocks_value_list.append(actual_stock_values[stocks]['close'])
        
    actual_stock_values_dataframe['Price'] = actual_stocks_value_list  
    return(actual_stock_values_dataframe)   
    
