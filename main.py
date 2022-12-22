# Blinky example

import time
from machine import Pin

# This is the only LED pin available on the Nano RP2040,
# other than the RGB LED connected to Nina WiFi module.
led = Pin(6, Pin.OUT)

while (True):
   led.on()
   time.sleep_ms(150)
   led.off()
   time.sleep_ms(100)
   led.on()
   time.sleep_ms(150)
   led.off()
   time.sleep_ms(600)
