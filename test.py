# import cv2
# import os
# #要提取视频的文件名，隐藏后缀
# sourceFileName='videos'
# #在这里把后缀接上
# video_path = os.path.join("", "", sourceFileName+'.mp4')
# times=0
# #提取视频的频率，每25帧提取一个
# frameFrequency=25
# #输出图片到当前目录vedio文件夹下
# outPutDirName='vedio/'+sourceFileName+'/'
# if not os.path.exists(outPutDirName):
#     #如果文件目录不存在则创建目录
#     os.makedirs(outPutDirName)
# camera = cv2.VideoCapture(video_path)
# while True:
#     times+=1
#     res, image = camera.read()
#     if not res:
#         print('not res , not image')
#         break
#     # if times%frameFrequency==0:
#     cv2.imwrite(outPutDirName + str(times)+'.jpg', image)
#     print(outPutDirName + str(times)+'.jpg')
# print('图片提取结束')

import cv2
import numpy as np
url = "rtsp://admin:Hist1207@192.168.58.19//Streaming/Channels/1"
cap = cv2.VideoCapture(url)
i = 0
while True:
    (ret, frame) = cap.read()
    cv2.imwrite('./data/' + str(i).zfill(6) + '.jpg' , frame)
    i += 1
    cv2.imshow("Video", frame)
    cv2.waitKey(1)
