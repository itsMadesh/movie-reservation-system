from seats_display import seats_selection
import cx_Oracle
from tkinter import *
class register:
    def __init__(self):
        try:
            self.loggedInUser=None
            self.root = Tk()
            self.root.title('PythonGuides')
            self.root.config(bg='lightblue')
            self.con = cx_Oracle.connect('scott/orcl@//localhost:1521/orcl')
            self.cursor=self.con.cursor()                
            self.right_frame = Frame(self.root, bd=2, bg='#CCCCCC',relief=SOLID, padx=10, pady=10)

            Label(self.right_frame, text="Username(Unique)", bg='#CCCCCC').grid(row=0, column=0, sticky=W, pady=10)
            Label(self.right_frame, text="Enter Name", bg='#CCCCCC').grid(row=1, column=0, sticky=W, pady=10)
            Label( self.right_frame, text="Enter Email", bg='#CCCCCC').grid(row=2, column=0, sticky=W, pady=10)
            Label(self.right_frame, text="Contact Number", bg='#CCCCCC').grid(row=3, column=0, sticky=W, pady=10)
            Label(self.right_frame, text="Enter Password", bg='#CCCCCC').grid(row=4, column=0, sticky=W, pady=10)
            self.register_uname=Entry(self.right_frame)
            self.register_name = Entry(self.right_frame)
            self.register_email = Entry(self.right_frame)
            self.register_mobile = Entry(self.right_frame)
            self.register_pwd = Entry(self.right_frame, show='*')
            self.register_btn = Button(self.right_frame, width=15, text='Register',  relief=SOLID,cursor='hand2',command=self.insert)

            self.register_uname.grid(row=0, column=1, pady=10, padx=20)
            self.register_name.grid(row=1, column=1, pady=10, padx=20)
            self.register_email.grid(row=2, column=1, pady=10, padx=20) 
            self.register_mobile.grid(row=3, column=1, pady=10, padx=20)
            self.register_pwd.grid(row=4, column=1, pady=10, padx=20)
            self.register_btn.grid(row=5, column=1, pady=10, padx=20)
            self.right_frame.pack(padx=100,pady=100)

            self.root.mainloop()
        except cx_Oracle.DatabaseError as e:
            print("Problem connecting to Oracle", e)
            # Close the all database operation
        finally:
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()
    def reg_success(self):
        obj=seats_selection(self.loggedInUser)
    def incorrect_user(self):
        Error=Label(self.root,text="Invalid Username/password!",fg="white",bg="darkblue",font=16)
        Error.pack()
    def insert(self):
        self.logInUser=self.register_uname.get()
        uname=self.register_uname.get()
        name=self.register_name.get()
        pwd=self.register_pwd.get()
        phoneno=self.register_mobile.get()
        emailid=self.register_email.get()
        self.cursor.execute(f"insert into customer values(:name,:c_id,:pwd,:phoneno,:emailid)",{'name':name,'c_id':uname,'pwd':pwd,'phoneno':phoneno,'emailid':emailid})
        self.con.commit()
        self.cursor.execute(f'select * from customer where c_id=:uname and c_password=:pwd',{'uname':uname,'pwd':pwd})
        self.con.commit()
        record =self.cursor.fetchall()
        print(record)
        if record:
            self.reg_success()
        else:
            self.incorrect_user()
