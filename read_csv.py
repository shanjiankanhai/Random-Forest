"""
# 打开csv文件，将csv文件中的矩阵读取出来
# 调用get_sample模块采集样本点，得到一个文件的样本点矩阵
"""

import tkinter as tk
from tkinter import filedialog
import numpy as np
from get_sample import get_patches
from get_sample_fix import get_patches_fix
from convert import convert_to_pixel

root = tk.Tk()
root.withdraw()


def read_file_from_directory(file_cal, file_pos, file_ang, file_depth, file_travel):
    """
    读取文件夹中的文件
    :param file_cal: cal文件路径
    :param file_pos: pos文件路径
    :param file_ang: ang文件路径
    :param file_depth: depth文件路径
    :param file_travel: 针对pos和ang文件，指循环的文件序号
    :return:
    """
    f_cal = open(file_cal, "rb")
    cal_9_1_d = np.loadtxt(f_cal, delimiter=',', skiprows=0)  # 得到9行1列
    f_cal.close()

    f_pos = open(file_pos, 'rb')
    position_3_n_d = np.loadtxt(f_pos, delimiter=',', skiprows=0)  # 得到3行N列的位置矩阵
    f_pos.close()

    f_ang = open(file_ang, 'rb')
    ang_3_n_d = np.loadtxt(f_ang, delimiter=',', skiprows=0)  # 得到3行N列的角度矩阵矩阵
    f_ang.close()

    f_depth = open(file_depth, 'rb')
    depth_matrix_d = np.loadtxt(f_depth, delimiter=',', skiprows=0)
    f_depth.close()

    position_3_1_d = position_3_n_d[:, file_travel]  # 矩阵切片,第0列所有行
    ang_3_1_d = ang_3_n_d[:, file_travel]

    # print('file_travel:', file_travel)

    # 因为默认是二维数组，所以此处对数组进行重构
    re_cal_d = cal_9_1_d.reshape(9, 1)
    re_position_d = position_3_1_d.reshape(3, 1)
    re_ang_d = ang_3_1_d.reshape(3, 1)

    c_1_d, c_2_d = convert_to_pixel(re_cal_d, re_position_d)
    # print('头部位置的像素坐标为：', c_1_d, c_2_d)

    # 得到取样的矩阵
    # 选择采样算法
    # sample_pitch_d = get_patches(c_1_d, c_2_d, depth_matrix_d, re_cal_d, re_position_d, re_ang_d)     # 国字脸采样算法
    sample_pitch_d = get_patches_fix(c_1_d, c_2_d, depth_matrix_d, re_cal_d, re_position_d, re_ang_d)   # 椭圆脸采样算法
    # sample_pitch_d = get_patches_fix(c_1_d, c_2_d, depth_matrix_d, re_cal_d, re_position_d, re_ang_d)  # 菱形脸采样算法

    # 返回一个文件采集的碎片
    return sample_pitch_d

