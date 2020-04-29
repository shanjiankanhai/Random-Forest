"""
# 这个程序是用来训练决策树和随机森林
# 独立运行，没有函数调用关系
"""
import numpy as np
import tkinter as tk
from tkinter import filedialog
from sklearn.model_selection import train_test_split, cross_val_score   # 分割训练集和测试集
from sklearn import tree
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor    # 导入随机森林分类器

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
f_test = open(test_path, 'rb')
test_matrix = np.loadtxt(test_path, delimiter=',', skiprows=0, dtype=float, encoding='utf_8_sig')
f_test.close()

'''
# 控制矩阵的行数，已经失效
x, y = matrix.shape   # x是矩阵的行数
cut = int(input("输入要减去的数字："))
x_matrix = x-cut     # 控制矩阵的采集大小
'''

x_data = matrix[:, 0:789]        # 取出训练数据
x_predict = test_matrix[:, 0:789]    # 取出测试数据，不包括最后6列

y_target = matrix[:, 794:795]   # 最后一列作为target
y_predict = test_matrix[:, 794:795]  # 真实数据最后一列

x, y = test_matrix.shape  # x是矩阵的行数
print(x_predict.shape)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_target, random_state=0, test_size=0.2)

regressor = tree.DecisionTreeRegressor(random_state=0)    # 建立回归树
clf = regressor.fit(x_train, y_train)
score = regressor.score(x_test, y_test)
print('模型预测的准确度是：{}'.format(score))
data_predict = regressor.predict(x_predict)    # 得出预测数据的值

rft = RandomForestRegressor(random_state=0, n_estimators=25)
rft_f = rft.fit(x_train, y_train)
f_score = rft.score(x_test, y_test)
print('森林的准确度是：', f_score)
forest_predict = rft.predict(x_predict)
# 预测值写入文件
dt_csv = data_predict.reshape(1, x)   # 矩阵重构，把列矩阵变为行矩阵
dt = DataFrame(dt_csv)
dt.to_csv(outfile_path, mode='a', index=False, header=False)

# 真实值写入文件
yt_csv = y_predict.reshape(1, x)
yt = DataFrame(yt_csv)
yt.to_csv(outfile_path, mode='a', index=False, header=False)

#
forest_csv = forest_predict.reshape(1, x)
forest = DataFrame(forest_csv)
forest.to_csv(outfile_path, mode='a', index=False, header=False)

print('数值预测完成')