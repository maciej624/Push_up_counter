import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

licznik = 0 # counting push ups
pozycja = None #either top or bottom
pokazuj_efekt = 0 #ile klatek pokazuje obrazek

efekt = cv2.imread(r"C:\Users\kaenk\Desktop\efekt.jpg",cv2.IMREAD_UNCHANGED)
if efekt is not None:
    efekt = cv2.resize(efekt, (200, 200))
else:
    print("PNG - not found moving on")


def naklej_png(frame, obrazek, x, y):
    h, w = obrazek.shape[:2]
    frame[y:y+h, x:x+w] = obrazek
    return frame


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    wynik = pose.process(rgb)

    if wynik.pose_landmarks:
        mp_draw.draw_landmarks(
            frame,
            wynik.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_draw.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=4),
            connection_drawing_spec=mp_draw.DrawingSpec(color=(255, 0, 255), thickness=2)
)

        punkty = wynik.pose_landmarks.landmark

        lokiec = punkty[mp_pose.PoseLandmark.LEFT_ELBOW].y
        bark   = punkty[mp_pose.PoseLandmark.LEFT_SHOULDER].y


        if lokiec > bark + 0.15:
            stan = "DOL"
        else:
            stan = "GORA"

        if pozycja == "DOL" and stan == "GORA":
            licznik += 1
            pokazuj_efekt = 20 

        pozycja = stan

        cv2.putText(frame, f"Pompki: {licznik}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
        cv2.putText(frame, stan, (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)

    if pokazuj_efekt > 0 and efekt is not None:
        frame = naklej_png(frame, efekt, 400,10)
        pokazuj_efekt -= 1           

    cv2.imshow("Licznik pompek", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()