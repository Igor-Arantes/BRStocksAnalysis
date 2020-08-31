# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:38:49 2020

@author: Igor
"""

import pandas as pd
import API_Functions

xlsx_path = ('Carteira Acoes B3.xlsx')

bought_stocks_dataframe = pd.read_excel(xlsx_path)
bought_stocks_dataframe['Total Paid'] = bought_stocks_dataframe['Qty'] * bought_stocks_dataframe['Price Paid']

my_stocks_list = bought_stocks_dataframe['Ticker'].unique()

actual_stock_values = {}
actual_stock_values_dataframe = pd.DataFrame()


#Functions for portifolio dataframe construction

def get_stocks_price():
    for stocks in my_stocks_list:
        temporary_stock_value = API_Functions.get_api_marketstack_bvmf_data(stocks)
        actual_stock_values.update({stocks:temporary_stock_value})
    return(actual_stock_values)    
    

def actual_stock_values_dataframe(actual_stock_values):
    actual_stock_values_dataframe = pd.DataFrame()
    actual_stock_values_dataframe['Ticker'] = my_stocks_list
    actual_stocks_value_list = []
    for stocks in my_stocks_list:
        actual_stocks_value_list.append(actual_stock_values[stocks]['close'])
    actual_stock_values_dataframe['Price'] = actual_stocks_value_list  
    return(actual_stock_values_dataframe)   
    

def portifolio_data_construction():
    portifolio_dataframe = pd.DataFrame()
    portifolio_dataframe['Ticker'] = my_stocks_list
    x=[]
    for ticker in my_stocks_list:
        x.append(bought_stocks_dataframe[(bought_stocks_dataframe.Ticker==ticker)].Qty.sum())
    portifolio_dataframe['Qty']=x
    x=[]    
    for ticker in my_stocks_list:
        x.append(mean_price_paid(ticker))
    portifolio_dataframe['Mean Price Paid'] = x
    x=[]
    portifolio_dataframe['Total Paid'] =  portifolio_dataframe['Qty'] * portifolio_dataframe['Mean Price Paid']
    
    return(portifolio_dataframe)   


def find_all_stock(ticker_desired):
    return bought_stocks_dataframe['Ticker']==ticker_desired       

def sum_stock_desired(ticker_desired):
    x=bought_stocks_dataframe[find_all_stock(ticker_desired)].sum()
    return x[1]

def mean_price_paid(ticker_desired):
    x=bought_stocks_dataframe[find_all_stock(ticker_desired)].sum()
    return round(x[-1]/x[1],2)

def valuation(ticker_desired):
    return round((actual_stock_values_dataframe.loc[ticker_desired, 'Price']-mean_price_paid(ticker_desired))*sum_stock_desired(ticker_desired),2)



def percent_variation(ticker_desired):
    return round(((actual_stock_values_dataframe.loc[ticker_desired, 'Price']-mean_price_paid(ticker_desired))/actual_stock_values.loc[ticker_desired, 'Price'])*100,2)


def main_analisys_values():
    stocks_stats = pd.DataFrame(my_stocks_list, columns=['Ticker'])
    v=[]
    for i in my_stocks_list:
        v.append(mean_price_paid(i))
    stocks_stats['Mean price paid'] = v
    v=[]
    for i in my_stocks_list:
        v.append(sum_stock_desired(i))
    stocks_stats['Qty'] = v
    stocks_stats['Total Paid'] = stocks_stats['Mean price paid']*stocks_stats['Qty']
    v=[]
    for i in my_stocks_list:
        v.append(actual_stock_values.loc[i, 'Preco'])
    stocks_stats['Un Value Now'] = v
    stocks_stats['Total Value Now'] = stocks_stats['Un Value Now']*stocks_stats['Qty']
    stocks_stats.drop(columns='Un Value Now', inplace=True)
    v=[]    
    for i in my_stocks_list:
        v.append(valuation(i))
    stocks_stats['Valuation'] = v
    v=[]
    for i in my_stocks_list:
        v.append(percent_variation(i))
    stocks_stats['Percent variation'] = v
    v=[]
    return stocks_stats


