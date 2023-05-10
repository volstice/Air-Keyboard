import cv2
import HandTrackModule as htm
cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)

detector = htm.handDetector(detectionCon=0.8)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)