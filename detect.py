import os
import cv2
import config
import time
import argparse
import numpy as np
import tensorflow as tf
from timeit import default_timer as timer
from yolo_predict import yolo_predictor
from PIL import Image, ImageFont, ImageDraw
from utils import letterbox_image, load_weights
# 指定使用GPU的Index
# os.environ["CUDA_VISIBLE_DEVICES"] = config.gpu_index

def detect(image, yolo_weights = config.yolo3_weights_path,image_size=(416,416)):
    """
    Introduction
    ------------
        加载模型，进行预测
    Parameters
    ----------
        model_path: 模型路径
        image_path: 图片路径
    """
    image = Image.open(image)
    if image_size != (None, None):

        assert image_size[0] % 32 == 0, 'Multiples of 32 required'
        assert image_size[1] % 32 == 0, 'Multiples of 32 required'
        resize_image = letterbox_image(image, tuple(reversed(image_size)))
    else:
        new_image_size = (image.width - (image.width % 32),
                          image.height - (image.height % 32))
        resize_image = letterbox_image(image, new_image_size)

    image_data = np.array(resize_image, dtype = 'float32')
    image_data /= 255.
    image_data = np.expand_dims(image_data, axis = 0)
    print(image_data.shape)
    input_image_shape = tf.placeholder(dtype = tf.int32, shape = (2,))
    input_image = tf.placeholder(shape = [None, 416, 416, 3], dtype = tf.float32)
    predictor = yolo_predictor(config.obj_threshold, config.nms_threshold, config.classes_path, config.anchors_path)
    boxes, scores, classes = predictor.predict(input_image, input_image_shape)
    with tf.Session() as sess:
            if yolo_weights is not None:
                print("yes")
                with tf.variable_scope('predict'):
                    boxes, scores, classes = predictor.predict(input_image, input_image_shape)
                load_op = load_weights(tf.global_variables(scope = 'predict'), weights_file = yolo_weights)
                sess.run(load_op)
            else:
                saver = tf.train.Saver()
                saver.restore(sess,  config.yolo3_weights_path)
            out_boxes, out_scores, out_classes = sess.run(
                [boxes, scores, classes],
                feed_dict={
                    input_image: image_data,
                    input_image_shape: [image.size[1], image.size[0]]
                })
            print('Found {} boxes for {}'.format(len(out_boxes), 'img'))
            font = ImageFont.truetype(font = 'font/FiraMono-Medium.otf', size = np.floor(3e-2 * image.size[1] + 0.5).astype('int32'))
            thickness = (image.size[0] + image.size[1]) // 300

            for i, c in reversed(list(enumerate(out_classes))):
                predicted_class = predictor.class_names[c]
                box = out_boxes[i]
                score = out_scores[i]

                label = '{} {:.2f}'.format(predicted_class, score)
                draw = ImageDraw.Draw(image)
                label_size = draw.textsize(label, font)

                top, left, bottom, right = box
                top = max(0, np.floor(top + 0.5).astype('int32'))
                left = max(0, np.floor(left + 0.5).astype('int32'))
                bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
                right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
                print(label, (left, top), (right, bottom))

                if top - label_size[1] >= 0:
                    text_origin = np.array([left, top - label_size[1]])
                else:
                    text_origin = np.array([left, top + 1])

                # My kingdom for a good redistributable image drawing library.
                for i in range(thickness):
                    draw.rectangle(
                        [left + i, top + i, right - i, bottom - i],
                        outline = predictor.colors[c])
                draw.rectangle(
                    [tuple(text_origin), tuple(text_origin + label_size)],
                    fill = predictor.colors[c])
                draw.text(text_origin, label, fill=(0, 0, 0), font=font)
                del draw
            result = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
            result = np.asarray(result)
            cv2.imwrite("./output.png", result)
# detect('./a.jpg')
image = detect(image='./a.jpg', yolo_weights = config.yolo3_weights_path,image_size=(416,416))
    # print(image)
    # if config.pre_train_yolo3 == True:
    #     print("s")

def detect_video( video_path='./videos.mp4', output_path=""):
    vid = cv2.VideoCapture(video_path)
    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    # video_FourCC = cv2.VideoWriter_fourcc(*"mp4v")
    # video_FourCC = int(vid.get(cv2.CAP_PROP_FOURCC))
    # video_fps = vid.get(cv2.CAP_PROP_FPS)
    # video_size = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
    #               int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # isOutput = True if output_path != "" else False
    # if isOutput:
    #     print("!!! TYPE:", type(output_path), type(video_FourCC), type(video_fps), type(video_size))
    #     out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)
    # accum_time = 0
    # curr_fps = 0
    fps = "FPS: ??"
    i=0
    # prev_time = timer()
    while True:

        return_value, frame = vid.read()
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # image=Image.fromarray(frame)

        image=detect(image)
        result = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
       #  result = np.asarray(result)


        cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)

        # cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        #
        # cv2.imshow("result", result)

        cv2.imwrite("./output/"+str(i)+".png",result)
        i+=1
        
        # if isOutput:
        #     out.write(result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
detect_video()



# else:

