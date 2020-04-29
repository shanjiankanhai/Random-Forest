"""
# 图像光照补偿
# 读取图像的R、G、B三通道数据
"""
import cv2
import tkinter as tk
from tkinter import filedialog
import time
import numpy as np
from pandas import DataFrame

root = tk.Tk()
root.withdraw()

img_path = filedialog.askopenfilename()     # 得到测试图片的路径
# matrix_path = filedialog.askopenfilename()  # 获取要写入矩阵的文件路径
img_write = filedialog.askdirectory()       # 获得需要写入的文件夹路径

img = cv2.imread(img_path)      # 读取图像数据
row, col, height = img.shape    # 读取图片的矩阵状态，包括行数，列数
b, g, r = cv2.split(img)        # 取得r、g、b三色矩阵分别存放
dst = np.zeros((row, col, 3), dtype=int)   # 用来存放图像矩阵数据
print(row, col, height)

b_matrix = np.array(b)
b_average = np.mean(b_matrix)   # 求矩阵的平均值

g_matrix = np.array(g)
g_average = np.mean(g_matrix)

r_matrix = np.array(r)
r_average = np.mean(r_matrix)

gray_average = (b_average + g_average + r_average)/3     # 平均灰度值
print(b_average, g_average, r_average)

# 循环写入矩阵，验证程序的可行性
for i in range(row):
    for m in range(col):
        R_rgb = r[i, m]
        G_rgb = g[i, m]
        B_rgb = b[i, m]
        kr = 0 if R_rgb == 0 else (gray_average/r_average)    # 求取每个点的增益系数，需要去除像素点值为0的情况
        kg = 0 if G_rgb == 0 else (gray_average/g_average)
        kb = 0 if B_rgb == 0 else (gray_average/b_average)
        R1 = int(min(R_rgb * kr, 255))     # 比255大的数值设置为255
        # print(R_rgb, R1)
        # time.sleep(0.01)
        G1 = int(min(G_rgb * kg, 255))
        B1 = int(min(B_rgb * kb, 255))
        dst[i, m] = np.uint8((B1, G1, R1))


print('平均灰度值', gray_average)
# 将处理好的图片保存
img_write_path = img_write + r'/' + 'test_02.jpg'
cv2.imwrite(img_write_path, dst)

# dt.to_csv(matrix_path, index=False, mode='a', header=False, encoding='utf-8')
# cv2.imwrite("./new_img.jpg", img)
# cv2.imshow("Blue 1", b)
# time.sleep(10)
# cv2.imshow("Green 1", g)
# time.sleep(10)
# cv2.imshow("Red 1", r)
#
# print(b, g, r)
