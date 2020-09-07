# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:23:44 2020

@author: Igor
"""

import matplotlib.pyplot as plt
import seaborn as sns

import portifolio_manipulation




#Setting green to positive values and red to negative ones
custom_palette={}
for i in range(0, len(portifolio_manipulation.main_analisys_values_dataframe.Valuation)):
    if  portifolio_manipulation.main_analisys_values_dataframe.Valuation[i] >= 0:
        custom_palette[portifolio_manipulation.main_analisys_values_dataframe.Ticker[i]] = 'g'
    else:
        custom_palette[portifolio_manipulation.main_analisys_values_dataframe.Ticker[i]] = 'r'
        
custom_palette={}
for i in range(0, len(portifolio_manipulation.main_analisys_values_dataframe['Percent Variation'])):
    if  portifolio_manipulation.main_analisys_values_dataframe['Percent Variation'][i] >= 0:
        custom_palette[portifolio_manipulation.main_analisys_values_dataframe.Ticker[i]] = 'g'
    else:
        custom_palette[portifolio_manipulation.main_analisys_values_dataframe.Ticker[i]] = 'r'
        
#Ploting percent data
sns.set(style='whitegrid')
plt.figure(figsize=(15,8))
sns.barplot(y='Ticker', x='Percent Variation', data=portifolio_manipulation.main_analisys_values_dataframe, palette=custom_palette)

       
#Ploting valuations data
sns.set(style='whitegrid')
plt.figure(figsize=(15,8)) 
sns.barplot(x='Ticker', y='Valuation', data=portifolio_manipulation.main_analisys_values_dataframe, palette=custom_palette)
    

print(portifolio_manipulation.get_portifolio_perfomace())

