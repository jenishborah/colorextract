import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import cv2
from skimage.color import rgb2lab, deltaE_cie76
from collections import Counter
import os
from colorthief import ColorThief

img = cv2.imread('color.png')
cv2.imshow("Original_Image", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
red = img.copy()
red[ : , : , 0] = 0
red[ : , : , 1] = 0
cv2.imshow("Red_Color", red)
green = img.copy()
green[ : , : , 0] = 0
green[ : , : , 2] = 0
cv2.imshow("Green_Color", green)
blue = img.copy()
blue[ : , : , 1] = 0
blue[ : , : , 2] = 0
cv2.imshow("Blue_Color", blue)

#brown
light_brown = np.array([10,120,20])
dark_brown = np.array([20,255,200])
x=cv2.inRange(img,light_brown,dark_brown)
z=cv2.bitwise_and(img,img,mask=x)
cv2.imshow("Brown_Color", z)

#Yellow
light_yellow = np.array([20,100,100])
dark_yellow = np.array([30,255,255])
a=cv2.inRange(img,light_yellow, dark_yellow)
b=cv2.bitwise_and(img,img,mask=a)
cv2.imshow("Yellow_Color", b)

#Pink
light_pink = np.array([125,100,30])
dark_pink = np.array([255,255,255])
j=cv2.inRange(img,light_pink, dark_pink)
k=cv2.bitwise_and(img,img,mask=j)
cv2.imshow("Pink_Color", k)

#White
white1 = np.array([0,0,168])
white2 = np.array([172,111,255])
w=cv2.inRange(img,white1, white2)
y=cv2.bitwise_and(img,img,mask=w)
cv2.imshow("White_Color", y)

#black
black1 = np.array([180,255,30])
black2 = np.array([0,0,0])
m=cv2.inRange(img,black1, black2)
n=cv2.bitwise_and(img,img,mask=m)
cv2.imshow("Black_Color", n)

#blue
blue1 = np.array([110,100,100])
blue2 = np.array([130,255,255])
e=cv2.inRange(img,blue1, blue2)
f=cv2.bitwise_and(img,img,mask=e)
cv2.imshow("Blue_Color", f)

#red
red1 = np.array([160,50,50])
red2 = np.array([180,255,255])
r=cv2.inRange(img,red1, red2)
s=cv2.bitwise_and(img,img,mask=r)
cv2.imshow("Red_Color", s)


#bar
ct = ColorThief("color.png")
palette = ct.get_palette(color_count=7)
plt.imshow([[palette[i] for i in range(7)]])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()