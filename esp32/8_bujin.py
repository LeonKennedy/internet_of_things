from machine import PWM, Pin
import time



# GND：黑褐色
# VCC：红色
# 数据线：橙色

# 不能接错 电流过大 很热

class Servo:
    # 舵机只需要一段时间调整到位就行，所以每次发送信号后就关闭。减少cpu中断的占用
    def __init__(self, pin_num):
        self.pin_num = pin_num
        self.pwm = PWM(Pin(self.pin_num), freq=50) # 调整频率 50Hz (default 5kHz)
    
    
    
    def _mirco_second(self, ms):
        self.pwm.duty_ns(int(1e6 * ms))
        
    def angle0(self):
        self._mirco_second(0.5) 
        
    def angle45(self):
        self._mirco_second(1)
        
    def angle90(self):
        self._mirco_second(1.5)
        
    def angle145(self):
        self._mirco_second(2)

    def angle180(self):
        self._mirco_second(2.5)
        
    def show(self):
        while 1:
            for i in [0.5, 1, 1.5, 2, 2.5]:
                self._mirco_second(i)
                time.sleep(1)
        
    
if __name__ == "__main__":
    ser = Servo(15)
    ser.show()
