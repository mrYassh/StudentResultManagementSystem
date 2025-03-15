from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip inistall pillow
#import pymysql # type: ignore #pip install pymysql
import sqlite3
import os

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #======= Bg Image======

       # self.bg=ImageTk.photoImage(file="images/C:/Users/NEXTGENPC/OneDrive/Desktop")
      #  bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=0,relheight=1)

        # ======= LEFT  Image======

        #self.left= ImageTk.photoImage(file="images/ add path")
       # left= Label(self.root, image=self.left).place(x=80, y=100, width=400, relheight=500)
 
 #=========Background Color======

        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)


        #======Register frame======

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title = Label(frame1,text="REGISTER HERE",font=("time  new roman", 20, "bold"), bg="white", fg="green").place(x=50,y=30)

        #---------------Row1
        
        f_name = Label(frame1, text="FIRST NAME", font=("time  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)


        l_name = Label(frame1, text="Last NAME", font=("time  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("time new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #----------------------Row2
        contact = Label(frame1, text="Contact.No", font=("time  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email= Label(frame1, text="Email", font=("time  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)


        #------------------------Row3
        question = Label(frame1, text="Security Question ", font=("times  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=50, y=240)

        self.cmb_quest= ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("select","Your First name ","Your Birth plece","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer= Label(frame1, text="Answer", font=("times  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        #-------------------Row4

        Password= Label(frame1, text="Password", font=("times  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="confirm Password", font=("time  new roman", 15, "bold"), bg="white", fg="GRAY").place(x=370,y=310)
        self.txt_cpassword = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)


        #--------Terms and condition-------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Condition",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        #self.btn_img=ImageTk.PhotoImage(file="Register button.jpeg")
        btn_register=Button(frame1,text="Register",bg="green",font=("times new roman",12),bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420,width=250)

        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20), bd=0, cursor="hand2").place(x=720, y=640,width=180 )

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)



    def register_data(self): 
        if self.txt_fname.get()=="" or  self.txt_contact.get()==""or  self.txt_email.get()=="" or self.cmb_quest.get()=="select"or  self.txt_answer.get()==""or  self.txt_password.get()==""or  self.txt_cpassword.get()=="" :
              messagebox.showerror("Error","all fields Are required",parent=self.root)
        elif  self.txt_password.get()!=  self.txt_cpassword.get() :
            messagebox.showerror("Error", "password & confirm password shoud be same", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "please Agree our terms & condition", parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor( )
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error", "user already exist please try with anothar email", parent=self.root)
                else:
                      cur.execute("insert into employee(f_name,l_name,email,contact,question,answer,password) values(?,?,?,?,?,?,?)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_email.get(),
                             self.txt_contact.get(),
                             self.cmb_quest.get(),
                             self.txt_answer.get(),
                             self.txt_password.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("success","Register successfull", parent=self.root)
                self.clear()
                self.login_window()


            except Exception as es:
                messagebox.showerror("Error", f"Eroor due to: {str(es)}", parent=self.root)

root=Tk()
obj=register(root)
root.mainloop()

