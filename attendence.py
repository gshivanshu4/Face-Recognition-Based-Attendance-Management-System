from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x790+0+0")
        self.root.title("Face Recognition System")

        #variables

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()


        img=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\student portal.jpg")
        img=img.resize((1300,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=130)

        title_lbl=Label(f_lbl,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="White",fg="Blue")
        title_lbl.place(x=35,y=70,width=1200,height=45)

        main_frame=Frame(self.root)
        main_frame.place(x=0,y=155,width=1300,height=700)

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendence Details",font=("times new roman",10,"bold"))
        left_frame.place(x=2,y=0,width=630,height=470)

        img_right=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\learn.jpeg")
        img_right=img_right.resize((600,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(left_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=620,height=130)

       

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=8,y=135,width=610,height=300)

        #label and entry
        #attendence
        attendanceId_level=Label(left_inside_frame,text="StudentId:",font=("times new roman",13,"bold"),bg="White")
        attendanceId_level.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=16,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #roll
        rollLabel=Label(left_inside_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="White")
        rollLabel.grid(row=0,column=2,padx=10,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=14,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=8,sticky=W)


        namelevel=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="White")
        namelevel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=16,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="White")
        depLabel.grid(row=1,column=2,padx=10,pady=8,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=14,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=8,sticky=W)


        timelevel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="White")
        timelevel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=16,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="White")
        dateLabel.grid(row=2,column=2,padx=10,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=14,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=8,sticky=W)


        attendence_level=Label(left_inside_frame,text="Attendence Status",font=("times new roman",13,"bold"),bg="White")
        attendence_level.grid(row=3,column=0,padx=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendence,width=13,font="comicsansns 13 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=10,sticky=W)


                #button frame

        btn_frame=Frame(left_inside_frame,bd=3,relief=RIDGE,bg="White")
        btn_frame.place(x=4,y=200,width=583,height=38)


        save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=13,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=13,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=14,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        reset_btn.grid(row=0,column=3)


        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",10,"bold"))
        Right_frame.place(x=640,y=0,width=630,height=470)

        table_frame=Frame(Right_frame,bd=3,relief=RIDGE,bg="White")
        table_frame.place(x=5,y=5,width=615,height=420)

        #scroll bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,column=("id","roll No","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)
        self.AttendaceReportTable.heading("id",text="Attendence ID")
        self.AttendaceReportTable.heading("roll No",text="Roll No")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendance",text="Attendance")

        self.AttendaceReportTable["show"]="headings"
        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("roll No",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("attendance",width=100)

        self.AttendaceReportTable.pack(fill=BOTH,expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #fetch data

    def fetchdata(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data Export","your data exported to"+os.path.basename(fln)+"successfully")
        
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")













       






if __name__ == "__main__":
    root = Tk()
    obj=Attendance(root)
    root.mainloop()