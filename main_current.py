HELP = "v/c: set param\n"\
            "r : read raw value [LSB]\n"\
            "m : read voltage/current value [V/A]\n"\
            "l : callibration [mV/mA]\n"\
            "cnt : continous mode\n"\
            "h : help\n"

from ina219 import INA219_Voltage, INA219_Current
from display import Display
import machine
import time

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

ina219 = {'v':INA219_Voltage(i2c, 0x40), 'c':INA219_Current(i2c, 0x40)}
current_param = 'v'

display = Display(i2c)

while True:
    
    current = ina219['c'].measure()
    voltage = ina219['v'].measure()
    display.show_ina219(current/1000, voltage/1000)    
    
    command = input("Give command:")
    
    tokens = command.split()
    
    if tokens[0] == 'v':
        current_param = 'v'
    elif tokens[0] == 'c':
        current_param = 'c'
    elif tokens[0] == 'r':
        lsb_val = ina219[current_param].measure_raw()
        print(f"{lsb_val} LSB")
    elif tokens[0] == 'm':
        voltage = ina219[current_param].measure()
        print(f"{voltage} mV")
    elif tokens[0] == 'l':
        ina219[current_param].callib(int(tokens[1]))
#     elif tokens[0] == 'cnt':
#         break;
    elif tokens[0] == 'h':
        print(HELP)
    else:
        print(HELP)
        
# while True:
#     current = ina219['c'].measure()
#     voltage = ina219['v'].measure()
#     display.show_ina219(current/1000, voltage/1000)
#     time.sleep(1)
