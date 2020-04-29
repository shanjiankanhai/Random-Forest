"""
# 决策树的测试程序，不用于整个程序中
"""


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor    # 导入随机森林分类器
from sklearn.datasets import load_wine, load_boston       # 导入红酒数据和波士顿房价
from sklearn.model_selection import train_test_split   # 分割训练集和测试集
from sklearn import tree
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
import numpy as np

boston = load_boston()     # 实例化波士顿房价数据
print(type(boston.data))
x_matrix = np.loadtxt(open("xtest.csv", "rb"), delimiter=",", skiprows=0)
y_matrix = np.loadtxt(open("ytest.csv", "rb"), delimiter=",", skiprows=0)

X_train, X_test, Y_train, Y_test = train_test_split(x_matrix, y_matrix, random_state=0, test_size=0.3)

regressor = tree.DecisionTreeRegressor(random_state=0)    # 建立回归树
clf = regressor.fit(X_train, Y_train)
score = regressor.score(X_test, Y_test)

rfc = RandomForestRegressor(random_state=0)
# clf = clf.fit(X_train, Y_train)
rfc = rfc.fit(X_train, Y_train)
score_c = clf.score(X_test, Y_test)
score_r = rfc.score(X_test, Y_test)

cv_scores = []		# 用来放每个模型的结果值
for n in range(1, 20):
    knn = tree.DecisionTreeRegressor(n)   # knn模型，这里一个超参数可以做预测，当多个超参数时需要使用另一种方法GridSearchCV
    scores = cross_val_score(knn, X_train, Y_train, cv=10, scoring='accuracy')  # cv：选择每次测试折数  accuracy：评价指标是准确度,可以省略使用默认值，具体使用参考下面。
    cv_scores.append(scores.mean())

print(score)

X02_test_data = [[6.32E-03,1.80E+01,2.31E+00,0.00E+00,5.38E-01,6.58E+00,6.52E+01,4.09E+00,1.00E+00,2.96E+02,1.53E+01,3.97E+02,2.40E+01
],[2.73E-02,0.00E+00,7.07E+00,0.00E+00,4.69E-01,6.42E+00,7.89E+01,4.97E+00,2.00E+00,2.42E+02,1.78E+01,3.97E+02,2.16E+01
]]
# cross_val_score(regressor, boston.data, boston.target, cv=10, scoring="neg_mean_squared_error")   # 交叉验证
X_test_data = [[2.73E-02,0.00E+00,7.07E+00,0.00E+00,4.69E-01,6.42E+00,7.89E+01,4.97, 2.00, 2.42E+02, 1.78E01, 3.97E02, 9.14],\
               [2.73E-02,0.00,7.07E+00,0.00E+00,4.69E-01,6.42E+00,7.89E+01,4.97E+00,2.00E+00,2.42E+02,1.78E+01,3.97E+02,9.14E+00],\
               [6.91E-02,0.00E+00,2.18E+00,0.00E+00,4.58E-01,7.15E+00,5.42E+01,6.06E+00,3.00E+00,2.22E+02,1.87E+01,3.97E+02,5.33E+00
]]
datasize = clf.predict(X02_test_data)
print(datasize)

# 用于把矩阵数据写入CSV文件
# np.savetxt('matrix.csv', boston.data, delimiter=',')
# np.savetxt('target.csv', boston.target, delimiter=',')

'''
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
# X_train, X_test, Y_train, Y_test = train_test_split(df[data.feature_names], df['target'], random_state=0)
X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, random_state=0)
print(type(data.data))
print(type(X_train))
clf = tree.DecisionTreeClassifier(criterion='entropy')
clfm = clf.fit(X_train,Y_train)
score = clf.score(X_test,Y_test)
print(score)
print(clf.feature_importances_)
'''
'''
wine = load_wine()    # 红酒数据实例化
print(type(wine.data))
print(type(wine.target))
# pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
Xtrain, Ytrain, Xtest, Ytest = train_test_split(df[wine.feature_names], df['target'], test_size=0.3)
print(type(Xtrain))
clf = tree.DecisionTreeClassifier(criterion='entropy')
clfme = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest,Ytest)
print(score)
# print(type(Xtrain))
# clf.fit(X_train, Y_train)
# score = clf.score(X_test, Y_tesin)
# score = clf.score(Xtest, Ytest)  # 返回预测的准确度
# print(score)
'''