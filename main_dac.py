HELP = "r: write 12-bit value to dac [LSB]\n"\
            "v : write voltage to dac [mV]\n"\
            "l : callibration [mV]\n"\
            "h : help\n"

from mcp4725 import MCP4725
from display import Display
import machine

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

dac = MCP4725(i2c)
display = Display(i2c)

while True:
    
    raw_val = dac.read_raw()[2]
    voltage = dac.read()
    display.show_dac(raw_val, voltage/1000)
    
    
    command = input("Give command:")
    
    tokens = command.split()
    
    if tokens[0] == 'r':
        dac.write_raw(int(tokens[1]))
    elif tokens[0] == 'v':
        dac.write(int(tokens[1]))
    elif tokens[0] == 'l':
        dac.callib(int(tokens[1]))
    elif tokens[0] == 'h':
        print(HELP)
    else:
        print(HELP)
        
    
    
