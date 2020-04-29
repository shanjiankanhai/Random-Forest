"""
# 色彩空间转换模块
"""
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

png_path = filedialog.askopenfilename()  # 获取需要打开的文件路径
dir_path = filedialog.askdirectory()

img = cv2.imread(png_path)
rst = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
rst2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

process_name = dir_path+r'/hsv_01.png'
process_name_y = dir_path+r'/YCrCb.png'
cv2.imwrite(process_name, rst)
cv2.imwrite(process_name_y, rst2)
