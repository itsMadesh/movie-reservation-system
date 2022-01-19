from tkinter import *
import cx_Oracle
root=Tk()
ticket_id=2
con = cx_Oracle.connect('scott/orcl@//localhost:1521/orcl')
cursor=con.cursor()
cursor.execute(f'select th.t_name,th.t_location,m.movie_name,s.show_id,s.show_date,show_time,t.ticket_id from theater th,movie m,show s,tickets t where th.t_id=s.th_id and m.movie_id=s.movie_id and s.show_id=t.show_id  and t.ticket_id=%d'%(ticket_id))
seats=[1,2]
seats=",".join(str(elem) for elem in seats)
records=cursor.fetchall()
records[0]=list(records[0])
records[0].append(seats)
print(records)
desc=["Theater Name:","Theater Location:","Movie name:","Show id:","Show Date:","Show Time:","Ticket id:","Seat Numbers:"]
tInformation_frame=Frame(root,bg="#CCCCCC", relief=SOLID)
Label(tInformation_frame,text="Ticket Info:",width=25,fg="black",bg='white',font=("Times new Roman",15)).grid(row=0,column=0,padx=10,pady=10) 
for i in range(len(records[0])):
    if(i==4):
        current=records[0][i].strftime("%d-%b-%y")
    else:
        current=records[0][i]
    Label(tInformation_frame,text=desc[i],width=25,fg="black",bg='White',font=("Times new Roman",15)).grid(row=i+1,column=0,padx=10,pady=10) 
    Label(tInformation_frame,text=current,width=25,fg="white",bg='Darkblue',font=("Times new Roman",15)).grid(row=i+1,column=1,padx=10,pady=10) 
tInformation_frame.pack(padx=100,pady=100)
root.mainloop()