import cv2
import os
import sys

__author__      = "Vanarp0915"

videoCaptureObject = cv2.VideoCapture(0)
image_path= "data"
next_path= sys.argv[1]
path=os.path.join(image_path, next_path)
os.mkdir(path)
count = int(sys.argv[2])
i,start=0,False
print(image_path)
start_point = (5,5)
end_point=(245,245)
while(True):
    ret,frame = videoCaptureObject.read()
    text = "Collecting image for {} :{}".format(next_path,i)
    cv2.putText(frame, text, (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.rectangle(frame, start_point, end_point, (255,255,0), 2)
    if start == True:
        if i == count:
            break
        else:
            cropped = frame[5:245, 5:245]
            save_path = os.path.join(path, '{}.jpg'.format(i+1))
            cv2.imwrite(save_path,cropped)
            print("its happening")
        i=i+1
    cv2.imshow("Collecting images", frame)
    k = cv2.waitKey(10)
    if k == ord('a'):
        start = True
    if k == ord('q'):
        break
videoCaptureObject.release()
cv2.destroyAllWindows()
