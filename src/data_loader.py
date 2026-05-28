import fastf1

session = fastf1.get_session(2023,'Bahrain', 'R') #ye srif address dega ki data yaha rkha hai
session.load() #ye data load karega ya esa samjho ye data ko leke ayegga

for driver_number in session.drivers:
    driver_info = session.get_driver(driver_number)
    if driver_info['LastName']== 'Hamilton': #ye hamilton ke data ko filter karega
      #  print(driver_info['DriverNumber']) #ye hamilton ke driver number ko print karega
      #  print(driver_info['Abbreviation']) #ye hamilton ke abbreviation ko print karega

         ham_driver_num = driver_info['DriverNumber'] #ye hamilton ke driver number ko ham_driver_num variable me
         ham_driver_abrev = driver_info['Abbreviation'] #ye hamilton ke abbreviation ko ham_driver_abrev variable me store karega
         

         laps = session.laps.pick_drivers(ham_driver_num) #ye hamilton ke laps ko filter karega driver num se kyuki ye unique hota hai 


         if laps.empty:
             laps = session.laps.pick_drivers(ham_driver_abrev) #ye hamilton ke laps ko filter karega abbreviation se kyuki driver num se filter karne par empty aa raha hai

         if laps.empty:
             print("No laps found for Hamilton.")

         else:
              print(laps)


         break
