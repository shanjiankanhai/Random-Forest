# coding:utf-8
"""
# 视频图像识别的主函数
# 读取摄像头实时数据
# 识别并画出人脸所在的区域
# 计算头部的姿态
"""
import cv2
import numpy as np
import time

# 调用摄像头，读取视频数据
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# capture = cv2.VideoCapture('视频文件完整路径')

# 训练完成的算法
face_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_frontalface_alt.xml'
# face_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_frontalface_alt_tree.xml'
face_cascade = cv2.CascadeClassifier(face_path)
# eye_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_eye.xml'
eye_path = r'D:\BaiduNetdiskDownload\RGB\haarcascade_eye_tree_eyeglasses.xml'
eye_cascade = cv2.CascadeClassifier(eye_path)

'''
while capture.isOpened():
    ret, frame = capture.read()    # 抽取视频帧为图片
    faces = face_cascade.detectMultiScale(frame, 1.2, 2)   # 检测人脸所在的位置
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 用颜色为BGR（255,0,0）粗度为2的线条在img画出识别出的矩型
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'lennon', (x+20, y-5), font, 0.75, (0, 255, 0))

        face_re = frame[y:y + h, x:x + w]  # 抽取出框出的脸部部分，注意顺序y在前
        # cv2.imwrite(file_name, face_re)  # 把剪出的面部区域存储
        eyes = eye_cascade.detectMultiScale(face_re)  # 在框出的脸部部分识别眼睛
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_re, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    c = cv2.waitKey(25)    # 按ESC结束
    if c == 27:
        break
'''
'''
while capture.isOpened():
    ret, frame = capture.read()    # 抽取视频帧为图片
    
    # 第一种算法，检测人脸的位置并框出来
    faces = face_cascade.detectMultiScale(frame, 1.2, 2)   # 检测人脸所在的位置
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 用颜色为BGR（255,0,0）粗度为2的线条在img画出识别出的矩型
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'lennon', (x+20, y-5), font, 0.75, (0, 255, 0))

        face_re = frame[y:y + h, x:x + w]  # 抽取出框出的脸部部分，注意顺序y在前
        # cv2.imwrite(file_name, face_re)  # 把剪出的面部区域存储
        
        eyes = eye_cascade.detectMultiScale(face_re)  # 在框出的脸部部分识别眼睛
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_re, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    c = cv2.waitKey(25)    # 按ESC结束
    if c == 27:
        break
'''
# 新加的功能，显示脸部的截取图片
while capture.isOpened():
    ret, frame = capture.read()    # 抽取视频帧为图片
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return_number, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros(frame.shape, np.uint8)  # 做一个纯黑的画布
    mask = cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)
    cv2.imshow('mask', mask)

    '''
    # 图片镜像，
    # 镜像过后会有明显卡顿，不建议镜像，或者采用其他方法进行镜像
    rows, cols = frame.shape[:2]
    mapx = np.zeros(frame.shape[:2], np.float32)
    mapy = np.zeros(frame.shape[:2], np.float32)
    for i in range(rows):
        for j in range(cols):
            mapx.itemset((i, j), cols-1-j)
            mapy.itemset((i, j), i)
    rst_mask = cv2.remap(mask, mapx, mapy, cv2.INTER_LINEAR)
    cv2.imshow('mask', rst_mask)
    '''

    loc = cv2.bitwise_and(frame, mask)
    # rst_loc = cv2.remap(loc, mapx, mapy, cv2.INTER_LINEAR)  # 图片镜像
    # cv2.imshow('loc', rst_loc)
    cv2.imshow('loc', loc)
    c = cv2.waitKey(25)  # 按ESC结束
    if c == 27:
        break
# return_number, img = capture.read()   # 捕获帧
# cv2.imshow('name', img)
# time.sleep(10)
# cv2.waitKey(0)
capture.release()   # 释放摄像头
cv2.destroyAllWindows()
