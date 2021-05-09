import KeyBoard as kb
from MotorCode import Motor

import cv2
from time import sleep
import pandas as pd
import os
import datetime

motor = Motor(5, 6, 26, 23, 24, 25)
kb.display_initiate()
countFolder = 0
count = 0
imgList = []
steeringList = []
myDirectory = os.path.join(os.getcwd(), 'DataCollected')

while os.path.exists(os.path.join(myDirectory, f'IMG{str(countFolder)}')):
    countFolder += 1
newPath = myDirectory + "/IMG" + str(countFolder)
os.makedirs(newPath)

class dataCol():
    def __init__(self):
        pass

    def saveData(self, img, steering):
        global imgList, steeringList
        now = datetime.now()
        timestamp = str(datetime.timestamp(now)).replace('.', '')
        fileName = os.path.join(newPath, f'Image_{timestamp}.jpg')
        cv2.imwrite(fileName, img)
        imgList.append(fileName)
        steeringList.append(steering)

    def saveLog(self):
        global imgList, steeringList
        rawData = {'Image': imgList,
                   'Steering': steeringList}
        df = pd.DataFrame(rawData)
        df.to_csv(os.path.join(myDirectory, f'log_{str(countFolder)}.csv'), index=False, header=False)
        print('Log Saved')
        print('Total Images: ', len(imgList))


class Cam:
    def __init__(self):
        pass

    def getImg(self, display=False, size=[480, 240]):
        _, img = cap.read()
        img = cv2.resize(img, (size[0], size[1]))
        if display:
            cv2.imshow('IMG', img)
        return img


def main():
    if kb.getKey('UP'):
        motor.move(0.6, 0, 0.1)
        img = Cam.getImg(True, size=[240, 120])
        print(img)
        dataCol.saveData(img, "UP")
    elif kb.getKey('DOWN'):
        motor.move(-0.6, 0, 0.1)
        img = Cam.getImg(True, size=[240, 120])
        dataCol.saveData(img, "DOWN")
    if kb.getKey('LEFT'):
        motor.move(0.5, 0.3, 0.1)
        img = Cam.getImg(True, size=[240, 120])
        dataCol.saveData(img, "LEFT")
    elif kb.getKey('RIGHT'):
        motor.move(0.5, -0.3, 0.1)
        img = Cam.getImg(True, size=[240, 120])
        dataCol.saveData(img, "RIGHT")
    else:
        motor.stop(0.1)
        dataCol.saveLog()


if __name__ == '__main__':
    while True:
        main()
