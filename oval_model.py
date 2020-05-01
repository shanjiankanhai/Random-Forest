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

file_path = filedialog.askopenfilename()
img_read = cv2.imread(file_path)

'''
d = 400
img = np.ones((d, d, 3), dtype='uint8')*255
center = (round(d/2), round(d/2))
size = (100, 200)
for i in range(0, 10):
    angle = np.random.randint(0, 361)
    color = np.random.randint(0, high=256, size=(3, )).tolist()
    thickness = np.random.randint(1, 9)
    cv2.ellipse(img_read, center, size, angle, 0, 360, color, thickness)
cv2.imshow('demo', img_read)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

oval_matrix = np.zeros((256, 256), dtype=np.uint8)   # 建立一个用于存储椭圆模型的矩阵

center = (round(113), round(155.6))
size = (25, 12)
angle = 43
# color = np.random.randint(0, high=256, size=(3, )).tolist()
color = 255
thickness = np.random.randint(1, 9)
img = cv2.ellipse(oval_matrix, center, size, angle, 0, 360, color, thickness=-1)
cv2.imshow('name', oval_matrix)
cv2.waitKey(0)

'''
def make_oval(cb, cv):
    """
    :param cb: 色彩空间Cb
    :param cv:

    :return:
    """
    cx = 109.38
    cy = 152.02
    angle = 2.53
    ecx = 1.6
    ecy = 2.41
    a = 25.39
    b = 14.03
    x = math.cos(angle) * (cb - cx) + math.sin(angle) * (cv - cy)
    y = -math.sin(angle) * (cb - cx) + math.cos(angle) * (cv - cy)
    output = ((x - ecx)**2)/(a**2) + ((y - ecy)**2)/(b**2)
    print(output)
    if (output <= 1) and (output >= 0):
        oval_matrix[cb, cv] = 1
    else:
        oval_matrix[cb, cv] = 0
    # print(oval_matrix[cb, cv])
    # time.sleep(0.01)


# 循环建立椭圆肤色模型
for row in range(5):
    for col in range(5):
        make_oval(row, col)

oval_csv = DataFrame(oval_matrix)
oval_csv.to_csv(file_path, index=False, header=False, mode='w')
'''

