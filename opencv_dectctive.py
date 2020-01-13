
from imageai.Detection import ObjectDetection
import os

execution_path=os.getcwd()
detector=ObjectDetection()

detector.setModelTypeAsRetinaNet()
detector.setModelPath("./opencv_yolo10/yolo.h5")
detector.loadModel()
detections=detector.detectObjectsFromImage(input_image=os.path.join(execution_path,"./a.jpg"),output_image_path=os.path.join(execution_path,"imagenew.jpg"))
for eachObject in detections:
    print(eachObject["name"]+" : "+eachObject["percentage_probability"])