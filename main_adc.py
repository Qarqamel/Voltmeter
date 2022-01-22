HELP = "ch: set channel\n"\
            "r : read raw value [LSB]\n"\
            "v : read voltage value [V]\n"\
            "l : callibration [mV]\n"\
            "cnt : continous mode\n"\
            "h : help\n"

from mcp3424 import MCP3424
from display import Display
import machine

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

adc = MCP3424(i2c)
display = Display(i2c)

while True:
    
#     raw_val = adc.read_raw()
#     voltage = adc.read()
#     display.show_dac(raw_val, voltage/1000)    
    
    command = input("Give command:")
    
    tokens = command.split()
    
    if tokens[0] == 'ch':
        adc.set_channel(int(tokens[1]))
    elif tokens[0] == 'r':
        lsb_val = adc.read_raw()
        print(f"{lsb_val} LSB")
    elif tokens[0] == 'v':
        voltage = adc.read()
        print(f"{voltage} V")
    elif tokens[0] == 'l':
        adc.callib(int(tokens[1]))
#     elif tokens[0] == 'cnt':
#         while True:
#             reads=[]
#             for i in range(4):
#                 adc.set_channel(i)
#                 reads.append(adc.read())
#             display.show_adc_cnt(reads)
    elif tokens[0] == 'h':
        print(HELP)
    else:
        print(HELP)