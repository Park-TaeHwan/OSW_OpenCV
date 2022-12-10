import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True : 
    success, img = cap.read()
    hands, img = detector.findHands(img) #with draw
    #hands, img = detector.findHands(img, draw = False)
    
    if hands : 
        #hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] # List of 21 Landmarks points
        bbox1 = hand1["bbox"] # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"] # center of the hand cx, cy
        handType1 = hand1["type"] # hand type left or right

        #print(handType1)
        fingers1 = detector.fingersUp(hand1)
        #length, info, img = detector.findDistance(lmList1[8], lmList1[12], img)
        #length, img = detector.findDistance(lmList1[8], lmList1[12])

        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"] # List of 21 Landmarks points
            bbox2 = hand2["bbox"] # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"] # center of the hand cx, cy
            handType2 = hand2["type"] # hand type left or right

            fingers2 = detector.fingersUp(hand2)

            #print(fingers1, fingers2)
            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)



    cv2.imshow("Image", img)
    cv2.waitKey(1)
