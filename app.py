import cv2
import numpy as np
import time
import camera
import model
import serial
class App:
    def __init__(self):
        self.model = model.Model()
        self.camera = camera.Camera()
        self.serial = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

        self.timeCheck = time.time()
        self.future = 3
        self.do()
    def do(self):
        while True:
            self.camera.get_frame()
            try:
                if time.time() >= self.timeCheck:
                    ret,image = self.camera.get_frame()
                    name, score,type_of_object = self.model.predict(image)
                    print(f"Class: {name}")
                    print("Confidence Score:", score)
                    print("type_of_object:", type_of_object)
                    self.send_serial(type_of_object)
                    print("--------------------------------------")        
                    self.timeCheck = time.time()+self.future
                else:
                    self.camera.grab() 
                
            except:
                pass
    def send_serial(self,type_of_object):
        if type_of_object == 1:
            self.serial.write(b"1")
        elif type_of_object == 2:
            self.serial.write(b"2")