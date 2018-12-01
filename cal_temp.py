#cal Temp Program

import BME280_sample as BME280
import lcd_i2c as lcd

Weather_data = BME280.readData()

print(Weather_data)
print(type(Weather_data))
