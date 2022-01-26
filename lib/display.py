import machine
from ssd1306 import SSD1306_I2C
import framebuf
import freesans24
import freesans28
import freesans46
import writer

class Display:
    
    __CHAN_NAMES = {0:'core', 1:'peri', 2:'ddm', 3:'dda', 4:'disc'}
    
    def __init__(self, i2c):    
        self._oled = SSD1306_I2C(128, 64, i2c)
        self._font_writer_24 = writer.Writer(self._oled, freesans24)
        self._font_writer_dac = writer.Writer(self._oled, freesans28)
        self._font_writer_temp = writer.Writer(self._oled, freesans46)
        
        
    def show(self, chan_nr, curr, vol):
        self._oled.fill(0)
        for x,y,t in zip((0,48,48),(22,8,40),(self.__CHAN_NAMES[chan_nr],f"{curr:.3f}V",f"{vol:.3f}A")):
            self._font_writer_24.set_textpos(x, y)
            self._font_writer_24.printstring(t)
        self._oled.show()
        
    def show_dac(self, lsb, vol):
        self._oled.fill(0)
        for x,y,t in zip((0,0), (0,32), (f"{lsb:04} LSB", f"{vol:.3f} V")):
            self._font_writer_dac.set_textpos(x, y)
            self._font_writer_dac.printstring(t)
        self._oled.show()
        
    def show_ina219(self, curr, vol):
        self._oled.fill(0)
        for x,y,t in zip((0,0), (0,32), (f"{curr:.3f} A", f"{vol:.3f} V")):
            self._font_writer_dac.set_textpos(x, y)
            self._font_writer_dac.printstring(t)
        self._oled.show()
    
    def show_adc(self, vol):
        self._oled.fill(0)
        self._font_writer_dac.set_textpos(0, 20)
        self._font_writer_dac.printstring(f"{vol:.3f} V")
        self._oled.show()
    
    def show_adc_cnt(self, voltages):
        self._oled.fill(0)
        for x,y,t in zip((0,0), (0,32), (f"{voltages[0]:.3f} V", f"{voltages[1]:.3f} V")):
            self._font_writer_dac.set_textpos(x, y)
            self._font_writer_dac.printstring(t)
        self._oled.show()
        
    def show_temp(self, temp):
        self._oled.fill(0)
        self._font_writer_temp.set_textpos(0, 10)
        self._font_writer_temp.printstring(f"{temp:.1f}C")
        self._oled.show()
            
            
            