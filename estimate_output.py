"""
# 这个程序是用来评定预测结果和实际结果的差值（准确度）
# 程序被当作模块调用
# 作为模块调用时，需要被train_forest调用
"""


def estimate_outcome(x_predict, x_real, y_predict, y_real, z_predict, z_real):
    """
    参数都是numpy数组，所以可以使用numpy的一些方法属性
    :param x_predict: x预测矩阵数据
    :param x_real: x真实值矩阵数据
    :param y_predict；
    :param y_real
    :param z_predict
    :param z_real
    :return: 返回三个坐标系的准确率
    """
    # 读出每个矩阵行和列的数目
    # 其实只需要一行代码，读取一个矩阵的行和列即可，其他用作测试
    x_predict_row, x_predict_column = x_predict.shape
    x_real_row, x_real_column = x_real.shape
    y_predict_row, y_predict_column = y_predict.shape
    y_real_row, y_real_column = y_real.shape
    z_predict_row, z_predict_column = z_predict.shape
    z_real_row, z_real_column = z_real.shape

    x_accurate = calculate_proportion(x_predict, x_real)
    y_accurate = calculate_proportion(y_predict, y_real)
    z_accurate = calculate_proportion(z_predict, z_real)

    return x_accurate, y_accurate, z_accurate


def calculate_proportion(x_predict, x_real):
    """

    :param x_predict: 预测矩阵
    :param x_real: 真实数据矩阵
    :param
    :return: 预测数据的准确率
    """
    x_invalid, x_predict_column = x_predict.shape
    accurate_number = 0  # 设置准确数值
    inaccurate_number = 0

    # for循环，循环遍历矩阵的每一个数据
    for x_matrix in range(x_predict_column):
        x_data = x_predict[0, x_matrix]  # 预测矩阵的数据
        x_number = x_real[0, x_matrix]  # 实际矩阵的数据
        cut_number = x_number - x_data  # 实际值和预测值的差值

        if abs(x_number) <= 1:
            if abs(cut_number) < 1:
                accurate_number = accurate_number + 1
            else:
                inaccurate_number = inaccurate_number + 1

        elif ((x_number < -1) and (x_number >= -6)) or ((x_number > 1) and (x_number <= 6)):
            if abs(cut_number) < 2:
                accurate_number = accurate_number + 1
            else:
                inaccurate_number = inaccurate_number + 1

        elif ((x_number < -6) and (x_number >= -12)) or ((x_number > 6) and (x_number <= 12)):
            if abs(cut_number) < 3:
                accurate_number = accurate_number + 1
            else:
                inaccurate_number = inaccurate_number + 1

        elif ((x_number < -12) and (x_number >= -20)) or ((x_number > 12) and (x_number <= 20)):
            if abs(cut_number) < 4:
                accurate_number = accurate_number + 1
            else:
                inaccurate_number = inaccurate_number + 1

        else:
            if abs(cut_number) < 5:
                accurate_number = accurate_number + 1
            else:
                inaccurate_number = inaccurate_number + 1

    # 取得准确和不准确数据的量
    # 计算准确率
    x_accurate_proportion = accurate_number / x_predict_column
    return x_accurate_proportion


