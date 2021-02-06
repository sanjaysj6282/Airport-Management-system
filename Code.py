
#Mysql connection
import mysql.connector as sql
mycon=sql.connector.connect(host="localhost",user="root",passwd="arya123")
#To check wheather python is successfully connected to SQL
if mycon.is_connected():
    print "Successfully Connected"
else:
    print "Connection failed"

cursor=mycon.cursor()
cursor.execute("use mysql")

#To create table PASSPORT
cursor.execute("create table PASSPORT(Passport_Number varchar(20),Passport_Name varchar(20))")

cursor.execute(“insert into PASSPORT values ('P 7896324','Lolan K')
cursor.execute(“insert into PASSPORT values ('G 8521497','Shambu B')
cursor.execute(“insert into PASSPORT values ('S 5214488','Shibu C S')
cursor.execute(“insert into PASSPORT values ('H 5214986','Nikhil U')
cursor.execute(“insert into PASSPORT values ('K 87964114','George K')
cursor.execute(“insert into PASSPORT values ('G 8521469',Babu Nambuthiri')
cursor.execute(“insert into PASSPORT values ('L 8469712','Sura Nambuthiri')
cursor.execute(“insert into PASSPORT values ('H 8246971,'Vaidhyanathan K')
cursor.execute(“insert into PASSPORT values ('N 8936147','Veni D')
cursor.execute(“insert into PASSPORT values ('K 9631721','Kunjappan B')
cursor.execute(“insert into PASSPORT values ('M 8547964','Abhijith A')
cursor.execute(“insert into PASSPORT values ('Q 9631458','Varun C')
cursor.execute(“insert into PASSPORT values ('T 7531495','Abhiram K')
cursor.execute(“insert into PASSPORT values ('P 8214544','Adarsh R')
cursor.execute(“insert into PASSPORT values ('W 852444','Damodaran A')
cursor.execute(“insert into PASSPORT values ('R 7924741',Mothilal B')
cursor.execute(“insert into PASSPORT values ('U 7963154','Tovino T ')
cursor.execute(“insert into PASSPORT values ('K 6529629','Sreeja N')
cursor.execute(“insert into PASSPORT values ('P 7896324','Lolan K')
cursor.execute(“insert into PASSPORT values ('H 2648309','Kumar VT')
cursor.execute(“insert into PASSPORT values ('V 6492879','Robert Downey')
cursor.execute(“insert into PASSPORT values ('X 1188553','Chris Evans ')
cursor.execute(“insert into PASSPORT values ('C 2361986','Sanjay ')
cursor.execute(“insert into PASSPORT values ('D 1329854','Abhiram KK')
cursor.execute(“insert into PASSPORT values ('G 1329467','Abhijith S')
cursor.execute(“insert into PASSPORT values ('J 2548326','Ajay D')
cursor.execute(“insert into PASSPORT values ('H 2809329','Jacob B')
cursor.execute(“insert into PASSPORT values ('J 9648752','Raji')
cursor.execute(“insert into PASSPORT values ('G 2555529','Baby John')
cursor.execute(“insert into PASSPORT values ('E 7842164','Arjun B')
cursor.execute(“insert into PASSPORT values ('D 4832147','Joy TK')
cursor.execute(“insert into PASSPORT values ('H 7963258','Sabastian')
cursor.execute(“insert into PASSPORT values ('S 893215','Mariyam')
cursor.execute(“insert into PASSPORT values ('Q 563107','Jose')
cursor.execute(“insert into PASSPORT values ('R 9634875','Mohanlal')
cursor.execute(“insert into PASSPORT values ('M 4257896','Vijay')
cursor.execute(“insert into PASSPORT values ('P 1879634','Surya')
cursor.execute(“insert into PASSPORT values ('U 7946137','Mamotty')
cursor.execute(“insert into PASSPORT values ('T 418679','Suresh PK')
cursor.execute(“insert into PASSPORT values ('Z 4791567','Williams')
cursor.execute(“insert into PASSPORT values ('H 1348794','Anu')
cursor.execute(“insert into PASSPORT values ('D 3846215','Aadra')
cursor.execute(“insert into PASSPORT values ('A 9645259','Akhila')
cursor.execute(“insert into PASSPORT values ('S 9624587','Anupama')
cursor.execute(“insert into PASSPORT values ('N 9648752','Sahil')
cursor.execute(“insert into PASSPORT values ('Y 2864791','Pranav')
cursor.execute(“insert into PASSPORT values ('V 9647252','Alen ST')
cursor.execute(“insert into PASSPORT values ('X 3549712','Vaishnav MT')
cursor.execute(“insert into PASSPORT values ('C 8954852','Samyuktha M')
cursor.execute(“insert into PASSPORT values ('B 9685741','Janaki Devi')
cursor.execute(“insert into PASSPORT values ('R 9625143','Ramachandran')
cursor.execute(“insert into PASSPORT values ('U 3614857','Nivin P')

#To create table Flight
cursor.execute("create table Flight(Flight_Number varchar(20),Flight varchar(30),Boarding varchar(30),Destination varchar(20),Date date,price")

cursor.execute(“insert into Flight values ('6E 450', 'Singapore Airlines','Chennai','Srinagar','2019/5/12',)
cursor.execute(“insert into Flight values ('5A 268','Spicejet airlines','Chennai','Srinagar,'2019/7/5',)
cursor.execute(“insert into Flight values ('6G 246','Indigo airlines',:Chennai','Srinagar','2019/6/8',)
cursor.execute(“insert into Flight values ('7S 908,'Air India','Chennai','Srinagar','2019/5/9',)
cursor.execute(“insert into Flight values ('2J 550,'Kingfisher Airlines','Chennai','Singar','2019/10/3',)
cursor.execute(“insert into Flight values ('6E 451', 'Singapore Airlines','Srinagar,'Kanyakumari','2019/12/12',)
cursor.execute(“insert into Flight values ('5A 269','Spicejet airlines','Srinagar,'Kanyakumari,'2019/2/5',)
cursor.execute(“insert into Flight values ('6G 247','Indigo airlines',Srinagar,'Kanyakumari','2019/6/4',)
cursor.execute(“insert into Flight values ('7S 909,'Air India','Srinagar,'Kanyakumari','2019/5/6',)
cursor.execute(“insert into Flight values ('2J 551,'Kingfisher Airlines','Srinagar,'Kanyakumari','2019/11/3',)
cursor.execute(“insert into Flight values ('6E 452', 'Singapore Airlines','Hyderabad,'Bangalore','2019/7/12',)
cursor.execute(“insert into Flight values ('5A 270','Spicejet airlines','Hyderabad,'Bangalore,'2019/2/7',)
cursor.execute(“insert into Flight values ('6G 248','Indigo airlines',Hyderabad,'Bangalore','2019/6/4',)
cursor.execute(“insert into Flight values ('7S 910,'Air India','Hyderabad,'Bangalore','2019/5/10',)
cursor.execute(“insert into Flight values ('2J 552,'Kingfisher Airlines','Hyderabad,'Bangalore','2019/8/3',)
cursor.execute(“insert into Flight values ('6E 453', 'Singapore Airlines','Delhi,'Trivandrum','2019/9/12',)
cursor.execute(“insert into Flight values ('5A 271','Spicejet airlines','Delhi,'Trivandrum,'2019/5/7',)
cursor.execute(“insert into Flight values ('6G 249','Indigo airlines',Delhi,'Trivandrum','2019/2/4',)
cursor.execute(“insert into Flight values ('7S 911,'Air India','Delhi,'Trivandrum','2019/5/11',)
cursor.execute(“insert into Flight values ('2J 554,'Kingfisher Airlines','Patna,'Mumbai','2019/10/3',)
cursor.execute(“insert into Flight values ('6E 454', 'Singapore Airlines','Patna,'Mumbai','2019/9/9',)
cursor.execute(“insert into Flight values ('5A 272','Spicejet airlines','Patna,'Mumbai,'2019/5/8',)
cursor.execute(“insert into Flight values ('6G 250','Indigo airlines',Patna,'Mumbai','2019/7/4',)
cursor.execute(“insert into Flight values ('7S 912,'Air India','Patna,'Mumbai','2019/6/11',)
cursor.execute(“insert into Flight values ('2J 555,'Kingfisher Airlines','Patna,'Mumbai','2019/11/4',)
cursor.execute(“insert into Flight values ('6E 455', 'Singapore Airlines','Mumbai','Kolkata','2019/10/9',)
cursor.execute(“insert into Flight values ('5A 273','Spicejet airlines','Mumbai','Kolkata,'2019/11/8',)
cursor.execute(“insert into Flight values ('6G 251','Indigo airlines',Mumbai','Kolkata','2019/7/12',)
cursor.execute(“insert into Flight values ('7S 913,'Air India','Mumbai','Kolkata','2019/6/1',)
cursor.execute(“insert into Flight values ('2J 556,'Kingfisher Airlines','Kolkata','Chennai','2019/1/5',)
cursor.execute(“insert into Flight values ('6E 456', 'Singapore Airlines','Kolkata','Chennai','2019/1/9',)
cursor.execute(“insert into Flight values ('5A 274','Spicejet airlines','Kolkata','Chennai,'2019/1/8',)
cursor.execute(“insert into Flight values ('6G 252','Indigo airlines','Kolkata','Chennai','2019/7/12',)
cursor.execute(“insert into Flight values ('7S 914,'Air India','Kolkata','Chennai','2019/6/3')
cursor.execute(“insert into Flight values ('2J 557,'Kingfisher Airlines','Kolkata','Chennai','2019/1/11')
cursor.execute(“insert into Flight values ('6E 457', 'Singapore Airlines','Punjab','Haryana','2019/4/9')
cursor.execute(“insert into Flight values ('5A 275','Spicejet airlines','Punjab','Haryana','2019/1/6')
cursor.execute(“insert into Flight values ('6G 253','Indigo airlines','Punjab','Haryana','2019/11/12')
cursor.execute(“insert into Flight values ('7S 915,'Air India','Punjab','Haryana','2019/2/3')
cursor.execute(“insert into Flight values ('2J 558','Kingfisher Airlines','Punjab','Haryana','2019/2/11')
cursor.execute(“insert into Flight values ('6E 458', 'Singapore Airlines','Goa','Kolkata','2019/4/9')
cursor.execute(“insert into Flight values ('5A 276','Spicejet airlines','Goa','Kolkata','2019/10/6')
cursor.execute(“insert into Flight values ('6G 254','Indigo airlines','Goa','Kolkata','2019/11/12')
cursor.execute(“insert into Flight values ('7S 916,'Air India','Goa','Kolkata','2019/2/3')
cursor.execute(“insert into Flight values ('2J 559','Kingfisher Airlines','Goa','Kolkata','2019/4/11')
cursor.execute(“insert into Flight values ('6E 459', 'Singapore Airlines','Thiruvananthapuram','Ranchi','2019/7/9')
cursor.execute(“insert into Flight values ('5A 277','Spicejet airlines','Thiruvananthapuram','Ranchi','2019/10/9')
cursor.execute(“insert into Flight values ('6G 255','Indigo airlines','Thiruvananthapuram','Ranchi','2019/11/12')
cursor.execute(“insert into Flight values ('7S 917','Air India','Thiruvananthapuram','Ranchi','2019/2/6')
cursor.execute(“insert into Flight values ('2J 560','Kingfisher Airlines','Thiruvananthapuram','Ranchi','2019/2/11')

#To create table Book
cursor.execute("create table Book(Passport_Number varchar(20),Passport_Name varchar(20),Airline varchar(20),Boarding varchar(30),Destination varchar(30),Class varchar(20),Date date")

#print(“'Flights available are:
                      Vistara
                      Air India
                      Fly emirates
                      Qatar Airways
	   Singapore airlines”')

                       
def planes(place):
     Chicago              
     San Fransicso
     Colombia(SL)  
     Bangkok
     New York
     Ontario
     Hong Kong
     Switzerland
     Delhi


#Function to check whether a passport exists or not
def check(x,y):
     cursor.execute("select Passportnumber from PASSPORT")
     data=cursor.fetchall()
     for i in data:
         if i==x:
            print(“Passport exists”)

#Function to check the available flights
def Flights_available( From,To, Date1):
     cursor.execute("select * from Flight where Boarding=From,Destination=To,Date=Date1")
     data1=cursor.fetchall()
     for i in data:
         print(i)
 
#Function to book flight
def  book(x,y,date):
      check(x,y)
       print(“Enter the Details”)       
       From=raw_input(“From”)
       To=raw_input(“To”)
       Date=raw_input(“Date”)
       Class=raw_input(“Business /Economy “)
       
        Flights_available( From,To, Date)
       
        R=raw_input(“Enter the Airline”)
        
        cursor.execute("insert into  Book(x,y, R,From, To, Class,Date)")
 
#Function to search
def search():
     print(“Enter Search based on 1-Passport Number     
                                                     2-  Flight
                                                     3-Date”)
      choice=raw_input(“Enter the choice”)
      if choice==1:
          Pno=raw_input(“Enter the Passport Number”)
          cursor.execute("select * from Booked where Passport_Number=Pno")
      elif choice==2:
           Flight=raw_input(“Enter the Flight”)
           cursor.execute("select * from Booked where Airline=Flight")
      elif choice==3:
            date=raw_input(“Enter the Date”)
            cursor.execute("select * from Booked where Date=date")
       for i in data:
            print i
#Function to cancel booking
def cancel():
      Pno=raw_input(“Enter the Passport Number”)
      date=raw_input(“Enter the Date”)
      cursor.execute("delete from Booked where Passport_Number=Pno,Date=date")

print(“AIRLINE BOOKING SYSTEM”)

while True:
         print("Do you want to continue")
         ch=raw_input("Enter your choice Y to continue,N to stop")
         if ch==Y:
             print(“Enter 1-Cancel Booking
                    2-Search flight
                    3-Book Flight”)

              function=raw_input(“Enter your choice”)
              if function==1:
                  cancel(Pno, Pname)

              elif function==2:
                   search()

              elif function==3:
                    Pno=raw_input(“Enter the Passport Number”)
      	 Pname==raw_input(“Enter Name”)
     	 book(Pno, Pname)

               else:
     	 print(“Inavlid choice”)

         elif ch==N:
               break
       
         else:
                print("Invalid choice")










