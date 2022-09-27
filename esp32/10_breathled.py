from machine import Pin, PWM
import time



class BreathLed:

    def __init__(self, num:int, freq: int = 50):
        self.led = PWM(Pin(4), freq=freq) # frequency from 1Hz to 40MHz

    def cyclic(self, seconds: int = 2):
        while 1:
            for i in range(50, 1023, 20):  # 0-1023
                self.led.duty(i) #  duty_u16 get current duty cycle, range 0-65535
                time.sleep_ms(20)
            for i in range(1023, 50, -20):
                print(i)
                self.led.duty(i)
                time.sleep_ms(20)



if __name__ == "__main__":
    # out 用来接受输入
    breath_led =  BreathLed(4)
    breath_led.cyclic()

