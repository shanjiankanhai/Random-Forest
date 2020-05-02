"""
# 阈值处理
"""
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

png_path = filedialog.askopenfilename()
# save_path = filedialog.askdirectory()
save_path = r'D:\BaiduNetdiskDownload\RGB\threshold_06.png'

img = cv2.imread(png_path, 0)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 转换成灰度图
r, rst = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('save', rst)
cv2.imwrite(save_path, rst)
cv2.waitKey()
cv2.destroyWindow('save')
