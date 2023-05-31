
import cv2

class Camera:

    def __init__(self):
        self.camera = cv2.VideoCapture("rtsp://admin:1EcO3974@192.168.1.5/Streaming/Channels/1")
        if not self.camera.isOpened():
            raise ValueError("Unable to open camera!")
        
        self.width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
    def grab(self):
        self.camera.grab()
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None