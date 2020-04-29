# coding:utf-8
import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
# 调用电脑的摄像头
cv2.namedWindow("Face Detection System")
cap = cv2.VideoCapture(0)
# 读取每帧图片和是否读取成功的success
success, frame = cap.read()
# 获取opencv的分类器——人眼识别和人脸识别
face_Cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
[x, y, w, h] = [0, 0, 0, 0]
while success:
    success, frame = cap.read()
    # 将每帧图片灰度化
    size = frame.shape[:2]
    image = np.zeros(size, dtype=np.float16)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 直方图均衡
    image = cv2.equalizeHist(image)
    im_h, im_w = size
    minSize_1 = (im_w//10, im_h//10)
    faceRects = face_Cascade.detectMultiScale(image, 1.05, 2, cv2.CASCADE_SCALE_IMAGE, minSize_1)
    if len(faceRects) > 0:
        for faceRect in faceRects:
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x, y), (x+w, y+h), [255, 255, 0], 2)
                cv2.rectangle(frame,(int(x+0.25*w),int(y-0.4*h)),(int(x+0.75*w),y),[0,255,0],thickness=-1)
                cv2.putText(frame,'hat', (int(x+0.45*w),int(y-0.2*h)),font,0.6,(255,0,0), 1)
                face_im = np.zeros([w,h],dtype=np.float16)
                temp_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                face_im = temp_image[y:y+h,x:x+w]
                eyeRects = eye_cascade.detectMultiScale(face_im,1.05,2,cv2.CASCADE_SCALE_IMAGE,(w//10,h//10))
                if(len(eyeRects)==2):
                    x1,y1,w1,h1 = eyeRects[0]
                    x2,y2,w2,h2 = eyeRects[1]
                    point_1 = [(2*(x+x1)+w1)//2,(2*(y+y1)+h1)//2]
                    point_2 = [(2*(x+x2)+w2)//2,(2*(y+y2)+h2)//2]
                    r1 = w1//2
                    r2 = w2//2
                    cv2.circle(frame,(point_1[0],point_1[1]),r1,(255,0,255),2)
                    cv2.circle(frame,(point_2[0],point_2[1]),r2,(255,0,255),2)
                    if(x2>x1):
                        cv2.line(frame,(point_1[0]+r1,point_1[1]),(point_2[0]-r2,point_2[1]),(255,0,255),2)
                    else:
                        cv2.line(frame,(point_2[0]+r2,point_2[1]),(point_1[0]-r1,point_1[1]),(255,0,255),2)
    cv2.rectangle(frame,(x, y),(x+w,y+h),[255,255,0],2)
    cv2.imshow("Face Detection System", frame)
    key=cv2.waitKey(5)
    if key==32:
        break
cv2.destroyWindow("Face Detection System")
