import time
import board
import busio
import adafruit_pm25
import csv
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

reset_pin = None

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)



print("Found PM2.5 sensor, reading data...")

f = open("Lab4Data.csv","w", newline='')
meta_data = ["Time", "pm10_standard", "pm25_standard", "pm100_standard"]
writer = csv.writer(f)
writer.writerow(meta_data)

for i in range(0,10):
    time.sleep(1)
    timeCurrent = time.time()
    print(timeCurrent)
    
    try:
        aqdata = pm25.read()
        #print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    
    writer.writerow([timeCurrent, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]]) 

f.close()
