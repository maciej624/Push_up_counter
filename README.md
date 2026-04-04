# 💪 AI Push-Up Counter (MediaPipe)
![demo](demo_push_ups.gif)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-AI-orange.svg)

A real-time push-up counter using Computer Vision. The script analyzes the user's pose via webcam, tracks body landmarks, and automatically counts repetitions based on the vertical distance between the elbow and shoulder.

---

## 🚀 Features

* **Real-time Pose Detection:** Uses Google's MediaPipe library to track 33 body landmarks.
* **Automatic Repetition Counting:** Logic based on the Y-coordinate relationship between the elbow and shoulder.
* **Visual Feedback:** * Displays a real-time "skeleton" (landmarks and connections).
    * HUD showing the current count and state (UP/DOWN).
    * Dynamic image overlay (reward effect) triggered upon successful completion of a push-up.
* **Efficient Logic:** Simple state-machine approach to prevent double-counting.

---

## 🛠️ How It Works

1. **Preprocessing:** The frame is captured via OpenCV, flipped for a mirror effect, and converted from BGR to RGB (required by MediaPipe).
2. **Landmark Extraction:** The system identifies the `LEFT_SHOULDER` and `LEFT_ELBOW` points.
3. **Overlay System:** When a repetition is counted, a timer (`show_effect`) is activated to display a custom image on the screen for 20 frames.

---

## 📋 Requirements

* Python 3.9+
* Webcam
* **Libraries:**
  ```bash
  pip install opencv-python mediapipe
