from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        title_lbl = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        img_top = Image.open(r"Camera Roll\developer2.jpeg")
        img_top = img_top.resize((1530, 750), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=750)

        #frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1050, y=430, width=420, height=200)

        img_top1 = Image.open(r"Camera Roll\developer1.jpeg")
        img_top1 = img_top1.resize((100, 100), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=0, y=0, width=200, height=200)

        #label
        dev_label = Label(main_frame, text="Amith Kulkarni", font=(
            "times new roman", 20, "bold"), bg="white")
        dev_label.place(x=210,y=10)

        dev1_label = Label(main_frame, text="Ankitha Naik", font=(
            "times new roman", 20, "bold"), bg="white")
        dev1_label.place(x=210,y=50)

        dev2_label = Label(main_frame, text=" Contact Us For more projects", font=(
            "times new roman", 10, "bold"), bg="white")
        dev2_label.place(x=210,y=100)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
