from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from student import Student
from attendence import Attendence
from train import Train
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime
import os
from face_recognition import Face_Recognition


class Face_Recognitation_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE_RECOGNITION ATTENDENCE SYSTEM")

    # first image
        img = Image.open(r"Camera Roll\first.jpeg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
    # second image
        img1 = Image.open(r"Camera Roll\second.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

    # third image
        img2 = Image.open(r"Camera Roll\third.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

     # background image
        img3 = Image.open(r"Camera Roll\background.jpeg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

    # text on top of background
        title_lbl = Label(bg_img, text=" ATTENDANCE MANAGEMENT USING FACE RECOGNITION", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=40)

    # Time on title label
        def time():
            string = strftime('%H:%M:%S%p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=(
            "times new roman", 14, "bold"), bg="white", fg="Black")
        lbl.place(x=0, y=0, width=95, height=30)
        time()

    # student details button
        img4 = Image.open(r"Camera Roll\student.jpeg")
        img4 = img4.resize((200, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=250, y=100, width=150, height=150)

        b1 = Button(bg_img, text="Student details", command=self.student_details,
                    cursor="hand2", font=("times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=250, y=250, width=150, height=30)

    # detect face button
        img5 = Image.open(r"Camera Roll\detectface.jpeg")
        img5 = img5.resize((200, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b1.place(x=450, y=100, width=150, height=150)

        b1 = Button(bg_img, text="Detect Face", cursor="hand2", command=self.face_data, font=(
            "times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=450, y=250, width=150, height=30)

    #  Attendence button
        img6 = Image.open(r"Camera Roll\attendence.jpeg")
        img6 = img6.resize((200, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    cursor="hand2", command=self.attendence_data)
        b1.place(x=650, y=100, width=150, height=150)

        b1 = Button(bg_img, text="Attendence", cursor="hand2", command=self.attendence_data, font=(
            "times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=650, y=250, width=150, height=30)

    #  Help Desk button
        img7 = Image.open(r"Camera Roll\helpdesk.png")
        img7 = img7.resize((200, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,
                    cursor="hand2", command=self.Help_data)
        b1.place(x=850, y=100, width=150, height=150)

        b1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.Help_data, font=(
            "times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=850, y=250, width=150, height=30)

    # Train  Model button
        img8 = Image.open(r"Camera Roll\trainmodel.jpeg")
        img8 = img8.resize((200, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b1.place(x=250, y=350, width=150, height=150)

        b1 = Button(bg_img, text="Train Model", cursor="hand2", command=self.train_data, font=(
            "times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=250, y=500, width=150, height=30)

     # Photo Face button
        img9 = Image.open(r"Camera Roll\photoface.jpeg")
        img9 = img9.resize((200, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img)
        b1.place(x=450, y=350, width=150, height=150)

        b1 = Button(bg_img, text="Photo Face", command=self.open_img, cursor="hand2", font=(
            "times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=450, y=500, width=150, height=30)

     # Developer Contact buttons
        img10 = Image.open(r"Camera Roll\developer.jpeg")
        img10 = img10.resize((200, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,
                    cursor="hand2", command=self.Developer_data)
        b1.place(x=650, y=350, width=150, height=150)

        b1 = Button(bg_img, text="Developer Contact", cursor="hand2", command=self.Developer_data, font=(
            "times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=650, y=500, width=150, height=30)

    # Exit button
        img11 = Image.open(r"Camera Roll\exit.jpeg")
        img11 = img11.resize((200, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,
                    cursor="hand2", command=self.iExit)
        b1.place(x=850, y=350, width=150, height=150)

        b1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=(
            "times new roman", 10, "bold"), bg="black", fg="orange")
        b1.place(x=850, y=500, width=150, height=30)

    # photos module

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "face recognition", "are you sure to exit", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

       ################# function buttons ##############
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def Developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def Help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognitation_System(root)
    root.mainloop()
