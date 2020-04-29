"""
# 用于重命名mx文件夹下的文件，方便后面的读取操作
# 单独运行，没有函数调用关系
"""
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

dir_path = filedialog.askdirectory()  # 获得要更改的文件夹目录
# file_path = filedialog.askdirectory()
# file_name_path = filedialog.askopenfilename()
length_files = len(os.listdir(dir_path))   # 获取文件夹下文件的数量
print(length_files)
# file_name = file_path + r'/' + '01.csv'
# os.rename(file_name_path, file_name)

'''
for m in range(1, 3):
    dir_in_path = dir_path + r'/' + '{number:02d}'.format(number=m)  # 合成文件夹01、02等的路径
    # print(dir_in_path)
    # 循环遍历每个文件夹，为每个文件夹下的问价更名
    # 这个函数暂时不能实现，因为每个文件夹下的文件名命名规则不一样
    for i in range(1, length_files + 1):
        y_file_name = 'frame_00{file_number_depth:03d}_depth_mask.csv'.format(file_number_depth=i + 3)  # 原来的文件名
        y_file_path = dir_path + r'/' + y_file_name  # 源文件文件完整路径
        g_file_path = dir_path + r'/' + 'depth_{number:02d}.csv'.format(number=i)
        os.rename(y_file_path, g_file_path)

'''
for i in range(1, length_files+1):
    # y_file_name = 'frame_00{file_number_depth:03d}_depth_mask.csv'.format(file_number_depth=i)   # 原来的文件名
    y_file_name = 'depth_{number:02d}.csv'.format(number=i)
    y_file_path = dir_path + r'/' + y_file_name     # 源文件文件完整路径
    g_file_path = dir_path + r'/' + 'depth_{number:03d}.csv'.format(number=i)
    os.rename(y_file_path, g_file_path)
