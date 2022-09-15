import mariadb
con = mariadb.connect(
    user='root',
    password='250105',
    host='localhost',
    port=3306,
    database='employ' )
con.autocommit=True
cur=con.cursor()

try:
    cur.execute("create table emp11(fname varchar(10),lname varchar(10),phn bigint(20),age int(10),salary int(10),city varchar(10),dep varchar(15),pincode int(8))")
    print("created")
except Exception as e:
    print("error")


while True:
    fname=input("enter the first name: ")
    lname=input("enter the Last name: ")
    if str(fname).isalpha() and str(lname).isalpha():
        print(f"Your full name is {fname}{lname}")
        break     
    else:
        print("enter valid name.. name should be alphabets and not empty")
#phone
while True:
    phn=input("enter the phone number: ")
    if phn.isdigit():
        if len(phn) == 10:
            print(f"your Phone number is {phn}")
            break
        else:
            print("enter valid mobile number of 10 digits ")
    else:
        print("Phone numbers should not be alphabets and Empty")
#age        
while True:
    age=input("enter the Age: ")
    if age.isdigit():
        if int(age) >= 20:
            print(f"your Age is {age}")
            break
        else:
            print("enter valid age should be greater than 20 ")
    else:
        print("Age should not be alphabets and empty")
#salary        
while True:
    sal=input("enter the Salary: ")
    if sal.isnumeric():
        if int(sal) > 0:
            print(f"your Salary is {sal}")
            break
        else:
            print("enter valid salary that cannot be -ve ")
    else:
        print("Salary should not be alphabets and empty")
 #city       
while True:
    city=input("enter the City: ")
    if city =='':
        print("enter valid City name ")
    else:
        print(f"your City is {city}")
        break
#department    
while True:
    dep=input("enter the Department: ")
    if dep =='':
        print("enter valid Department name ")
    else:
        print(f"your Department is {dep}")
        break
 #pincode   
while True:
    pin=input("enter the Pincode number of City: ")
    if pin.isdigit():
        if len(pin) == 6:
            print(f"your Phone number is {pin}")
            break
        else:
            print("enter valid Pincode of 6 digits ")
    else:
        print("Pincode should not be alphabets and Empty")





quer="insert into emp11(fname,lname,phn,age,salary,city,dep,pincode) values(%s,%s,%d,%d,%d,%s,%s,%d)"
val=(fname,lname,int(phn),int(age),int(sal),city,dep,int(pin))
cur.execute(quer,val)
##    cur.execute("select * from emp1")
print("inserted")






