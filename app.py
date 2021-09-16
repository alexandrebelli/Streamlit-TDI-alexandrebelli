#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Wed Sep 15 @author: alexandrebelli"""import requestsimport pandas as pdimport streamlit as stsymbol = 'BA'import osimport dotenvfrom dotenv import load_dotenvst.title("Visualizing Time Series Stock")st.sidebar.write(f'(Enter Symbol (e.g. BA): : ', symbol)load_dotenv()CONSUMER_KEY = os.environ.get("Key")# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey='+CONSUMER_KEY#r = requests.get(url)#data = pd.read_json(url)##data = r.json()##data= pd.json_normalize(data['Time Series (Daily)'])#print(data)url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol='+str(symbol)+'&apikey='+str(CONSUMER_KEY)+'&datatype=csv'#r = requests.get(url)#print('checkPoint')data = pd.read_csv(url)#data = r.json()#data= pd.json_normalize(data['Time Series (Daily)'])#print(data)import numpy as npfrom bokeh.layouts import gridplotfrom bokeh.plotting import figure, show#from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT#def datetime(x):    return np.array(x, dtype=np.datetime64)p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")p1.grid.grid_line_alpha=0.3p1.xaxis.axis_label = 'Date'p1.yaxis.axis_label = 'Price'st.line_chart(datetime(data))#show(p1)#print('DONE')