import fastf1

session = fastf1.get_session(2023,'Bahrain', 'R') #ye srif address dega ki data yaha rkha hai
session.load() #ye data load karega ya esa samjho ye data ko leke ayegga

driver_last_name = 'Verstappen'

for driver_number in session.drivers:
    driver_info = session.get_driver(driver_number)
    if driver_info['LastName']== driver_last_name: #ye hamilton ke data ko filter karega
      #  print(driver_info['DriverNumber']) #ye hamilton ke driver number ko print karega
      #  print(driver_info['Abbreviation']) #ye hamilton ke abbreviation ko print karega

         ham_driver_num = driver_info['DriverNumber'] #ye hamilton ke driver number ko ham_driver_num variable me
         ham_driver_abrev = driver_info['Abbreviation'] #ye hamilton ke abbreviation ko ham_driver_abrev variable me store karega
         

         laps = session.laps.pick_drivers(ham_driver_num) #ye hamilton ke laps ko filter karega driver num se kyuki ye unique hota hai 


         if laps.empty:
             laps = session.laps.pick_drivers(ham_driver_abrev) #ye hamilton ke laps ko filter karega abbreviation se kyuki driver num se filter karne par empty aa raha hai

         if laps.empty:
             print(f"No laps found for {driver_last_name}.")

         else:
              print(laps)


         #break

clean_laps = laps[laps['IsAccurate'] == True]
clean_laps = clean_laps[['Time', 'LapNumber', 'LapTime', 
                          'Sector1Time', 'Sector2Time', 'Sector3Time',
                          'SpeedI1', 'SpeedI2', 'SpeedFL',
                          'Compound', 'TyreLife', 'Position', 
                          'IsAccurate']]
print(clean_laps)

best_lap = clean_laps[clean_laps['LapTime']==clean_laps['LapTime'].min()]
print(best_lap)
 
clean_laps.to_csv(f'processed_data/{driver_last_name}_2023_bahrain.csv', index=False) #ye clean laps ko csv file me save karega
 