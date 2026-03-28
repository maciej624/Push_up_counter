# Push-up Counter 💪

Real-time push-up counter using MediaPipe pose detection and OpenCV.

![demo](demo_push_ups.gif)

## What it does

- Detects your body position in real time using MediaPipe
- Counts push-ups automatically when you go from bottom to top position
- Shows fireworks effect after each push-up
- Displays current position (UP/DOWN) and total count on screen

## How it works

MediaPipe detects 33 body landmarks in real time.
The program tracks the Y position of the left elbow and shoulder.
When elbow drops below shoulder level - position is DOWN.
When elbow rises back up - position is UP and counter increases by 1.
```
Camera → MediaPipe → elbow Y vs shoulder Y → count push-up
```

## Tech stack

- Python 3.9
- MediaPipe
- OpenCV

## Requirements
```
pip install mediapipe opencv-python
```

## How to run
```
python push_ups.py
```

Stand sideways to the camera so your elbow and shoulder are clearly visible.
Press Q to quit.

## Tips

- Stand sideways to the camera for best detection
- Make sure your full upper body is visible
- If counting feels off, adjust the `0.15` threshold in the code
