import machine
from ssd1306 import SSD1306_I2C
import framebuf
import freesans23
import freesans24
import freesans28
import writer

class Display:
    
    __CHAN_NAMES = {0:'core', 1:'peri', 2:'ddm', 3:'dda', 4:'disc'}
    
    def __init__(self, i2c):    
        self._oled = SSD1306_I2C(128, 64, i2c)
        self._font_writer_24 = writer.Writer(self._oled, freesans24)
        self._font_writer_28 = writer.Writer(self._oled, freesans28)
        
    def show(self, chan_nr, curr, vol):
        self._oled.fill(0)
        for x,y,t in zip((0,48,48),(22,8,40),(self.__CHAN_NAMES[chan_nr],f"{curr:.3f}V",f"{vol:.3f}A")):
            self._font_writer_24.set_textpos(x, y)
            self._font_writer_24.printstring(t)
        self._oled.show()
        
    def show_dac(self, lsb, vol):
        self._oled.fill(0)
        for x,y,t in zip((0,0), (0,32), (f"{lsb:04} LSB", f"{vol:.3f} V")):
            self._font_writer_28.set_textpos(x, y)
            self._font_writer_28.printstring(t)
        self._oled.show()

    def show_adc_cnt(self, vals):
        self._oled.fill(0)
        for x,y,t in zip((0,65,65,0), (6,6,35,35), [f"{val:.3f}" for val in vals]):
            self._font_writer_24.set_textpos(x, y)
            self._font_writer_24.printstring(t)
        self._oled.show()
            
            
            
            