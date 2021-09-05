import cv2
import numpy as np
import dlib
from math import hypot
from playsound import playsound

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
blink_counter = 0

def midpoint(p1,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
while True :
    _,frame = capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces :
        landmarks = predictor(gray,face)
        # eye blink detection
        leftup = midpoint(landmarks.part(37), landmarks.part(38))
        leftdown = midpoint(landmarks.part(40), landmarks.part(41))
        rightup  = midpoint(landmarks.part(43), landmarks.part(44))
        rightdown = midpoint(landmarks.part(47), landmarks.part(46))
        leftlength= hypot((leftup[0] - leftdown[0]), (leftup[1] - leftdown[1]))
        rightlength = hypot((rightup[0] - rightdown[0]), (rightup[1] - rightdown[1]))
        avglength = (leftlength+rightlength)/2
        cv2.circle(frame,(leftup[0],leftup[1]),3,(255,0,0),-1)
        cv2.circle(frame, (leftdown[0], leftdown[1]), 3, (255, 0, 0), -1)
        cv2.circle(frame, (rightup[0], rightup[1]), 3, (255, 0, 0), -1)
        cv2.circle(frame, (rightdown[0], rightdown[1]), 3, (255, 0, 0), -1)
        print(avglength)
        #print(rightlength)

        #yawning detection
        lengthmouth = hypot((landmarks.part(62).x - landmarks.part(66).x), (landmarks.part(62).y - landmarks.part(66).y))
        cv2.circle(frame,(landmarks.part(62).x,landmarks.part(62).y),3,(255,0,0),-1)
        cv2.circle(frame, (landmarks.part(66).x, landmarks.part(66).y), 3, (255, 0, 0), -1)
        print(lengthmouth)

        if avglength < 7:
            cv2.putText(frame, "BLINKING", (30, 200), font, 3, (255, 0, 0))
            blink_counter = blink_counter + 1
        if lengthmouth > 20:
            cv2.putText(frame, "Yawning", (30, 300), font, 3, (255, 255, 0))
       # if blink_counter > 100:
        #    playsound(
         #       "C:/Users/Manmeet Singh/Desktop/music/Warsongs Piercing Light Mako Remix  Music  League of Legends.mp3")
          #  print("playing...")

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
#music player:

