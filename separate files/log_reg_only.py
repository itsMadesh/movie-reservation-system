import cx_Oracle
from tkinter import *
# con = cx_Oracle.connect('system/2002@//localhost:1522/oracle')
log_frame=None
register_frame=None
log_name=None
log_pwd=None
error=None
register_uname=None
register_uname=None
register_name=None
register_pwd=None
register_mobile=None
register_email=None

loggedInUser = None
def registerpage():
    log_frame.pack_forget()
    register(root,cursor,con)
    register_frame.tkraise()
# def login_success(self):
#     Theater_selection()
def incorrect_user():
    print("maddy")
    global error
    error.destroy()
    error=Label(root,text="Invalid Username/password!",fg="white",bg="darkblue",font=16)
    error.pack()
def verify():
    uname=log_name.get()
    pwd=log_pwd.get()
    cursor.execute(f'select * from customer where c_id=:uname and c_password=:pwd',{'uname':uname,'pwd':pwd})
    record =cursor.fetchall()
    print(record)
    if record:
        global loggedInUser
        loggedInUser= uname
        # login_success()
    else:
        incorrect_user()
    con.commit()
def login(root,cursor,con):
    global log_frame,log_name,log_pwd 
    log_frame = Frame(root, bd=2, bg='#CCCCCC',relief=SOLID, padx=10, pady=10)
    Label(log_frame, text="Enter Username", bg='#CCCCCC').grid(row=0, column=0, sticky=W, pady=10)
    Label(log_frame, text="Enter Password", bg='#CCCCCC').grid(row=1, column=0, sticky=W, pady=10)
    Label(log_frame, text="Not registered yet?", bg='#CCCCCC').grid(row=3, column=0, sticky=W, pady=10)
    log_name= Entry(log_frame)
    log_pwd = Entry(log_frame, show='*')
    log_btn = Button(log_frame, width=15, text='LOG-IN',relief=SOLID,cursor='hand2',command=verify)
    create = Button(log_frame, width=15, text='Create an account',activebackground="Darkblue",activeforeground="White",command=registerpage)

    log_name.grid(row=0, column=1, pady=10, padx=20)
    log_pwd.grid(row=1, column=1, pady=10, padx=20)
    log_btn.grid(row=2, column=1, pady=10, padx=20)
    create.grid(row=3, column=1, pady=10, padx=20)
    log_frame.pack(padx=100,pady=100)
def insert():
    global loggedInUser
    loggedInUser=register_uname.get()
    uname=register_uname.get()
    name=register_name.get()
    pwd=register_pwd.get()
    phoneno=register_mobile.get()
    emailid=register_email.get()
    cursor.execute(f"insert into customer values(:name,:c_id,:pwd,:phoneno,:emailid)",{'name':name,'c_id':uname,'pwd':pwd,'phoneno':phoneno,'emailid':emailid})
    con.commit()
    cursor.execute(f'select * from customer where c_id=:uname and c_password=:pwd',{'uname':uname,'pwd':pwd})
    con.commit()
    record =cursor.fetchall()
    print(record)
    if record:
        pass
        # login_success()
    else:
        incorrect_user()
def register(root,cursor,con):
    global register_uname,register_uname,register_name,register_pwd,register_mobile,register_email
    register_frame = Frame(root, bd=2, bg='#CCCCCC',relief=SOLID, padx=10, pady=10)
    Label(register_frame, text="Username(Unique)", bg='#CCCCCC').grid(row=0, column=0, sticky=W, pady=10)
    Label(register_frame, text="Enter Name", bg='#CCCCCC').grid(row=1, column=0, sticky=W, pady=10)
    Label(register_frame, text="Enter Email", bg='#CCCCCC').grid(row=2, column=0, sticky=W, pady=10)
    Label(register_frame, text="Contact Number", bg='#CCCCCC').grid(row=3, column=0, sticky=W, pady=10)
    Label(register_frame, text="Enter Password", bg='#CCCCCC').grid(row=4, column=0, sticky=W, pady=10)
    register_uname=Entry(register_frame)
    register_name = Entry(register_frame)
    register_email = Entry(register_frame)
    register_mobile = Entry(register_frame)
    register_pwd = Entry(register_frame, show='*')
    register_btn = Button(register_frame, width=15, text='Register',  relief=SOLID,cursor='hand2',command=insert)

    register_uname.grid(row=0, column=1, pady=10, padx=20)
    register_name.grid(row=1, column=1, pady=10, padx=20)
    register_email.grid(row=2, column=1, pady=10, padx=20) 
    register_mobile.grid(row=3, column=1, pady=10, padx=20)
    register_pwd.grid(row=4, column=1, pady=10, padx=20)
    register_btn.grid(row=5, column=1, pady=10, padx=20)
    register_frame.pack(padx=100,pady=100)

if __name__ == "__main__":
    try:
        root = Tk()
        root.title('Movie reservation')
        root.config(bg='gray')
        webname=Label(root,text="Movie Ticket Reservation",fg="white",bg="darkblue",font=24)
        webname.pack()
        error=Label(root,text="Invalid Username/password!",fg="white",bg="darkblue",font=16)
        con = cx_Oracle.connect('scott/orcl@//localhost:1521/orcl')
        cursor=con.cursor()
        login(root,cursor,con)
        root.mainloop()
    except cx_Oracle.DatabaseError as e:
        print("Problem connecting to Oracle", e)
        # Close the all database operation
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
