#Driver Code for backend 
import mysql.connector
import random
import string
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
#Temporary delete function, will update when alen finishes his work
delete=input('Would you like to delete the seat tables now?(Y/N)')
if delete=='Y' or delete=='y':
    for book3 in booking_tables:
        delete_query2='Drop table '+book3
        mycursor.execute(delete_query2)
    
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

print('Welcome To INTERNATIONAL AIRPORT✈ ')
print('Enter P for Passengers')
print('Enter S for Security Personnal')
print('Enter E to Exit')
a=input('Enter Your Choice:')
if (a.upper()=='P'):
  print('Enter W for Web Checking')
  print('Enter B for Booking Tickets')
  print('Enter D for Departures AND Arrivals')
  b=input('Enter Your Choice:')
  if (b.upper()=='B'):
      fname=input("enter your first name")
      lname=input("enter your last name")
      flight_num=input("enter flight number ")
      pnr=id_generator()
      query="insert into passengers values (%s,%s)"
      tuple1=(pnr,fname,lname,flight_num,"Pending")
      mydb.execute(query,tuple1)
  if (b.upper()=='W'):
      mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airport3')
      mycursor=mydb.cursor()
      h= input("Enter your PNR number: ")
      name = (input("Enter your Last name: ")).upper()
      sql=mycursor.execute("UPDATE passengers WHERE First_name LIKE %s", ("%" + h + "%",))
      mycursor.execute(sql)
      print('Web Checking Done')      
  elif (b.upper()=='D'):
        import mysql.connector
        from tabulate import tabulate
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airport3')
        mycursor=mydb.cursor()
        sql = ("SELECT * FROM flights")
        mycursor.execute(sql)
        results = mycursor.fetchall()
        print(tabulate(results, headers=['Flight Name','Flight Name','Source','Destination','Departure Time', 'Connecting Flight Available'], tablefmt='psql'))        
  else:
        print('Wrong command')      
if (a.upper()=='S'):
        countcapt=3
        j=randomString()
        print ("Please Enter this Captcha for Human Verification-->",j)
        security='NO'
        for i in range(countcapt):
            g=str(input('Enter The Text Displayed Above:'))
            if g==j:
               print('Correct Captcha Verification done ✓')
               security='OK'
               break
            else:
                print('Wrong Captcha Try Again') 
        else:
            print('Wrong Captcha Entered multiple Times Try Again later')
        if security=='OK':
           
            passw='last2012'
            mode='user'
            count=5
            for i in range(1,count+1):
                 print('Please Enter Your Password:')
                 c=str(input(':'))
                 if c==passw:
                        print('Password Correct Security Mode Activated 🔓')
                        mode='true'
                        break
                 elif c!=passw:
                     count-=1
                     if count==0:
                              print('You Have Exhausted Your chances.Please Contact the Nearest Station for Help 🔒')  
                              break         
                     print('Password Incorrect You have',count,'Chances left Try Again')
            if mode=='true':
                 print("")   
                 print('Airport Security Terminal🛡')
                 import time
                 import sys
                 animation = "|/-\\"
                 for i in range(30):
                     time.sleep(0.1)
                     sys.stdout.write("\r" + animation[i % len(animation)])
                     sys.stdout.flush()
                 print('\rTerminal Loaded')
                 print("")
                 print("Enter ad for Today's Arrival and Departure.")
                 print("")
                 print('Enter search to Find a specific Passenger.')
                 print("")
                 print('Enter your command')
                 g=str(input(':'))
                 if (g.upper()=='AD'):
                    import mysql.connector
                    from tabulate import tabulate
                    mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airport3')
                    mycursor=mydb.cursor()
                    sql = ("SELECT * FROM flights")
                    mycursor.execute(sql)
                    results = mycursor.fetchall()
                    print(tabulate(results, headers=['Flight Name','Flight Name','Source','Destination','Departure Time', 'Connecting Flight Available'], tablefmt='psql'))
                 elif (g.upper()=='SEARCH'):
                     import mysql.connector
                     from tabulate import tabulate
                     mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airport3')
                     h=str(input('Enter First Name:'))
                     c=str(input('Enter Sir Name:'))
                     mycursor=mydb.cursor()
                     sql2=mycursor.execute("SELECT * FROM passengers WHERE First_name LIKE %s", ("%" + h + "%",)) #PARTIALLY WORKS
                     mycursor.execute(sql2)
                     results=mycursor.fetchall()
                     print(tabulate(results, headers=['PNR','First Name','Last Name','Flight No.','Checkin Status'], tablefmt='psql'))
                 else:
                     print("Wrong Comannd Pls Try Again")
