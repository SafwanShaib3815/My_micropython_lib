from machine import Pin, Timer, PWM
import time
import _thread

#my imports
import ocdoor
lock = _thread.allocate_lock()
reset = Pin(20, Pin.IN, Pin.PULL_UP)
pir = Pin(5, Pin.IN, Pin.PULL_UP)
led1= Pin(21, Pin.OUT)

#*************************************************************
def run(task_id):
    lock.acquire()
    led = Pin(25, Pin.OUT)
    while True:
        for x in range(3):
            led.high()
            time.sleep(0.2)
            led.low()
            time.sleep(0.05)
        if reset.value() == 0:
            ocdoor.opendoor()
        if pir.value() == 0:
            print("blink releasing .......")
            lock.release()
            return
#*************************************************************
def fade():
    pwm = PWM(Pin(25))
    # Set the PWM frequency.
    pwm.freq(1000)
    duty = 0
    direction = 1
    while True:
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)
        if pir.value() == 1:
            return



def main():
    ocdoor.opendoor()
#     _thread.start_new_thread(run, ("fade",))

    while True:
        fade()
        ocdoor.closedoor()
        led1.high()
        time.sleep(0.4)
        print("LED On")
        _thread.start_new_thread(run, ("blink",))
        
        time.sleep(1)
        while reset.value():
            time.sleep(0.01)
            if reset.value() == 0:
                ocdoor.opendoor()
                led1.low()
                time.sleep(0.3)
                continue                      
          
if __name__ == "__main__":
    main()

