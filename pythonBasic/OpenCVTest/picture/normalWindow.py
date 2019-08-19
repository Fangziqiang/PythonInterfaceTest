#coding=utf-8
# _*_ coding:utf-8 _*_
import numpy as np
import cv2

#读入图像
img=cv2.imread('2.jpg',0)

#显示图像
cv2.namedWindow('window',cv2.WINDOW_NORMAL)
cv2.imshow('window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()