# Untitled - By: Will - Sat Nov 19 2022

#import time
from machine import Pin, ADC
import machine
from time import sleep
#import dht
#define DHTTYPE DHT11
#pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)
#pin = Pin(27, Pin.IN, Pin.PULL_UP)
#d = dht.DHT11(pin)
print("Hello")
#adcpin = machine.Pin(29, Pin.OUT)
adcpin = machine.Pin(29)
sensor = machine.ADC(adcpin)
#sensor.atten(ADC.ATTN_11DB)
while True:
    sleep(2)
    #print(machine.Pin(27, Pin.IN, machine.Pin.PULL_UP).value())
    #try:
    value = sensor.read_u16()
    #value = adcpin.value()
    print(value)
        #d.measure()
        #temp = d.temperature()
        #print(d.temperature())
        #print(temp)
    #except OSError as e:
        #print('Failed to read sensor.')
#i2c = I2C(scl=Pin(13), sda=Pin(12))
#print('i2c scan:',i2c.scan())

#import at24c32n
#eeprom = at24c32n.AT24C32N(i2c)
## read 32 bytes starting from memory address 0
#eeprom.read(0, 32)


#import ds1307
#ds = ds1307.DS1307(i2c)
#ds.datetime()
#ds.datetime(now)

#print(ds.datetime)
#led = Pin(18, Pin.OUT)
##light =

#while (True):
    #led.on()
    #time.sleep_ms(250)
    #led.off()
    #time.sleep_ms(250)
