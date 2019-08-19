#coding=utf-8
# _*_ coding:utf-8 _*_
import numpy as np
import cv2

#读入图像
img=cv2.imread('3.jpg',0)

#显示图像
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#保存图像
# cv2.imwrite('test.png',img)