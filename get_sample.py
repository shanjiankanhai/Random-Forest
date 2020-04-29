"""
# 国字脸采样算法
# 函数由read_csv文件调用
#
# 程序逻辑：
"""
import numpy as np
from convert import convert_to_cal
# mask = np.zeros((3, 187), dtype=float)      # 定义一个3行187列的矩阵，用于存放采样数据集
mask = np.zeros((1, 567), dtype=float)    # 定义一个1行567列的矩阵，用于存储转换完成的数据
mask_depth = np.zeros((1, 49), dtype=float)


def get_pi(c1, c2, depth):
    """
    :param c1: 像素坐标系X坐标
    :param c2: 像素坐标系Y坐标
    :param depth: 深度矩阵
    :return:
    """
    pass


def get_patches(c1, c2, depth, cal, ctr, ang):
    """
    :param c1: 像素坐标系X坐标
    :param c2: 像素坐标系Y坐标
    :param depth: 深度矩阵
    :param cal: 9行1列的转换矩阵
    :param ctr: 头部位置矩阵,3行1列，第三个为深度值
    :param ang: 头部的角度矩阵
    :return: mask 用于存放相机坐标系下矩阵数据
    """
    i = 0
    # for循环用于在一个文件中采样

    for x in range(-5, 6, 1):
        for y in range(-8, 9, 1):
            # 调用convert_to_cal函数把坐标进行转换,转换成相机坐标系坐标
            # 改动此处前需要先把最开始的np矩阵更改
            # mask[0, i], mask[1, i] = convert_to_cal(c1+x * 6, c2+y * 6, cal, ctr[2, 0])
            # mask[2, i] = depth[c2 + y * 6, c1 + x * 6]  # 此处y和x必须对掉，因为坐标系和矩阵的索引不一样
            # mask[0, i] = c1 + x * 6
            # mask[1, i] = c2 + y * 6

            # 定义X、Y、Z 与头部中心点相减之后的坐标数值
            # 改动此处前需要先改动最开始定义的np矩阵

            mask_x, mask_y = convert_to_cal(c1 + x * 6, c2 + y * 6, cal, ctr[2, 0])
            '''
            print('mask_x:', mask_x)
            print('mask_y:', mask_y)
            print('ctr00:', ctr[0, 0])
            print('ctr10:', ctr[1, 0])
            '''
            # 像素坐标系和矩阵坐标系有不同的地方
            mask_z = depth[c2 + y * 6, c1 + x * 6]

            mask[0, i * 3] = mask_x - ctr[0, 0]
            mask[0, i * 3 + 1] = mask_y - ctr[1, 0]
            mask[0, i * 3 + 2] = mask_z - ctr[2, 0]

            # 循环值
            i = i + 1

    # print('i的数值为：', i)

    mask[0, 561] = ctr[0, 0]
    mask[0, 562] = ctr[1, 0]
    mask[0, 563] = ctr[2, 0]

    mask[0, 564] = ang[0, 0]
    mask[0, 565] = ang[1, 0]
    mask[0, 566] = ang[2, 0]

    return mask
