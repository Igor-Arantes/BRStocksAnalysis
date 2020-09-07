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
main_analisys_values_dataframe = pd.DataFrame()


#Functions for portifolio dataframe construction

def get_stocks_price():
    for stocks in my_stocks_list:
        temporary_stock_value = API_Functions.get_api_marketstack_bvmf_data(stocks)
        actual_stock_values.update({stocks:temporary_stock_value})
    return(actual_stock_values)    
    

def actual_stock_values_dataframe_construction(actual_stock_values):
    actual_stock_values_dataframe = pd.DataFrame()
    actual_stock_values_dataframe['Ticker'] = my_stocks_list
    actual_stocks_value_list = []
    for stocks in my_stocks_list:
        actual_stocks_value_list.append(actual_stock_values[stocks]['close'])
    actual_stock_values_dataframe['Price'] = actual_stocks_value_list 
    actual_stock_values_dataframe.set_index('Ticker', inplace=True)
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


def percent_variation(ticker_desired):
    return round(((actual_stock_values_dataframe.loc[ticker_desired, 'Price']-mean_price_paid(ticker_desired))/actual_stock_values.loc[ticker_desired, 'Price'])*100,2)


def main_analisys_values_dataframe_construction():
    main_analisys_values_dataframe = portifolio_dataframe
    actual_stock_values_dataframe = actual_stock_values_dataframe_construction(actual_stock_values)
    v=[]
    for i in my_stocks_list:
        v.append(actual_stock_values_dataframe.loc[i, 'Price'])
    main_analisys_values_dataframe['Unitary Price Now'] = v
    
    main_analisys_values_dataframe['Total Price Now'] = main_analisys_values_dataframe['Qty'] * main_analisys_values_dataframe['Unitary Price Now']
    
    main_analisys_values_dataframe['Valuation'] =round( (main_analisys_values_dataframe['Unitary Price Now'] - main_analisys_values_dataframe['Mean Price Paid']) * main_analisys_values_dataframe['Qty'],2)
    
    main_analisys_values_dataframe['Percent Variation'] = round((main_analisys_values_dataframe['Unitary Price Now']- main_analisys_values_dataframe['Mean Price Paid'])/main_analisys_values_dataframe['Unitary Price Now']*100,2)
    
    main_analisys_values_dataframe['Composition'] = round(main_analisys_values_dataframe['Total Price Now']/main_analisys_values_dataframe['Total Price Now'].sum()*100,2)
    
    return(main_analisys_values_dataframe)
    
portifolio_dataframe = portifolio_data_construction()       
  

def get_portifolio_perfomace():
    portifolio_performance_dic = {'Total_Invested':[main_analisys_values_dataframe['Total Paid'].sum()],'Total_Value_Now':[main_analisys_values_dataframe['Total Price Now'].sum()]}
    portifolio_performance = pd.DataFrame(portifolio_performance_dic)
    portifolio_performance['Total_Earn_Or_Loss'] = portifolio_performance.Total_Value_Now - portifolio_performance.Total_Invested 
    portifolio_performance['Total_Percent_Variation'] = round((portifolio_performance.Total_Value_Now/portifolio_performance.Total_Invested - 1)*100,2) 
    
    return(portifolio_performance)



actual_stock_values_dataframe = actual_stock_values_dataframe_construction(get_stocks_price())
main_analisys_values_dataframe = main_analisys_values_dataframe_construction()
portifolio_dataframe = portifolio_data_construction()   
portifolio_performance = get_portifolio_perfomace()
    


