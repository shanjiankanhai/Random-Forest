"""
# 图像滤波
"""
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

img_path = filedialog.askopenfilename()   # 获取图像的完整路径
save_dir = filedialog.askdirectory()   # 获取保存文件的文件夹路径

save_filename = save_dir + r'/output.png'    # 合成输出文件路径

img = cv2.imread(img_path)
r30 = cv2.blur(img, (30, 30))   # 滤波算法
cv2.imwrite(save_filename, r30)
