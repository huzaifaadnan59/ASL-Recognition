import tkinter as tk
from PIL import ImageTk, Image
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math


class ASLRecognitionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("ASL Recognition")

        # Add the heading label
        self.heading_label = tk.Label(window, text="Welcome to ASL Recognition", font=("Arial", 18, "bold"))
        self.heading_label.pack(pady=10)

        self.video_label = tk.Label(window)
        self.video_label.pack()

        self.detector = HandDetector(maxHands=2)
        self.classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

        self.offset = 20
        self.imgSize = 300
        self.labels = ["A", "B", "C", "D"]

        self.cap = cv2.VideoCapture(0)
        self.video_loop()

        # Bind the 'a' key press event
        self.window.bind('a', self.close_program)

    def close_program(self, event):
        self.window.destroy()

    def video_loop(self):
        success, img = self.cap.read()
        if success:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            hands, img = self.detector.findHands(img)

            for hand in hands:
                x, y, w, h = hand['bbox']
                imgWhite = np.ones((self.imgSize, self.imgSize, 3), np.uint8) * 255
                imgCrop = img[y - self.offset:y + h + self.offset, x - self.offset:x + w + self.offset]

                if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
                    aspectRatio = h / w

                    if aspectRatio > 1:
                        k = self.imgSize / h
                        wCal = math.ceil(k * w)
                        imgResize = cv2.resize(imgCrop, (wCal, self.imgSize))
                        wGap = math.ceil((self.imgSize - wCal) / 2)
                        imgWhite[:, wGap:wCal + wGap] = imgResize
                        prediction, index = self.classifier.getPrediction(imgWhite, draw=False)
                        print(prediction, index)

                    else:
                        k = self.imgSize / w
                        hCal = math.ceil(k * h)
                        imgResize = cv2.resize(imgCrop, (self.imgSize, hCal))
                        hGap = math.ceil((self.imgSize - hCal) / 2)
                        imgWhite[hGap:hCal + hGap, :] = imgResize
                        prediction, index = self.classifier.getPrediction(imgWhite, draw=False)

                    cv2.rectangle(img, (x - self.offset, y - self.offset - 50),
                                  (x - self.offset + 90, y - self.offset - 50 + 50), (255, 0, 255), cv2.FILLED)
                    cv2.putText(img, self.labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
                    cv2.rectangle(img, (x - self.offset, y - self.offset),
                                  (x + w + self.offset, y + h + self.offset), (255, 0, 255), 4)

            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.window.after(1, self.video_loop)


if __name__ == '__main__':
    root = tk.Tk()
    app = ASLRecognitionApp(root)
    root.mainloop()
