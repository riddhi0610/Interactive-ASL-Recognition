import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480
#webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam) #sets width size of webcam
cap.set(4, hCam) #sets height size of webcam

#stores images
folderPath = "ASLHandImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}') #prints each path image
    overlayList.append(image)

print(len(overlayList)) #prints out 6
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20] #ids of tips of all 5 fingers

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0: #gets tip of finger and than recognizes where it is finger 1 - 5
        fingers = []
        horizontalfingers = []
        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        # counts number of vertical fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)

        # counts number of horizontal fingers
        for id in range(1,5):
            if lmList[tipIds[id]][1] > lmList[tipIds[id]-2][1]:
               horizontalfingers.append(1)
            else:
                horizontalfingers.append(0)

        horizontalFingers = horizontalfingers.count(1)

        # A
        if (lmList[tipIds[0]][2] < lmList[16][2]) and (lmList[tipIds[0]][2] < lmList[20][2]) and (
                lmList[tipIds[0]][2] < lmList[12][2]) and (lmList[tipIds[0]][1] > lmList[5][1]) and (lmList[tipIds[0]][2] < lmList[10][2]) and (totalFingers == 0): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED) #prints out text box
            cv2.putText(img, str("A"), (45, 375), cv2.FONT_HERSHEY_PLAIN, #prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[0].shape
            img[0:h, 0:w] = overlayList[0] #prints out a.jpg

        # B
        if (totalFingers == 4): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("B"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[1].shape
            img[0:h, 0:w] = overlayList[1]  # prints out b.png

        # C
        if (lmList[tipIds[4]][2] > lmList[19][2]) and (lmList[tipIds[4]][2] < lmList[tipIds[0]][2]) and (lmList[tipIds[1]][2] < lmList[tipIds[0]][2]) and (lmList[tipIds[0]][2] < lmList[tipIds[0]-1][2]) and (horizontalFingers == 4): #conditions
            cv2.imshow("Image", img)
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("C"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[2].shape
            img[0:h, 0:w] = overlayList[2]  # prints out c.png

        # D
        if (totalFingers == 1) and (lmList[tipIds[0]][2] <= lmList[tipIds[2]][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("D"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[3].shape
            img[0:h, 0:w] = overlayList[3]  # prints out d.jpg

        # E
        if (lmList[tipIds[0]][2] > lmList[tipIds[2]][2]) and (lmList[tipIds[0]][2] > lmList[tipIds[1]][2]) and (lmList[tipIds[0]][2] > lmList[tipIds[3]][2]) and (lmList[tipIds[0]][2] > lmList[tipIds[4]][2]) and (totalFingers == 0) and (horizontalFingers == 3): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("E"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[4].shape
            img[0:h, 0:w] = overlayList[4]  # prints out e.jpg

        # F
        if (totalFingers == 3) and (lmList[tipIds[0]][2] <= lmList[tipIds[1]][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("F"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[5].shape
            img[0:h, 0:w] = overlayList[5]  # prints out f.png

        # G
        if (horizontalFingers == 1): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("G"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[6].shape
            img[0:h, 0:w] = overlayList[6]  # prints out g.png

        # H
        if (horizontalFingers == 2): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("H"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[7].shape
            img[0:h, 0:w] = overlayList[7]  # prints out h.png

        # I
        if (totalFingers == 1) and (lmList[tipIds[4]][2] < lmList[tipIds[1]][2]) and (lmList[tipIds[0]][2] < lmList[tipIds[2]-1][2]) and (lmList[tipIds[0]][2] > lmList[5][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("I"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[8].shape
            img[0:h, 0:w] = overlayList[8]  # prints out i.jpg

        # J
        if (totalFingers == 1) and (horizontalFingers == 1) and (lmList[tipIds[4]][1] > lmList[tipIds[1]][1]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("J"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[9].shape
            img[0:h, 0:w] = overlayList[9]  # prints out j.png

        # K
        if (totalFingers == 2) and (lmList[tipIds[0]][2] < lmList[tipIds[3]-2][2]) and (horizontalFingers == 3): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("K"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[10].shape
            img[0:h, 0:w] = overlayList[10]  # prints out k.png

        # L
        if (totalFingers == 1) and (horizontalFingers >= 2) and (lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("L"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[11].shape
            img[0:h, 0:w] = overlayList[11]  # prints out l.png

        # M
        if (lmList[tipIds[0]][2] < lmList[tipIds[4]][2]) and (totalFingers == 0) and (lmList[tipIds[0]][2] > lmList[14][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("M"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[12].shape
            img[0:h, 0:w] = overlayList[12]  # prints out m.png

        # N
        if (lmList[tipIds[0]][2] < lmList[tipIds[4]][2]) and (totalFingers == 0) and (lmList[tipIds[0]][2] < lmList[14][2]) and (lmList[tipIds[0]][2] > lmList[10][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("N"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[13].shape
            img[0:h, 0:w] = overlayList[13]  # prints out n.png

        # O
        if (lmList[tipIds[4]][2] > lmList[tipIds[0]][2]) and (horizontalFingers == 4) and (lmList[tipIds[1]][2] > lmList[tipIds[0]][2]) and (totalFingers == 0): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("O"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[14].shape
            img[0:h, 0:w] = overlayList[14]  # prints out o.png

        # P
        if (horizontalFingers == 2) and (lmList[tipIds[0]][2] < lmList[tipIds[2]][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("P"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[15].shape
            img[0:h, 0:w] = overlayList[15]  # prints out p.png

        # Q
        if (totalFingers == 3) and (horizontalFingers == 0) and (lmList[tipIds[1]][2] > lmList[tipIds[2]][2]) and (lmList[tipIds[0]][2] > lmList[tipIds[2]][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("Q"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[16].shape
            img[0:h, 0:w] = overlayList[16]  # prints out q.png

        # R
        if (totalFingers == 2) and (lmList[tipIds[1]][1] < lmList[tipIds[2]][1]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("R"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[17].shape
            img[0:h, 0:w] = overlayList[17]  # prints out r.png

        # S
        if (lmList[tipIds[0]][2] < lmList[tipIds[2]][2]) and (lmList[tipIds[0]][2] < lmList[tipIds[1]][2]) and (
            lmList[tipIds[0]][2] < lmList[tipIds[3]][2]) and (lmList[tipIds[0]][2] < lmList[tipIds[4]][2]) and (
            totalFingers == 0) and (horizontalFingers == 0): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("S"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[18].shape
            img[0:h, 0:w] = overlayList[18]  # prints out s.jpg

        # T
        if (lmList[tipIds[0]][1] < lmList[5][1]) and (totalFingers == 0) and (horizontalFingers <= 2): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("T"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[19].shape
            img[0:h, 0:w] = overlayList[19]  # prints out t.png

        # U
        if (totalFingers == 2) and (horizontalFingers == 4): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("U"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[20].shape
            img[0:h, 0:w] = overlayList[20]  # prints out u.jpg

        # V
        if (totalFingers == 2) and (lmList[tipIds[0]][2] > lmList[tipIds[3]-2][2]) and (horizontalFingers == 3): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("V"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[21].shape
            img[0:h, 0:w] = overlayList[21]  # prints out v.jpg

        # W
        if (totalFingers == 3) and (horizontalFingers == 3): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("W"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[22].shape
            img[0:h, 0:w] = overlayList[22]  # prints out w.png

        # X
        if (totalFingers == 0) and (lmList[tipIds[1]][2] > lmList[7][2]) and (lmList[7][2] < lmList[6][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("X"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[23].shape
            img[0:h, 0:w] = overlayList[23]  # prints out x.png

        # Y
        if (totalFingers == 1) and (lmList[tipIds[4]][2] < lmList[tipIds[1]][2]) and (
                    lmList[tipIds[0]][2] < lmList[5][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("Y"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[24].shape
            img[0:h, 0:w] = overlayList[24]  # prints out y.png

        # Z
        if (totalFingers == 1) and (lmList[tipIds[0]][2] <= lmList[9][2]) and (lmList[tipIds[1]][2] < lmList[6][2]): #conditions
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)  # prints out text box
            cv2.putText(img, str("Z"), (45, 375), cv2.FONT_HERSHEY_PLAIN,  # prints out letter on text box
                        10, (255, 0, 0), 25)
            h, w, c = overlayList[25].shape
            img[0:h, 0:w] = overlayList[25]  # prints out z.png

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
