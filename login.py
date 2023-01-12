from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3 , os,email_pass,time
import smtplib
class Login_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x712+0+0")
        self.root.title("Inventory Management System|Login")
        self.root.config(bg="#fafafa")
        
        #========Images====================
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0)
        self.lbl_phone_image.place(x=200,y=50)
        
        self.otp=''
        #============Login Frame =============
        self.employee_id=StringVar()
        self.password=StringVar()
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#fafafa")
        login_frame.place(x=650,y=90,width=350,height=460)
        
        title=Label(login_frame,text="Login",font=("Kalam",35,"bold"),bg="#fafafa").place(x=0,y=30,relwidth=1)
        
        
        lbl_user=Label(login_frame,text="Employee ID",font=("Nunito",15,"bold"),bg="#fafafa",fg="#767171").place(x=40,y=120)
        txt_employee_id=Entry(login_frame,font=("times new roman",15),textvariable=self.employee_id,bg="#ECECEC").place(x=40,y=160,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Nunito",15,"bold"),bg="#fafafa",fg="#767171").place(x=40,y=210)
        txt_pass=Entry(login_frame,font=("times new roman",15),show="*",textvariable=self.password,bg="#ECECEC").place(x=40,y=250,width=250)
        
        btn_login=Button(login_frame,text="Login Now",command=self.login,font=("Nunito",15,"bold"),activebackground="#00B0F0",bg="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=40,y=300,width=250,height=40)
        
        hr=Label(login_frame,text="",bg="lightgray").place(x=40,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="#fafafa",fg="lightgray",font=("Nunito",15,"bold")).place(x=150,y=353)
        
        btn_forget_pass=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("Nunito",11,"bold"),bg="#fafafa",fg="#00759E",bd=0,activebackground="#fafafa",activeforeground="#00759E").place(x=100,y=390)
        
        #===========Animation Images=========================
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")
        
        self.lbl_change_img=Label(self.root,bg="white")
        self.lbl_change_img.place(x=367,y=153,width=240,height=428)
        self.animate()
        
# =========================All Functions========================
    def login(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required!",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? and pass=?",(self.employee_id.get(),self.password.get(),))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Employee ID or Password!",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_img.config(image=self.im)
        self.lbl_change_img.after(3000,self.animate)
        
    def forget_window(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must me required!",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID, try again!",parent=self.root)
                else:
                    # ==============Forget Window============
                    # call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error, Try again",parent=self.root)
                    else:
                        self.var_otp=StringVar()
                        self.var_new_pass=StringVar()
                        self.var_conf_pass=StringVar()
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("Reset Password")
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win, text='Reset Password',font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white').pack(side=TOP,fill=X)
                        
                        
                        lbl_reset=Label(self.forget_win, text='Enter OTP send on Register Email',font=("times new roman",15)).place(x=20,y=60)
                        text_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        
                        lbl_newpass=Label(self.forget_win, text='New Password',font=("times new roman",15)).place(x=20,y=160)
                        text_newpass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                        
                        lbl_confpass=Label(self.forget_win, text='confirm Password',font=("times new roman",15)).place(x=20,y=225)
                        text_confpass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=250,width=250,height=30)
                        
                        self.update=Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=("times new roman",15),bg="lightblue")
                        self.update.place(x=150,y=300,width=100,height=30)
                        
                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp_functon,font=("times new roman",15),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def update_password(self):
        if self.var_new_pass.get()==""or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is required", self.forget_win)
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Error","New Password and Confirm Password should be same", self.forget_win)
        else:
            con=sqlite3.connect(database=r'BMS.db')
            cur=con.cursor()
            try:
                cur.execute("update employee set pass=? where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated successfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.forget_win)
            
    def validate_otp_functon(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP, Try Again",parent=self.forget_win)
    def send_email(self,to_):
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        email_=email_pass.email
        pass_=email_pass.pass_
        s.login(email_,pass_)
        self.otp=int(time.strftime("%S%M%H"))+int(time.strftime("%S"))
        subj='IMS- Reset Password OTP'
        msg=f'Dear sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'
        
root=Tk()
obj=Login_system(root)
root.mainloop()