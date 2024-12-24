# ASL Recognition System

This project implements a **real-time American Sign Language (ASL) recognition system** using computer vision and machine learning techniques. The system is designed to recognize individual ASL hand gestures through a webcam feed and display the corresponding ASL letter on the screen.

## Features
- **Real-time Hand Detection**: Uses MediaPipe for hand landmark detection.
- **Gesture Recognition**: Classifies ASL gestures using a trained Random Forest model.
- **User-Friendly GUI**: Built with Tkinter to display live predictions.
- **Accessible Implementation**: Focused on enhancing communication for the ASL community.

## Tools and Libraries
- **Programming Language**: Python
- **Libraries Used**:
  - OpenCV: For real-time video capture and image processing.
  - MediaPipe: For hand landmark detection.
  - Scikit-learn: For machine learning model training.
  - Tkinter: For creating the graphical user interface.
  - Pickle: For saving and loading models and data.

## How It Works
1. **Data Collection**: Captures images of ASL gestures using OpenCV.
2. **Data Preprocessing**: Extracts hand landmarks and processes them for uniformity.
3. **Model Training**: Trains a Random Forest classifier using extracted features.
4. **Real-time Recognition**: Processes webcam frames, predicts gestures, and displays results in real-time via GUI.

## Usage
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd ASL-Recognition-System
