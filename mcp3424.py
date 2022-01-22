from mcp342x import MCP342x
from nonvolatile_float import nonvolatile_float

class MCP3424:
    
    __CHANNEL_NR = 4
    
    def __init__(self,
                 i2c,
                 address = 0x68,
                 gain=1,
                 resolution=16,):
        
        self._Channels = [MCP342x(i2c, address,device='MCP3424',channel = i, gain = gain, resolution = resolution) for i in range(self.__CHANNEL_NR)]
        self._callib_coef = [nonvolatile_float() for i in range(self.__CHANNEL_NR)]
        self._ch_nr = 0
        
        
    def set_channel(self, nr):
        self._ch_nr = nr
        
    def read_raw(self):
        return self._Channels[self._ch_nr].raw_read()[0]
    
    def read(self):
        return self.read_raw()*self._callib_coef[self._ch_nr].get()
    
    def callib(self, measured_mili):
        self._callib_coef[self._ch_nr].set(measured_mili/self.read_raw())
        self._callib_coef[self._ch_nr].save()
        
    def read_coefficient(self):
        return self._callib_coef[self._ch_nr].get()
    
    
        
    