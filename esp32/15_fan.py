# 电风扇

from machine import Pin, PWM

p1 = Pin(13, Pin.OUT)
p2 = Pin(12, Pin.OUT)


def on():
    p1.value(0)
    p2.value(1)

def inverse():
    p1.value(1)
    p2.value(0)

def off():
    p1.value(0)
    p2.value(0)

