#coding=utf-8

import numpy as np
import cv2

print u"原图"
img =cv2.imread('2.jpg',0)
cv2.imshow('test',img)

k=cv2.waitKey(0)
#wait for ESC key to exit
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):  #wait for 's' key to save and exit
    cv2.imwrite('save.png',img)
    cv2.destroyAllWindows()