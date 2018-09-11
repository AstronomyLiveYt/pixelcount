import os
import sys
import numpy as np
import cv2
import collections

if len(sys.argv) != 3:
    print('Proper usage: python pixelcount.py image1.xxx image2.xxx')
    exit()
image1 = cv2.imread(sys.argv[1])
image1gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
height1, width1 = image1gray.shape
image2 = cv2.imread(sys.argv[2])
image2gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
height2, width2 = image2gray.shape
image1sum = 0
for h in range(0, height1):
    for w in range(0, width1):
        if image1gray[h,w] > 0:
            image1sum = image1sum + 1
print(image1sum)
image2sum = 0
for h in range(0, height2):
    for w in range(0, width2):
        if image2gray[h,w] > 0:
            image2sum = image2sum + 1
print(image2sum)
