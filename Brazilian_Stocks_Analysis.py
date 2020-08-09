#!/usr/bin/env python
# coding: utf-8

# In[232]:


# Libraries Importation


# In[233]:


import pandas as pd


# In[234]:


import seaborn as sns


# In[235]:


import matplotlib.pyplot as plt


# In[236]:


#Dada source


# In[237]:


url = "https://docs.google.com/spreadsheets/d/1I93xay8dfxiL25qYohMAFIbh204vHBJSC3iKm_Y-Apc/edit?usp=sharing"


# In[238]:


o = pd.read_html(url, index_col=1, skiprows = 1)


# In[239]:


xlsx_path = ('Carteira Acoes B3.xlsx')


# In[240]:


e = pd.read_excel(xlsx_path)


# In[ ]:





# In[241]:


#Fitting Data


# In[242]:


stocks_now = o[0]
stocks_now = stocks_now.dropna().drop(columns=['1'])
stocks_dataframe = e.dropna()
stocks_dataframe.rename(columns={'Codigo da Açao':'Ticker', 'Valor Pago': 'Valor_Pago'}, inplace = True)


# In[ ]:





# In[ ]:





# In[243]:


#Pick Sotock by Ticker


# In[244]:


def ticker_location(ticker_desired):
    return raw_data.loc[(raw_data["Ticker"] == ticker_desired)]
    


# In[245]:


#Finding the total price and add then to the dataframe


# In[246]:


stocks_dataframe['Valor Total'] = stocks_dataframe['Quantidade'] * stocks_dataframe['Valor_Pago']


# In[247]:


#Find Stock by Ticker


# In[248]:


def find_all_stock(ticker_desired):
    return stocks_dataframe['Ticker']==ticker_desired


# In[ ]:





# In[249]:


#Mean Value Stock Price


# In[250]:


def mean_price_paid(ticker_desired):
    x=stocks_dataframe[find_all_stock(ticker_desired)].sum()
    return round(x[-1]/x[1],2)


# In[251]:


#Sum of desired stock


# In[252]:


def sum_stock_desired(ticker_desired):
    x=stocks_dataframe[find_all_stock(ticker_desired)].sum()
    return x[1]


# In[253]:


#valuation or devaluation in total


# In[254]:


def valuation(ticker_desired):
    return round((stocks_now.loc[ticker_desired, 'Preco']-mean_price_paid(ticker_desired))*sum_stock_desired(ticker_desired),2)


# In[255]:


#Percent variation


# In[256]:


def percent_variation(ticker_desired):
    return round(((stocks_now.loc[ticker_desired, 'Preco']-mean_price_paid(ticker_desired))/stocks_now.loc[ticker_desired, 'Preco'])*100,2)


# In[257]:


#Geting a series of uniques stocks names


# In[258]:


unique_stocks_ticker = stocks_dataframe['Ticker'].unique()


# In[259]:


#Creating a data frame with the main analysis values


# In[420]:


def main_analisys_values():
    stocks_stats = pd.DataFrame(unique_stocks_ticker, columns=['Ticker'])
    v=[]
    for i in unique_stocks_ticker:
        v.append(mean_price_paid(i))
    stocks_stats['Mean price paid'] = v
    v=[]
    for i in unique_stocks_ticker:
        v.append(sum_stock_desired(i))
    stocks_stats['Qty'] = v
    stocks_stats['Total Paid'] = stocks_stats['Mean price paid']*stocks_stats['Qty']
    v=[]
    for i in unique_stocks_ticker:
        v.append(stocks_now.loc[i, 'Preco'])
    stocks_stats['Un Value Now'] = v
    stocks_stats['Total Value Now'] = stocks_stats['Un Value Now']*stocks_stats['Qty']
    stocks_stats.drop(columns='Un Value Now', inplace=True)
    v=[]    
    for i in unique_stocks_ticker:
        v.append(valuation(i))
    stocks_stats['Valuation'] = v
    v=[]
    for i in unique_stocks_ticker:
        v.append(percent_variation(i))
    stocks_stats['Percent variation'] = v
    v=[]
    return stocks_stats


# In[421]:


stocks_stats = main_analisys_values()


# In[ ]:


#Print the results


# In[462]:


print(stocks_stats)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




