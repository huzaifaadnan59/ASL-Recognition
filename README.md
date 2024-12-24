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

## Limitations
- Recognition limited to individual ASL letters.
- Accuracy may vary with different lighting or hand positions.
- Dataset size and diversity are limited.

---

## Future Enhancements
- Expand to recognize ASL words and sentences.
- Improve performance with optimized algorithms or hardware acceleration.
- Integrate with assistive technologies for real-world applications.

---

## Contributors
- Huzaifa Adnan
- Areej Dar

---

## Conclusion
The **ASL Recognition System** bridges communication barriers between ASL and non-ASL users. By leveraging computer vision and machine learning, it provides an intuitive solution for recognizing ASL gestures in real time. Future work can focus on enhancing gesture vocabulary, optimizing performance, and expanding real-world usability to better support the ASL community.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/huzaifaadnan59/ASL-Recognition.git
   cd ASL-Recognition-System
