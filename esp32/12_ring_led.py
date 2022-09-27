from machine import Pin
from neopixel import NeoPixel

pin = Pin(13, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
pini = Pin(2, Pin.IN)  
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 0, 0) # set the first pixel to white
np[1] = (0, 255, 0)
np[2] = (0, 0, 255)
np.write()              # write data to all pixels
r, g, b = np[6]         # get first pixel colour
print(r, g, b)
