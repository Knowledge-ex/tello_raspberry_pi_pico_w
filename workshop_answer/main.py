from tello import Tello
from machine import Pin
import time

swTakeOff = Pin(14,Pin.IN,Pin.PULL_DOWN)
swLanding = Pin(15,Pin.IN,Pin.PULL_DOWN)
swUp      = Pin(17,Pin.IN,Pin.PULL_DOWN)
swDown    = Pin(24,Pin.IN,Pin.PULL_DOWN)
swForward = Pin(15,Pin.IN,Pin.PULL_DOWN)
swBack    = Pin(26,Pin.IN,Pin.PULL_DOWN)
swLeft    = Pin(12,Pin.IN,Pin.PULL_DOWN)
swRight   = Pin(10,Pin.IN,Pin.PULL_DOWN)
swCw      = Pin(29,Pin.IN,Pin.PULL_DOWN)
swCCw     = Pin(31,Pin.IN,Pin.PULL_DOWN)

led=Pin("LED",Pin.OUT)
led.high()

print("ドローンプログラミング")

tello=Tello("TELLO-E") # "TELLO-E"はTelloのSSIDです。適宜書き換えてください。

while True:
    if(swTakeOff.value()==1):
        print("TakeOff")
        tello.sendCommand("takeoff")
    if(swLanding.value()==1):
        print("Land")
        tello.sendCommand("land")
    if(swUp.value()==1):
        print("Up")
        tello.sendCommand("up 30")
    if(swDown.value()==1):
        print("Down")
        tello.sendCommand("down 30")
    if(swForward.value()==1):
        print("Forward")
        tello.sendCommand("forward 30")
    if(swBack.value()==1):
        print("Back")
        tello.sendCommand("back 30")
    if(swLeft.value()==1):
        print("Left")
        tello.sendCommand("left 30")
    if(swRight.value()==1):
        print("Right")
        tello.sendCommand("right 30")
    if(swCw.value()==1):
        print("ClockWise")
        tello.sendCommand("cw 90")
    if(swCCw.value()==1):
        print("CounterClockWise")
        tello.sendCommand("ccw 90")
    time.sleep(0.5)
