from machine import Pin, ADC
import time


x = ADC(Pin(12), atten = ADC.ATTN_6DB)
y = ADC(Pin(13), atten = ADC.ATTN_6DB)
z = Pin(14, Pin.IN)


while 1:
    print(x.read(), y.read(), z.value())
    time.sleep_ms(100)
