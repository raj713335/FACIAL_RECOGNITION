from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import home
import cv2
from threading import Thread
import pyautogui
from main import video_sync
import os
from datetime import date


global version

version='1.0.0'




# THE STARING OF PYTHON CODE
def mainx():
    regwindowx = tk.Tk()
    screen_widthx = regwindowx.winfo_screenwidth()
    # screen_heightx = regwindowx.winfo_screenheight()
    regwindowx.destroy()

    def loading():
        rootx = tk.Tk()
        rootx.iconbitmap(default='LOGO/home.ico')
        # The image must be stored to Tk or it will be garbage collected.
        rootx.image = tk.PhotoImage(file='LOGO/load.gif')
        labelx = tk.Label(rootx, image=rootx.image, bg='white')
        rootx.overrideredirect(True)
        rootx.geometry("+280+0")
        # root.lift()
        rootx.wm_attributes("-topmost", True)
        rootx.wm_attributes("-disabled", True)
        rootx.wm_attributes("-transparentcolor", "white")
        labelx.pack()
        labelx.after(500, lambda: labelx.destroy())
        rootx.after(500, lambda: rootx.destroy())  # Destroy the widget after 0.5 seconds
        labelx.mainloop()


    for i in range(0,3):
        loading()







    class Store_DATA_IN_INI():

        # OPTION SELECT POP UP CREATION

        def __init__(self, win):


            load = cv2.imread('LOGO/home_background.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(800), int(450)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=-1, y=0)

            # load = cv2.imread('LOGO/eyexa.png', 1)
            # cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            # load = Image.fromarray(cv2imagex1)
            # load = load.resize((int(150), int(80)), Image.ANTIALIAS)
            # render = ImageTk.PhotoImage(load)
            # img = tk.Label(image=render)
            # img.image = render
            # img.place(x=600, y=0)

            self.b1 = ttk.Button(win, text='ATTENDANCE', width=20, command=self.attandance)
            self.b1.place(x=80, y=50, width=200, height=50)


            self.b2 = ttk.Button(win, text='ADD IMAGES', width=20, command=self.user_video)
            self.b2.place(x=80, y=125, width=200, height=50)

            self.b3 = ttk.Button(win, text='START', width=20, command=self.store_INI)
            self.b3.place(x=80, y=200, width=200, height=50)

        def attandance(self):

            os.startfile(os.getcwd()+'/DATA/Attendence.csv')
            print("HELLO")
            # from subprocess import Popen
            # p = Popen('DATA/Attendence.csv', shell=True)



        def user_video(self):
            window.destroy()
            home.display()


        def store_INI(self):

            window.destroy()
            video_sync()




    window = Tk()
    window.iconbitmap(default='LOGO/home.ico')
    option_window = Store_DATA_IN_INI(window)
    window.config(background='white')
    window.attributes('-alpha', 0.9)
    window.title('FACIAL RECOGNITION ' + version)
    window.geometry("750x450")
    window.mainloop()






if __name__ == '__main__':
    Thread(target=mainx).start()



















