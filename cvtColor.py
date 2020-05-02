"""
# 色彩空间转换模块
"""
import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

root = tk.Tk()
root.withdraw()

png_path = filedialog.askopenfilename()  # 获取需要打开的文件路径
dir_path = filedialog.askdirectory()
eye_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_path)

img = cv2.imread(png_path)
rst = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# rst2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

process_name = dir_path+r'/hsv_01.png'
# process_name_y = dir_path+r'/YCrCb.png'
cv2.imwrite(process_name, rst)
# cv2.imwrite(process_name_y, rst2)
H, S, V = cv2.split(rst)
img_binary = cv2.threshold(V, 127, 255, cv2.THRESH_BINARY )

eyes = eye_cascade.detectMultiScale(img)  # 在框出的脸部部分识别眼睛
for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)


'''
circles = cv2.HoughCircles(V, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=10, maxRadius=30)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(V,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(V,(i[0],i[1]),2,(0,0,255),3)
'''
cv2.imshow('name', img)

while True:
    c = cv2.waitKey(25)
    if c == 27:
       break
cv2.destroyAllWindows()
