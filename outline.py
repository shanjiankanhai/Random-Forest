"""
# 绘制图像轮廓
"""
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
png_path = filedialog.askopenfilename()
face_path = filedialog.askopenfilename()
dir_path = filedialog.askdirectory()
save_path = dir_path + r'/outline_01.png'

img = cv2.imread(png_path)
img_face = cv2.imread(face_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 获取轮廓最大值的索引
area = []
for i in range(len(contours)):
    area.append(cv2.contourArea(contours[i]))
max_idx = np.argmax(area)   # 获得最大值索引

M = cv2.moments(contours[max_idx])
if M['m00'] !=0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
else:
    cX, cY = 0, 0

'''
# 画出图形的中心点
for c in contours:
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
'''

# cnt_centroid = cv2.centroid()
print(max_idx)

mask = np.zeros(img.shape, np.uint8)    # 做一个纯黑的画布
mask = cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)   # 画出轮廓线
cv2.fillConvexPoly(mask, contours[max_idx], 255)   # 填充区域
x, y, w, h = cv2.boundingRect(contours[max_idx])   # 得到最大连通区域的矩形框坐标
br = np.array([[[x, y]], [[x+w, y]], [[x+w, y+h]], [[x, y+h]]])
cv2.drawContours(mask, [br], -1, (255, 255, 255), 2)   # 画出矩形框框住人脸
cv2.circle(mask, (cX, cY), 5, (0, 0, 255), -1)   # 画出中心点所在位置
cv2.imshow('mask', mask)

loc = cv2.bitwise_and(img, mask)
cv2.imshow('loc', loc)

face_cut = img_face[y:y+h, x:x+w]
cv2.imwrite(save_path, face_cut)
while True:
    c = cv2.waitKey(25)
    if c == 27:
        break
cv2.destroyAllWindows()
