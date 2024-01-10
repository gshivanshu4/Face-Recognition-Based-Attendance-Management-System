from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="White",fg="Blue")
        title_lbl.place(x=35,y=10,width=1200,height=45)

        img_top=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\face.jpeg")
        img_top=img_top.resize((650,200),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=60,width=650,height=200)

        img_top1=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\face2.jpeg")
        img_top1=img_top1.resize((650,200),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=651,y=60,width=650,height=200)

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="Blue",fg="White")
        b1_1.place(x=35,y=270,width=1200,height=50)



        img_bottom=Image.open(r"c:\Users\gshiv\OneDrive\Desktop\face recognition\peoples.jpeg")
        img_bottom=img_bottom.resize((1300,310),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=330,width=1300,height=310)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!")





if __name__ == "__main__":
    root = Tk()
    obj=Train(root)
    root.mainloop()
