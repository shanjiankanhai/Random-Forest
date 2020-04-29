"""
# 读取文件最基础的程序
# 文件调用顺序是
# read_dir_from_dir文件
# read_directory文件  ——  read_directory_files函数
# read_csv文件  ——  read_file_from_directory函数
# convert文件 ——  convert_to_pixel函数
# get_sample文件 —— get_patches函数

"""

import tkinter as tk
from tkinter import filedialog
import os
from read_directory import read_directory_files

root = tk.Tk()
root.withdraw()

cal_dir_path = filedialog.askdirectory()  # 选择cal文件夹
pos_dir_path = filedialog.askdirectory()  # 选择position文件夹
depth_dir_path = filedialog.askdirectory()  # 选择要遍历的mx大文件夹
pitch_dir_path = filedialog.askdirectory()  # 选择存放样本的pitch文件夹


# for i in range(1, 4):
for i in range(1, 25):
    """
    # 循环遍历mx文件夹下的01、02文件夹，合成01、02等文件夹的路径，为读取文件做准备
    # 这个循环是最基础的循环
    """
    # 得到一个cal和一个position文件的完整路径
    filename_cal = cal_dir_path + r'/' + 'rgb_cal_{cal_number:02d}.csv'.format(cal_number=i)
    filename_pos = pos_dir_path + r'/' + 'loc_{pos_number:02d}.csv'.format(pos_number=i)
    filename_ang = pos_dir_path + r'/' + 'ang_{ang_number:02d}.csv'.format(ang_number=i)  # 获得头部角度文件完整路径

    print(filename_cal, filename_pos, filename_ang)

    # 合成存放样本的文件路径
    filename_pitch = pitch_dir_path + r'/' + 'pitch_{pitch_number:02d}.csv'.format(pitch_number=i)

    # 合成01、02文件夹完整路径
    depth_dir_path_dir = depth_dir_path + r'/{number:02d}'.format(number=i)   # 合成文件夹01的路径
    length_of_file = len(os.listdir(depth_dir_path_dir))  # 获取01、02等文件夹下文件的数量

    print(filename_pitch, depth_dir_path_dir)

    # 循环遍历的文件数，针对pos和ang文件
    # file_travel = i-1

    # 读取01、02等文件夹下的文件信息，不是直接读取文件内容
    read_directory_files(depth_dir_path_dir, length_of_file, filename_cal, filename_pos, filename_ang, filename_pitch)
    # print(length_of_file)





