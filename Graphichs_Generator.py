# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:23:44 2020

@author: Igor
"""

import matplotlib as plt
import seaborn as sns

import portifolio_manipulation

actual_stock_values_dataframe, portifolio_dataframe, main_analisys_values_dataframe, portifolio_performance = portifolio_manipulation.get_all_dataframes()


#Setting green to positive values and red to negative ones
custom_palette={}
for i in range(0, len(main_analisys_values_dataframe.Valuation)):
    if  main_analisys_values_dataframe.Valuation[i] >= 0:
        custom_palette[main_analisys_values_dataframe.Ticker[i]] = 'g'
    else:
        custom_palette[main_analisys_values_dataframe.Ticker[i]] = 'r'
        
custom_palette={}
for i in range(0, len(main_analisys_values_dataframe['Percent variation'])):
    if  main_analisys_values_dataframe['Percent variation'][i] >= 0:
        custom_palette[main_analisys_values_dataframe.Ticker[i]] = 'g'
    else:
        custom_palette[main_analisys_values_dataframe.Ticker[i]] = 'r'
        
#Ploting percent data
sns.set(style='whitegrid')
plt.figure(figsize=(15,12)) 
sns.barplot(y='Ticker', x='Percent variation', data=main_analisys_values_dataframe, palette=custom_palette)

       
#Ploting valuations data
sns.set(style='whitegrid')
plt.figure(figsize=(15,8)) 
sns.barplot(x='Ticker', y='Valuation', data=main_analisys_values_dataframe, palette=custom_palette)


