"""
# 实验程序
# 读取一个灰度图并显示出来
# 因为深度矩阵中的数值普遍大于255，所以只有0和255两种灰度值
# 后续需要改进
"""
import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()  # 选择需要读取的文件完整路径
dir_path = filedialog.askdirectory()   # 选择存放文件的文件夹路径

gray_img = np.loadtxt(file_path, delimiter=',', skiprows=0)    # 读取矩阵文件所包含的内容
print(gray_img.shape)

cv2.imshow('gray_img', gray_img)
cv2.waitKey()
cv2.destroyWindow()


