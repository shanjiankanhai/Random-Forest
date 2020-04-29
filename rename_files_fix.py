"""
# 作为重命名文件的补充程序，处理文件名不规范的文件和断层的文件
# 单独运行，没有函数调用关系
"""
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

dir_path = filedialog.askdirectory()  # 获得要更改的文件夹目录
for i in range(1, 25):
    # y_file_name = 'frame_00{file_number_depth:03d}_depth_mask.csv'.format(file_number_depth=i)   # 原来的文件名
    # y_file_name = 'depth_f_{file_number:03d}.csv'.format(file_number=i)
    y_file_name = '{number:02d}ang.csv'.format(number=i)

    y_file_path = dir_path + r'/' + y_file_name     # 源文件文件完整路径

    # g_file_path = dir_path + r'/' + 'depth_{number:03d}.csv'.format(number=i-130)
    g_file_path = dir_path + r'/' + 'ang_{number:02d}.csv'.format(number=i)
    os.rename(y_file_path, g_file_path)
