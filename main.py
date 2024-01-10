from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\img.jpg")
        img=img.resize((1300,700),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=700)

        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="White",fg="Blue")
        title_lbl.place(x=35,y=30,width=1200,height=45)

        #time

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

            lbl = Label(title_lbl,font = ('times new roman',14,'bold'),background = 'white',foreground = 'blue')
            lbl.place(x=0,y=0,width=110,height=50)
            time()

        #Student button
        img4=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\student.jpg")
        img4=img4.resize((150,180),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(f_lbl,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=180)

        b1_1=Button(f_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=200,y=290,width=150,height=30)


        #detect button
        img5=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\detection.png")
        img5=img5.resize((150,180),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(f_lbl,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=150,height=180)

        b1_1=Button(f_lbl,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=450,y=290,width=150,height=30)


         #Attendence button
        img6=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\attendence.jpeg")
        img6=img6.resize((150,180),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(f_lbl,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=150,height=180)

        b1_1=Button(f_lbl,text="Attendence",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=700,y=290,width=150,height=30)


         #Help button
        img7=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\help desk.png")
        img7=img7.resize((150,180),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(f_lbl,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=950,y=100,width=150,height=180)

        b1_1=Button(f_lbl,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=950,y=290,width=150,height=30)


        #Train button
        img8=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\train face.jpeg")
        img8=img8.resize((150,180),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(f_lbl,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=350,width=150,height=180)

        b1_1=Button(f_lbl,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=200,y=540,width=150,height=30)

        #photos button
        img9=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\photos.jpeg")
        img9=img9.resize((150,180),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(f_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=350,width=150,height=180)

        b1_1=Button(f_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=450,y=540,width=150,height=30)

         #developer button
        img10=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\deveplor.jpeg")
        img10=img10.resize((150,180),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(f_lbl,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=350,width=150,height=180)

        b1_1=Button(f_lbl,text="Devloper",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=700,y=540,width=150,height=30)

        
        img11=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\exit.jpeg")
        img11=img11.resize((150,180),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(f_lbl,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=950,y=350,width=150,height=180)

        b1_1=Button(f_lbl,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="White",fg="Blue")
        b1_1.place(x=950,y=540,width=150,height=30)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        #function
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


