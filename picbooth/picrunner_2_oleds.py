import urequests
import machine
import utime as  time
import framebuf
import base64
import math

from machine import Pin, SoftI2C

from .oled_setup_2_oleds import oled1, oled2

oled_width = 128
oled_height = 64

def custom_to_buff(data):
    width = data[0]
    height = data[1]
    fbuff = framebuf.FrameBuffer(data[2:],width,height, framebuf.MONO_HLSB)
    return fbuff
      
def show_image(image,display):
    display.blit(image, 0, 0)
    display.show()

my_sleep = 3

while True:
    try:
        pic = str(urequests.get('http://192.168.0.94:5000/picbooth/').text)
    except:       
        #Set a default pic if you like
        pic =''
    finally:
        ziva_image = custom_to_buff(bytearray(base64.b64decode(pic)))
        show_image(ziva_image, oled1)
        show_image(ziva_image, oled2)
        print(f"sleeping {my_sleep}")
        time.sleep(my_sleep)
    
