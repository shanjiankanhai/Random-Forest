"""
# 从HSV图像中提取出肤色模型
"""
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

face_path = filedialog.askopenfilename()
dir_path = filedialog.askdirectory()

output_file = dir_path + r'/out_face.png'

img =cv2.imread(face_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
minHue = 5
maxHue = 170
hueMask = cv2.inRange(h, minHue, maxHue)
minSat = 25
maxSat = 166
satMask = cv2.inRange(s, minSat, maxSat)
mask = hueMask & satMask
roi = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite(output_file, roi)
