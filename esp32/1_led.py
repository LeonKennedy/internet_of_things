from machine import Pin, PWM
import time

p2 = Pin(2, Pin.OUT)    # create output pin on GPIO0
p2.on()                 # set pin to "on" (high) level


def flash():
    

    while 1:
        time.sleep(1)
        p2.on()
        time.sleep(2)
        p2.off()


# PWN Pulse Width Modulation
def pwn_exp():
    led = PWM(p2)
    
    while 1:
        for i in range(1024):
            led.duty(i)
            time.sleep_ms(2)
        for j in range(1023, -1, -1):
            led.duty(j)
            time.sleep_ms(2)
            

pwn_exp()
            