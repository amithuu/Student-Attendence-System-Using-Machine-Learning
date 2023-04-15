from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np  # which makes convertion of array to 88% faster
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


# title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 35, "bold"), bg="white", fg="Black")
        title_lbl.place(x=0, y=0, width=1530, height=40)

    # left image
        img_left = Image.open(r"Camera Roll\first.jpeg")
        img_left = img_left.resize((765, 750), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=40, width=765, height=750)

    # right image
        img_right = Image.open(r"Camera Roll\background.jpeg")
        img_right = img_right.resize((765, 750), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=765, y=40, width=760, height=750)

        # button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=(
            "times new roman", 18, "bold"), bg="black", fg="white")
        b1_1.place(x=500, y=600, width=200, height=40)

    ########## attendence taking function ##########

    def mark_attendence(self, i, r, n, d):
        with open("amith.csv", "r+", newline="\n") as f:
            mydataList = f.readlines()
            name_list = []  # we store data in this list:
            for line in mydataList:
                entry = line.split((","))  # eg: amith,2,cs
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    ############ face recognition function  ##############

    def face_recog(self):
        def draw_boundary(img, classifier, scalerFactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scalerFactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="amithMYSQL@1999", database="facerecognizer")
                my_cursor = conn.cursor()


# to fetch data
                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute(
                    "select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    self.mark_attendence(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unkown face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while (True):
            # ret is we are returning the variable simple.
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("welcome to face recognization", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
