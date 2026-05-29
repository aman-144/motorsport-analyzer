import pandas as pd

def load_driver_data(driver_last_name):
    data = pd.read_csv(f'processed_data/{driver_last_name}_2023_bahrain.csv')
    return data

ham_data = load_driver_data('hamilton')
ver_data = load_driver_data('verstappen')

print (ham_data)
print (ver_data)









