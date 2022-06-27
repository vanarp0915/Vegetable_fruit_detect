from keras.models import load_model
import cv2
import numpy as np
import sys



REV_CLASS_MAP = {    0:"Apple",
    1:"Banana",
    2:"colgate",
    3:"fanta",
    4:"Onion",
    5:"Orange",
    6:"sprite",
    7:"surf",
    8:"Tomato",
    9:"Watermelon"}



model = load_model("fandV.h5")

class prediction_class:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.iden = None
    def mapper(self,val):
        return REV_CLASS_MAP[val]
    
    def callback(self):
        return self.iden

    def prediction(self):
        cnt=0   
        while True:
            ret, frame = self.cap.read()
            cv2.putText(frame, "Frame", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            cv2.rectangle(frame, (5,5), (245,245), (255,255,0), 2)
            img = frame[5:245, 5:245]
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (227, 227))

            pred = model.predict(np.array([img]))

            move_code = np.argmax(pred[0])
            move_name = self.mapper(move_code)
            print (move_name)
            self.callback()
            cnt=cnt+1
            cv2.imshow('Output', img)

            c = cv2.waitKey(1)
            if c == 27 or cnt>2000:
                break

        self.cap.release()
        cv2.destroyAllWindows()
        print("got it")


detect = prediction_class()
detect.prediction()
