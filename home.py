from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import cv2
import pyautogui
import FACIAL_RECOGNITION
import os
from tkinter import messagebox



global version

version='1.0.0'



def display():

    class INIX():


        def __init__(self, win):

            screen_widthx = win.winfo_screenwidth()

            screen_heightx = win.winfo_screenheight()




            load = cv2.imread('LOGO/background.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(screen_widthx), int(screen_heightx)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=-1, y=0)

            # load = cv2.imread('LOGO/eyexa.png', 1)
            # cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            # load = Image.fromarray(cv2imagex1)
            # load = load.resize((int(100), int(50)), Image.ANTIALIAS)
            # render = ImageTk.PhotoImage(load)
            # img = tk.Label(image=render)
            # img.image = render
            # img.place(x=-1, y=0)






            cap = cv2.VideoCapture(0)

            def video_stream():
                if (cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_POS_FRAMES)):
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                _, frame = cap.read()
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                im5 = img.resize((int(screen_widthx)-100, int(screen_heightx)-100), Image.ANTIALIAS)
                imgtk = ImageTk.PhotoImage(image=im5)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                lmain.after(1, video_stream)

            lmain = tk.Label(win, font=('Arial', int(15 * 3.5), 'bold'), fg="black", bg='white',anchor='center')
            lmain.place(x=50, y=50)
            video_stream()


            def start_recording():
                pyautogui.screenshot('IMAGES/demo.jpeg',region=(50, 50, (int(screen_widthx)-100), int((screen_heightx)-100)))
                print("DONE SUCCESFULLY")

                class INIXX():

                    def __init__(self, win):
                        self.name = ttk.Entry(win, text="name", font=("Ariel", 15), width=20)
                        self.name.place(x=20, y=10)

                        self.b22 = ttk.Button(win, text='SAVE', width=20, command=self.save)
                        self.b22.place(x=20, y=55, width=100, height=30)

                        self.b33 = ttk.Button(win, text='CANCEL', width=20, command=self.cancel)
                        self.b33.place(x=145, y=55, width=100, height=30)

                    def save(self):

                        namex=str(self.name.get())
                        messagebox.showinfo("SAVED", "Saved Succesfully")
                        os.rename('IMAGES/demo.jpeg', 'IMAGES/'+namex+'.jpeg')
                        window0.destroy()

                    def cancel(self):
                        os.remove('IMAGES/demo.jpeg')
                        window0.destroy()

                window0 = Tk()
                window0.iconbitmap(default='LOGO/home.ico')
                option_window = INIXX(window0)
                # window0.attributes('-fullscreen', TRUE)
                window0.config(background='white')
                window0.attributes('-alpha', 0.9)
                window0.title('ENTER NAME')
                window0.geometry("265x100")
                window0.mainloop()










            def stop_recording():

                cap.release()
                window1.destroy()
                FACIAL_RECOGNITION.mainx()





            style = Style()
            style.configure('TButton', font=
            ('calibri', 20, 'bold'),
                            borderwidth='4')

            # Changes will be reflected
            # by the movement of mouse.
            style.map('TButton', foreground=[('active', '!disabled', 'green')],
                      background=[('active', 'black')])

            self.b3 = ttk.Button(win, width=20, command=start_recording)
            self.b3.place(x=1320, y=51, width=45, height=50)

            self.b4 = ttk.Button(win, width=20, command=stop_recording)
            self.b4.place(x=2, y=51, width=48, height=50)














    window1 = Tk()
    window1.iconbitmap(default='LOGO/home.ico')
    option_window = INIX(window1)
    window1.attributes('-fullscreen',TRUE)
    window1.config(background='white')
    window1.attributes('-alpha', 1)
    window1.title('FACIAL RECOGNITION ' + version)
    window1.mainloop()


# display()
