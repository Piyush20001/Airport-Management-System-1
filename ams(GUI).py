#Driver Code for backend 
import mysql.connector
import random
import string
import tkinter
from tkinter import messagebox,scrolledtext
import tabulate
#User Defined Functions
def flight_no():
    x=random.randint(1001,9999)
    return x

def time():
    x=random.randint(0,23)
    y=random.randint(0,59)
    if x<10:
        if y<10:
            z='0'+str(x)+':'+'0'+str(y)+':'+'00'
            return z
        else:
            z='0'+str(x)+':'+str(y)+':'+'00'
            return z
    else:
        if y<10:
            z=str(x)+':'+'0'+str(y)+':'+'00'
            return z
        else:
            z=str(x)+':'+str(y)+':'+'00'
            return z
        
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def passengerflight():
    r4=random.randint(0,len(flightnumbers)-1)
    c=flightnumbers[r4]
    return c

def checkin():
    status=['Completed','Pending']
    r4=random.randint(0,1)
    c=status[r4]
    return c    
database1=input('Please enter the name of the MySQL database you will be using:')
password1=input('Please enter the the password for your MySQL server:')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#Flights table generator

#List of Cities
depart=['New_Delhi','Sydney','New_York','London','Abu_Dhabi','Paris','Beijing','Berlin','Moscow',
        'Brasilia','Toronto','Mexico_City','Colombo','Madrid','Geneva','Karachi','Tokyo','Dhaka']

#List of airlines
airlines={'New_Delhi':'Air_India','Sydney':'Quantas','New_York':'United_Airlines','London':'British_Airways','Abu_Dhabi':'Emirates','Paris':'Air_France','Beijing':'Hainan_Airways','Berlin':'Luftansa','Moscow':'Aeroflot',
        'Brasilia':'LAN_Airlines','Toronto':'Delta_Airlines','Mexico_City':'Aeroméxico','Colombo':'SriLankan','Madrid':'Iberia','Geneva':'Swiss_Air','Karachi':'Airblue','Tokyo':'Japan_Airlines','Dhaka':'Regent_Airways'}

mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
mycursor.execute('drop table if exists flights')
mycursor.execute('drop table if exists passengers')
flight_creation='create table flights (flight_number char(4) not null primary key,flight_name varchar(20),source_airport varchar(30) not null,destination_airport varchar(20) not null,departure_time time not null,connecting_flight char(3) not null)'
passenger_creation=('create table passengers (PNR char(6) not null primary key,First_name varchar(10),Last_name varchar(10),FLight_no char(4) not null,checkin_status varchar(10) default "Pending");')
mycursor.execute(passenger_creation)
mycursor.execute(flight_creation)
#To erase any previously existing data in the table
delete=('delete from flights')
mycursor.execute(delete)

#Inserting data into MySQL
flightnumbers=[]
for i in range(5):
    query=('insert into flights values(%s,%s,%s,%s,%s,%s)')
    fnum=flight_no()
    flightnumbers.append(fnum)
    r=random.randint(0,len(depart)-1)
    sa=depart[r]
    while True:
        r2=random.randint(0,len(depart)-1)
        temp=depart[r2]
        if temp!=sa:
            da=temp
            break
        else:
            continue
    fname=airlines[sa]
    dtime=time()
    cfstatus=['yes','no']
    r3=random.randint(0,1)
    cf=cfstatus[r3]
    tup=(fnum,fname,sa,da,dtime,cf)
    mycursor.execute(query,tup)
mydb.commit()
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#Passenger table generator

s='Jodee,Marielle,Phillip,Colby,Stephany,Dione,Grover,Napoleon,Nicholas,Alysa,Noma,Leta,Ciera,Donny,Buc,Iren,Renato,Glory,Stacia,Bennie,Soo,Mitzie,Kaci,Peggy,Hilma,Melva,Cindie,Miyoko,Melina,Cammy,Blanche,Rhea,Jill,Kellye,Ailene,Vida,Alva,Sau,Hollis,Oswaldo,Marty'
first_names=s.split(',')

s2='Bula,Bibi,Rolf,Tayna,Ardith,Art,Jeannetta,Patrina,Ronny,Maida,Cleopatra,Sherry,Vincenza,Sheri,Sherlyn,Shayne,Geneva,Javier,Celine,Saran,Shari,Boris,Gwyneth,Summer,Maryellen,Rufina,Essie,Palma,Rafael,Cordell,Jude,Jenine,Manuel,Cleveland,Daphine,Lavina,Candi,Rossie,Brunilda,Gilberte,Nick,Hoyt,Lucius,Ardis,Tyler,Dwain,Caleb,Aide,Mckinley,Margurite'
last_names=s2.split(',')

#Establishing MySQL connection
try:
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
except:
    print('Unable to establish SQL connection, make sure password and database details are correct')

#To erase any previously existing data in the table
delete=('delete from passengers')
mycursor.execute(delete)

#Inserting data into MySQL
nkey=random.randint(20,41)
for i in range(nkey):
    query=('insert into passengers value(%s,%s,%s,%s,%s)')
    fkey=random.randint(0,40)
    lkey=random.randint(0,40)
    tup=(id_generator(),first_names[fkey],last_names[lkey],passengerflight(),checkin())
    mycursor.execute(query,tup)
mydb.commit()
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#Seats table generator

select_query='select flight_number,flight_name from flights'
mycursor.execute(select_query)
records = mycursor.fetchall()
flight_numbers=[]
flight_names=[]
for i in records:
    flight_numbers.append(i[0])
    flight_names.append(i[1])
    
seat_status=['Booked','Vacant']
booking_tables=[]
for book in range(5):
    create_query='create table'+' '+(flight_numbers[book])+'_'+flight_names[book]+' (Seat_Number char(5) not null primary key,Class varchar(20) not null,Booking_Status char(10) not null)'
    delete_query='drop table if exists'+' '+(flight_numbers[book])+'_'+flight_names[book]
    booking_tables.append((flight_numbers[book])+'_'+flight_names[book])
    mycursor.execute(delete_query)
    mycursor.execute(create_query)

seats1={'A':'First Class','B':'Business Class','C':'Business Class','D':'Economy Class','E':'Economy Class'}
def seatno(alpha,num):
    z=alpha+str(num)
    return z
    
def status():
    z=random.choice(seat_status)
    return z
def refresh_query(a):
    z='delete from '+a
    return z
for book2 in booking_tables:
    mycursor.execute(refresh_query(book2))
    for seat in seats1:
        for kk in range(1,10):
            z='insert into '+book2+' values(%s,%s,%s)'
            vals=(seatno(seat,kk),seats1[seat],status())
            mycursor.execute(z,vals)

    
mydb.commit()
#MENU STARTS HERE 
try:
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
except:
    print('Unable to establish SQL connection, make sure password and database details are correct')
import random
import mysql.connector

def randomString(stringLength=6):
    a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return ''.join(random.choice(a) for i in range(stringLength))

def AD():
           
            import mysql.connector
            from tabulate import tabulate
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
            mycursor=mydb.cursor()
            sql = ("SELECT * FROM flights")
            mycursor.execute(sql)
            results = mycursor.fetchall()
            x=(tabulate(results, headers=['Flight Number','Flight Name','Source','Destination','Departure Time', 'Connecting Flight Available'], tablefmt='psql'))
            adwindow=tkinter.Toplevel()
            adwindow.title('Arrivals and Departures')
            adwindow.geometry('850x150+120+120')
            label=scrolledtext.ScrolledText(adwindow,height=150,width=850)
            label.pack()
            label.insert(tkinter.INSERT,x)
            label.config(state=tkinter.DISABLED)
            mydb.commit()
            
def BT():
    def submot():
        fname=name.get()
        lname=name2.get()
        fno=z.get()
        query="insert into passengers values (%s,%s,%s,%s,%s)"
        tuple1=(pnr,fname,lname,fno,"Pending")
        mycursor.execute(query,tuple1)
        mydb.commit()
        info='Your flight details are: PNR: ',pnr,',first name: ',fname,',last name: ',lname,' ,flight number: ',fno,'\nPlease keep these handy'
        messagebox.showinfo('Flight Details',info)
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    swindow=tkinter.Toplevel()
    tkinter.Label(swindow,text='Enter First Name:').grid(row=1)
    name=tkinter.Entry(swindow,font='Menlo')
    name.focus_set()
    name.grid(row=1,column=2)
    
    tkinter.Label(swindow,text='Enter Surname:').grid(row=2)
    name2=tkinter.Entry(swindow,font='Menlo')
    name2.grid(row=2,column=2)
    
    tkinter.Label(swindow,text='Please enter flight number:').grid(row=3)
    z=tkinter.Entry(swindow,font='Menlo')
    z.grid(row=3,column=2)
    pnr=id_generator()
    tkinter.Button(swindow,text='Submit',width=5,height=1,command=submot).grid(row=6, column=2)
    
def WC():
    def submot2():
        name4=name3.get()
        h2=(name4,)
        sql=("UPDATE passengers set checkin_status='completed' where pnr = %s")
        mycursor.execute(sql,h2)
        mydb.commit()
        messagebox.showinfo('Alert','Check-in succesfully done.')
        
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    pwindow=tkinter.Toplevel()
    tkinter.Label(pwindow,text='Enter PNR Number:').grid(row=1)
    name3=tkinter.Entry(pwindow,font='Menlo')
    name3.grid(row=1,column=2)
    tkinter.Button(pwindow,text='Submit',width=5,height=1,command=submot2).grid(row=2, column=2)
    
    

def civilians():
    passengers1=tkinter.Toplevel()
    passengers1.title('Passenger Window')
    passengers1.geometry('670x600+120+120')
    passengers1.configure(bg='sky blue')
    label=tkinter.Label(passengers1,text='Passengers',font='Menlo 50',bg='Sky Blue',bd=10 ,fg='Black').place(x=160,y=10)
    ad=tkinter.Button(passengers1,text='Arrivals and Departures',width=50,height=1,font='Terminal 20',command=AD).place(x=10,y=200)
    wc=tkinter.Button(passengers1,text='Web Check-in',width=50,height=1,font='Terminal 20',command=WC).place(x=10,y=350)
    bt=tkinter.Button(passengers1,text='Booking Tickets',width=50,height=1,font='Terminal 20',command=BT).place(x=10,y=500)
    
def status1():
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    fwindow=tkinter.Toplevel()
    fwindow.title('Seats Status')
    fwindow.geometry('400x400+120+120')
    z=(booking_tables[0])
    sql=('SELECT * FROM '+ z)
    
    mycursor.execute(sql)
    results = mycursor.fetchall()
    x=(tabulate(results, headers=['Seat Number','Class','Booking Status'], tablefmt='psql'))
    label=scrolledtext.ScrolledText(fwindow)
    label.pack()
    label.insert(tkinter.INSERT,x)
    label.config(state=tkinter.DISABLED)
    mydb.commit()

def status2():
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    fwindow=tkinter.Toplevel()
    fwindow.title('Seats Status')
    fwindow.geometry('400x400+120+120')
    z=(booking_tables[1])
    sql=('SELECT * FROM '+ z)
    
    mycursor.execute(sql)
    results = mycursor.fetchall()
    x=(tabulate(results, headers=['Seat Number','Class','Booking Status'], tablefmt='psql'))
    label=scrolledtext.ScrolledText(fwindow)
    label.pack()
    label.insert(tkinter.INSERT,x)
    label.config(state=tkinter.DISABLED)
    mydb.commit() 
    
def status3():
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    fwindow=tkinter.Toplevel()
    fwindow.title('Seats Status')
    fwindow.geometry('400x400+120+120')
    z=(booking_tables[2])
    sql=('SELECT * FROM '+ z)
    
    mycursor.execute(sql)
    results = mycursor.fetchall()
    x=(tabulate(results, headers=['Seat Number','Class','Booking Status'], tablefmt='psql'))
    label=scrolledtext.ScrolledText(fwindow)
    label.pack()
    label.insert(tkinter.INSERT,x)
    label.config(state=tkinter.DISABLED)
    mydb.commit()

def status4():
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    fwindow=tkinter.Toplevel()
    fwindow.title('Seats Status')
    fwindow.geometry('400x400+120+120')
    z=(booking_tables[3])
    sql=('SELECT * FROM '+ z)
    
    mycursor.execute(sql)
    results = mycursor.fetchall()
    x=(tabulate(results, headers=['Seat Number','Class','Booking Status'], tablefmt='psql'))
    label=scrolledtext.ScrolledText(fwindow)
    label.pack()
    label.insert(tkinter.INSERT,x)
    label.config(state=tkinter.DISABLED)
    mydb.commit()
    
def status5():
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    fwindow=tkinter.Toplevel()
    fwindow.title('Seats Status')
    fwindow.geometry('400x400+120+120')
    z=(booking_tables[4])
    sql=('SELECT * FROM '+ z)
    mycursor.execute(sql)
    results = mycursor.fetchall()
    x=(tabulate(results, headers=['Seat Number','Class','Booking Status'], tablefmt='psql'))
    label=scrolledtext.ScrolledText(fwindow)
    label.pack()
    label.insert(tkinter.INSERT,x)
    label.config(state=tkinter.DISABLED)
    mydb.commit()
    
    
    
def flight_seats():
     
     seater=tkinter.Toplevel()
     seater.title('Flight Seats Status')
     seater.geometry('675x700+120+120')
     seater.configure(bg='sky blue')
     temp=booking_tables[:]
     for op in range(5):
         temp[op]=temp[op].replace('_',' ')
     label=tkinter.Label(seater,text='Flight Seats Status',font='Menlo 50',bd=10 ,fg='Black').place(x=40,y=10)
     f1=tkinter.Button(seater,text=temp[0],width=50,height=1,font='Terminal 20',command=status1).place(x=10,y=200)
     f2=tkinter.Button(seater,text=temp[1],width=50,height=1,font='Terminal 20',command=status2).place(x=10,y=300)
     f3=tkinter.Button(seater,text=temp[2],width=50,height=1,font='Terminal 20',command=status3).place(x=10,y=400)
     f4=tkinter.Button(seater,text=temp[3],width=50,height=1,font='Terminal 20',command=status4).place(x=10,y=500)
     f5=tkinter.Button(seater,text=temp[4],width=50,height=1,font='Terminal 20',command=status5).place(x=10,y=600)
     
         
         

def protection():
    def protection_command():
        def search():
            def sea():
                if h!='' or c!='':
                    swindow2=tkinter.Toplevel()
                    fn=h.get()
                    ln=c.get()
                    swindow.destroy()
                    swindow2.title('Passenger Search')
                    swindow2.geometry('550x200+120+120')
                    sql2=("SELECT * FROM passengers WHERE First_name=" + "'"+fn+"'") 
                    mycursor.execute(sql2)
                    results=mycursor.fetchall()
                    x=(tabulate(results,headers=['PNR','First Name','Last Name','Flight No','Checkin Status'], tablefmt='psql'))
                    label=scrolledtext.ScrolledText(swindow2)
                    label.pack()
                    label.insert(tkinter.INSERT,x)
                    label.config(state=tkinter.DISABLED)
                    mydb.commit()
            import mysql.connector
            from tabulate import tabulate
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
            mycursor=mydb.cursor()
            swindow=tkinter.Toplevel()
            tkinter.Label(swindow,text='Enter First Name:').grid(row=1)
            h=tkinter.Entry(swindow,font='Menlo')
            h.grid(row=1,column=2)
            
            tkinter.Label(swindow,text='Enter Surname:').grid(row=2)
            c=tkinter.Entry(swindow,font='Menlo')
            c.grid(row=2,column=2)
            
            tkinter.Button(swindow,text='Submit',width=5,height=1, command=sea).grid(row=3, column=1)
            swindow.title('Search for a passenger')
            swindow.geometry('350x100')
            swindow.configure(bg='white')
            swindow.resizable(0,0)
            
            
            
           
        def p_list():
            import mysql.connector
            from tabulate import tabulate
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
            mycursor=mydb.cursor()
            sql = ("SELECT * FROM passengers")
            mycursor.execute(sql)
            results = mycursor.fetchall()
            x=(tabulate(results, headers=['PNR','First Name','Last Name','Flight Number','Check-in Status'], tablefmt='psql'))
            adwindow=tkinter.Toplevel()
            adwindow.title('Passengers')
            adwindow.geometry('600x400+120+120')
            adwindow.configure(bg='white')
            label=scrolledtext.ScrolledText(adwindow)
            label.pack()
            label.insert(tkinter.INSERT,x)
            label.config(state=tkinter.DISABLED)
            mydb.commit()
            
        
        passw=e.get()
        if passw=='last2012':
            security=tkinter.Toplevel()
            protect.destroy()
            security.title('Airport Personnel')
            security.geometry('700x700+120+120')
            security.configure(bg='sky blue')
            security.resizable(0,0)
            label=tkinter.Label(security,text='A͢i͢r͢p͢o͢r͢t͢ ͢P͢e͢r͢s͢o͢n͢n͢e͢l͢',font='Menlo 50',bg='Sky Blue',bd=10 ,fg='Black').place(x=90,y=10)
            ad=tkinter.Button(security,text='Arrivals and Departures',width=50,height=1,font='Terminal 20',command=AD).place(x=10,y=200)
            search=tkinter.Button(security,text='Search For A Passenger',width=50,height=1,font='Terminal 20',command=search).place(x=10,y=350)
            list_p=tkinter.Button(security,text='List of Passengers',width=50,height=1,font='Terminal 20',command=p_list).place(x=10,y=500)
            list_s=tkinter.Button(security,text='FLights',width=50,height=1,font='Terminal 20',command=flight_seats).place(x=10,y=650)
        else:
            messagebox.showerror("Incorrect Password", "The password you have entered is incorrect")
            protect.destroy()
    protect=tkinter.Toplevel()
    protect.title('Security')
    protect.geometry('500x30+120+120')
    tkinter.Label(protect, text="Please enter the password to continue:").grid(row=1)
    e=tkinter.Entry(protect,show='*',font='Menlo')
    e.grid(row=1, column=2)
    tkinter.Button(protect,text='Submit',width=5,height=1, command=protection_command).grid(row=1, column=5)
window=tkinter.Tk()
window.title('Airport Management System')
window.geometry('800x600+120+120')
window.configure(bg='sky blue')
label=tkinter.Label(window,text='A͢i͢r͢p͢o͢r͢t͢ ͢M͢a͢n͢a͢g͢e͢m͢e͢n͢t͢ ͢S͢y͢s͢t͢e͢m͢',font='Menlo 50',bg='Sky Blue',bd=10 ,fg='Black').place(x=5,y=10)
passen=tkinter.Button(window,text='Passenger',width=20,height=5,font='Courier 30',command=civilians).place(x=200,y=150)
security=tkinter.Button(window,text='Airport Personnel',width=20,height=5,font='Courier 30',command=protection).place(x=200,y=400)

window.mainloop()

mydb=mysql.connector.connect(host='localhost',user='root',passwd=password1,database=database1,auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
for book3 in booking_tables:
    delete_query2='Drop table '+book3
    mycursor.execute(delete_query2)
mydb.commit()
