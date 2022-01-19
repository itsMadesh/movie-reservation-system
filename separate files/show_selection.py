import cx_Oracle
from tkinter import *
import datetime

try:
    con = cx_Oracle.connect("scott/orcl@//localhost:1521/orcl")
    cursor = con.cursor()
    root = Tk()
    show_frame = Frame(root, bd=3, bg="#CCCCCC", relief=SOLID)
    show_frame.config(width=1000, height=1000)
    Dates_list = [""] * 7
    date = datetime.datetime.now()
    for i in range(7):
        date += datetime.timedelta(days=1)
        Dates_list[i] = date.strftime("%d-%b-%y")
    def seat_selection(show_id):
        print(show_id)
    def print_shows(date_pos):
        sid_list=[]
        current_date = Dates_list[date_pos]
        cursor.execute(f"select show_id,movie_name,show_time from movie natural join show where th_id=%s and show_date='%s'"%(2,current_date))
        records = cursor.fetchall()
        details = [""] * len(records)
        for i in range(len(records)):
            for j in range(len(records[i])):
                if(j==0):
                    sid_list.append(records[i][j])
                else:     
                    details[i] += str(records[i][j]) + "|"
        Label(show_frame,text="Select movie and show_time :",width=50,bg="Gray").grid(row=2, column=3,columnspan=1,padx=10,pady=10)
        for i in range(len(details)):
            movies = Button( show_frame,text=details[i],width=50,activebackground="blue",padx=5,pady=5,command=lambda i=i:seat_selection(sid_list[i]))
            movies.grid(row=3 + i, column=3,columnspan=1,padx=10,pady=10)

    switch_date = [None] * 7
    print_shows(0)
    for i in range(7):
        switch_date[i] = Button(show_frame,text=Dates_list[i],width=15,activebackground="blue",padx=5,pady=5,command=lambda i=i: print_shows(i))
        switch_date[i].grid(column=i,row=0)
    show_frame.pack(padx=100, pady=100)
    root.mainloop()
except cx_Oracle.DatabaseError as e:
    print("Problem connecting to Oracle", e)
    # Close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
