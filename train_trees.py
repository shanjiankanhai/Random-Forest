"""
# 这个程序是用来训练决策树的
# 独立运行，没有函数调用关系
"""
import numpy as np
import tkinter as tk
from tkinter import filedialog
from sklearn.model_selection import train_test_split, cross_val_score   # 分割训练集和测试集
from sklearn import tree
from pandas import DataFrame
from estimate_output import calculate_proportion

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()  # 获取训练数据example的路径
test_path = filedialog.askopenfilename()  # 获取输入的测试数据test路径
outfile_path = filedialog.askopenfilename()  # 获取输出文件outfile的路径

# 打开训练文件读取数据
f_pitch = open(file_path, 'rb')
matrix = np.loadtxt(file_path, delimiter=',', skiprows=0, dtype=float, encoding='utf_8_sig')
f_pitch.close()

# 打开测试文件读取数据
# 已经废掉了
f_test = open(test_path, 'rb')
test_matrix = np.loadtxt(test_path, delimiter=',', skiprows=0, dtype=float, encoding='utf_8_sig')
f_test.close()

x_row, y_column = matrix.shape
x_data = matrix[:, 0:y_column-6]        # 取出训练数据
x_predict = test_matrix[:, 0:y_column-6]    # 取出测试数据，不包括最后6列

x, y = test_matrix.shape  # x是矩阵的行数
y_target = matrix[:, y-1:y]   # 最后一列作为target
y_predict = test_matrix[:, y-1:y]  # 真实数据最后一列


print(x_predict.shape)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_target, random_state=0, test_size=0.2)
regressor = tree.DecisionTreeRegressor(random_state=0)    # 建立回归树
clf = regressor.fit(x_train, y_train)
score = regressor.score(x_test, y_test)
print('模型预测的准确度是：{}'.format(score))

data_predict = regressor.predict(x_predict)    # 得出预测数据的值

# 预测值写入文件
dt_csv = data_predict.reshape(1, x)   # 矩阵重构，把列矩阵变为行矩阵
dt = DataFrame(dt_csv)
dt.to_csv(outfile_path, mode='a', index=False, header=False)

# 真实值写入文件
yt_csv = y_predict.reshape(1, x)
yt = DataFrame(yt_csv)
yt.to_csv(outfile_path, mode='a', index=False, header=False)

x_accurate = calculate_proportion(dt_csv, yt_csv)
print('数据的准确度为:', x_accurate)
print('数值预测完成')

