"""
# 循环读取文件夹中的文件
# 读取的数据以矩阵的形式存放
# 函数由read_dir_from_dir模块调用
"""
import os
import tkinter as tk
from tkinter import filedialog
from read_csv import read_file_from_directory
import pandas as pd
from pandas import DataFrame

root = tk.Tk()
root.withdraw()

# 选择需要读取的文件夹路径
# 此处注释掉是为了方便调试，改动对程序无影响
# 分别是cal相机校正矩阵文件、position头部位置文件、depth深度矩阵文件
# Folder_path_cal = filedialog.askdirectory()
# Folder_path_position = filedialog.askdirectory()
# Folder_path_depth = filedialog.askdirectory()

# 路径截取
# (file_full_path, filename) = os.path.split(Folder_path_cal)
# print(file_full_path)
# (filename,extension) = os.path.splitext(tempfilename)

# read_file_from_directory(filename_cal, filename_position, filename_depth)
# for循环结束

# print(filename_position)
# print(filename_depth)


def read_directory_files(dir_path, sum_number, cal_path, pos_path, ang_path,  file_pitch):
    """
    此函数是用来合成csv文件的路径，用于read_csv模块读取csv文件
    :param dir_path: 01、02等文件夹路径
    :param sum_number: 文件夹下文件的数量
    :param cal_path: cal文件完整路径
    :param pos_path: pos文件的完整路径
    :param ang_path: ang文件的完整路径
    :param file_pitch: 存放样本的文件
    :return:
    """
    # 此处循环用来控制mx文件夹的01、02文件夹下文件的读取数量
    # for i in range(1, 50):
    for i in range(1, sum_number+1):

        """
        循环得到01、02文件夹下所有文件路径
        """

        filename_depth = 'depth_{file_number_depth:03d}.csv'.format(file_number_depth=i)

        # 用于控制pos和ang的循环
        file_travel = i-1

        # 合成文件路径
        # 合成一个路径就要读取一个文件
        file_path_depth = dir_path + r'/' + filename_depth

        # 调用函数读取单个csv文件，返回1行N列的采样数据
        pitch = read_file_from_directory(cal_path, pos_path, ang_path, file_path_depth, file_travel)

        # 写入到CSV文件中，每行写一次，每个文件夹一个csv文件
        # f_pitch = open(file_pitch, 'a+')
        dt = DataFrame(pitch)
        # dt.to_csv()
        dt.to_csv(file_pitch, mode='a', index=False, header=False)

        print('第{number:03d}个文件写入完成'.format(number=i))



