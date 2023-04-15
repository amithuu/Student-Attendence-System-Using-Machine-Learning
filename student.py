from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student")

    # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

    # first image
        img = Image.open(
            r"C:\Users\Amith\Desktop\Face Recog\Camera Roll\first.jpeg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
    # second image
        img1 = Image.open(
            r"C:\Users\Amith\Desktop\Face Recog\Camera Roll\second.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

    # third image
        img2 = Image.open(
            r"C:\Users\Amith\Desktop\Face Recog\Camera Roll\third.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

     # background image
        img3 = Image.open(
            r"C:\Users\Amith\Desktop\Face Recog\Camera Roll\background.jpeg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

    # text on top of background
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=40)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=15, y=50, width=1500, height=650)

    # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=720, height=630)

    # background image of left frame
        img_left = Image.open(
            r"C:\Users\Amith\Desktop\Face Recog\Camera Roll\leftframe.jpeg")
        img_left = img_left.resize((720, 710), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=130)

    # current course
        current_course = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                    text="Current Course Info", font=("times new roman", 12, "bold"))
        current_course.place(x=5, y=135, width=710, height=120)

    # dept
        dept_label = Label(current_course, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dept_label.grid(row=0, column=0, padx=10, sticky=W)

        dept_combo = ttk.Combobox(current_course, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dept_combo["values"] = ("Select Department",
                                "CS", "MECH", "ECE", "CSA")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

    # course
        course_label = Label(current_course, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"] = (
            "Select Course", "Java", "Testing", "ML", "AI")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

     # Year
        year_label = Label(current_course, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

     # Semester
        semenster_label = Label(current_course, text="Semenster", font=(
            "times new roman", 12, "bold"), bg="white")
        semenster_label.grid(row=1, column=2, padx=10, sticky=W)

        semenster_combo = ttk.Combobox(current_course, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        semenster_combo["values"] = (
            "Select Semester", "1st", "2nd", "3rd", "4th")
        semenster_combo.current(0)
        semenster_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

    # Class Student Information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=260, width=710, height=345)

    # student id label
        studentID_label = Label(class_student_frame, text="Student ID:", font=(
            "times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.va_std_id, width=17, font=(
            "times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

     # student name label
        studentname_label = Label(class_student_frame, text="Student Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        studentname_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_name, width=17, font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

    #  class division label
        classdivision_label = Label(class_student_frame, text="Class Divisinon:", font=(
            "times new roman", 12, "bold"), bg="white")
        classdivision_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), width=18, state="readonly")
        div_combo["values"] = ("Select Division", "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

    #  Roll No label
        Rollno_label = Label(class_student_frame, text="Roll No:", font=(
            "times new roman", 12, "bold"), bg="white")
        Rollno_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Rollno_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=17, font=(
            "times new roman", 12, "bold"))
        Rollno_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

    #  Gender label
        Gender_label = Label(class_student_frame, text="Gender:", font=(
            "times new roman", 12, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select Gender", "male", "female", "others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

     #   DOB label
        DOB_label = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 12, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=17, font=(
            "times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

    #  Email label
        Email_label = Label(class_student_frame, text="Email:", font=(
            "times new roman", 12, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=17, font=(
            "times new roman", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

     #   Phoneno label
        Phoneno_label = Label(class_student_frame, text="Phone No:", font=(
            "times new roman", 12, "bold"), bg="white")
        Phoneno_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        Phoneno_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=17, font=(
            "times new roman", 12, "bold"))
        Phoneno_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

       # Address label
        Address_label = Label(class_student_frame, text="Address:", font=(
            "times new roman", 12, "bold"), bg="white")
        Address_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=17, font=(
            "times new roman", 12, "bold"))
        Address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

     #  Teacher Name label
        TeacherName_label = Label(class_student_frame, text="Teacher Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        TeacherName_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)

        TeacherName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_teacher, width=17, font=("times new roman", 12, "bold"))
        TeacherName_entry.grid(row=4, column=3, padx=10, pady=10, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take a photo", value="Yes")
        Radiobutton1.grid(row=5, column=0)

        Radiobutton2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        Radiobutton2.grid(row=5, column=1)

     # Button frame
        btn_frame = LabelFrame(class_student_frame, bd=2,
                               bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=250, width=705, height=68)

    # Save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

    # Update button
        Update_btn = Button(btn_frame, text="Update", command=self.update_data, width=18, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)

     # Delete button
        Delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        Delete_btn.grid(row=0, column=2)

     # Reset button
        Reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)

    # Take photo Sample button
        takephoto_btn = Button(btn_frame, command=self.generate_dataset, text="Take Photo Sample", width=20, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        takephoto_btn.grid(row=1, column=0)

    # Update Photo Sample button
        Updatephoto_btn = Button(btn_frame, text="Update Photo Sample", width=20, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        Updatephoto_btn.grid(row=1, column=2)

    # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=630)

        img_right = Image.open(
            r"C:\Users\Amith\Desktop\Face Recog\Camera Roll\leftframe.jpeg")
        img_right = img_right.resize((720, 710), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=710, height=130)

    # Search System Frame
        Search_Frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search Student Information", font=("times new roman", 12, "bold"))
        Search_Frame.place(x=5, y=135, width=710, height=70)

    # Search label
        Search_label = Label(Search_Frame, text="Search Student", font=(
            "times new roman", 12, "bold"), bg="white")
        Search_label.grid(row=0, column=0, padx=10, sticky=W)

        Search_combo = ttk.Combobox(Search_Frame, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Search_combo["values"] = ("Select", "Register", "Name")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(
            Search_Frame, width=15, font=("times new roman", 12, "bold"))
        Search_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

    # Search button
        Search_btn = Button(Search_Frame, text="Search", width=12, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        Search_btn.grid(row=0, column=4)

     # Show All button
        ShowAll_btn = Button(Search_Frame, text="ShowALL", width=12, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        ShowAll_btn.grid(row=0, column=5, padx=7)

    # Table System Frame
        Table_Frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        Table_Frame.place(x=5, y=210, width=710, height=350)

    # Scroll bar

        scrollbar_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scrollbar_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_Frame, column=("dep", "course", "year", "sem", "id", "name", "division", "roll", "Gender",
                                          "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x.config(command=self.student_table.xview)
        scrollbar_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Sem")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("division", text="Division")
        self.student_table.heading("roll", text="Rollno")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("dob", text="Dob")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("division", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # function to add data
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are requred", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="amithMYSQL@1999", database="facerecognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.va_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "student details ahs been added", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # databse fetch
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="amithMYSQL@1999", database="facerecognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),  # changed here
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fiels are requred", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "do you want to update this details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="amithMYSQL@1999", database="facerecognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "students detals updates successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "student delete page", "do you want to delete details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="amithMYSQL@1999", database="facerecognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                messagebox.showinfo(
                    "delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


# generate photo set and take sample:

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fiels are requred", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="amithMYSQL@1999", database="facerecognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.va_std_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

            # Load predifened data on face frontacls from opencv
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # minimum Neighbour=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (600, 600))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (100, 100),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data set completed successfully")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
