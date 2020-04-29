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
save_path = r'D:\BaiduNetdiskDownload\RGB\threshold_03.png'

img = cv2.imread(png_path, 0)
r, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('save', rst)
cv2.imwrite(save_path, rst)
cv2.waitKey()
cv2.destroyWindow('save')
