"""
# 用于对斜着的脸进行眼睛定位
"""
import cv2
import numpy as np

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

face_png = filedialog.askopenfilename()   # 选择要识别的文件
eye_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_eye.xml'

eye_cascade = cv2.CascadeClassifier(eye_path)
img1 = cv2.imread(face_png)

eyes = eye_cascade.detectMultiScale(img1)  # 在框出的脸部部分识别眼睛
print(eyes)
for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img1, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
cv2.imshow('name', img1)

while True:
    c = cv2.waitKey(25)
    if c == 27:
        break
cv2.destroyAllWindows()