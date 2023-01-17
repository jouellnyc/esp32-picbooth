# ESP32-picbooth

## What is this?
Take a selfie on your mobile phone and upload it to your esp32 OLED screen.

Or maybe your sleeping cat?

<img src="images/cat.jpg"  width="200"/>



## What is this (II)?
It is also possible to run https://guvcview.sourceforge.net/ on a Raspberry Pi / Eee Pc like a real "Picture Booth" and have that image show on the esp32's OLED.
That was the orignal intent. 

## Why?
This can be a fun ice-breaker at a holiday get together / party  like Thanksgiving or wherever humans gather.

## Requirements
- esp32
- Raspberry Pi or equivalent like EEE PC running linux
- An OLED - this works great - https://www.amazon.com/gp/product/B08KY21SR2/  - 0.96" OLED Display 128x64 Pixel SSD1306 I2C

## Setup
- In order to set this up you'll first install your esp32 on your wireless network and connect an OLED screen.
For fun, in this project I have 2 OLED screens connected to the esp32 using the ssd1306 driver as well as the sh1106  driver. 

- If you want a 'real' photo at a decent size, this project also supports the - 320x240 SPI Serial ILI9341 - https://www.amazon.com/dp/B09XHJ9KRX - (set displayt in  pic_runner.py)

- Since the esp32 is not powerful enough to process images and does not have the pillow package you'll need another computer like a Raspberry Pi to process the images. This machine will be running Flask/Flask Reuploaded and will accept the uploaded images, process them and make available (run pic_booth.sh to move them in the background). A text string is what the esp32 will consume to be able to  display the image on its OLED.

I would recommend reviewing the Brilliant Walk Through for more in depth technichal details as they have already done the work.

- Configs / Libraries shared in https://github.com/jouellnyc/mcconfigs

## Mobile Screen Shot

<img src="images/mobile.jpg"  width="200"/>

## Hints
- Lighting is EVERYTHING!
- modify your DNS to point to something like 'upload' to find the upload server easily.

## References
- sh1106 driver

https://github.com/robert-hh/SH1106/blob/master/sh1106.py

- Gurgle Apps (base64 and ssd1306 driver)

https://github.com/gurgleapps/image-to-code

https://gurgleapps.com/tools/image-to-code

- Brilliant Walk Through

https://www.youtube.com/watch?v=MOI9qBAAClo&t=728s

- Flask Reuploaded

https://pypi.org/project/Flask-Reuploaded/

- ESP32 PINOUTS / HW

https://docs.micropython.org/en/latest/esp32/quickref.html#hardware-i2c-bus

https://lastminuteengineers.com/esp32-pinout-reference/

https://docs.micropython.org/en/latest/esp32/quickref.html

https://microcontrollerslab.com/esp32-pinout-use-gpio-pins/

https://electronics.stackexchange.com/questions/583433/is-it-possible-to-use-two-i2c-interfaces-with-the-esp32-using-micropython

