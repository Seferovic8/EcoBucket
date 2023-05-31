from PIL import Image, ImageOps  # Install pillow instead of PIL
import tflite_runtime.interpreter as tflite
import cv2
import numpy as np
class Model:
    def __init__(self):
        self.interpreter = tflite.Interpreter(model_path='/home/pi/EcoBucket/ecobucket_model.tflite')
        self.min_score=0.65
    def predict(self, img):
        cv2.imwrite(
            "/home/pi/EcoBucket/test.jpg",
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB)[200:-100, 280:1000],
        )
        class_names = [
            "cigaretes",
            "marker",
            "paper",
            "plastic_box",
            "rubics",
            "nothing",
        ]
        type_of_object = {
            "cigaretes":2,
            "marker":1,
            "paper":2,
            "plastic_box":1,
            "rubics":1,
            "nothing":0,
        }
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.uint8)
        image = Image.open("/home/pi/EcoBucket/test.jpg").convert("RGB")
        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        # turn the image into a numpy array
        image_array = np.asarray(image)
        data[0] = image_array
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()
        # Predicts the model
        self.interpreter.allocate_tensors()
        self.interpreter.set_tensor(input_details[0]['index'], data)
        self.interpreter.invoke()
        prediction = self.interpreter.get_tensor(output_details[0]['index'])[0]
        index = np.argmax(prediction)
        class_name = class_names[index]
        score=prediction[index]/255.0
        if(score>=self.min_score):
            return class_name, str(np.round(score * 100))[:-2] + "%",type_of_object[class_name]
        return class_name, str(np.round(score * 100))[:-2] + "%",0
