import pandas as pd
import requests
import json
from PIL import Image
import streamlit as st

#---------------------------------#


#---------------------------------#
# Title

image = Image.open('curr4.jfif')

# st.image(image,width=550)

st.image(image,use_column_width=True)
# st.subheader('Currency Convertor App')


st.markdown('''
**This app converts the value of foreign currencies!!**
''')

#---------------------------------------------#
#Sidebar + Main Panel
st.sidebar.header('Input Options')

### Sidebar - Currency price unit
currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
base_price_unit = st.sidebar.selectbox('Select base currency:',currency_list)
symbols_price_unit = st.sidebar.selectbox('Select target currency:',currency_list)

#Retrieving currency data from ratesapi.io

@st.cache
def load_data():
    url = ''.join(['https://api.ratesapi.io/api/latest?base=',base_price_unit,'&symbols=',symbols_price_unit])
    response = requests.get(url)
    data = response.json()
    base_currency = pd.Series(data['base'],name = 'Base Currency')
    rates_df = pd.DataFrame.from_dict(data['rates'].items())
    rates_df.columns = ['Converted Currency','Price']
    conversion_date = pd.Series(data['date'],name = 'Date')
    df = pd.concat([base_currency,rates_df,conversion_date],axis = 1)
    return df


df = load_data()
st.balloons()
st.subheader('Currency Conversion')

st.table(df)

#About

st.info('** Python Libraries** : pandas, streamlit, json and requests ')
st.info('** Data Source**: https://ratesapi.io')

