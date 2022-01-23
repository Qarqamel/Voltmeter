from machine import Pin,SoftSPI
from max31865 import MAX31865
from display import Display

RTD_NOMINAL = 100
RTD_REF = 430
RTD_WIRES = 4

sck = Pin(10, Pin.OUT)
miso = Pin(11, Pin.OUT)
mosi = Pin(12, Pin.IN)
cs = Pin(13, Pin.OUT, value = 1)
spi = SoftSPI(baudrate = 100000, sck=sck, mosi=mosi, miso=miso)

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

max31865 = MAX31865(spi, cs, wires = RTD_WIRES)
display = Display(i2c)

print(f"{max31865.temperature}")
display.show_temp(max31865.temperature)