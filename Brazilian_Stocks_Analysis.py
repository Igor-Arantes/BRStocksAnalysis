#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Libraries Importation


# In[2]:


import pandas as pd


# In[3]:


import seaborn as sns


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


#Dada source


# In[6]:


url = "https://docs.google.com/spreadsheets/d/1I93xay8dfxiL25qYohMAFIbh204vHBJSC3iKm_Y-Apc/edit?usp=sharing"


# In[7]:


o = pd.read_html(url, index_col=1, skiprows = 1)


# In[8]:


xlsx_path = ('Carteira Acoes B3.xlsx')


# In[9]:


e = pd.read_excel(xlsx_path)


# In[ ]:





# In[10]:


#Fitting Data


# In[11]:


stocks_now = o[0]
stocks_now = stocks_now.dropna().drop(columns=['1'])
stocks_dataframe = e.dropna()
stocks_dataframe.rename(columns={'Codigo da Açao':'Ticker', 'Valor Pago': 'Valor_Pago'}, inplace = True)


# In[ ]:





# In[12]:


#Pick Sotock by Ticker


# In[13]:


def ticker_location(ticker_desired):
    return raw_data.loc[(raw_data["Ticker"] == ticker_desired)]
    


# In[14]:


#Finding the total price and add then to the dataframe


# In[15]:


stocks_dataframe['Valor Total'] = stocks_dataframe['Quantidade'] * stocks_dataframe['Valor_Pago']


# In[16]:


#Find Stock by Ticker


# In[17]:


def find_all_stock(ticker_desired):
    return stocks_dataframe['Ticker']==ticker_desired


# In[ ]:





# In[18]:


#Mean Value Stock Price


# In[19]:


def mean_price_paid(ticker_desired):
    x=stocks_dataframe[find_all_stock(ticker_desired)].sum()
    return round(x[-1]/x[1],2)


# In[20]:


#Sum of desired stock


# In[21]:


def sum_stock_desired(ticker_desired):
    x=stocks_dataframe[find_all_stock(ticker_desired)].sum()
    return x[1]


# In[22]:


#valuation or devaluation in total


# In[23]:


def valuation(ticker_desired):
    return round((stocks_now.loc[ticker_desired, 'Preco']-mean_price_paid(ticker_desired))*sum_stock_desired(ticker_desired),2)


# In[24]:


#Percent variation


# In[25]:


def percent_variation(ticker_desired):
    return round(((stocks_now.loc[ticker_desired, 'Preco']-mean_price_paid(ticker_desired))/stocks_now.loc[ticker_desired, 'Preco'])*100,2)


# In[26]:


#Geting a series of uniques stocks names


# In[27]:


unique_stocks_ticker = stocks_dataframe['Ticker'].unique()


# In[28]:


#Creating a data frame with the main analysis values


# In[29]:


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


# In[30]:


stocks_stats = main_analisys_values()


# In[31]:


#Print the results


# In[115]:


print(stocks_stats)


# In[106]:


#Setting green to positive values and red to negative ones

for i in range(0, len(stocks_stats.Valuation)):
    if  stocks_stats.Valuation[i] >= 0:
        custom_palette[stocks_stats.Ticker[i]] = 'g'
    else:
        custom_palette[stocks_stats.Ticker[i]] = 'r'
        
#Ploting valuations data
sns.set(style='whitegrid')
plt.figure(figsize=(15,8)) 
sns.barplot(x='Ticker', y='Valuation', data=stocks_stats, palette=custom_palette)


# In[114]:


#Setting green to positive values and red to negative ones
for i in range(0, len(stocks_stats['Percent variation'])):
    if  stocks_stats['Percent variation'][i] >= 0:
        custom_palette[stocks_stats.Ticker[i]] = 'g'
    else:
        custom_palette[stocks_stats.Ticker[i]] = 'r'
        
#Ploting percent data
sns.set(style='whitegrid')
plt.figure(figsize=(15,8)) 
sns.barplot(x='Ticker', y='Percent variation', data=stocks_stats, palette=custom_palette)


# In[ ]:




