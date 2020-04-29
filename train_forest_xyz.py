"""
# 这个程序是用来训练决策树和随机森林
# 训练XYZ三个坐标，分开训练
# 只需要读取两个文件的数据，不再需要测试集文件
# 测试集和训练集直接使用函数分配，无需手动分配
# 独立运行，没有函数调用关系
"""
import numpy as np
import tkinter as tk
from tkinter import filedialog
from sklearn.model_selection import train_test_split, cross_val_score   # 分割训练集和测试集
from sklearn import tree
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor    # 导入随机森林分类器
from estimate_output import estimate_outcome

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()  # 获取训练数据example的路径

# outfile_path = filedialog.askopenfilename()  # 获取输出文件outfile的路径

# 打开训练文件读取数据
matrix = np.loadtxt(file_path, delimiter=',', skiprows=0, dtype=float, encoding='utf_8_sig')

x_row, y_column = matrix.shape              # 读取矩阵的行数和列数
train_data = matrix[:, 0:y_column-6]        # 取出训练数据
x_target = matrix[:, y_column-3:y_column-2]
y_target = matrix[:, y_column-2:y_column-1]
z_target = matrix[:, y_column-1:y_column]   # 最后一列作为target_z

print('训练数据读取完成')

# 将XYZ三个测试数据分为训练集和测试集
x_data_train, x_data_test, x_target_train, x_target_test = train_test_split(train_data, x_target, random_state=0, test_size=0.3)
y_data_train, y_data_test, y_target_train, y_target_test = train_test_split(train_data, y_target, random_state=0, test_size=0.3)
z_data_train, z_data_test, z_target_train, z_target_test = train_test_split(train_data, z_target, random_state=0, test_size=0.3)
print('训练数据分类完成')


# 建立随机森林
rtf_x = RandomForestRegressor(random_state=0, n_estimators=10)
rtf_x_f = rtf_x.fit(x_data_train, x_target_train)
x_predict = rtf_x.predict(x_data_test)       # 得到x的预测数据
(xm_x,) = x_predict.shape                   # 矩阵重构
x_predict_re = x_predict.reshape(1, xm_x)
x_target_test_re = x_target_test.reshape(1, xm_x)
print('x_depth', rtf_x.max_depth)
print('随机森林x训练完成')


rtf_y = RandomForestRegressor(random_state=0, n_estimators=10)
rtf_y_f = rtf_y.fit(y_data_train, y_target_train)
y_predict = rtf_y.predict(y_data_test)       # 得到y的预测数据
(y_x,) = y_predict.shape
y_predict_re = y_predict.reshape(1, y_x)
y_target_test_re = y_target_test.reshape(1, y_x)
print('随机森林y训练完成')

rtf_z = RandomForestRegressor(random_state=0, n_estimators=10)
rtf_z_f = rtf_z.fit(z_data_train, z_target_train)
z_predict = rtf_z.predict(z_data_test)       # 得到预测数据
(zm_x,) = z_predict.shape
z_predict_re = z_predict.reshape(1, zm_x)
z_target_test_re = z_target_test.reshape(1, zm_x)
print('随机森林z训练完成')

x_accurate, y_accurate, z_accurate = \
    estimate_outcome(x_predict_re, x_target_test_re, y_predict_re, y_target_test_re, z_predict_re, z_target_test_re)
print(x_accurate, y_accurate, z_accurate)
print('数值预测完成')
