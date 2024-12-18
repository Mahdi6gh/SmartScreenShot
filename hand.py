import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self):
        self.mediapipeHand = mp.solutions.hands
        self.hands = self.mediapipeHand.Hands(max_num_hands=1,min_detection_confidence=0.8,min_tracking_confidence=0.5)
        self.Draw = mp.solutions.drawing_utils
    def detect(self, frame,drawing=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)

                    if id == 4:
                        cv2.circle(frame, (x, y), 15, (105,105,15))
                if drawing:
                    self.Draw.draw_landmarks(frame, hand_landmarks, self.mediapipeHand.HAND_CONNECTIONS)
        return frame
    def positon(self,frame,drawing=True,Handnum=0):
        landmarksList = []
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)
        if self.results.multi_hand_landmarks:
            myHands=self.results.multi_hand_landmarks[Handnum]
            for hand_landmarks in self.results.multi_hand_landmarks:
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    landmarksList.append([id,x,y])

            if drawing:
                cv2.circle(frame, (x, y), 8, (105,105,15),-1)
        return landmarksList