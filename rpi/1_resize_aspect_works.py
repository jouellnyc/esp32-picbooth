#!/usr/bin/env python3

import sys

from PIL import Image

basewidth = 128
img = Image.open(sys.argv[1])
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
img.save('128.' + sys.argv[1])
