"""
# 用于存储椭圆肤色模型
"""
import cv2
import math
import numpy as np
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandas import DataFrame
import time

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()   # 读取RGB空间的图像
# Cr_csv_path = filedialog.askopenfilename()
# Cb_csv_path = filedialog.askopenfilename()
# img_csv_path = filedialog.askopenfilename()
# face_out_path = filedialog.askopenfilename()
dir_path = filedialog.askdirectory()
oval_name = dir_path + r'/oval_03.png'

img_read = cv2.imread(file_path)   # 读取图像内容
img_YCrCb = cv2.cvtColor(img_read, cv2.COLOR_RGB2YCrCb)   # 转换色彩空间

# 构建椭圆肤色模型
oval_matrix = np.zeros((256, 256), dtype=np.uint8)   # 建立一个用于存储椭圆模型的矩阵
center = (round(113), round(152))
size = (25, 12)
angle = -20
color = 255
thickness = np.random.randint(1, 9)
img = cv2.ellipse(oval_matrix, center, size, angle, 0, 360, color, thickness=-1)  # 取得椭圆肤色模型
# img_csv = DataFrame(img)
# img_csv.to_csv(img_csv_path, index=False, header=False, mode='w', decimal=',')
# print(img)

x, y, d = img_read.shape
x_matrix = np.zeros((x, y), dtype='uint8')  # 建立一个匹配的二值矩阵图像
Y, Cr, Cb = cv2.split(img_YCrCb)   # 取得三种矩阵
# Cb_csv = DataFrame(Cb)
# Cb_csv.to_csv(Cb_csv_path, index=False, header=False, mode='w', decimal=',')
# 遍历图片的每一个像素点
for row in range(x):
    for col in range(y):
        Cr_v = Cr[row, col]
        Cb_v = Cb[row, col]
        x_matrix[row, col] = img[Cb_v, Cr_v]

# x_csv = DataFrame(x_matrix)
# x_csv.to_csv(face_out_path, index=False, header=False, decimal=',', mode='w')
# 将图片和矩阵进行与运算
and_matrix = np.zeros((x, y, 3), dtype='uint8')
and_matrix[:, :, 0] = x_matrix
and_matrix[:, :, 1] = x_matrix
and_matrix[:, :, 2] = x_matrix
img_and = cv2.bitwise_and(img_read, and_matrix)   # 得到去除干扰的完整脸部
print(img_and.shape)
img_gray = cv2.cvtColor(img_and, cv2.COLOR_BGR2GRAY)   # 脸部转换成灰度图
r, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)  # 脸部转换成二值图，准备进行腐蚀操作
img_read_gray = cv2.cvtColor(img_read,cv2.COLOR_BGR2GRAY)   # 完整图片转换
# 图像腐蚀操作
kernel = np.ones((2, 2), np.uint8)
erosion = cv2.erode(img_binary, kernel)
# print(Y, Cr, Cb)


'''
# 圆检测
circles = cv2.HoughCircles(img_read_gray, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=100, minRadius=10, maxRadius=200)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # 画圆
    cv2.circle(img_read, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 画圆心点
    cv2.circle(img_read, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imshow('detected circles', img_read)
# cv2.imshow('name', erosion)
# cv2.imwrite(oval_name, img_binary)
cv2.waitKey(0)
'''