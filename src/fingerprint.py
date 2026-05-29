import pandas as pd

def load_driver_data(driver_last_name):
    data = pd.read_csv(f'processed_data/{driver_last_name}_2023_bahrain.csv')
    return data

ham_data = load_driver_data('hamilton')
ver_data = load_driver_data('verstappen')

print (ham_data)
print (ver_data)

def get_average_time(data):
    data['LapTime'] = pd.to_timedelta(data['LapTime'])
    data['Sector1Time'] = pd.to_timedelta(data['Sector1Time'])
    data['Sector2Time'] = pd.to_timedelta(data['Sector2Time'])
    data['Sector3Time'] = pd.to_timedelta(data['Sector3Time'])

    avg_Laptime = data['LapTime'].mean()
    avg_Sector1Time = data['Sector1Time'].mean()
    avg_Sector2Time = data['Sector2Time'].mean()
    avg_Sector3Time = data['Sector3Time'].mean()
    return avg_Laptime, avg_Sector1Time, avg_Sector2Time, avg_Sector3Time

ham_avg_Laptime, ham_avg_S1time, ham_avg_S2time, ham_avg_S3time = get_average_time(ham_data)
ver_avg_Laptime, ver_avg_S1time, ver_avg_S2time, ver_avg_S3time = get_average_time(ver_data)


print("=== FINGERPRINT COMPARISON ===")
print(f"Avg Lap   — Hamilton: {ham_avg_Laptime} | Verstappen: {ver_avg_Laptime}")
print(f"Avg Sector 1  — Hamilton: {ham_avg_S1time} | Verstappen: {ver_avg_S1time}")
print(f"Avg Sector 2  — Hamilton: {ham_avg_S2time} | Verstappen: {ver_avg_S2time}")
print(f"Avg Sector 3  — Hamilton: {ham_avg_S3time} | Verstappen: {ver_avg_S3time}")




