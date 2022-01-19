create table customer (c_name varchar2(30),c_id  varchar2(25) primary key ,c_password varchar2(20),c_phoneno number(12),c_emailid varchar2(45));

create sequence theater_id;
create table theater (t_id number primary key,t_name varchar2(32),t_location varchar2(35),No_of_seats number);
insert into theater values(theater_id.nextval,'PVR','Grand Galada,Pallavaram',50);
insert into theater values(theater_id.nextval,'Rohini Silver Screens','Koyambedu',50);
insert into theater values(theater_id.nextval,'INOX','The Marina Mall,OMR',50)

create sequence movie_id;
create table movie(movie_id number primary key,movie_name varchar(30));
insert into movie values(movie_id.nextval,'Master');
insert into movie values(movie_id.nextval,'Beast');
insert into movie values(movie_id.nextval,'valimai');


create sequence show_id;
create table show (show_id number primary key,show_time varchar2(7),show_date Date,th_id number,movie_id number, available_seats number,
foreign key (th_id) references theater(t_id),
foreign key (movie_id) references movie(movie_id));

insert into show values(show_id.nextval,'10:15am','05-jan-2022',1,1,50);
insert into show values(show_id.nextval,'2:15pm','05-jan-2022',1,2,50);
insert into show values(show_id.nextval,'6:30pm','05-jan-2022',1,3,50);
insert into show values(show_id.nextval,'10:15pm','05-jan-2022',1,1,50);

insert into show values(show_id.nextval,'10:15am','06-jan-2022',1,1,50);
insert into show values(show_id.nextval,'2:15pm','06-jan-2022',1,2,50);
insert into show values(show_id.nextval,'6:30pm','06-jan-2022',1,3,50);
insert into show values(show_id.nextval,'10:15pm','06-jan-2022',1,1,50);

insert into show values(show_id.nextval,'10:15am','07-jan-2022',1,1,50);
insert into show values(show_id.nextval,'2:15pm','07-jan-2022',1,2,50);
insert into show values(show_id.nextval,'6:30pm','07-jan-2022',1,3,50);
insert into show values(show_id.nextval,'10:15pm','07-jan-2022',1,1,50);

insert into show values(show_id.nextval,'10:15am','08-jan-2022',1,1,50);
insert into show values(show_id.nextval,'2:15pm','08-jan-2022',1,2,50);
insert into show values(show_id.nextval,'6:30pm','08-jan-2022',1,3,50);
insert into show values(show_id.nextval,'10:15pm','08-jan-2022',1,1,50);

insert into show values(show_id.nextval,'10:15am','09-jan-2022',1,1,50);
insert into show values(show_id.nextval,'2:15pm','09-jan-2022',1,2,50);
insert into show values(show_id.nextval,'6:30pm','09-jan-2022',1,3,50);
insert into show values(show_id.nextval,'10:15pm','09-jan-2022',1,1,50);

insert into show values(show_id.nextval,'10:15am','10-jan-2022',1,1,50);
insert into show values(show_id.nextval,'2:15pm','10-jan-2022',1,2,50);
insert into show values(show_id.nextval,'6:30pm','10-jan-2022',1,3,50);
insert into show values(show_id.nextval,'10:15pm','10-jan-2022',1,1,50);

insert into show values(show_id.nextval,'10:15am','11-jan-2022',1,1,50);
insert into show values(show_id.nextval,'2:15pm','11-jan-2022',1,2,50);
insert into show values(show_id.nextval,'6:30pm','11-jan-2022',1,3,50);
insert into show values(show_id.nextval,'10:15pm','11-jan-2022',1,1,50);

insert into show values(show_id.nextval,'10:15am','05-jan-2022',2,1,50);
insert into show values(show_id.nextval,'2:15pm','05-jan-2022',2,2,50);
insert into show values(show_id.nextval,'6:30pm','05-jan-2022',2,3,50);
insert into show values(show_id.nextval,'10:15pm','05-jan-2022',2,1,50);

insert into show values(show_id.nextval,'10:15am','06-jan-2022',2,1,50);
insert into show values(show_id.nextval,'2:15pm','06-jan-2022',2,2,50);
insert into show values(show_id.nextval,'6:30pm','06-jan-2022',2,3,50);
insert into show values(show_id.nextval,'10:15pm','06-jan-2022',2,1,50);

insert into show values(show_id.nextval,'10:15am','07-jan-2022',2,1,50);
insert into show values(show_id.nextval,'2:15pm','07-jan-2022',2,2,50);
insert into show values(show_id.nextval,'6:30pm','07-jan-2022',2,3,50);
insert into show values(show_id.nextval,'10:15pm','07-jan-2022',2,1,50);

insert into show values(show_id.nextval,'10:15am','08-jan-2022',2,1,50);
insert into show values(show_id.nextval,'2:15pm','08-jan-2022',2,2,50);
insert into show values(show_id.nextval,'6:30pm','08-jan-2022',2,3,50);
insert into show values(show_id.nextval,'10:15pm','08-jan-2022',2,1,50);

insert into show values(show_id.nextval,'10:15am','09-jan-2022',2,1,50);
insert into show values(show_id.nextval,'2:15pm','09-jan-2022',2,2,50);
insert into show values(show_id.nextval,'6:30pm','09-jan-2022',2,3,50);
insert into show values(show_id.nextval,'10:15pm','09-jan-2022',2,1,50);

insert into show values(show_id.nextval,'10:15am','10-jan-2022',2,1,50);
insert into show values(show_id.nextval,'2:15pm','10-jan-2022',2,2,50);
insert into show values(show_id.nextval,'6:30pm','10-jan-2022',2,3,50);
insert into show values(show_id.nextval,'10:15pm','10-jan-2022',2,1,50);

insert into show values(show_id.nextval,'10:15am','11-jan-2022',2,1,50);
insert into show values(show_id.nextval,'2:15pm','11-jan-2022',2,2,50);
insert into show values(show_id.nextval,'6:30pm','11-jan-2022',2,3,50);
insert into show values(show_id.nextval,'10:15pm','11-jan-2022',2,1,50);

insert into show values(show_id.nextval,'10:15am','05-jan-2022',3,1,50);
insert into show values(show_id.nextval,'2:15pm','05-jan-2022',3,2,50);
insert into show values(show_id.nextval,'6:30pm','05-jan-2022',3,3,50);
insert into show values(show_id.nextval,'10:15pm','05-jan-2022',3,1,50);

insert into show values(show_id.nextval,'10:15am','06-jan-2022',3,1,50);
insert into show values(show_id.nextval,'2:15pm','06-jan-2022',3,2,50);
insert into show values(show_id.nextval,'6:30pm','06-jan-2022',3,3,50);
insert into show values(show_id.nextval,'10:15pm','06-jan-2022',3,1,50);

insert into show values(show_id.nextval,'10:15am','07-jan-2022',3,1,50);
insert into show values(show_id.nextval,'2:15pm','07-jan-2022',3,2,50);
insert into show values(show_id.nextval,'6:30pm','07-jan-2022',3,3,50);
insert into show values(show_id.nextval,'10:15pm','07-jan-2022',3,1,50);

insert into show values(show_id.nextval,'10:15am','08-jan-2022',3,1,50);
insert into show values(show_id.nextval,'2:15pm','08-jan-2022',3,2,50);
insert into show values(show_id.nextval,'6:30pm','08-jan-2022',3,3,50);
insert into show values(show_id.nextval,'10:15pm','08-jan-2022',3,1,50);

insert into show values(show_id.nextval,'10:15am','09-jan-2022',3,1,50);
insert into show values(show_id.nextval,'2:15pm','09-jan-2022',3,2,50);
insert into show values(show_id.nextval,'6:30pm','09-jan-2022',3,3,50);
insert into show values(show_id.nextval,'10:15pm','09-jan-2022',3,1,50);

insert into show values(show_id.nextval,'10:15am','10-jan-2022',3,1,50);
insert into show values(show_id.nextval,'2:15pm','10-jan-2022',3,2,50);
insert into show values(show_id.nextval,'6:30pm','10-jan-2022',3,3,50);
insert into show values(show_id.nextval,'10:15pm','10-jan-2022',3,1,50);

insert into show values(show_id.nextval,'10:15am','11-jan-2022',3,1,50);
insert into show values(show_id.nextval,'2:15pm','11-jan-2022',3,2,50);
insert into show values(show_id.nextval,'6:30pm','11-jan-2022',3,3,50);
insert into show values(show_id.nextval,'10:15pm','11-jan-2022',3,1,50);



create sequence ticket_id start with 1 increment by 1;
create table tickets(ticket_id number primary key,show_id number,c_id varchar2(25),
foreign key(show_id) references show(show_id),foreign key(c_id) references customer(c_id));

create sequence b_id start with 1 increment by 1;
create table booked_seats(b_id number primary key,ticket_id number,seat_no number
,foreign key(ticket_id) references tickets(ticket_id));

alter table movie add image_url varchar(45);
update movie set image_url='images/movies/beast.png' where movie_name='Beast';
update movie set image_url='images/movies/valimai.png' where movie_name='valimai';
update movie set image_url='images/movies/master.png' where movie_name='Master';

alter table theater add image_url varchar(45);
update theater set image_url='images/theaters/pvr.png' where t_name='PVR';
update theater set image_url='images/theaters/inox.png' where t_name='INOX';
update theater set image_url='images/theaters/rohini.png' where t_name='Rohini Silver Screens';

-- mytickets query:

select t.ticket_id, th.t_name, m.movie_name,s.show_id, s.show_date, s.show_time, bs.seat_no from theater th, movie m, show s, tickets t, booked_seats bs 
where th.t_id=s.th_id 
and m.movie_id=s.movie_id
and s.show_id=t.show_id
and t.ticket_id = bs.ticket_id
and t.c_id = 'itsmadesh';


-- ticket information of current booking customer:

select distinct th.t_name,th.t_id,m.movie_name,s.show_id,s.show_date,show_time,t.ticket_id from theater th,movie m,show s,tickets t 
where th.t_id=s.th_id 
and m.movie_id=s.movie_id 
and s.show_id=t.show_id
and t.ticket_id=2;