
import random
import string
import mysql.connector

def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print('Welcome To INDIRA GHANDHI INTERNATIONAL AIRPORT')
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
      print('put function for booking of mysql for booking here')
  if (b.upper()=='W'):
       pnr = input("Enter your PNR number: ")
       name = (input("Enter your Last name: ")).upper()
       print('funtion for doing web checking with mysql')
        #function for web checking with mysql here
  elif (b.upper()=='D'):
        print('put function for displaying arrivals and departures from table here')
                 #function for displaying departures           
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
            count=5
            for i in range(1,count+1):
                 print('Please Enter Your Password:')
                 c=str(input(':'))
                 if c==passw:
                        print('Password Correct Security Mode Activated')
                        break
                 elif c!=passw:
                     count-=1
                     if count==0:
                              print('You Have Exhausted Your chances.Please Contact the Nearest Station for Help')  
                              break
                         
                     print('Password Incorrect You have',count,'Chances left Try Again' )
                       
                     
                
                     
                        
                    
                
                     
            
              
               
        
