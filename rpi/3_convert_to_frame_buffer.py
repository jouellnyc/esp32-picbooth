#!/usr/bin/env python3
import sys
try:
    import PIL
except ModuleNotFoundError:
    print('Requires Pillow - python3 -m pip install --upgrade Pillow')
    sys.exit(1)
from PIL import Image
try:
    import numpy as np
except ModuleNotFoundError:
    print('Requires numpy - python3 -m pip install --upgrade numpy')
    sys.exit(1)
from numpy import asarray
import base64
import json
import argparse
"""
GurgleApps.com code to convert images to various formats to use in code for screens
"""
#print('Pillow Version:', PIL.__version__)

# image path to 2d array of 0 & 1s
def imageToArray(path,verbose,invert):
    image = Image.open(path)
    if verbose:
        print("Image format: ",image.format)
        print("Image size: ",image.size)
    gray = image.convert('L')
    bw = np.asarray(gray).copy()
    if invert:
        bw[bw < 128] = 1
        bw[bw >= 128] = 0
    else:
        bw[bw < 128] = 0    # Black
        bw[bw >= 128] = 1 # White
    return asarray(bw)

# 2d array of 0 & 1s turned into 2d array of bytes
def bytesFromBits(bitArray):
    dataBytes = []
    for line in bitArray:
        newLine = []
        for x in range(0, len(line), 8):
            byte = sum(2**(7-n) for n, bit in enumerate(line[x:x+8]) if bit == 1)
            newLine.append(byte)
        dataBytes.append(newLine)
    return dataBytes

# 2d array of bytes turned into our format a bytearray 1st 2 bytes width and height
def customImageFormat(byteArray):
    height = len(byteArray)
    width = len(byteArray[0]) * 8
    byteList = [width,height]
    for line in byteArray:
        byteList.extend(iter(line))
    return bytearray(byteList)


def doStuff(imagePath,verbose,invert):
    if verbose:
        print(f'Converting {imagePath}')
    data = imageToArray(imagePath,verbose,invert)
    np.set_printoptions(threshold=np.inf)
    dataBytes = bytesFromBits(data)
    bArray = customImageFormat(dataBytes)
    return base64.b64encode(bArray)

parser = argparse.ArgumentParser(description='Images to bits, bytes, code, and more ... ')
parser.add_argument("imagePath",help="path to the input image to convert")
parser.add_argument("-v",action="store_true",help="Verbose output")
parser.add_argument("-i",action="store_true",help="Invert")
args = parser.parse_args()

enc = doStuff(args.imagePath,args.v,args.i)
encoded_text  = enc.decode('UTF-8')                 

print(encoded_text)                                           
file='/root/picbooth/enc_text.txt'                           
with open(file,'w') as fh:                                 
    fh.write(encoded_text)
