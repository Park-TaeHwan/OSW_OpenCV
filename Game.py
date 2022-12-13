import random
import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone
import time

# Read Web cammera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand Detector function
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Variables array of find the Function
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2) 

# Game local Variables
number = 1
cx, cy = 250, 250
color = (255, 0, 255)
counter = 0
score = 0
timeStart = time.time()
totalTime = 30

# Loop to camera
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Check by time
    if time.time()-timeStart < totalTime:

        hands = detector.findHands(img, draw=False)

        # Read hands and find distance
        if hands:
            lmList = hands[0]['lmList']
            x, y, w, h = hands[0]['bbox']
            x1, y1 = lmList[5][:2]
            x2, y2 = lmList[17][:2]

            distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
            A, B, C = coff
            distanceCM = A * distance ** 2 + B * distance + C

            if distanceCM < 40:
                if x < cx < x + w and y < cy < y + h:
                    counter = 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
            cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10), colorR=(0, 255, 0))

        # If hand meets image of file with planet.
        if counter:
            counter += 1
            color = (0, 255, 0)
            if counter == 3:
                cx = random.randint(100, 1100)
                cy = random.randint(100, 600)
                number = random.randint(1,7)
                color = (255, 0, 255)
                score +=1
                counter = 0

        # Initial draw image about counter with hand
        img1 = cv2.imread('./image/1.jpg')
        dst = cv2.resize(img1, dsize=(100, 100), interpolation=cv2.INTER_AREA)
        img_cut = cv2.rectangle(dst, (0,0), (100, 100), color, thickness=3)
        img[cy-50:cy+50, cx-50:cx+50] = img_cut
        cvzone.putTextRect(img, f'Earth', (cx-40, cy-60), scale=2,colorR=(0, 255, 0))

        # Draw image about counter with hand, check the random number.
        if number == 1:
            img1 = cv2.imread('./image/1.jpg')
            dst = cv2.resize(img1, dsize=(100, 100), interpolation=cv2.INTER_AREA)
            img_cut = cv2.rectangle(dst, (0,0), (100, 100), color, thickness=3)
            img[cy-50:cy+50, cx-50:cx+50] = img_cut
            cvzone.putTextRect(img, f'Earth', (cx-40, cy-60), scale=2,colorR=(0, 255, 0))
        elif number == 2:
            img1 = cv2.imread('./image/2.jpg')
            dst = cv2.resize(img1, dsize=(100, 100), interpolation=cv2.INTER_AREA)
            img_cut = cv2.rectangle(dst, (0,0), (100, 100), color, thickness=3)
            img[cy-50:cy+50, cx-50:cx+50] = img_cut
            cvzone.putTextRect(img, f'Moon', (cx-40, cy-60), scale=2,colorR=(0, 255, 0))
        elif number == 3:
            img1 = cv2.imread('./image/3.jpg')
            dst = cv2.resize(img1, dsize=(100, 100), interpolation=cv2.INTER_AREA)
            img_cut = cv2.rectangle(dst, (0,0), (100, 100), color, thickness=3)
            img[cy-50:cy+50, cx-50:cx+50] = img_cut
            cvzone.putTextRect(img, f'Mars', (cx-40, cy-60), scale=2,colorR=(0, 255, 0))
        elif number == 5:
            img1 = cv2.imread('./image/4.jpg')
            dst = cv2.resize(img1, dsize=(100, 100), interpolation=cv2.INTER_AREA)
            img_cut = cv2.rectangle(dst, (0,0), (100, 100), color, thickness=3)
            img[cy-50:cy+50, cx-50:cx+50] = img_cut
            cvzone.putTextRect(img, f'Jupiter', (cx-40, cy-60), scale=2,colorR=(0, 255, 0))
        elif number == 6:
            img1 = cv2.imread('./image/5.jpg')
            dst = cv2.resize(img1, dsize=(100, 100), interpolation=cv2.INTER_AREA)
            img_cut = cv2.rectangle(dst, (0,0), (100, 100), color, thickness=3)
            img[cy-50:cy+50, cx-50:cx+50] = img_cut
            cvzone.putTextRect(img, f'Venus', (cx-40, cy-60), scale=2,colorR=(0, 255, 0))
        elif number == 7:
            img1 = cv2.imread('./image/6.jpg')
            dst = cv2.resize(img1, dsize=(100, 100), interpolation=cv2.INTER_AREA)
            img_cut = cv2.rectangle(dst, (0,0), (100, 100), color, thickness=3)
            img[cy-50:cy+50, cx-50:cx+50] = img_cut   
            cvzone.putTextRect(img, f'Mercury', (cx-40, cy-60), scale=2,colorR=(0, 255, 0))         


        # Game GUI and other text screen.
        cvzone.putTextRect(img, f'Time: {int(totalTime-(time.time()-timeStart))}',
                           (1000, 75), scale=3, colorR=(0, 255, 0), offset=20)
        cvzone.putTextRect(img, f'Score: {str(score).zfill(2)}', (60, 75), scale=3, colorR=(0, 255, 0), offset=20)
    else:
        cvzone.putTextRect(img, 'Game Over', (400, 400), scale=5, offset=30, thickness=7, colorR=(0, 0, 0))
        cvzone.putTextRect(img, f'Your Score: {score}', (450, 500), scale=3, offset=20, colorR=(0, 0, 0))
        cvzone.putTextRect(img, 'Press R to restart', (460, 575), scale=2, offset=1, colorR=(0, 0, 0))



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        timeStart = time.time()
        score = 0