#!/usr/bin/env python3

import sys
from PIL import Image

img = Image.open(sys.argv[1])
img.convert("1")
img.save(f'bw.{sys.argv[1]}')

