import talib
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date, datetime, timedelta

def get_pattern_names ():
    current_date = date.today()
    thirty_days_prior = datetime.today() - timedelta(days=30)
    
    candle_names_and_values = []
    
    candle_names = talib.get_function_groups()['Pattern Recognition']

    gold_data = pdr.get_data_yahoo('GOLD', str(thirty_days_prior), str(current_date))

    op = gold_data['Open']
    hi = gold_data['High']
    lo = gold_data['Low']
    cl = gold_data['Close']

    for candle in candle_names:
        gold_data[candle] = getattr(talib, candle)(op, hi, lo, cl)
        for item in gold_data[candle]:
            if item > 1 or item < 0: 
                candle_names_and_values.append({'name':candle, 'value': item})

    return candle_names_and_values    