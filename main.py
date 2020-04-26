## IMPORTS
import cv2
import numpy as np

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)


## READ THE IMAGE
imgpath = ''
img = cv2.imread(imgpath)

## DETECT THE EDGES
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_inv = 255 - gray
img_blur = cv2.GaussianBlur(gray_inv, ksize=(21, 21),sigmaX=0, sigmaY=0)
img_blend = dodgeV2(gray, img_blur)
img_blend *= 12

## SAVE THE IMAGE
outpath = ''
cv2.imwrite(outpath,img_blend)