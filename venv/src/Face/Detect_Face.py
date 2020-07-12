import cv2
import os
import mmap
import pygame

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#Loading The Music Library
with open('song.mp3') as f:
    PlayedMp3File = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

pygame.mixer.init(44100, -16,2,2048)

pygame.mixer.music.load(PlayedMp3File)


# To capture video from webcam.
cap = cv2.VideoCapture(0)



EVENT1=False
EVENT2=False

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    iter=0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        iter+=1

    if iter>=5:
        if EVENT1==False:
            pygame.mixer.music.play()
            EVENT1=True
            EVENT2=False
    else:
        if EVENT2==False and EVENT1==True:
            pygame.mixer.music.pause()
            EVENT2=True
            EVENT1=False


    # Display
    font = cv2.FONT_HERSHEY_DUPLEX

    cv2.putText(img, "People Detected : "+str(iter), (0, 50), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('img', img)

    # Stop if q button/key is pressed
    if cv2.waitKey(113) == ord('q'):
        break

# Release the VideoCapture object
cap.release()