import cx_Oracle
import tkinter.messagebox
from tkinter import *
# Connecting to DB
loggedInUser=None
Theater_id=None
try:
    con = cx_Oracle.connect('scott/orcl@//localhost:1521/orcl')
    cursor = con.cursor()
    root=Tk()
    cursor.execute(f"select * from theater")
    records=cursor.fetchall()
    t_id=[]
    details=[""]*len(records)
    for i in range(len(records)):
        for j in range(len(records[i])):
            if(j==0):
                t_id.append(records[i][j])
            details[i]+=str(records[i][j])+"-"
    print(t_id,"\n",details)
    def theater_movies(t_id):
        Theater_id=t_id
    tl_frame=LabelFrame(root,text="Click to select theater:",font=20,bd=3,bg='#CCCCCC',relief=SOLID,padx=20,pady=20)
    Theater1=Button(tl_frame,text=details[0],fg="white",bg="Black",command=lambda:theater_movies(t_id[0]))
    Theater2=Button(tl_frame,text=details[1],fg="white",bg="Black",command=lambda:theater_movies(t_id[1]))
    Theater3=Button(tl_frame,text=details[2],fg="white",bg="Black",command=lambda:theater_movies(t_id[2]))
    Theater1.grid(row=0,column=0,padx=10,pady=10)
    Theater2.grid(row=1,column=0,padx=10,pady=10)
    Theater3.grid(row=2,column=0,padx=10,pady=10)
    tl_frame.pack(padx=200,pady=200)
    root.mainloop() 
except cx_Oracle.DatabaseError as e:
    print("Problem connecting to Oracle", e)
    # Close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()