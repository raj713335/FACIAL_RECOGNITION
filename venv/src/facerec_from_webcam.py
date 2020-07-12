import face_recognition
import cv2
import numpy as np
#from gtts import gTTS
import os
#import voice
import threading
from threading import Thread
from datetime import datetime

def face_recognition_start():


    video_capture = cv2.VideoCapture(0)


    obama_image = face_recognition.load_image_file("obama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]


    arnab_image = face_recognition.load_image_file("arnab.jpg")
    arnab_face_encoding = face_recognition.face_encodings(arnab_image)[0]


    piyush_image = face_recognition.load_image_file("piyush.jpg")
    piyush_face_encoding = face_recognition.face_encodings(piyush_image)[0]

    prajwal_image = face_recognition.load_image_file("Prajwal.jpg")
    prajwal_face_encoding = face_recognition.face_encodings(prajwal_image)[0]
    #
    santosh_image = face_recognition.load_image_file("santosh.jpg")
    santosh_face_encoding = face_recognition.face_encodings(santosh_image)[0]

    vikas_image = face_recognition.load_image_file("vikas.jpg")
    vikas_face_encoding = face_recognition.face_encodings(vikas_image)[0]

    amulya_image = face_recognition.load_image_file("amulya.jpg")
    amulya_face_encoding = face_recognition.face_encodings(amulya_image)[0]

    anand_image = face_recognition.load_image_file("anand.jpg")
    anand_face_encoding = face_recognition.face_encodings(anand_image)[0]


    sandeep_image = face_recognition.load_image_file("Sandeep.jpg")
    sandeep_face_encoding = face_recognition.face_encodings(sandeep_image)[0]

    arun_image = face_recognition.load_image_file("Arun.jpg")
    arun_face_encoding = face_recognition.face_encodings(arun_image)[0]


    arvind_image = face_recognition.load_image_file("Arvind.jpg")
    arvind_face_encoding = face_recognition.face_encodings(arvind_image)[0]

    abhishek_image = face_recognition.load_image_file("abhishek.jpg")
    abhishek_face_encoding = face_recognition.face_encodings(abhishek_image)[0]

    pandey_image = face_recognition.load_image_file("chandra.jpg")
    pandey_face_encoding = face_recognition.face_encodings(pandey_image)[0]

    chetan_image = face_recognition.load_image_file("chetan.jpg")
    chetan_face_encoding = face_recognition.face_encodings(chetan_image)[0]


    """nandakumar_image = face_recognition.load_image_file("nadakumar.jpg")
    nandakumar_face_encoding = face_recognition.face_encodings(nandakumar_image)[0]"""

    jirav_image = face_recognition.load_image_file("jirav.jpg")
    jirav_face_encoding = face_recognition.face_encodings(jirav_image)[0]

    anant_image = face_recognition.load_image_file("ingole.jpg")
    anant_face_encoding = face_recognition.face_encodings(anant_image)[0]

    pramod_image = face_recognition.load_image_file("pramod.jpg")
    pramod_face_encoding = face_recognition.face_encodings(pramod_image)[0]

    sub_image = face_recognition.load_image_file("sub.jpg")
    sub_face_encoding = face_recognition.face_encodings(sub_image)[0]

    chandrarao_image = face_recognition.load_image_file("chandrarao.jpg")
    chandrarao_face_encoding = face_recognition.face_encodings(chandrarao_image)[0]

    kapil_image = face_recognition.load_image_file("kapil.jpg")
    kapil_face_encoding = face_recognition.face_encodings(kapil_image)[0]

    gaurav_image = face_recognition.load_image_file("gaurav.jpg")
    gaurav_face_encoding = face_recognition.face_encodings(gaurav_image)[0]

    ashish_image = face_recognition.load_image_file("ashish.jpg")
    ashish_face_encoding = face_recognition.face_encodings(ashish_image)[0]

    kunal_image = face_recognition.load_image_file("kunal.jpg")
    kunal_face_encoding = face_recognition.face_encodings(kunal_image)[0]

    murtaza_image = face_recognition.load_image_file("murtaza.jpg")
    murtaza_face_encoding = face_recognition.face_encodings(murtaza_image)[0]

    ronil_image = face_recognition.load_image_file("ronyl.jpg")
    ronil_face_encoding = face_recognition.face_encodings(ronil_image)[0]



    jaigude_image = face_recognition.load_image_file("jaigude.jpg")
    jaigude_face_encoding = face_recognition.face_encodings(jaigude_image)[0]

    saifu_image = face_recognition.load_image_file("saifu.jpg")
    saifu_face_encoding = face_recognition.face_encodings(saifu_image)[0]

    amol_image = face_recognition.load_image_file("amol.jpg")
    amol_face_encoding = face_recognition.face_encodings(amol_image)[0]

    manish_image = face_recognition.load_image_file("amol.jpg")
    manish_face_encoding = face_recognition.face_encodings(manish_image)[0]

    harshada_image = face_recognition.load_image_file("harshada.jpg")
    harshada_face_encoding = face_recognition.face_encodings(harshada_image)[0]

    niladri_image = face_recognition.load_image_file("niladri.jpg")
    niladri_face_encoding = face_recognition.face_encodings(niladri_image)[0]

    ########################################################################

    Ajay_Holey_image = face_recognition.load_image_file("Ajay Holey.jpg")
    Ajay_Holey_face_encoding = face_recognition.face_encodings(Ajay_Holey_image)[0]



    Chirag_Panjikar_image = face_recognition.load_image_file("Chirag Panjikar.jpg")
    Chirag_Panjikar_face_encoding = face_recognition.face_encodings(Chirag_Panjikar_image)[0]

    Huma_image = face_recognition.load_image_file("Huma.jpg")
    Huma_face_encoding = face_recognition.face_encodings(Huma_image)[0]

    Jarash_image = face_recognition.load_image_file("Jarash.jpg")
    Jarash_face_encoding = face_recognition.face_encodings(Jarash_image)[0]

    Jeyatanjan_Chithranjan_image = face_recognition.load_image_file("Jeyatanjan Chithranjan.jpg")
    Jeyatanjan_Chithranjan_face_encoding = face_recognition.face_encodings(Jeyatanjan_Chithranjan_image)[0]

    Kunal_Chavan_image = face_recognition.load_image_file("Kunal Chavan.jpg")
    Kunal_Chavan_face_encoding = face_recognition.face_encodings(Kunal_Chavan_image)[0]



    Nitin_Ambi_image = face_recognition.load_image_file("Nitin Ambi.jpg")
    Nitin_Ambi_face_encoding = face_recognition.face_encodings(Nitin_Ambi_image)[0]

    NItin_Dhane_image = face_recognition.load_image_file("NItin Dhane.jpg")
    NItin_Dhane_face_encoding = face_recognition.face_encodings(NItin_Dhane_image)[0]

    Nitin_R_Chavan_image = face_recognition.load_image_file("Nitin R Chavan.jpg")
    Nitin_R_Chavan_face_encoding = face_recognition.face_encodings(Nitin_R_Chavan_image)[0]

    Rajdatt_image = face_recognition.load_image_file("Rajdatt.jpg")
    Rajdatt_face_encoding = face_recognition.face_encodings(Rajdatt_image)[0]

    Roshni_image = face_recognition.load_image_file("Roshni.jpg")
    Roshni_face_encoding = face_recognition.face_encodings(Roshni_image)[0]

    Sagar_Gadgil_image = face_recognition.load_image_file("Sagar Gadgil.jpg")
    Sagar_Gadgil_face_encoding = face_recognition.face_encodings(Sagar_Gadgil_image)[0]

    Sanjay_Majeethia_image = face_recognition.load_image_file("Sanjay Majeethia.jpg")
    Sanjay_Majeethia_face_encoding = face_recognition.face_encodings(Sanjay_Majeethia_image)[0]

    Udayan_Joshi_image = face_recognition.load_image_file("Udayan Joshi.jpg")
    Udayan_Joshi_face_encoding = face_recognition.face_encodings(Udayan_Joshi_image)[0]

    Umakanth_Joshi_image = face_recognition.load_image_file("Umakanth Joshi.jpg")
    Umakanth_Joshi_face_encoding = face_recognition.face_encodings(Umakanth_Joshi_image)[0]

    nandakumar_image = face_recognition.load_image_file("nadakumar.jpg")
    nandakumar_face_encoding = face_recognition.face_encodings(nandakumar_image)[0]

    known_face_encodings = [
        obama_face_encoding,
        arnab_face_encoding,
        piyush_face_encoding,
        prajwal_face_encoding,
        santosh_face_encoding,
        vikas_face_encoding,
        amulya_face_encoding,
        anand_face_encoding,
        sandeep_face_encoding,
        arvind_face_encoding,
        abhishek_face_encoding,
        arun_face_encoding,
        pandey_face_encoding,
        chetan_face_encoding,
        jirav_face_encoding,
        anant_face_encoding,
        pramod_face_encoding,
        sub_face_encoding,
        chandrarao_face_encoding,
        kapil_face_encoding,
        gaurav_face_encoding,
        ashish_face_encoding,
        kunal_face_encoding,
        murtaza_face_encoding,
        ronil_face_encoding,
        jaigude_face_encoding,
        saifu_face_encoding,
        amol_face_encoding,
        manish_face_encoding,
        harshada_face_encoding,


        Ajay_Holey_face_encoding,
        Chirag_Panjikar_face_encoding,
        Huma_face_encoding,
        Jarash_face_encoding,
        Jeyatanjan_Chithranjan_face_encoding,
        Kunal_Chavan_face_encoding,
        Nitin_Ambi_face_encoding,
        NItin_Dhane_face_encoding,
        Nitin_R_Chavan_face_encoding,
        Rajdatt_face_encoding,
        Roshni_face_encoding,
        Sagar_Gadgil_face_encoding,
        Sanjay_Majeethia_face_encoding,
        Udayan_Joshi_face_encoding,
        Umakanth_Joshi_face_encoding,
        niladri_face_encoding,
        nandakumar_face_encoding


    ]




    known_face_names = [
        "Barack Obama",
        "Arnab Das",
        "Piyush Gupta",
        "Langde Prajwal",
        "Santosh Jaiswal",
        "Vikas Malviya",
        "Amulya Balusupati",
        "Anand Balagopalan",
        "Sandeep Joshi",
        "Arvind Kumar",
        "Abhishek Jaiswal",
        "Arun Narvariya",
        "Chandrakant Pandey ",
        "Chetan Ranka",
        "Fadia Jirav",
        "Anant Ingole",
        "Vijaykumar Pramod",
        "Shubhashish Sharma",
        "Anandrao Dhaygude",
        "Kapil Parish  Kumar",
        "Gaurav Kulkarni",
        "Ashish Patil",
        "Krunal K Patel",
        "Murtaza Moni Hita",
        "Ronil Mehta",
        "Jaigude Sandip",
        "Acharya Safalya Kumar",
        "Amol Shejawal",
        "Manish Shah",
        "Harshada",

        'Ajay Holey',
        'Chirag Panjikar',
        'Huma',
        'Jarash',
        'Jeyatanjan Chithranjan',
        'Kunal Chavan',
        'Nitin Ambi',
        'NItin Dhane',
        'Nitin R Chavan',
        'Rajdatt',
        'Roshni',
        'Sagar Gadgil',
        'Sanjay Majeethia',
        'Udayan Joshi',
        'Umakanth Nair',
        "Niladri",
        "V Nandakumar"

    ]

    while True:

        ret, frame = video_capture.read()


        rgb_frame = frame[:, :, ::-1]


        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"


            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]




            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)


            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            cv2.putText(frame, "WELCOME EVERYONE", (500,500), font, 1.0, (255, 255, 255), 1)

            print(name)

            """mytext = 'Welcome'+name
    
            # Language in which you want to convert
            language = 'en'
    
            # Passing the text and language to the engine,
            # here we have marked slow=False. Which tells
            # the module that the converted audio should
            # have a high speed
            myobj = gTTS(text=mytext, lang=language, slow=False)
    
            # Saving the converted audio in a mp3 file named
            # welcome
    
            myobj.save("welcome.mp3")
    
            # Playing the converted file
            os.system("welcome.mp3")"""

            #voice.start_voice(name)
            #Thread(target=voice.start_voice(name)).start()

            """now = datetime.now()

            print("now =", str(now)[17:19])
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%S")
            print("date and time =",str(now)[17:19])

            if int(str(now)[17:19])%5==0:
                Thread(target=voice.start_voice(name)).start()"""


        cv2.imshow('Video', cv2.resize(frame, (1366,768)))



        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video_capture.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    Thread(target=face_recognition_start).start()

