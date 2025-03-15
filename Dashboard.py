from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from course import CourseClass
from student import studentclass
from result import resultClass
from tkinter import messagebox
from report import reportClass
import os
import sqlite3

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Analysis System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #  icons
       
        #  title  
        title=Label(self.root,text="Student Result Analysis System",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=80)

        #  Menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Subject",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_Student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_View=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_Logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)
        
        #  content

        #  Update_detail
        self.lbl_course=Label(self.root,text="Total Subject\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)
      
        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        #  footer  
        footer=Label(self.root,text="Student Result Analysis System\nContact Us for any Technical Issue:9888888888",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()

#==========================================================        

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()          
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Subject\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

     
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentclass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def signin(self):
        op=messagebox.askyesno("confirm","Do you really want to signin?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python signin.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
          
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to Logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()