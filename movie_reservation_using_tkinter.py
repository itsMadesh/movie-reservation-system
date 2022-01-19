import cx_Oracle
from tkinter import *
from PIL import ImageTk, Image
import datetime
import tkinter.ttk as ttk
class App:
    def __init__(self,root,cursor,con):
        self.con=con
        self.root=root
        self.cursor=cursor
        self.loggedInUser = None
        self.theater_id=None
        self.ticket_id=None
        self.show_id=None
        self.backbtn=None
        self.login()
        self.log_frame.tkraise()
        self.error=Label(self.root,text="Invalid Username/password!",fg="white",bg="darkblue",font=16) 
    def login(self):
        self.log_frame = Frame(self.root,highlightthickness=2,bg='#CCCCCC',relief=SOLID, padx=10, pady=10)
        self.log_frame.config(highlightbackground="Darkblue")
        Label(self.log_frame, text="Enter Username:", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=0, column=0, sticky=W, pady=10)
        Label(self.log_frame, text="Enter Password:", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=1, column=0, sticky=W, pady=10)
        Label(self.log_frame, text="Not registered yet?", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=3, column=0, sticky=W, pady=10)

        self.log_name = Entry(self.log_frame,font=("Times new Roman",15))
        self.log_pwd = Entry(self.log_frame, show='*',font=("Times new Roman",15))
        self.log_btn = Button(self.log_frame, width=15, text='LOG-IN',relief=SOLID,font=("Times new Roman",15),cursor='hand2',command=self.verify)
        self.create = Button(self.log_frame, width=15,font=("Times new Roman",15) ,text='Create an account',activebackground="Darkblue",activeforeground="White",command=self.registerpage)

        self.log_name.grid(row=0, column=1, pady=10, padx=20)
        self.log_pwd.grid(row=1, column=1, pady=10, padx=20)
        self.log_btn.grid(row=2, column=1, pady=10, padx=20)
        self.create.grid(row=3, column=1, pady=10, padx=20)
        self.log_frame.pack(padx=100,pady=100)

    def register(self):
        self.register_frame = Frame(self.root, bd=2, bg='#CCCCCC',relief=SOLID, padx=10, pady=10)

        Label(self.register_frame, text="Username(Unique)", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=0, column=0, sticky=W, pady=10)
        Label(self.register_frame, text="Enter Name", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=1, column=0, sticky=W, pady=10)
        Label(self.register_frame, text="Enter Email", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=2, column=0, sticky=W, pady=10)
        Label(self.register_frame, text="Contact Number", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=3, column=0, sticky=W, pady=10)
        Label(self.register_frame, text="Enter Password", bg='#CCCCCC',font=("Times new Roman",15)).grid(row=4, column=0, sticky=W, pady=10)
        self.register_uname=Entry(self.register_frame,font=("Times new Roman",15))
        self.register_name = Entry(self.register_frame,font=("Times new Roman",15))
        self.register_email = Entry(self.register_frame,font=("Times new Roman",15))
        self.register_mobile = Entry(self.register_frame,font=("Times new Roman",15))
        self.register_pwd = Entry(self.register_frame, show='*',font=("Times new Roman",15))
        self.register_btn = Button(self.register_frame, width=15, text='Register',font=("Times new Roman",15)  ,relief=SOLID,cursor='hand2',command=self.cus_insert)

        self.register_uname.grid(row=0, column=1, pady=10, padx=20)
        self.register_name.grid(row=1, column=1, pady=10, padx=20)
        self.register_email.grid(row=2, column=1, pady=10, padx=20) 
        self.register_mobile.grid(row=3, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=4, column=1, pady=10, padx=20)
        self.register_btn.grid(row=5, column=1, pady=10, padx=20)
        self.register_frame.pack(padx=100,pady=100)
    
    def theater_movies(self,th_id):
        self.tl_frame.pack_forget()
        self.show_frame=None
        self.theater_id=th_id
        self.date_frame = Frame(self.root, bd=3, bg="#CCCCCC", relief=SOLID)
        self.dates_list = [""] * 7
        date = datetime.datetime.now()
        for i in range(7):
            self.dates_list[i] = date.strftime("%d-%b-%y")
            date += datetime.timedelta(days=1)
        switch_date = [None] * 7
        for i in range(7):
            switch_date[i] = Button(self.date_frame,text=self.dates_list[i],width=15,activebackground="blue",padx=5,pady=5,command=lambda i=i: self.print_shows(i))
            switch_date[i].grid(column=i,row=0)
        self.date_frame.pack(padx=20, pady=20)
        self.print_shows(0)
    def print_shows(self,date_pos):
        if self.show_frame:
            self.show_frame.pack_forget()
        self.current_date = self.dates_list[date_pos]
        self.show_frame = Frame(self.root, bd=3, bg="#CCCCCC", relief=SOLID)
        self.cursor.execute(f"select show_id,movie_name,show_time,available_seats,image_url from movie natural join show where th_id=%s and show_date='%s'"%(self.theater_id,self.current_date))
        records = self.cursor.fetchall()
        ShId_list=[]
        MvName_list=[]
        ShTime_list=[]
        AvailSeats_list=[]
        MvImages_list=[]
        for i in range(len(records)):
            ShId_list.append(records[i][0])
            MvName_list.append(records[i][1])
            ShTime_list.append(records[i][2])
            AvailSeats_list.append(records[i][3])
            MvImages_list.append(str(records[i][4])) 
        self.movie_images=[None]*len(MvImages_list)
        self.show_frame=Frame(self.root,bd=3,bg='#CCCCCC')
        Label(self.show_frame,text="Show Date:"+self.current_date,fg="white",bg='Darkblue',font=("Times new Roman",15)).grid(row=0,column=0,padx=4,pady=4)
        for i in range(len(records)):
            self.movie_images[i] = Image.open(MvImages_list[i])
            self.movie_images[i] = self.movie_images[i].resize((100,100), Image.ANTIALIAS)
            self.movie_images[i]=(ImageTk.PhotoImage(self.movie_images[i]))
            Label(self.show_frame,image=self.movie_images[i]).grid(row=i+1,column=0,padx=4,pady=4)
            Label(self.show_frame,text="Name:"+MvName_list[i],fg="steelblue4",bg='#CCCCCC',font=("Times new Roman",15)).grid(row=i+1,column=1,padx=5,pady=5)
            Label(self.show_frame,text="Show Time:"+ShTime_list[i],fg="steelblue4",bg='#CCCCCC',font=("Times new Roman",15)).grid(row=i+1,column=2,padx=5,pady=5)
            Label(self.show_frame,text="Available seats:"+str(AvailSeats_list[i]),fg="steelblue4",bg='#CCCCCC',font=("Times new Roman",15)).grid(row=i+1,column=3,padx=5,pady=5)
            Theater=Button(self.show_frame,text="Click",fg="white",bg="Darkblue",width=15,command=lambda i=i:self.seat_selection(ShId_list[i]))
            Theater.grid(row=i+1,column=4,padx=10,pady=10)
        self.show_frame.pack(padx=50,pady=50)
    def ticket_information(self):
        self.seats_frame.pack_forget()
        self.booking_frame.pack_forget()
        self.cursor.execute(f'select th.t_name,th.t_location,m.movie_name,s.show_id,s.show_date,show_time,t.ticket_id from theater th,movie m,show s,tickets t where th.t_id=s.th_id and m.movie_id=s.movie_id and s.show_id=t.show_id  and t.ticket_id=%d'%(self.ticket_id))
        records=self.cursor.fetchall()
        records[0]=list(records[0])
        records[0].append(self.seats_str)
        print(records)
        desc=["Theater Name:","Theater Location:","Movie name:","Show id:","Show Date:","Show Time:","Ticket id:","Seat Numbers:"]
        self.tInformation_frame=Frame(root,bg="#CCCCCC", relief=SOLID)
        Label(self.tInformation_frame,text="Ticket Info:",width=25,fg="black",bg='Steelblue',font=("Times new Roman",15)).grid(row=0,column=0,padx=10,pady=10) 
        for i in range(len(records[0])):
            if(i==4):
                current=records[0][i].strftime("%d-%b-%y")
            else:
                current=records[0][i]
            Label(self.tInformation_frame,text=desc[i],width=25,fg="black",bg='White',font=("Times new Roman",15)).grid(row=i+1,column=0,padx=10,pady=10) 
            Label(self.tInformation_frame,text=current,width=25,fg="white",bg='Darkblue',font=("Times new Roman",15)).grid(row=i+1,column=1,padx=10,pady=10) 
        self.tInformation_frame.pack(padx=100,pady=100)
    def booking(self):
        self.cursor.execute("select max(ticket_id) from tickets")
        self.con.commit()
        records=self.cursor.fetchall()
        self.seats_str=self.seatno.get()
        self.seats=self.seats_str.split(',')
        if records[0][0] is None:
            self.ticket_id=1
        else:
            self.ticket_id=int(records[0][0])+1
        print(self.ticket_id)
        self.cursor.execute(f"Insert into tickets values(:ticket_id,:show_id,:c_id)",{'ticket_id':self.ticket_id,'show_id':self.show_id,'c_id':self.loggedInUser})
        self.con.commit()

        for i in range(len(self.seats)):
            self.cursor.execute(f"Insert into booked_seats values(b_id.nextval,:ticket_id,:seat_no)",{'ticket_id':self.ticket_id,'seat_no':int(self.seats[i])}) 
        self.cursor.execute("Update show set available_seats=available_seats-%d where show_id=%s"%(len(self.seats),self.show_id))
        self.con.commit() 
        self.ticket_information()
    def seat_selection(self,show_id):
        self.date_frame.pack_forget()
        self.show_frame.pack_forget()
        self.seats_frame=Frame(self.root, bd=3, bg="#CCCCCC", relief=SOLID)
        self.show_id=show_id
        self.cursor.execute(f"select no_of_seats from  theater where t_id=%d"%(self.theater_id))
        records=self.cursor.fetchall()
        total_seats=records[0][0]
        self.cursor.execute(f"select seat_no from booked_seats  b,tickets  t where b.ticket_id=t.ticket_id and t.show_id=%d"%(self.show_id))
        records=self.cursor.fetchall()
        print("show_id::",show_id,"booked_seats::",records)
        print(f"select seat_no from booked_seats  b,tickets  t where b.ticket_id=t.ticket_id and t.show_id=%d"%(self.show_id))
        records = [record[0] for record in records]
        print(records)
        row=1
        col=0
        for i in range(1,total_seats+1):
            if i in records:
                seats=Button(self.seats_frame,text=i,fg="white",bg="red",padx=10,pady=10)
                seats.grid(row=row,column=col,padx=10,pady=10)
            else:
                seats=Button(self.seats_frame,text=i,fg="white",bg="Green",padx=10,pady=10)
                seats.grid(row=row,column=col,padx=10,pady=10)
            col+=1
            if(i%10==0):     
                row+=1
                col=0
        self.seats_frame.pack(padx=50, pady=50)
        self.booking_frame=Frame(self.root, bd=3, bg="#CCCCCC", relief=SOLID)
        Label(self.booking_frame,text="Enter seat number:").grid(row=1,column=0)
        self.seatno=Entry(self.booking_frame)
        self.Book = Button(self.booking_frame, width=15, text='Book-Ticket',relief=SOLID,cursor='hand2',command=self.booking)
        Label(self.booking_frame,text="Available",bg="Green",fg="black").grid(row=0, column=0, pady=10, padx=20)
        Label(self.booking_frame,text="Booked",bg="Red",fg="black").grid(row=0, column=1, pady=10, padx=20)
        self.seatno.grid(row=1, column=1, pady=10, padx=20)
        self.Book.grid(row=2, column=1, pady=10, padx=20)
        self.booking_frame.pack(padx=50, pady=50)

    def Theater_selection(self):
        self.cursor.execute(f"select * from theater")
        records=self.cursor.fetchall()
        ThId_list=[]
        ThName_list=[]
        ThLocation_list=[]
        ThSeats_list=[]
        ThImages_list=[]
        for i in range(len(records)):
            ThId_list.append(records[i][0])
            ThName_list.append(records[i][1])
            ThLocation_list.append(records[i][2])
            ThSeats_list.append(records[i][3])
            ThImages_list.append(str(records[i][4])) 
        print(ThImages_list)
        self.final_images=[None]*len(ThImages_list)
        self.tl_frame=Frame(self.root,bd=3,bg='#CCCCCC',padx=20,pady=20)
        self.thid_frames=[None]*len(ThId_list)
        for i in range(len(records)):
            self.final_images[i] = Image.open(ThImages_list[i])
            self.final_images[i] = self.final_images[i].resize((100,100), Image.ANTIALIAS)
            self.final_images[i]=(ImageTk.PhotoImage(self.final_images[i]))
            Label(self.tl_frame,image=self.final_images[i]).grid(row=i,column=0,padx=4,pady=4)
            Label(self.tl_frame,text="Name:"+ThName_list[i],fg="steelblue4",bg='#CCCCCC',font=("Times new Roman",15)).grid(row=i,column=1,padx=5,pady=5)
            Label(self.tl_frame,text="Location:"+ThLocation_list[i],fg="steelblue4",bg='#CCCCCC',font=("Times new Roman",15)).grid(row=i,column=2,padx=5,pady=5)
            Label(self.tl_frame,text="Total seats:"+str(ThSeats_list[i]),fg="steelblue4",bg='#CCCCCC',font=("Times new Roman",15)).grid(row=i,column=3,padx=5,pady=5)
            self.thid_frames[i]=Button(self.tl_frame,text="Click",fg="white",bg="Darkblue",width=15,command=lambda i=i:self.theater_movies(ThId_list[i]))
            self.thid_frames[i].grid(row=i,column=4,padx=10,pady=10)

        self.tl_frame.pack(padx=20,pady=20)
    def cus_insert(self):
        self.loggedInUser=self.register_uname.get()
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
            self.register_success()
        else:
            self.incorrect_user()
    def registerpage(self):
        self.log_frame.pack_forget()
        self.register()
        self.register_frame.tkraise()
    def register_success(self):
        self.error.destroy()
        self.register_frame.pack_forget()
        self.Theater_selection()
        self.tl_frame.tkraise()
    def login_success(self):
        self.error.destroy()
        self.log_frame.pack_forget()
        self.Theater_selection()
        self.tl_frame.tkraise()
    def incorrect_user(self):
        self.error.destroy()
        self.error=Label(self.root,text="Invalid Username/password!",fg="white",bg="darkblue",font=16)
        self.error.pack()
    def verify(self):
        uname=self.log_name.get()
        pwd=self.log_pwd.get()
        self.cursor.execute(f'select * from customer where c_id=:uname and c_password=:pwd',{'uname':uname,'pwd':pwd})
        record =self.cursor.fetchall()
        if record:
            self.loggedInUser = uname
            self.login_success()
        else:
            self.incorrect_user()
        self.con.commit()
if __name__ == "__main__":
    try:
        con = cx_Oracle.connect('scott/orcl@//localhost:1521/orcl')
        cursor=con.cursor()
        root = Tk()
        root.config(bg="dodgerblue4")
        root.title("Movie Reservation")
        root.iconbitmap("images/logo/theater.ico")
        webname=Button(root,text="Movie Ticket Reservation",fg="Darkblue",font=24,relief=RAISED)
        webname.pack()
        m=App(root,cursor,con)
    except cx_Oracle.DatabaseError as e:
        print("Problem connecting to Oracle", e)
    finally:
        if root:
            root.mainloop()
        if cursor:
            cursor.close()
        if con:
            con.close()
