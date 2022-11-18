from machine import Pin, SoftI2C
from . import ssd1306
from time import sleep

oled_width = 128
oled_height = 64

#ssd1306
i2c = SoftI2C(scl=Pin(13), sda=Pin(15))
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#sh1106
##i2c = SoftI2C(scl=Pin(13), sda=Pin(15), freq=400000)
##oled = sh1106.SH1106_I2C(oled_width, oled_height, i2c, None, 0x3c,  rotate=180)
