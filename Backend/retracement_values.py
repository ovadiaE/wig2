from pandas_datareader import data as pdr
import pandas as pd

def get_retracement_values():

    df = pdr.get_data_yahoo('GOLD','2022-01-01', '2022-01-31')

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
        return {'minimum_price': minimum_price} 

    if average >= fourth_level and average < third_level:
        return {'fourth_level':fourth_level}

    if average >= third_level and average < second_level:
        print({'third_level':third_level})
        return {'third_level':third_level}

    if average >= second_level and average < first_level:
        return {'second_level':second_level}

    if average >= first_level and average < maximum_price:
        return {'first_level':first_level}

    if average >= maximum_price:
        return {'maximum_price':maximum_price}