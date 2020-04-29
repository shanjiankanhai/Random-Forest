"""
两个转换函数，函数1负责把相机坐标转换成像素坐标系，函数2负责把相机坐标系转换成像素坐标
"""


def convert_to_pixel(array_cal, array_pos):
    """
    将相机坐标转换成像素坐标,像素坐标必须是整数
    :param array_cal: 9行1列的转换矩阵
    :param array_pos: 3行列的头部位置矩阵
    :returns c1: 像素坐标系的X坐标
    :returns c2: 像素坐标系的Y坐标
    """
    c1_1 = (array_pos[0] * array_cal[0, 0]) / array_pos[2] + array_cal[2, 0]
    c2_2 = (array_pos[1] * array_cal[4, 0]) / array_pos[2] + array_cal[5, 0]

    c1 = int(c1_1)
    c2 = int(c2_2)

    return c1, c2


def convert_to_cal(c1, c2, cal, ctr2):
    """
    把像素坐标转换成相机坐标
    :param c1: 像素坐标系的x坐标
    :param c2:  像素坐标系的y坐标
    :param cal: 9行1列的相机转换矩阵
    :param ctr2: 采样像素点处的深度数值
    :return: ctr0和ctr1是相机坐标
    """
    ctr0 = ((c1 - cal[2, 0])/cal[0, 0]) * ctr2
    ctr1 = ((c2 - cal[5, 0])/cal[4, 0]) * ctr2

    return ctr0, ctr1

