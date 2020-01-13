import cv2
import os
#图片路径
im_dir = './output/'
#输出视频路径
video_dir = './videoss.avi'
#帧率
fps = 10
#图片数
num = 426
#图片尺寸
img_size = (1920,1080)
#fourcc = cv2.cv.CV_FOURCC('M','J','P','G')#opencv2.4
fourcc = cv2.VideoWriter_fourcc('M','J','P','G') #opencv3.0
videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
for i in range(0,97):
    im_name = os.path.join(im_dir, str(i)+'.png')
    print(im_name)
    frame = cv2.imread(im_name)
    videoWriter.write(frame)
videoWriter.release()
print ('finish')


