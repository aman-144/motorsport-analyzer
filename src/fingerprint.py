import pandas as pd

data = pd.read_csv('processed_data/hamilton_2023_bahrain.csv') 
print(data)

data['LapTime'] = pd.to_timedelta(data['LapTime'])
avg_lap_time = data['LapTime'].mean() 
print( "Average Lap Time:",avg_lap_time)

data['Sector1Time']=pd.to_timedelta(data['Sector1Time'])
data['Sector2Time']=pd.to_timedelta(data['Sector2Time'])
data['Sector3Time']=pd.to_timedelta(data['Sector3Time'])
avg_sector1_time = data['Sector1Time'].mean()
avg_sector2_time = data['Sector2Time'].mean()
avg_sector3_time = data['Sector3Time'].mean()
print("Average Sector 1 Time:", avg_sector1_time)
print("Average Sector 2 Time:", avg_sector2_time)
print("Average Sector 3 Time:", avg_sector3_time)
