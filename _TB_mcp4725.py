import machine
from mcp4725 import MCP4725


sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

mcp4725 = MCP4725(i2c, 0x60)
# mcp.config()

print(mcp4725.write(1600))