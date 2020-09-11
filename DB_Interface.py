# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 19:12:37 2020

@author: Igor
"""
import pandas as pd
import DB_Conetion as dbc



def get_purchased_table():
    query = ("SELECT * FROM purchased ;")
    return pd.read_sql(query, dbc.conn)

def get_sold_table():
    query = ("SELECT * FROM sold ;")
    return pd.read_sql(query, dbc.conn)

def register_purchase(Ticker, QTY, Price, Class, Purchase_Date, Market):
    return dbc.cur.execute("INSERT INTO purchased(ID, Ticker,  QTY , Price ,  Class, Purchase_Date, Market) VALUES(NULL, ?,?,?,?,?,?);",(Ticker, QTY, Price, Class, Purchase_Date, Market)), dbc.conn.commit()

def register_sales(Ticker, QTY, Price, Sale_Date, Market):
    return dbc.cur.execute("INSERT INTO sales(ID, Ticker,  QTY , Price ,  Class, Sale_Date, Market) VALUES(NULL, ?,?,?,?,?,?);",(Ticker, QTY, Price, Sale_Date, Market)), dbc.conn.commit()


