"""
# 独立运行的程序，用来制作大矩阵
# 作为make_matrix文件的补充模块，使用另一种方法制作训练集和测试集合
# 按规律分出测试集合和训练集，已作废
"""

import numpy as np
import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame

root = tk.Tk()
root.withdraw()

pitch_dir_path = filedialog.askdirectory()  # 获取存储样本的pitch文件夹路径
example_pitch = filedialog.askopenfilename()  # 获取储存example数据文件的路径
test_path = filedialog.askopenfilename()    # 获取储存测试数据的otest文件路径
# print(example_pitch)

# 循环遍历pitch_01、02等文件，组成一个更大的训练矩阵
for i in range(3, 12):
    filename_pitch = 'pitch_{number:02d}.csv'.format(number=i)
    file_pitch_path = pitch_dir_path + r'/' + filename_pitch
    # print(file_pitch_path)

    f_pitch = open(file_pitch_path, 'rb')
    # 此处存疑loadtxt()函数的用法
    matrix_pitch = np.loadtxt(file_pitch_path, delimiter=',', skiprows=0, encoding='utf_8_sig')  # 读取csv文件中的矩阵

    # 每个文件中取出60行作为测试数据
    x, y = matrix_pitch.shape  # 导出矩阵的行数和列数
    matrix_re = np.zeros((x - 60, y), dtype=float)
    test_re = np.zeros((60, y), dtype=float)

    matrix_re[0:90, :] = matrix_pitch[0:90, :]
    test_re[0:20, :] = matrix_pitch[90:110, :]
    matrix_re[90:180, :] = matrix_pitch[110:200, :]
    test_re[20:40, :] = matrix_pitch[200:220, :]
    matrix_re[180:270, :] = matrix_pitch[220:310, :]
    test_re[40:60, :] = matrix_pitch[310:330, :]

    matrix_re[270:x-60, :] = matrix_pitch[330:x, :]   # 把剩余数据写入

    f_pitch.close()

    dt = DataFrame(matrix_re)
    dt.to_csv(example_pitch, mode='a', index=False, header=False, encoding='utf_8_sig')  # 把样本写入训练文件

    dt_test = DataFrame(test_re)
    dt_test.to_csv(test_path, mode='a', index=False, header=False, encoding='utf_8_sig')     # 把测试数据写入测试文件

    # print(matrix_pitch.shape)
    # print(type(matrix_pitch))
    # print(type(dt))

    print('第{number:02d}个文件写入完成'.format(number=i))

print('文件写入完成')
