# import cv2
# import numpy as np
# import time
# from PIL import Image, ImageOps  # Install pillow instead of PIL
# import matplotlib.pyplot as plt
# import tflite_runtime.interpreter as tflite
import app
from time import sleep
def main():
    app.App()

if __name__ == "__main__":
    sleep(40)
    main()

# camera= cv2.VideoCapture("rtsp://admin:1EcO3974@192.168.1.5/Streaming/Channels/1")
# timeCheck = time.time()
# future = 3
# print('init')
# def get_frame():
#         if camera.isOpened():
#             ret, frame = camera.read()

#             if ret:
#                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#             else:
#                 return (ret, None)
#         else:
#             return None
# def predict(img):
#     cv2.imwrite(
#         "/home/pi/EcoBucket/test.jpg",
#         cv2.cvtColor(img, cv2.COLOR_BGR2RGB)[180:-50, 280:1000],
#     )
#     class_names = [
#         "0 cardboard",
#         "1 marker",
#         "2 paper",
#         "3 plastic_box",
#         "4 rubics",
#         "5 nothing",
#     ]
#     data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.uint8)
#     interpreter = tflite.Interpreter(model_path='ecobucket_model.tflite')
#     image = Image.open("/home/pi/EcoBucket/test.jpg").convert("RGB")
#     # resizing the image to be at least 224x224 and then cropping from the center
#     size = (224, 224)
#     image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
#     # turn the image into a numpy array
#     image_array = np.asarray(image)
#     data[0] = image_array
#     input_details = interpreter.get_input_details()
#     output_details = interpreter.get_output_details()
#     # Predicts the model
#     interpreter.allocate_tensors()
#     interpreter.set_tensor(input_details[0]['index'], data)
#     interpreter.invoke()
#     prediction = interpreter.get_tensor(output_details[0]['index'])[0]
#     print(prediction)
#     index = np.argmax(prediction)
#     class_name = class_names[index]
#     max_score=score=prediction[index]/255.0
#     return class_name, str(np.round(max_score * 100))[:-2] + "%"
# while True:
#     get_frame()
#     try:
#         if time.time() >= timeCheck:
#             ret,image = get_frame()
#             name, score = predict(image)
#             print("Class:", name[2:], end="")
#             print("Confidence Score:", score)
#             print("--------------------------------------")        
#             timeCheck = time.time()+future
#         else:
#             ret = cam.grab() 
        
#     except:
#         pass

# if camera.isOpened():
#     camera.release()
