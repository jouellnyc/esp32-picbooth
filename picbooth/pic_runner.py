import urequests
import machine
import utime as  time
import framebuf
import base64
import math

from .oled_setup import oled as display

my_sleep=3

def custom_to_buff(data):
    width = data[0]
    height = data[1]
    fbuff = framebuf.FrameBuffer(data[2:],width,height, framebuf.MONO_HLSB)
    return fbuff
      
def show_image(image):
    display.blit(image, 0, 0)
    display.show()

while True:
    try:
        ziva = str(urequests.get('http://192.168.0.94:5000/picbooth/').text)
        print('Got it!')
    except:       
        ziva='gGD//////////////////4AA//////////////////+EAP//////////////////hgD//////////////////4YA//////////////////+GAP//////////////////DwD//////////////////x8A//////////////////8fAP//////////////////H4D//////////////////x+A//////////////////8fwP/////////////////+H8D//////////////////h/A//////////////////4/4P/////////////////+P+D//////////////////D/g//////////////////w/4P/////////////////8P/D//////////////////H/w//////////////////h/8P/////////////////wf/j/////////////////4H/4/////////////////8B/+P////////////////+Af/j/////////////////gD/8/////////////////4A//P/////////////////AP/7/////////////////wD/+////////////////v8A//v//////////////wAPAP/7//////////////gAAwD////////////////0AAEAf///////////////4AAAAH///////////////+AAAAB////////////////AAAAAf///////////////gAAAAH///////////////wAAAAA///////////////8AAAAAP//////////////+AOAAAD///////////////gf4AAA///////////////4D8AAAP//////////////+B/wAAD///////////////gf4AAA///////////////4H8AAAH//////////////+GjAAAB///////////////hgAAAAf//////////////8AAAAAH//////////////4AAAAAB//////////////+AAAAAAf////7QQAD/////wAAAAAH/4AAAAAAA/////8AAAAAA/+AAAAAAAP////+AAAAAAP/gAAAA////////gAAAAAD/wAAAAP///////4AAEAAA/+AAAAD////////CAAAAAP/gAAAA////////4AAAAAD/4AAAAf///////+AAAAAA/+AAAAH////////gAAAAAP/gAAAB////////8AAABAD/wAAAAf////////AAAAQAf8AAAAH////////4AAAIAH/AAAAB////////8AAACAB/wAAAAf////////AAABgAf8AAAAP////////wAAAYAH/AAAAD////////8AAAOAB/wAAAA////////+AAAHgAP8AAAAP///////xgAAD8MH/AAAAD///////hwAAB/CA/wAAAA///////AYAAAfwAf8AAAAP/////+AGAAAP8AH/AAAAD/////8AAAAAD/AB/wAAAA/////wAAAAAAfgAP8AAAAP////gAAAAAAB4AD/AAAAD////AAAAAAAAAAB/wAAAA////gAAAAAAAAAAP8AAAAP///wAAAAAAAAAAD/AAAAD///8AAAAAAAAAAA/wAAAA///+AAAAAAAAAAAPwAAAAP///AAAAAAAAAAADwAAAAD///wAAAAAAAAAABgAAAAB///4AAAAAAAAAAAAAAAAAP//+AAAAAAAAAAAAAAAAAAAAPAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
    finally:
        ziva_image = custom_to_buff(bytearray(base64.b64decode(ziva)))
        show_image(ziva_image)
        print(f"sleeping {my_sleep}")
        time.sleep(my_sleep)
    
    