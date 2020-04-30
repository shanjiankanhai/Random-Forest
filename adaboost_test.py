"""
# 用于实验adaboost算法
# 包含图像切片保存
"""
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# face_path = filedialog.askopenfilename()  # 选择face_cascade文件
# eye_path = filedialog.askopenfilename()   # 选择eye_cascade文件
face_png = filedialog.askopenfilename()   # 选择要识别的文件
# dir_path = filedialog.askdirectory()

# 手动设置路径
face_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_frontalface_alt.xml'
eye_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_eye.xml'
file_name = r'D:\BaiduNetdiskDownload\RGB\saves_15.png'

# 导入分类器
# face_cascade = cv2.CascadeClassifier(r'D:\opencv\sources\data\haarcascades/haarcascade_frontalface_alt.xml')
# eye_cascade = cv2.CascadeClassifier(r'D:\opencv\sources\data\haarcascades/haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)

img1 = cv2.imread(face_png)
# img = cv2.resize(img1, (240, 320), interpolation=cv2.INTER_LINEAR)
img2 = cv2.resize(img1, dsize=(1280, 960), fx=2, fy=2)
# img2_name = dir_path + r'/test06_2.png'
# cv2.imwrite(img2_name, img2)

img = img1

faces = face_cascade.detectMultiScale(img, 1.2, 2)
# face_cut = img[faces[0][0]: faces[0][0]+faces[0][2], faces[0][1]:faces[0][1]+faces[0][3]]   # 剪出面部所在区域

print('faces:', faces)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # 用颜色为BGR（255,0,0）粗度为2的线条在img画出识别出的矩型
    face_re = img[y:y+h, x:x+w]  # 抽取出框出的脸部部分，注意顺序y在前
    cv2.imwrite(file_name, face_re)   # 把剪出的面部区域存储
    eyes = eye_cascade.detectMultiScale(face_re)  # 在框出的脸部部分识别眼睛
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_re, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
cv2.imshow('img', img)
# cv2.imwrite(file_name, face_cut)
key = cv2.waitKey(0)
if key == 27:
    cv2.destoryWindow('img')
