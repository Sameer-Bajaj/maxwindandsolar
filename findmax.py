import pandas as pd
import pytz


def maxwindsolar(input_csv):
    data = pd.read_csv(input_csv)
    data['period'] = pd.to_datetime(data['period'])
    data['period'] = data['period'].dt.tz_localize('UTC')
    data['period'] = data['period'].dt.tz_convert('US/Pacific')
    tot_WS = data.groupby("period")["value"].sum()
    tot = data.groupby('period')['total'].first()
    share = (tot_WS/tot).fillna(0)
    max_period = share.idxmax()
    FTshares = data[data["period"] == max_period]
    FTshares = FTshares[['period','type-name', 'value', 'value-units']]
    FTshares.to_csv(input_csv[:-4]+"maxshares.csv", index=False)
    print("The time with max share of wind and solar is ", max_period)
    print("The shares of each fueltype at that type is \n", FTshares)
input_csv = '' #Example: entire2021.csv
maxwindsolar(input_csv)
