"""
# 菱形脸模型采样算法
# 函数由read_csv文件调用
# get_patches这个函数用来从深度矩阵中取出特征点的三个坐标，并把像素坐标系转换成相机坐标系
# 暂时没做完
"""
import numpy as np
from convert import convert_to_cal
# mask = np.zeros((3, 187), dtype=float)      # 定义一个3行187列的矩阵，用于存放采样数据集
mask_depth = np.zeros((1, 795), dtype=float)
mask_diamond = np.zeros((), dtype=float)     # 定义一个矩阵，用来存储采集的书籍


def get_patches_diamond(c1, c2, depth, cal, ctr, ang):
    """
    像素坐标系和矩阵坐标系的XY轴正好相反
    :param c1: 像素坐标系X坐标
    :param c2: 像素坐标系Y坐标
    :param depth: 深度矩阵
    :param cal: 9行1列的转换矩阵
    :param ctr: 头部位置矩阵,3行1列，第三个为深度值
    :param ang: 头部的角度矩阵
    :return: mask 用于存放相机坐标系下矩阵数据
    """
    i = 0

    # 设置采样的间隔/步长
    space_sample = 5

    # 设置用于采集40
    for para_40 in [- 8 * space_sample, - 9 * space_sample, - 10 * space_sample]:    # 像素坐标系的Y坐标，矩阵的X坐标
        for para_4 in range(-4, 5, 1):  # 像素坐标系下的X坐标
            mask_x, mask_y = convert_to_cal(c1 + para_4 * space_sample, c2 + para_40, cal, ctr[2, 0])
            # 像素坐标系和矩阵坐标系有不同的地方
            # 从深度矩阵中取出深度值，坐标采用矩阵坐标系
            mask_z = depth[c2 + para_40, c1 + para_4 * space_sample]

            mask_depth[0, i * 3] = mask_x - ctr[0, 0]
            mask_depth[0, i * 3 + 1] = mask_y - ctr[1, 0]
            mask_depth[0, i * 3 + 2] = mask_z - ctr[2, 0]
            # print('循环40中i的数值为：', i)

            i = i+1

    # 设置用于采集50
    for para_50 in [- 5 * space_sample, -6 * space_sample, - 7 * space_sample, 9 * space_sample, 10 * space_sample]:
        for para_5 in range(-5, 6, 1):
            mask_x, mask_y = convert_to_cal(c1 + para_5 * space_sample, c2 + para_50, cal, ctr[2, 0])
            # 像素坐标系和矩阵坐标系有不同的地方
            # 从深度矩阵中取出深度值，坐标采用矩阵坐标系
            mask_z = depth[c2 + para_50, c1 + para_5 * space_sample]

            mask_depth[0, i * 3] = mask_x - ctr[0, 0]
            mask_depth[0, i * 3 + 1] = mask_y - ctr[1, 0]
            mask_depth[0, i * 3 + 2] = mask_z - ctr[2, 0]
            # print('循环50中i的数值为：', i)

            i = i + 1

    # 设置用于采集60
    for para_60 in [-1 * space_sample, -2 * space_sample, -3 * space_sample, -4 * space_sample, 6 * space_sample, 7 * space_sample, 8 *space_sample]:
        for para_6 in range(-6, 7, 1):
            mask_x, mask_y = convert_to_cal(c1 + para_6 * space_sample, c2 + para_60, cal, ctr[2, 0])
            # 像素坐标系和矩阵坐标系有不同的地方
            # 从深度矩阵中取出深度值，坐标采用矩阵坐标系
            mask_z = depth[c2 + para_60, c1 + para_6 * space_sample]

            mask_depth[0, i * 3] = mask_x - ctr[0, 0]
            mask_depth[0, i * 3 + 1] = mask_y - ctr[1, 0]
            mask_depth[0, i * 3 + 2] = mask_z - ctr[2, 0]
            # print('循环60中i的数值为：', i)

            i = i + 1

    # 设置用于采集70
    for para_70 in [0, space_sample, 2 * space_sample, 3 * space_sample, 4 * space_sample, 5 * space_sample]:
        for para_7 in range(-7, 8, 1):
            mask_x, mask_y = convert_to_cal(c1 + para_7 * space_sample, c2 + para_70, cal, ctr[2, 0])
            # 像素坐标系和矩阵坐标系有不同的地方
            # 从深度矩阵中取出深度值，坐标采用矩阵坐标系
            mask_z = depth[c2 + para_70, c1 + para_7 * space_sample]

            mask_depth[0, i * 3] = mask_x - ctr[0, 0]
            mask_depth[0, i * 3 + 1] = mask_y - ctr[1, 0]
            mask_depth[0, i * 3 + 2] = mask_z - ctr[2, 0]
            # print('循环70中i的数值为：', i)

            i = i + 1
    # print('i的值是：', i)

    mask_depth[0, 789] = ctr[0, 0]
    mask_depth[0, 790] = ctr[1, 0]
    mask_depth[0, 791] = ctr[2, 0]

    mask_depth[0, 792] = ang[0, 0]
    mask_depth[0, 793] = ang[1, 0]
    mask_depth[0, 794] = ang[2, 0]

    return mask_depth