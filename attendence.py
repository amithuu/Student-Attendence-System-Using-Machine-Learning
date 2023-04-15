from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

    # variables:
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendence = StringVar()

    # left image
        img_left = Image.open(r"Camera Roll\student1.jpeg")
        img_left = img_left.resize((800, 200), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=750, height=200)

    # right image
        img_right = Image.open(r"Camera Roll\student2.jpeg")
        img_right = img_right.resize((800, 200), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=750, y=0, width=750, height=200)

    # bg_image
        img3 = Image.open(
            r"Camera Roll\background.jpeg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=700)

        # title
        title_lbl = Label(bg_img, text="ATTENDENCE MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=40)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

    # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Attendence Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=0, y=0, width=740, height=550)

    # left frame background image
        img_left = Image.open(
            r"Camera Roll\leftframe.jpeg")
        img_left = img_left.resize((200, 210), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=735, height=100)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=105, width=730, height=300)

        # label and entry
    # Attendence id
        AttendenceID = Label(left_inside_frame, text="Attendence ID:", font=(
            "times new roman", 12, "bold"), bg="white")
        AttendenceID.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        AttendenceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=17, font=(
            "times new roman", 12, "bold"))
        AttendenceID_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    # roll:no
        Roll_no = Label(left_inside_frame, text="Roll:", font=(
            "times new roman", 12, "bold"), bg="white")
        Roll_no.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        Roll_no_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll, width=17, font=(
            "times new roman", 12, "bold"))
        Roll_no_entry.grid(row=0, column=4, padx=10, pady=10, sticky=W)

    # Name
        Name = Label(left_inside_frame, text="Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        Name.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        Name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=17, font=(
            "times new roman", 12, "bold"))
        Name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    # Department
        Department = Label(left_inside_frame, text="Department:", font=(
            "times new roman", 12, "bold"), bg="white")
        Department.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        Department_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep, width=17, font=(
            "times new roman", 12, "bold"))
        Department_entry.grid(row=1, column=4, padx=10, pady=10, sticky=W)

    # Time
        Time = Label(left_inside_frame, text="Time:", font=(
            "times new roman", 12, "bold"), bg="white")
        Time.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        Time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=17, font=(
            "times new roman", 12, "bold"))
        Time_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    # Date
        Date = Label(left_inside_frame, text="Date:", font=(
            "times new roman", 12, "bold"), bg="white")
        Date.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        Date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date, width=17, font=(
            "times new roman", 12, "bold"))
        Date_entry.grid(row=2, column=4, padx=10, pady=10, sticky=W)

    # Attendence status
        Attendence_status = Label(left_inside_frame, text="Attendence status:", font=(
            "times new roman", 12, "bold"), bg="white")
        Attendence_status.grid(row=3, column=1, padx=10, sticky=W)

        Attendence_status_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendence, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Attendence_status_combo["values"] = (
            "Status", "Present", "Absent")
        Attendence_status_combo.current(0)
        Attendence_status_combo.grid(
            row=3, column=2, padx=2, pady=10, sticky=W)

    # Buttons
        btn_frame = LabelFrame(left_inside_frame, bd=2,
                               bg="white", relief=RIDGE)
        btn_frame.place(x=2, y=253, width=720, height=38)

    # import csv button
        import_btn = Button(btn_frame, text="import csv", command=self.importCSV, width=27, font=(
            "times new roman", 12, "bold"), bg="black", fg="white")
        import_btn.grid(row=0, column=1)

    # export csv button
        export_btn = Button(btn_frame, text="export csv", command=self.exportCSV, width=27, font=(
            "times new roman", 12, "bold"), bg="black", fg="white")
        export_btn.grid(row=0, column=2)

    # Update button
        """Update_btn = Button(btn_frame, text="Update", width=19, font=(
            "times new roman", 12, "bold"), bg="black", fg="white")
        Update_btn.grid(row=0, column=3)"""

    # Reset button
        Reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=27, font=(
            "times new roman", 12, "bold"), bg="black", fg="white")
        Reset_btn.grid(row=0, column=4)

    # right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendence Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=0, width=740, height=550)

        right_inside_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        right_inside_frame.place(x=3, y=5, width=730, height=500)

    ####### scroll bar table#########

        scrollbar_x = ttk.Scrollbar(right_inside_frame, orient=HORIZONTAL)
        scrollbar_y = ttk.Scrollbar(right_inside_frame, orient=VERTICAL)

        self.AttendenceReportTable = ttk.Treeview(right_inside_frame, column=(
            "id", "roll", "name", "department", "time", "date", "attendence status"), xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x.config(command=self.AttendenceReportTable.xview)
        scrollbar_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id", text="Attendence ID")
        self.AttendenceReportTable.heading("roll", text="Roll")
        self.AttendenceReportTable.heading("name", text="Name")
        self.AttendenceReportTable.heading("department", text="Department")
        self.AttendenceReportTable.heading("time", text="Time")
        self.AttendenceReportTable.heading("date", text="Date")
        self.AttendenceReportTable.heading(
            "attendence status", text="Attendence Status")

        # to remove space from table at start
        self.AttendenceReportTable["show"] = "headings"

        self.AttendenceReportTable.column("id", width=100)
        self.AttendenceReportTable.column("roll", width=100)
        self.AttendenceReportTable.column("name", width=100)
        self.AttendenceReportTable.column("department", width=100)
        self.AttendenceReportTable.column("time", width=100)
        self.AttendenceReportTable.column("date", width=100)
        self.AttendenceReportTable.column("attendence status", width=120)

        self.AttendenceReportTable.pack(fill=BOTH, expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>", self.get_cursor)

    ######## fetch data#######
    def fetchData(self, rows):
        self.AttendenceReportTable.delete(
            *self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("", END, values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    ### export csv###
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data To Show", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    # a function which appends the data form file.
                    exp_write.writerow(i)
                messagebox.showinfo("Data Success", "Data Successfuly Exported To:" +
                                    os.path.basename(fln) + "", parent=self.root)

        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to:{str(es)}", parent=self.root)

    # function to diplay detials in student details frame :
    # there no value for event just we need to pass some argumnet so we are passing
    def get_cursor(self, event=""):
        cursor_row = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])

    # Reset function
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")


# REMOVE UPDATE FUNCTION######## BUTTON
if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
