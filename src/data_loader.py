import fastf1
session = fastf1.get_session(2023,'Bahrain', 'R') #ye srif address dega ki data yaha rkha hai
session.load() #ye data load karega ya esa samjho ye data ko leke ayegga
for driver_number in session.drivers:
    driver_info = session.get_driver(driver_number)
    if driver_info['LastName']== 'Hamilton': #ye hamilton ke data ko filter karega
        print(driver_info['DriverNumber']) #ye hamilton ke driver number ko print karega
        print(driver_info['Abbreviation']) #ye hamilton ke abbreviation ko print karega
