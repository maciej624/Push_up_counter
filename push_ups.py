"""Author: Maciej Drajewski"""

import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

count = 0 # counting push ups
position = None #either top or bottom
show_effect = 0 #how long the picture is shown

efekt = cv2.imread(r"photo.jpg",cv2.IMREAD_UNCHANGED) #photo
if efekt is not None:
    efekt = cv2.resize(efekt, (200, 200))
else:
    print("picture not found")

def photo_paste(frame, picture, x, y):
    h, w = picture.shape[:2]
    frame[y:y+h, x:x+w] = picture
    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #is needed cuz mediapipe work on RGB and opencv on BGR so gotta change
    wynik = pose.process(rgb)

    if wynik.pose_landmarks:
        mp_draw.draw_landmarks(
            frame,
            wynik.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_draw.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=4),
            connection_drawing_spec=mp_draw.DrawingSpec(color=(255, 0, 255), thickness=2)
)
        points = wynik.pose_landmarks.landmark
        elbow = points[mp_pose.PoseLandmark.LEFT_ELBOW].y
        shoulder   = points[mp_pose.PoseLandmark.LEFT_SHOULDER].y

        if elbow > shoulder + 0.15:
            state = "DOWN"
        else:
            state = "UP"

        if position == "DOWN" and state == "UP":
            count += 1
            show_effect = 20 

        position = state

        cv2.putText(frame, f"PUSH UPS: {count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
        cv2.putText(frame, state, (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)

    if show_effect > 0 and efekt is not None:
        frame = photo_paste(frame, efekt, 400,10)
        show_effect -= 1           

    cv2.imshow("Push ups counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
