
import Adafruit_DHT
import time
import os
import time
from smbus import SMBus

DEV_ADDR = 0x48
adc_channel = 0b1000010 # 0x42 (input AIN2 for ADC + use DAC)
dac_channel = 0b1000000 # 0x40

bus = SMBus(1)          # 1 - I2C bus address for RPi rev.2
sensor = Adafruit_DHT.DHT11
pin =17
RL=10
R0=76.63


humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
while True:
	os.system('clear')
    print("Press Ctrl C to stop...\n")
    # read sensor value from ADC
    bus.write_byte(DEV_ADDR, adc_channel)
    bus.read_byte(DEV_ADDR)
    bus.read_byte(DEV_ADDR)
    value = bus.read_byte(DEV_ADDR)
    if value > 120:
        bus.write_byte_data(DEV_ADDR, dac_channel, 220)
    else:
        bus.write_byte_data(DEV_ADDR, dac_channel, 0)
    Rs=( ( 5.0 * RL ) - ( RL* value ) ) / value
    ratio=Rs/R0
    ratio=ratio*0.3611
    CO2= (146.15*(2.868-ratio)+10)
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*C  Humidity={1:0.1f}% '.format(temperature,humidity))
		print(CO2,"ppm")
    time.sleep(0.1)



