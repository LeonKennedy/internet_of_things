import time
from machine import SoftI2C, Pin
from i2c_lcd import I2cLcd


DEFAULT_I2C_ADDR = 0x3f
i2c = SoftI2C(sda=Pin(15),scl=Pin(2),freq=100000)
print(i2c.scan())
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

i=0
while True:
    lcd.clear()
    lcd.putstr("Red with coffee\n")
    lcd.putstr(" " * i)
    lcd.putstr("520")
    
    
    time.sleep(1)
    i += 1
    if i > 12:
        i = 0