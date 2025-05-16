
---

# Drowsiness Detection System

## Table of Contents

 [Project Overview](#project-overview)
 [Features](#features)
 [Technologies Used](#technologies-used)
 [Installation](#installation)
 [Usage](#usage)
 [Code Structure](#code-structure)
 [Configuration](#configuration)
 [Testing](#testing)
 [Contributing](#contributing)
 [License](#license)
 [Acknowledgments](#acknowledgments)

---

## Project Overview

The Drowsiness Detection System is a real-time computer vision application that monitors eye activity to detect drowsiness. It uses the Eye Aspect Ratio (EAR) as a key metric and alerts the user via visual and audio cues when drowsiness is detected. This system is especially useful for drivers, machine operators, and other users who must stay alert during extended periods of activity.

---

## Features

 Real-time drowsiness detection using webcam input.
 Audio alerts when drowsiness is detected.
 Visual indicators for "Awake" and "Drowsy" states.
 Easily configurable EAR threshold and alert duration.

---

## Technologies Used

 Python: Main programming language.
 OpenCV: Image processing and video capture.
 dlib: Facial detection and landmark estimation.
 scipy: Scientific computations for distance calculation.
 imutils: Helper functions for OpenCV workflows.
 pygame: Audio playback for alerts.
 time: Built-in module for timing functions.

---

## Installation

Follow these steps to install and set up the project:

### 1. Clone the Repository

```bash
git clone https://github.com/MurtadhaJasim/Driver-Drowsiness-Detection
cd Driver-Drowsiness-Detection
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install opencv-python dlib scipy imutils pygame
```

### 4. Download Required Files

Dlib shape predictor model:
  Download `shape_predictor_68_face_landmarks.dat` from [dlib's model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2), extract it, and place it in the `models/` directory.
Alert Audio File:
  Place an audio file such as `alarm.wav` in the root directory or modify the path in `main.py`.

---

## Usage

Run the application using:

```bash
python main.py
```

### Controls

 Press `q` to quit the application.

---

## Code Structure

```
Driver-Drowsiness-Detection/
│
├── main.py                         # Main logic for video capture and detection
├── models/
│   └── shape_predictor_68_face_landmarks.dat  # Pretrained facial landmark model
├── alarm.wav                       # Sound file for alert
└── README.md
```

### `main.py` Overview

Contains the `DrowsinessDetector` class, which:

 Initializes video capture and loads models.
 Calculates the Eye Aspect Ratio (EAR).
 Triggers audio/visual alerts based on EAR analysis.

---

## Configuration

You can customize these parameters inside the `DrowsinessDetector` class:

 `ear_threshold`: EAR threshold to determine drowsiness.
 `frame_check_threshold`: Number of consecutive frames that must meet the EAR condition to trigger an alert.
 `alert_file`: Path to the alert sound file.

---

## Testing

Use the `unittest` framework to test functionality:

### Example Test

```python
import unittest
from main import DrowsinessDetector

class TestDrowsinessDetector(unittest.TestCase):
    def test_eye_aspect_ratio(self):
        eye_coordinates = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5), (0.5, 0)]
        detector = DrowsinessDetector()
        ear = detector.eye_aspect_ratio(eye_coordinates)
        self.assertIsInstance(ear, float)

if __name__ == '__main__':
    unittest.main()
```

---

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a feature branch:
   `git checkout -b feature/YourFeature`
3. Commit your changes:
   `git commit -m 'Add your feature'`
4. Push to the branch:
   `git push origin feature/YourFeature`
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

* Special thanks to the open-source community behind the libraries used.
* Inspired by academic research and other drowsiness detection projects.

---
