#Operators:In python operators used to perform operations between two opearnds or tw o variables.
#Arthemeetic opeartors,assiagnment opeartors,logical operators,Equality operators,
#Comparision operators,chaining operators,Teranary opeartors,Bitwise operators,Special Type of operators.
#Arthemetic operators: Used to perform mathamatical operations between two variables or two opearnds.
#Examples:
import time
x1=eval(input("Enter the number:"))
x2=eval(input("enter the number:"))
a1=x1+x2
a2=x1-x2
a3=x1*x2
a4=x1/x2
a5=x1//x2
a6=x1%x2
print("=====After_operations====")
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print()
time.sleep(2)
print("end of application")

# Assignment operators: Used to perform operations by utilizing memory management.
#x1+=x2,x1-=x2,x1*=x2....Etc.
#Examples:

import time
x1=eval(input("enter the number:"))
x2=eval(input('enter the number:'))
x1+=x2
print(x1)
x1-=x2
print(x1)
x1*=x2
print(x1)
x1/=x2
print(x1)
print()
time.sleep(2)
print("end of application")

#Logical Operators: Used to perform Logical operations as per the application requremnt.
#Logical operators are AND , OR , NOT.
#Lgical AND operator: Logical AND operator returns True if the both or each condition true.
#If at least one condition is false then total thing will be false.
# Example:
import time
My_Email="kiran83118311@gmail.com"
Password="Chandu@143"
if My_Email=="kiran83118311@gmail.com":
    print("Your Gmail acoount Fetched succesefully...")
    if Password=="Chandu@143":
        print("Login succesefully..")
    else:
        print("Incorrect password.......")
print()
time.sleep(2)
print("end of application")

######

import time
My_Email="kiran83118311@gmail.com"
Password="Chandu@143"
if My_Email=="kiran83118311@gmail.com" and Password=="Chandu@143":
    print("Your Gmail acoount Fetched succesefully...")
else:
    print("Incorrect deatils..Account not found....")
print()
time.sleep(2)
print("end of application")

#Logical OR operator: It returns true if at least one condition is true.
#Example;

import time
employee_permission_letter="True"
employee_ID_CARD="False"
if employee_permission_letter=="True" or employee_ID_CARD=="False":
    print("Allowed for working.....")
print()
time.sleep(2)
print('end of application')

##Example2;
import time
mobile_number="7013234455","9490151726","9390727285"
if mobile_number=="7013234455" or "9490151726" or "9390727285":
    print("Mobile_number_matches succesfully.....")
    print()
print()
time.sleep(2)
print("end of application")
##
# Equality operators:In pythin equality opearators used to content comaparision and rturns boolean values.
#Equality operators are == amd != (Equal to and not equal to).
#Exampes:

import time
l1=[1,2,3,4,5,6]
l2=[6,5,4,3,2,1]
print(type(l1))
print(type(l2))
print()
print(l1==l2)
print()
print(l1!=l2)
print()
print(type(l1==l2))
print(type(l1!=l2))
print()
time.sleep(2)
print("end of application")

#Example2:

import time
str1="Python"
str2="Full-stack python"
obj1=str1==str2
print(obj1)
obj2=str1!=str2
print(obj2)
print(type(obj1))
print(type(obj2))
print()
time.sleep(2)
print("end of application")

#Example3:

import time
age=24
name="chandra kiran"
if age==24 and name=="chandra kiran":
    print("Eligible for voting.....")
else:
    print("Not eligible for voting......")
print()
time.sleep(2)
print("end of application")

#Example:

import time
chandu_age=25
kiran_age=23
print(chandu_age==kiran_age)
print(type(chandu_age==kiran_age))
print(chandu_age!=kiran_age)
print(type(chandu_age!=kiran_age))
print()
time.sleep(2)
print("end of application")

#Comparision operators:Used to compare the variables or operands.
#Comparisionoperators are < and > and <= and >= .

#Examples:

import time
num1=120
num2=240
print(type(num1) and type(num2))
print("==Comparision_opeartors===")
print(num1<num2)
print(type(num1<num2))
print()
print(num1>num2)
print(type(num1>num2))
print()
print(num1<=num2)
print()
print(num1>=num2)
print(type(num1>=num2))
print()
time.sleep(2)
print("end of application")

#Example:

import time
str1="kiran"
str2="chandra"
print(type(str1) and type(str2))
print()
print(str1<str2)
print(str1>str2)
print(str1<=str2)
print(str1>=str2)
print()
print(type(str1<str2),type(str1>str2),type(str1<=str2),type(str1>=str2))
print()
time.sleep(2)
print("end of application")