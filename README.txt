# Drowsiness Detection System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview
The Drowsiness Detection System is a real-time application that monitors a user's eye state to detect drowsiness. By analyzing the Eye Aspect Ratio (EAR), the system alerts the user through visual indicators and audio warnings when drowsiness is detected. This project is particularly useful for drivers, machine operators, and anyone who needs to stay alert during prolonged activities.

## Features
- Real-time drowsiness detection using webcam input.
- Audio alert when drowsiness is detected.
- Visual indicators for "Awake" and "Drowsy" states.
- Configurable parameters for EAR threshold and alert duration.

## Technologies Used
- **Python**: The programming language used for the implementation.
- **OpenCV**: Library for image processing and video capture.
- **dlib**: Library for face detection and landmark prediction.
- **scipy**: Library for scientific computations, used for calculating distances.
- **imutils**: Library for basic image processing tasks.
- **pygame**: Library for sound playback.
- **time**: Standard library module for time-related functions.

## Installation
To set up the Drowsiness Detection System, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/drowsiness-detection.git
   cd drowsiness-detection


2.Install required packages: You can install the necessary Python packages using pip. It's recommended to create a virtual environment for this project:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install opencv-python dlib scipy imutils pygame


3.Download the dlib shape predictor model: You need the shape_predictor_68_face_landmarks.dat file for facial landmark detection. You can download it from dlib's model repository and place it in the models directory.

4.Download the audio alert file: Place your audio file (e.g., music.wav) in the project directory or update the path in the code.



Usage
To run the Drowsiness Detection System, execute the following command:
python main.py



Controls
Press q to quit the application.



Code Structure
The project is organized into the following files:



main.py: The main entry point of the application, where video capture and processing are handled.
models/shape_predictor_68_face_landmarks.dat: The pre-trained model for facial landmark detection.
alarm.wav: The audio file played when drowsiness is detected.



main.py Overview
The main.py file contains the DrowsinessDetector class and the main application logic. Key components include:


DrowsinessDetector class:
Initializes parameters and loads necessary models.
Contains methods for processing each video frame and calculating the Eye Aspect Ratio (EAR).
Plays audio alerts based on drowsiness detection.


Configuration
You can modify the following parameters in the DrowsinessDetector class:

ear_threshold: Set the threshold for the Eye Aspect Ratio below which drowsiness is detected.
frame_check_threshold: Number of consecutive frames where EAR is below the threshold to trigger an alert.
alert_file: Path to the audio alert file.


Testing
To ensure the system functions correctly, consider implementing unit tests for the key methods. Testing can be done using frameworks like unittest or pytest.


Example Test:
Here’s a simple example of a test you might implement:

import unittest
from main import DrowsinessDetector

class TestDrowsinessDetector(unittest.TestCase):
    def test_eye_aspect_ratio(self):
        # Example coordinates for testing
        eye_coordinates = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5), (0.5, 0)]
        detector = DrowsinessDetector()
        ear = detector.eye_aspect_ratio(eye_coordinates)
        self.assertIsInstance(ear, float)

if __name__ == '__main__':
    unittest.main()


Contributing
Contributions are welcome! If you would like to contribute to the Drowsiness Detection System, please follow these steps:

1.Fork the repository.
2.Create a new branch (git checkout -b feature/YourFeature).
3.Make your changes and commit them (git commit -m 'Add your feature').
4.Push to the branch (git push origin feature/YourFeature).
5.Open a pull request.


License
This project is licensed under the MIT License. See the LICENSE file for details.


Acknowledgments
Special thanks to the developers of the libraries used in this project.
Inspiration from various drowsiness detection research papers and projects.



### Notes
- Make sure to customize the GitHub repository URL and any other specific details based on your project.
- You can also expand or modify sections based on any additional features or requirements specific to your project.

Let me know if you need any changes or additions to this README!
