#RESTAURANT MANAGEMENT PROJECT
import mysql.connector

#establing the connection with mysql

mydb =mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="restaurant"
       )

c=mydb.cursor()

c.execute("create table if not exists HOTEL_SWEET_HEART(MENUID int(20), NAME  varchar(40), PRICE int(10))")
c.execute("insert into HOTEL_SWEET_HEART (MENUID, NAME, PRICE) VALUES (100,'CORN SOUP',120), (101,'VEG CURRY',220),(102, 'NONVEG CURRY', 250), (103, 'VEG BIRYANI', 270), (104,'CHICKEN BIRYANI', 300), (105,'COOL DRINK',30),(106, 'ICE CREAM', 50);")
mydb.commit()
yesOrNo = input("Are you Admin y or n?------")


def doAddMoreOrders():
    addOrders = "y"
    totalBill = 0
    while  addOrders =="y":    
        order=input("Please Enter Menu Id to Order : ")
        isRecordExists = False
        
        for x in records:
            if int(order) == x[0]:  #x [0] means table id number that is menuid number
                isRecordExists = True
                totalBill = totalBill + int(x[2])  #x[2] means table no 3 menu price 
                break
                
        if isRecordExists == True:
            addOrders = input("Added Menu Item Successfully In Your Order List. Do You Want To Add More y or n : ")            
        else:
            print("Menu Id not present in menu Id please provide a correct menu Id.") 
    
    
    return totalBill

def admintask(yesOrNo) : 
    while yesOrNo == "y":
     print("1. ADD A NEW RECORD")
     print("2. View All The Menu list")  
     print("3. SEARCH FOR A MENU ITEM") 
     print("4. Change the Price of a Menu Item")
     print("5. Delete a Menu Item") 
     ch=int(input("Enter Your Choice : "))
     if ch==1:
        
        print(" Add a New Record ")
        id=int(input("ENTER YOUR MENU ID : "))
        menunm=input("ENTER NAME OF MENU : ")
        Price=input("ENTER PRICE OF MENU : ")
       
        sql="insert into HOTEL_SWEET_HEART values(%s,%s,%s)"
        val=(id,menunm,Price) 

        c.execute(sql,val)
        mydb.commit() 
        print("Record Added Successfully ")
        print("*****************************")
        
     elif ch==2:  
        print("View All The Menu list is ")
        c.execute("select * from HOTEL_SWEET_HEART ")
        records=c.fetchall()
        for x in records:
           print(x)
        print("************************************")  
        
     elif ch==3:
        MENUID=input("Enter MenuId Number That You Want To Search : ")
        c.execute("select * from HOTEL_SWEET_HEART where MENUID="+MENUID)
        records=c.fetchall()
        for x in records:
           print(x)
        print("************************************")  
        
     elif ch==4:
        MENUID=input("Enter MenuId Number That Price You Want To Change : ")
        Price=input("Enter Price of Menu That You Want Change : ")
        c.execute("UPDATE HOTEL_SWEET_HEART SET PRICE =" + Price + " where MENUID =" + MENUID)
        mydb.commit()
        c.execute("select * from HOTEL_SWEET_HEART where MENUID="  +MENUID)    
        records=c.fetchall()
        for x in records:
           print(x)
        print("Price Changed Successfully!!!!!!")
        print("*****************************************")
        
        
     elif ch==5:
        MENUID=input("Enter MenuID Number That You Want To Delete : ")
        c.execute("DELETE FROM HOTEL_SWEET_HEART WHERE MENUID=" +MENUID)
        mydb.commit()
        count = c.rowcount
        print("Deleted records - " + str(count))
        if count>0:
          print("Menu Deleted Successfully!!!!")
        else:
          print("Please Select Correct Menu ID... ")
        print("*************************************")  
        
        
     else:
       print("Wrong Choice!!!!!") 
       break

if yesOrNo == "y":
   def login(user,pas):
        global dic        
        dic={
            'username':'password',
            'swamy':'bhadra0593'
            }
   
        if (user not in dic) or (dic[user]!=pas):                    
            return False
        else:
           return True
 
   username=input('Enter Your Username : ')  
   password=input('Enter Your Password : ')  
   isValid = login(username,password)
 
   if isValid:
      print("Logged in successfully")
      print("*******************************")
      admintask(yesOrNo)
   else:
      print("Invalid username or password")
      yesOrNo = "n"
      
else :
    print("***********************************")
    print("|| WELCOME TO HOTEL_SWEETHEART ||")
    print("***********************************")
    cname=input("Please Enter Your Name Sir/Mam :  ")
    print("***************************************")
    
    #print all menu list
    print("Here is List of All Menues Please select Menu from the List  ")
    c.execute("select * from HOTEL_SWEET_HEART ")
    records=c.fetchall()
    for x in records:
       print(x)
    print("************************************")   
    totalBill = doAddMoreOrders()
    print("************************************")
    print("Your total bill is ", totalBill)
    print("************************************")
    print("Thank you " + cname + ", please visit again!!!") 

    
 
    
    
    
    
    
    
    

       
   
