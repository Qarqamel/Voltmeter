import machine
from mcp3424 import MCP3424


sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

mcp3424 = MCP3424(i2c, 0x68, gain = 1, resolution = 16)

print(mcp3424.callib(10))