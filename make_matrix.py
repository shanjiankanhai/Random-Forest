"""
# 独立运行的程序，用来制作训练数据集和测试数据集
# 测试数据集和训练数据集其实只有大小的区别
"""

import numpy as np
import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame

root = tk.Tk()
root.withdraw()

pitch_dir_path = filedialog.askdirectory()  # 获取存储样本的pitch文件夹路径
# test_path = filedialog.askopenfilename()    # 获取储存测试数据的otest文件路径
example_pitch = filedialog.askopenfilename()  # 获取储存example数据文件的路径
# print(example_pitch)

# 循环遍历pitch_01、02等文件，组成一个更大的训练矩阵
for i in range(15, 25):
    filename_pitch = 'pitch_{number:02d}.csv'.format(number=i)
    file_pitch_path = pitch_dir_path + r'/' + filename_pitch
    # print(file_pitch_path)

    f_pitch = open(file_pitch_path, 'rb')
    # 此处存疑loadtxt()函数的用法
    matrix_pitch = np.loadtxt(file_pitch_path, delimiter=',', skiprows=0, encoding='utf_8_sig')   # 读取csv文件中的矩阵

    x, y = matrix_pitch.shape  # 导出矩阵的行数和列数
    # matrix_re = np.zeros((x, y), dtype=float)
    # matrix_re[:, :] = matrix_pitch[:, :]

    f_pitch.close()
    
    dt = DataFrame(matrix_pitch)
    # print(type(matrix_pitch))
    dt.to_csv(example_pitch, mode='a', index=False, header=False, encoding='utf_8_sig')     # 把样本写入训练文件
    # dt.to_csv(test_path, mode='a', index=False, header=False)     # 把样本写入测试文件

    # print(matrix_pitch.shape)
    # print(type(matrix_pitch))
    # print(type(dt))

    print('第{number:02d}个文件写入完成'.format(number=i))


print('文件写入完成')
