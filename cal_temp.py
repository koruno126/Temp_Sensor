#cal Temp Program

import BME280_sample as BME280
import lcd_i2c as lcd

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

#init LCD
lcd.lcd_init()

#Weather_data = BME280.readData()

#Test Read Weather Data
#print(Weather_data)
#print(type(Weather_data))

#Read BME280 Data
temp,hum,pres = BME280.readData()

lcd.lcd_string("T "+"{0:3.1f}".format(temp)+"C H "+"{0:3.1f}".format(hum)+"%",LCD_LINE_1)
lcd.lcd_string("Press "+"{0:5.1f}".format(pres)+"hPa",LCD_LINE_2)

