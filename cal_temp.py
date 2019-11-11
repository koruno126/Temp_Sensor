#cal Temp Program

import pycode

import pycode.BME280_sample as BME280
import pycode.lcd_i2c as lcd
import time
import datetime
import csv

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

#BKC height
height = 81

Error_flag = True
#interval of measureing temp
interval = 0.5
#init LCD
lcd.lcd_init()
#keep minute
keep_minute = -1

try:
	while True:
		#Weather_data = BME280.readData()
		
		#Test Read Weather Data
		#print(Weather_data)
		#print(type(Weather_data))
		try:
			if Error_flag:
				lcd.lcd_init()
				#BME280.setup()
				#BME280.get_calib_param()
				Error_flag = False
			#Read BME280 Data
			temp,hum,pres = BME280.readData()
			#print(temp)
			#pres_zero = zero height pres
			pres_zero = pres*pow((1-0.0065*height/(temp + 0.0065*height+273.15)),-5.257)

			lcd.lcd_string("T "+"{0:3.1f}".format(temp)+"C H "+"{0:3.1f}".format(hum)+"%",LCD_LINE_1)
			lcd.lcd_string("Press "+"{0:5.1f}".format(pres_zero)+"hPa",LCD_LINE_2)
		except IOError:
			print("IOError")
			Error_flag = True

		now = datetime.datetime.now()
		#now to str
		#now.strftime("%Y/%m/%d %H:%M:%S")
		
		if(now.minute != keep_minute):
			#print('csv write')
			#make temp data list by list
			temp_data_list = [now.strftime("%Y/%m/%d %H:%M"),temp,hum,pres_zero]

			data_file_name = 'temp_data/' + now.strftime("%Y_%m_%d") + ".csv"
			with open(data_file_name,'a') as f:
				writer = csv.writer(f,lineterminator='\n')
				writer.writerow(temp_data_list)
			keep_minute = now.minute
		
		time.sleep(interval)
except KeyboardInterrupt:
	time.sleep(0.01)
	lcd.lcd_byte(0x01,0)

