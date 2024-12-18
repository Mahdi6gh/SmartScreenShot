import cv2
import hand
from PIL import ImageGrab
Detecctor=hand.HandDetector()

def do():
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()
        frame=Detecctor.detect(frame)
        Listofln=Detecctor.positon(frame)
        cv2.imshow('Webcam', frame)
        key = cv2.waitKey(1)
        counter= []
        nokIndex=[8,12,16,20]
        if len(Listofln) > 0:
            for i in nokIndex:
                if Listofln[i][2]>Listofln[i-2][2]:
                    counter.append(1)
                else:counter.append(0)
        if counter == [0,1,1,1] or counter == [1,1,0,1] or counter == [1,1,1,1] or counter == [1,1,1,0]:
            print(counter)
            screenshot = ImageGrab.grab()

            # Save the screenshot to a file
            screenshot.save("screenshot.png")

            # Close the screenshot
            screenshot.close()
            continue
do()
