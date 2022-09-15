
from calc import *
import module.calc1 as c
from module import calc1 as c1

def details():
    name=input("enter name")
    age=int(input("enter age"))
    bsal=int(input("Enter basic salary"))
    hr=hra(bsal)
    d=c.da(bsal)
    bous=bonus(bsal)
    tot=bsal+hr+d+bous
    print("----------------")
    print(f"name is:{name}")
    print(f"name is:{age}")
    print(f"Total CTC is:{tot}")


details()
    

    
    
