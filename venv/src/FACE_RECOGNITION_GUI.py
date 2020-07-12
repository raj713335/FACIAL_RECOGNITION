from tkinter import *
from tkinter.ttk import Combobox
import csv
import configparser
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from datetime import date, datetime
import math
from tkinter import messagebox
from threading import Thread
import time
import socket
import tkinter.ttk as ttk
from tkinter import filedialog
import subprocess
from datetime import datetime
import numpy as np
import cv2


from tkinter import Entry, Frame, Label, StringVar
from tkinter.constants import *
from tkinter import Tk
from tkinter.messagebox import showinfo


def user_add_kc():
    # CLASS FOR ADDING STATION
    class user_add_kc():

        def __init__(self, window):

            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            shop_floor_canvax = tk.Canvas(window, width=screen_width, height=screen_height, background='white')
            shop_floor_canvax.grid(row=0, column=0)
            shop_floor_canvax.create_line((screen_width // 1.5), 0, (screen_width // 1.5), 750, fill='grey', width=3)
            shop_floor_canvax.create_line(-1, 71, screen_width, 71, fill='grey', width=3)

            load = cv2.imread('title.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(645), int(66)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=1145, y=0)

            load = cv2.imread('load.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(127), int(66)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=1790, y=0)

            """
            # COMMENTED FUNCTION FOR PLAYING VIDEO
            app = tk.Frame(window, bg="white")
            app.grid()
            # Create a label in the frame
            lmain = tk.Label(app)
            lmain.grid()

            # Capture from video File
            cap = cv2.VideoCapture('John Deere.mp4')

            # function for video streaming
            def video_stream():
                if (cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_POS_FRAMES)):
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                _, frame = cap.read()
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                im5 = img.resize((int(1300), int(660)), Image.ANTIALIAS)
                imgtk = ImageTk.PhotoImage(image=im5)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                lmain.after(1, video_stream)

            lmain = tk.Label(window, font=('Arial', int(1 * 3.5), 'bold'), fg="black", bg='white',
                             anchor='center')
            lmain.place(x=0, y=70)
            video_stream()"""

            self.btn1 = ttk.Button(window, text="ADD KC", width=20)
            self.btn1.place(x=0, y=0, width=230, height=70)

            self.btn2 = ttk.Button(window, text="MODIFY KC", width=20)
            self.btn2.place(x=230, y=0, width=230, height=70)

            self.btn3 = ttk.Button(window, text="RR", width=20)
            self.btn3.place(x=460, y=0, width=230, height=70)

            self.btn4 = ttk.Button(window, text="CAPABIITY", width=20)
            self.btn4.place(x=690, y=0, width=230, height=70)

            self.btn5 = ttk.Button(window, text="MEDICOES", width=20)
            self.btn5.place(x=920, y=0, width=230, height=70)





            def video_stream():

                def nothing(x):
                    pass

                #cv2.namedWindow("Tracking")
                cap = cv2.VideoCapture(0)

                """cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
                cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
                cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)

                cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
                cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
                cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)"""

                while True:
                    if (cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_POS_FRAMES)):
                        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        _, frame = cap.read()
                        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                        img = Image.fromarray(cv2image)
                        im5 = img.resize((int(1300), int(660)), Image.ANTIALIAS)
                        imgtk = ImageTk.PhotoImage(image=im5)
                        lmain.imgtk = imgtk
                        lmain.configure(image=imgtk)
                        lmain.after(1, video_stream)

            lmain = tk.Label(window, font=('Arial', int(1 * 3.5), 'bold'), fg="black", bg='white',
                             anchor='center')
            lmain.place(x=0, y=70)
            video_stream()

            """while True:
                _, frame = cap.read()
                # frame=cv2.imread('ball.jpg')

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                l_h = cv2.getTrackbarPos("LH", "Tracking")
                l_s = cv2.getTrackbarPos("LS", "Tracking")
                l_v = cv2.getTrackbarPos("LV", "Tracking")

                u_h = cv2.getTrackbarPos("UH", "Tracking")
                u_s = cv2.getTrackbarPos("US", "Tracking")
                u_v = cv2.getTrackbarPos("UV", "Tracking")

                l_b = np.array([l_h, l_s, l_v])
                u_b = np.array([u_h, u_s, u_v])

                mask = cv2.inRange(hsv, l_b, u_b)
                res = cv2.bitwise_and(frame, frame, mask=mask)

                # cv2.imshow('frame',frame)
                # cv2.imshow('mask',mask)
                cv2.imshow('res', res)

                key = cv2.waitKey(1)

                if key == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()"""

    user_add = tk.Tk()
    # user_add.overrideredirect(True)
    # user_add.geometry("{0}x{1}+0+0".format(user_add.winfo_screenwidth(), user_add.winfo_screenheight()))
    user_login_window = user_add_kc(user_add)
    user_add.config(background='white')
    user_add.attributes('-alpha', 1)
    user_add.iconbitmap(default='favicon.ico')
    user_add.title('ADD STATIONS')
    user_add.geometry("1920x1080")
    user_add.mainloop()




if __name__=="__main__":
    user_add_kc()

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
        "Dhaygude Anandrao",
        "Parish Kapil Kumar",
        "Kulkarni Gaurav",
        "Ashish Patil"
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
        'Umakanth Joshi'

    ]



























