from pandas_datareader import data as pdr
import pandas as pd
from datetime import date, datetime, timedelta
from particle_object import particles_json 
from flask import jsonify 

def get_retracement_values():
    current_date = date.today()
    thirty_days_prior = datetime.today() - timedelta(days=30)
    
    df = pdr.get_data_yahoo('GOLD', str(thirty_days_prior), str(current_date))

    maximum_price = df['Close'].max()
    minimum_price = df['Close'].min()
    average = 0
    
    #Calculates average closing price over the 30 day period
    for item in df['Close']:
        average += item
    average = average/len(df['Close'])
    
    #Creating the retracement levels using Fibbonacci ratios 
    difference = maximum_price - minimum_price
    first_level = maximum_price - difference * 0.236
    second_level = maximum_price - difference * 0.382
    third_level = maximum_price - difference * 0.5
    fourth_level = maximum_price - difference * 0.618
    
    if average <= minimum_price or average > minimum_price and average < fourth_level:
        return particles_json('#800080')

    if average >= fourth_level and average < third_level:
        return particles_json('#0000FF')

    if average >= third_level and average < second_level:
        return particles_json('#008000')
    
    if average >= second_level and average < first_level:
        return particles_json('#800080')

    if average >= first_level and average < maximum_price:
        return particles_json('#FFFF00')

    if average >= maximum_price:
        return particles_json('#FF0000')
