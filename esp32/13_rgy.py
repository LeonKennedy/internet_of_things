# 红路灯

from machine import Pin
import time

red = Pin(15, Pin.OUT) 
yellow = Pin(2, Pin.OUT) 
green = Pin(4, Pin.OUT) 

while 1:
    red.on()
    time.sleep(2)
    red.off()
    yellow.on()
    time.sleep(2)
    yellow.off()
    green.on()
    time.sleep(2)
    green.off()
