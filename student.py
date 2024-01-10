from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x790+0+0")
        self.root.title("Face Recognition System")


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semister=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        



        img=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\student portal.jpg")
        img=img.resize((1300,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=130)

         

        title_lbl=Label(f_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="White",fg="Blue")
        title_lbl.place(x=35,y=70,width=1200,height=45)

        main_frame=Frame(self.root)
        main_frame.place(x=10,y=125,width=1500,height=500)


        #left side level
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",10,"bold"))
        left_frame.place(x=2,y=0,width=630,height=500)

         #current course
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"))
        current_course_frame.place(x=2,y=0,width=610,height=150)
         #Department
        dep_level=Label(current_course_frame,text="department",font=("times new roman",13,"bold"),bg="White")
        dep_level.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_level=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="White")
        course_level.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","CSE","IOT","AIML","DS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_level=Label(current_course_frame,text="year",font=("times new roman",13,"bold"),bg="White")
        year_level.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #Semister
        semister_level=Label(current_course_frame,text="semister",font=("times new roman",13,"bold"),bg="White")
        semister_level.grid(row=1,column=2,padx=10,sticky=W)

        semister_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semister,font=("times new roman",13,"bold"),width=17,state="readonly")
        semister_combo["values"]=("Select semister","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semister_combo.current(0)
        semister_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

         #class student information
        class_Student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"))
        class_Student_frame.place(x=2,y=160,width=610,height=300)

         #student id
        studentId_level=Label(class_Student_frame,text="StudentId:",font=("times new roman",13,"bold"),bg="White")
        studentId_level.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=16,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        studentName_level=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="White")
        studentName_level.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=14,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class Division
        class_div_level=Label(class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="White")
        class_div_level.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=16,font=("times new roman",13,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=12,state="readonly")
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=9,pady=10,sticky=W)

        #Roll no

        roll_level=Label(class_Student_frame,text="Roll no:",font=("times new roman",13,"bold"),bg="White")
        roll_level.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=14,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #gender
        gender_level=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="White")
        gender_level.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=16,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=12,state="readonly")
        gender_combo["values"]=("Male","Female","others")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #dob number
        dob_level=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="White")
        dob_level.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=14,font=("times new roman",13,"bold"))
        dob_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #email
        email_level=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="White")
        email_level.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=16,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #phone number
        phone_level=Label(class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="White")
        phone_level.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=14,font=("times new roman",13,"bold"))
        phone_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_level=Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"),bg="White")
        address_level.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=16,font=("times new roman",13,"bold"))
        address_entry.grid(row=5,column=1,padx=9,pady=5,sticky=W)

        #teacher name
        teacher_level=Label(class_Student_frame,text="Teacher name:",font=("times new roman",13,"bold"),bg="White")
        teacher_level.grid(row=5,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=14,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=5,column=3,padx=10,pady=5,sticky=W)

        
        
       

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobtn1.grid(row=8,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=8,column=1)

        #button frame

        btn_frame=Frame(class_Student_frame,bd=3,relief=RIDGE,bg="White")
        btn_frame.place(x=4,y=200,width=583,height=38)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        reset_btn.grid(row=0,column=3)
         
        #button frame
        btn_frame1=Frame(class_Student_frame,bd=3,relief=RIDGE,bg="White")
        btn_frame1.place(x=4,y=236,width=583,height=38)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=27,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=29,font=("times new roman",13,"bold"),bg="Blue",fg="White")
        update_photo_btn.grid(row=1,column=1)


         #right side level
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",10,"bold"))
        Right_frame.place(x=640,y=0,width=610,height=500)

        img_right=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\learn.jpeg")
        img_right=img_right.resize((600,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=600,height=130)

        #search system

        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",10,"bold"))
        Search_frame.place(x=2,y=135,width=600,height=70)

        search_level=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),fg="Blue")
        search_level.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=10,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(Search_frame,text="Search",width=8,font=("times new roman",13,"bold"),bg="White",fg="Blue")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="ShowAll",width=8,font=("times new roman",13,"bold"),bg="White",fg="Blue")
        showAll_btn.grid(row=0,column=4)
         #table frame
         
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="White")
        table_frame.place(x=2,y=210,width=600,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll_no","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll_no",text="Roll_no")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@#080802",database="facerecognitionsystem")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semister.get(),
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
                messagebox.showinfo("Success","Student detail has been added successfully",parent=self.root)                                                                                                        
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@#080802",database="facerecognitionsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semister.set(data[3]),
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

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
          messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@#080802",database="facerecognitionsystem")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semister=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semister.get(),
                                                                                                                                                                                    #self.va_std_id.get(),
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
                        
                messagebox.showinfo("Success","Student detail successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                                                                                               
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@#080802",database="facerecognitionsystem")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semister.set("select Semister")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


#====Generate data set take photo sample
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@#080802",database="facerecognitionsystem")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semister=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semister.get(),
                                                                                                                                                                                    #self.va_std_id.get(),
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
                                                                                                                                                                                    self.va_std_id.get()==id+1
                                                                                                                                                                      ))     
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===load predefined data on face frontal from opencv====

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","generating data set completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()
