import cv2
import dlib
from scipy.spatial import distance
from imutils import face_utils
from pygame import mixer
import imutils
import time

# Sound initialization for alert
mixer.init()

class DrowsinessDetector:
    def __init__(self, ear_threshold=0.25, frame_check_threshold=20, alert_file="music.wav"):
        """
        Initialize the Drowsiness Detector system.
        :param ear_threshold: The minimum EAR value to trigger drowsiness alert.
        :param frame_check_threshold: Number of consecutive frames where EAR is below threshold to trigger alert.
        :param alert_file: Path to the audio file for the alert sound.
        """
        self.ear_threshold = ear_threshold
        self.frame_check_threshold = frame_check_threshold
        self.alert_file = alert_file
        self.flag = 0  # Counter for how many frames the EAR is below the threshold
        self.start_time = None  # Timer for eye closure duration
        
        # Load dlib face detector and facial landmarks predictor
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

        # Load the alert sound
        mixer.music.load(self.alert_file)

        # Facial landmarks indices for left and right eyes
        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
        (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

    @staticmethod
    def eye_aspect_ratio(eye):
        """
        Calculate the Eye Aspect Ratio (EAR) for a given eye.
        :param eye: Array of coordinates representing the eye landmarks.
        :return: The computed EAR value.
        """
        # Vertical distances between eye landmarks
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        # Horizontal distance
        C = distance.euclidean(eye[0], eye[3])
        # Compute EAR
        ear = (A + B) / (2.0 * C)
        return ear

    def process_frame(self, frame):
        """
        Process each frame to detect drowsiness based on EAR.
        :param frame: Current frame from the video capture.
        :return: Frame with drowsiness alert (if applicable).
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        subjects = self.detector(gray, 0)  # Detect faces in the frame

        for subject in subjects:
            shape = self.predictor(gray, subject)  # Get facial landmarks
            shape = face_utils.shape_to_np(shape)  # Convert landmarks to NumPy array

            # Extract left and right eye landmarks
            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]

            # Compute the EAR for both eyes
            leftEAR = self.eye_aspect_ratio(leftEye)
            rightEAR = self.eye_aspect_ratio(rightEye)

            # Average EAR for both eyes
            ear = (leftEAR + rightEAR) / 2.0

            # Draw eye contours on the frame
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            # Output EAR value to the console
            print(f"EAR: {ear:.2f}")

            # Check if EAR is below the threshold
            if ear < self.ear_threshold:
                self.flag += 1  # Increment the frame counter

                # Start the timer if it's the first frame below threshold
                if self.flag == 1:
                    self.start_time = time.time()

                # Check if the eyes have been closed for more than 2 seconds
                if self.start_time is not None and (time.time() - self.start_time) >= 2:
                    if not mixer.music.get_busy():  # Play the alert sound only if it's not already playing
                        mixer.music.play(-1)  # Play sound in loop
                # Update display text for drowsiness
                cv2.putText(frame, "Drowsy", (10, frame.shape[0] - 20), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # Show "Drowsy"
            else:
                self.flag = 0  # Reset the frame counter
                self.start_time = None  # Reset the timer
                if mixer.music.get_busy():  # Stop the sound if it's playing
                    mixer.music.stop()  
                cv2.putText(frame, "Awake", (10, frame.shape[0] - 20), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Show "Awake"

        return frame

def main():
    """
    Main function to initialize video capture and run the drowsiness detection loop.
    """
    # Create a DrowsinessDetector instance
    detector = DrowsinessDetector()

    # Start video capture from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()  # Capture each frame
        if not ret:
            break

        frame = imutils.resize(frame, width=450)  # Resize the frame for better performance

        # Process the frame for drowsiness detection
        frame = detector.process_frame(frame)

        # Show the frame with the drowsiness alert (if applicable)
        cv2.imshow("Drowsiness Detector", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
