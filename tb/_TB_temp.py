import sys
sys.path.append('../lib')

HELP = "m: read temp [C]\n"\
            "cnt : continous mode\n"\
            "h : help\n"

from machine import Pin,SoftSPI
from max31865 import MAX31865
from display import Display
from buzzer import Buzzer
import time

RTD_NOMINAL = 100
RTD_REF = 430
RTD_WIRES = 4

sck = Pin(10, Pin.OUT)
miso = Pin(11, Pin.OUT)
mosi = Pin(12, Pin.IN)
cs = Pin(13, Pin.OUT, value = 1)
spi = SoftSPI(baudrate = 100000, sck=sck, mosi=mosi, miso=miso)
buzzer_pin = Pin(1, Pin.OUT)

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

max31865 = MAX31865(spi, cs, wires = RTD_WIRES)
display = Display(i2c)
buzzer = Buzzer(buzzer_pin)

while True:
    buzzer.beep(0.05)
    time.sleep(1)
