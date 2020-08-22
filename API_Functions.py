# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:28:31 2020

@author: Igor
"""

import APIs_Keys
import requests


def get_api_marketstack_bvmf_data(ticker):
    params = {'access_key': APIs_Keys.api_marketstack_key}
    api_result = requests.get('http://api.marketstack.com/v1/tickers/{}.BVMF/eod/latest'.format(ticker), params)
    api_response = api_result.json()
    return api_response

