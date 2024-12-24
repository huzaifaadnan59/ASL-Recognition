# ASL-Recognition
This project implements a real-time American Sign Language (ASL) recognition system using computer vision and machine learning techniques. The system is designed to recognize individual ASL hand gestures through a webcam feed and display the corresponding ASL letter on the screen.

Features
Real-time Hand Detection: Uses MediaPipe for hand landmark detection.
Gesture Recognition: Classifies ASL gestures using a trained Random Forest model.
User-Friendly GUI: Built with Tkinter to display live predictions.
Accessible Implementation: Focused on enhancing communication for the ASL community.
Tools and Libraries
Programming Language: Python
Libraries Used:
OpenCV: For real-time video capture and image processing.
MediaPipe: For hand landmark detection.
Scikit-learn: For machine learning model training.
Tkinter: For creating the graphical user interface.
Pickle: For saving and loading models and data.
How It Works
Data Collection: Captures images of ASL gestures using OpenCV.
Data Preprocessing: Extracts hand landmarks and processes them for uniformity.
Model Training: Trains a Random Forest classifier using extracted features.
Real-time Recognition: Processes webcam frames, predicts gestures, and displays results in real-time via GUI.
Usage
Clone this repository:
bash
Copy code
git clone <repository_url>
cd ASL-Recognition-System
Install dependencies:
Copy code
pip install -r requirements.txt
Run the application:
Copy code
python asl_recognition.py
Use the GUI to start gesture recognition. Press the Exit button to quit.
Limitations
Restricted to recognizing individual ASL letters.
Performance may vary under different lighting conditions or hand orientations.
Dataset size and diversity could be expanded for improved accuracy.
Future Enhancements
Extend the system to recognize complete ASL words or sentences.
Improve real-time performance with optimized algorithms or hardware acceleration.
Integrate with assistive technologies for broader accessibility.
Contributors
Hzuaifa Adnan 
Areej Dar
