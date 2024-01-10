from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",25,"bold"),bg="White",fg="Blue")
        title_lbl.place(x=35,y=10,width=1200,height=45)

        img_top=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\img.jpg")
        img_top=img_top.resize((1300,600),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1300,height=600)


        studentName_level=Label(f_lbl,text="gshivanshu4@gmail.com",font=("times new roman",13,"bold"),bg="White")
        studentName_level.place(x=500,y=400)




if __name__ == "__main__":
    root = Tk()
    obj=Help(root)
    root.mainloop()