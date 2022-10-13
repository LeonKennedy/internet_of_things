from machine import Pin
import time

# 给模块1个最少10us的高电平，模块接受到高电平后开始发射8个40KHz的声波，
# echo脚会由0变为1,MCU开始计时，当超声波模块接收到返回的声波时，echo由1变为0,MCU停止计时，
# 这时间差就是测距总时间，在乘声音的传播速度340米/秒，除2就是距离。
trig = Pin(2, Pin.OUT)
echo = Pin(15, Pin.IN)

def distance():
    trig.on()
    time.sleep_us(14)
    trig.off()
    while echo.value() == 0:
        pass
    while echo.value() == 1:
        ts = time.ticks_us() # microseconds
        while echo.value() == 1:
            pass
        te = time.ticks_us()
        tc = te - ts
        distance_value = round(tc / 1000000 * 340 / 2, 2)
    return distance_value

while 1:
    dist = distance()
    print("ditance: ", dist, " m")
    time.sleep(2)