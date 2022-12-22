from machine import Pin,I2C#, RTC
from PicoDHT22 import PicoDHT22
import utime, time, machine, ds1307



import board
import busio
from digitalio import DigitalInOut
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
#from pytz import timezone
# DHT22 libray is available at
# https://github.com/danjperron/PicoDHT22
#tz = timezone('EST')
#datetime.now()

#rtc = RTC()
#rtc.datetime((2022, 11, 20, 7, 14, 03, 00, 0))
#TempSensor = machine.ADC(4)
#conversion_factor = 3.3 / 65535

#i2c = I2C(1)
#sleep(1)



#i2c=I2C(0, scl=Pin(13), sda=Pin(12))
#i2c = I2C(1)
#r=machine.RTC()

#print(i2c.scan())
#ds = ds1307.DS1307(i2c)
#ds.setDateTime([2021, 8, 26, 4, 23, 59, 58, 0])
#ds.halt(False)

#print("ds1307: ",ds.readDateTime())
#print("rtc:    ",r.datetime())

red = Pin(7, Pin.OUT, Pin.PULL_DOWN)
green = Pin(5, Pin.OUT, Pin.PULL_DOWN)
PirSensor = Pin(4, Pin.IN, Pin.PULL_DOWN)

def motion_det():
    if PirSensor.value() ==1:
        print("motion detected")
        red.value(1)
        green.value(0)
        return True
    else:
        print("no motion")
        red.value(0)
        green.value(1)
        return False

#dht_sensor = PicoDHT22(Pin(21,Pin.IN,Pin.PULL_UP),dht11=True)
dht_sensor = PicoDHT22(Pin(26,Pin.IN,Pin.PULL_UP),dht11=True)
while True:
    #data = TempSensor.read_u16() * conversion_factor
    #temperature = 27-(data-0.706)/0.001721
    #print(str(temperature))
    #print(rtc.datetime())
    value = motion_det()
    print (value)
    T,H = dht_sensor.read()
    if T is None:
        print(" sensor error")
    else:
        print("{}'C  {}%".format(T,H))
    time.sleep(10)

    #DHT22 not responsive if delay too short
    #utime.sleep_ms(1100)
