import mediapipe as mp
import pyautogui
import math
import cv2

capture=cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hand=mp_hands.Hands(max_num_hands=1)

while True:
    
        ret,frame=capture.read()
        frame= cv2.flip(frame,1)

        rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result= hand.process(rgb_frame)
        hand_landmarks=result.multi_hand_landmarks

        if hand_landmarks:
                for landmarks in hand_landmarks:
                    mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
                        

        cv2.imshow("On-Screen Keyboard", frame)
        if cv2.waitKey(1) & 0XFF==ord('q'):
                break
cv2.release()
cv2.destroyAllWindows()         