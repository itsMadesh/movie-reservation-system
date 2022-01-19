import cx_Oracle
import tkinter.messagebox
from tkinter import *
# Connecting to DB
class seats_selection:
    def __init__(self,loggedInUser):
        self.loggedInUser=loggedInUser
        try:
            con = cx_Oracle.connect('scott/orcl@//localhost:1521/orcl')
            cursor = con.cursor()
            root=Tk()
            scrollbar = Scrollbar(root, orient=VERTICAL)
            scrollbar.pack(side=RIGHT, fill=Y)    
            seats=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
            right_frame = Frame(root, bd=2, bg='#CCCCCC', padx=10, pady=10)
            for i in range(len(seats)):
                for j in range(1,12+1):
                    mylabel=Button(right_frame,text=seats[i]+str(j),padx=10,pady=10)
                    mylabel.grid(row=i,column=j-1)
            right_frame.pack(padx=50,pady=50)
            root.mainloop()
        except cx_Oracle.DatabaseError as e:
            print("Problem connecting to Oracle", e)
            # Close the all database operation
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
seats_selection(1)