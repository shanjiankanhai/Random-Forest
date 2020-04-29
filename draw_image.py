"""
# 画图，用来展示数据和结果
"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# 椭圆脸严格模式下的数据 100棵树
value_x = [40.3, 41.66, 40.49, 45.57, 43.42, 41.18]
value_y = [40.9, 66.6, 73, 71, 66.8, 75.07]
value_z = [35.12, 43.94, 42, 39.57, 38.71, 42.56]

# 椭圆脸严格数据，第二部分
value_strict_x = [57.01, 59.22, 60.52, 60.15, 58.12, 57.01]
value_strict_y = [23.8, 23.24, 24.35, 27.31, 28.41, 29.15]
value_strict_z = [31.55, 40.59, 40.77, 39.67, 43.36, 43.73]


# 椭圆脸普通模式下的数据 5，10，15，20，25，30，35棵树
value_relax_x = [93.35, 95.3, 90, 95.5, 95.5, 95.66, 92.2]
value_relax_y = [85.14, 87.8, 81.7, 88.91, 90.32, 89.85, 83.4]
value_relax_z = [71.79, 77.4, 64.2, 80.59, 80.32, 80.69, 65.7]

# 国字脸普通模式下的数据
guo_x = [95.08, 95.08, 95.13, 95.49, 95.6, 95.6]
guo_y = [85.98, 85.98, 87.96, 89.22, 89.17, 90.27]
guo_z = [77.34, 77.34, 79.54, 80.37, 80.79, 81.27]
# 国字形脸严格模式下的数据
voal_x = [47.52, 45.59, 44.9, 43.66, 42.56, 42.01]
voal_y = [30.99, 33.33, 30.85, 29.61, 29.3, 30.3]
voal_z = [23.27, 32.23, 37.05, 37.47, 37.19, 36.91]


range_for = [5, 10, 15, 20, 25, 30]
range_for_extend = [5, 10, 15, 20, 25, 30, 35]

# 椭圆脸严格模式下第二部分数据
plt.scatter(range_for, value_strict_x, marker='x', label='x')
plt.scatter(range_for, value_strict_y, marker='o', label='y')
plt.scatter(range_for, value_strict_z, marker='o', label='z')
plt.legend()
plt.show()

am1 = plt.subplot(1, 2, 1)
plt.scatter(range_for, guo_x, c='r', marker='x', label="value_x")
plt.scatter(range_for, guo_y, c='b', marker="o", label="value_y")
plt.scatter(range_for, guo_z, c='y', marker="x", label="value_z")
am1.set_title('relax_guozilian')
plt.legend()

am2 = plt.subplot(1, 2, 2)
plt.scatter(range_for, voal_x, c='r', marker='x', label="value_x")
plt.scatter(range_for, voal_y, c='b', marker="o", label="value_y")
plt.scatter(range_for, voal_z, c='y', marker="x", label="value_z")
am2.set_title('strict_guozilian')
plt.legend()
plt.show()

ax1 = plt.subplot(1, 2, 2)
plt.scatter(range_for, value_x, c='r', marker='x', label="value_x")
plt.scatter(range_for, value_y, c='b', marker="o", label="value_y")
plt.scatter(range_for, value_z, c='y', marker="x", label="value_z")
ax1.set_title('strict_voal')
plt.legend()

ax2 = plt.subplot(1, 2, 1)
plt.scatter(range_for_extend, value_relax_x, c='r', marker='x', label='value_relax_x')
plt.scatter(range_for_extend, value_relax_y, c='b', marker='o', label='value_relax_y')
plt.scatter(range_for_extend, value_relax_z, c='y', marker='x', label='value_relax_z')
ax2.set_title('relax_oval')
plt.legend()

plt.show()
