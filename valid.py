print("--------------------------------------------")
#name
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
 #adhar       
while True:
    adar=input("enter the Adhar number number : ")
    if adar.isdigit():
        if len(adar) == 12:
            print(f"your Adhar number is {adar}")
            break
        else:
            print("enter valid Adhar Number of 12 digits ")
    else:
        print("Adhar should not be alphabets and Empty")
#PAN
while True:
    pan=input("enter the PAN number number : ")
    if pan.isalnum():
        if len(pan) == 10:
            print(f"your PAN number is {pan}")
            break
        else:
            print("enter valid PAN Number of 10 digits ")
    else:
        print("PAN should not be Empty")
        
while True:
    doc=input("All the above Documents are available ? Yes/No:  ")
    if doc.lower() == 'yes' or doc.lower() == 'no':
        break
    else:
        print("Please provide yes or no info only")
        
print("--------------------------------------------")

print("Your Final details are:\n Firstname:{fname},\n Lastname:{lname},\n Phone No:{phn},\n Age:{age},\n Salary:{sal},\n City:{city},\n Pincode:{pin},\n Department:{dep},\n Adhar:{adar},\n PAN:{pan} ")