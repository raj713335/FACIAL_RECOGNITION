#import the required packages

import face_recognition
import cv2
import numpy as np
import os
from memory_data import memory_usage
from datetime import datetime,date


list_names=[]

def video_sync():

    #Importing Images
    #As we have imported before we can use the same face_recognition.load_image_file() function to import our images. But when we have multiple images, importing them individually can become messy. Therefore we will write a script to import all images in a given folder at once. For this we will need the os library so we will import that first. We will store all the images in one list and their names in another.

    path = 'IMAGES'
    images = []     # LIST CONTAINING ALL THE IMAGES
    className = []    # LIST CONTAINING ALL THE CORRESPONDING CLASS Names
    myList = os.listdir(path)
    print("Total Classes Detected:",len(myList))
    for x,cl in enumerate(myList):
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            className.append(os.path.splitext(cl)[0])







    #Compute Encodings
    #Now that we have a list of images we can iterate through those and create a corresponding encoded list for known faces. To do this we will create a function. As earlier we will first convert it into RGB and then find its encoding using the face_encodings() function. Then we will append each encoding to our list.

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    #Now we can simply call this function with the images list as the input arguments.

    encodeListKnown = findEncodings(images)
    print('Encodings Complete')


    #Starting the web Capture
    #The While loop
    #The while loop is created to run the webcam. But before the while loop we have to create a video capture object so that we can grab frames from the webcam.


    video_capture = cv2.VideoCapture(1)

    #Webcam Image
    #First we will read the image from the webcam and then resize it to quarter the size. This is done to increase the speed of the system. Even though the image being used is 1/4 th of the original, we will still use the original size while displaying. Next we will convert it to RGB.

    while True:
        success, img = video_capture.read()

        imgS = img[:, :, ::-1]
        # imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        # imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        #Webcam Encodings
        #Once we have the webcam frame we will find all the faces in our image. The face_locations function is used for this purpose. Later we will find the face_encodings as well.

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        #Find Matches
        # Now we can match the current face encodings to our known faces encoding list to find the matches. We will also compute the distance. This is done to find the best match in case more than one face is detected at a time.

        for (y1, x2, y2, x1), encodeFace in zip(facesCurFrame,encodesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            #Once we have the list of face distances we can find the minimum one, as this would be the best match.

            matchIndex = np.argmin(faceDis)
            # print(matchIndex)
            # y1, x2, y2, x1 = faceLoc
            # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            #Now based on the index value we can determine the name of the person and display it on the original Image.

            percentage_matched=int(round((1-faceDis[matchIndex])*100,0))
            print(percentage_matched)

            if percentage_matched>=50:

                if matches[matchIndex]:
                    name = className[matchIndex]
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)



                    CENTER = (x1, y1)

                    cv2.circle(img, CENTER, 15, (0,255,0), -1)

                    TEXT_FACE = cv2.FONT_HERSHEY_DUPLEX
                    TEXT_SCALE = 0.4
                    TEXT_THICKNESS = 1
                    TEXT = str(int(percentage_matched))

                    text_size, _ = cv2.getTextSize(TEXT, TEXT_FACE, TEXT_SCALE, TEXT_THICKNESS)
                    text_origin = (int(round((CENTER[0] - text_size[0] / 2),0)), int(round((CENTER[1] + text_size[1] / 2),0)))


                    cv2.putText(img, TEXT, text_origin, TEXT_FACE, TEXT_SCALE, (255, 255, 255), TEXT_THICKNESS, cv2.LINE_AA)

                    def markAttendance(name):
                        with open('DATA/Attendence.csv', 'r+') as f:
                            myDataList = f.readlines()
                            nameList = []
                            for line in myDataList:
                                entry = line.split(',')
                                nameList.append(entry[0])
                            if name not in line:
                                now = datetime.now()
                                dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
                                f.writelines(f'\n{name},{dt_string}')

                    markAttendance(name)










            else:

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)


        def memory_stack():



            h, w, _ = img.shape

            x = np.arange(w)

            B,G,R=memory_usage()

            B = img[:, :, 0].sum(axis=0)
            B = h - h * B / B.max()
            G = img[:, :, 1].sum(axis=0)
            G = h - h * G / G.max()
            R = img[:, :, 2].sum(axis=0)
            R = h - h * R / R.max()

            pts = np.vstack((x*0.1, B*0.1)).astype(np.int32).T
            cv2.polylines(img, [pts], isClosed=False, color=(255, 0, 0))
            pts = np.vstack((x*0.1, G*0.1)).astype(np.int32).T
            cv2.polylines(img, [pts], isClosed=False, color=(0, 255, 0))
            pts = np.vstack((x*0.1, R*0.1)).astype(np.int32).T
            cv2.polylines(img, [pts], isClosed=False, color=(0, 0, 255))



        memory_stack()

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('frame', img)

        #cv2.imshow('FACIAL RECOGNITION', cv2.resize(img, (640, 480)))

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break








