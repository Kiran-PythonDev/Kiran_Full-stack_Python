#List: It is a Mutable data type That means we can change or modify values in list.
#duplicates and hetereogeneous objects are allowed.
#Listvcan be indicated by.[]
#Examples:

import time
l1=[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
print(l1)
print(type(l1))
print("==Before_operations==")
print(l1)
print('==After_Operations==')
l1[0]="kiran"
l1[1]="chandu"
l1[2]="chandra kiran"
l1[3]="python"
l1[4]="python developer"
l1[5]="Full_stack_python_developer"
print(l1)
print(l1[2])
print(l1[3])
print(l1[4])
print()
time.sleep(2)
print("end of appliacation")
#Predefined functions in list:
#Append(),remove(),clear(),sort(),pop(),insert(),copy(),len(),index(),Extend().
#Examples:
#append() and remove(): We cana dd and remove objects in list data.
#clear() and copy(): clear used to delete the entire lost and copy used to copy the entire list.
#insert(): Used to insert the value using indexing posistaion.
#pop(): Used to remove objects from list withou parameter removes last object and with parameter can delete specific oject in list.
#sort(): Used to arrange list data in ascending order.
#index(): Used to find the indexing posisation of ibject in list.
#extend(): Used to combine the lists together like adding two lists.

# Examples:

import time
l1=[1,"kiran",2,"chandu",3,"hello",4,"chandra kiran"]
l1.append("python")
print(l1)
l1.remove("kiran")
print(l1)
l1.copy()
print(l1)
l1.clear()
print(l1)
l1.insert(1,"Full_stack_Pyhton_Developer")
print(l1)
l1.pop()
print(l1)
l1.sort()
print(l1)
l2=[1,2,3,4,5,6,7]
l2.sort()
print(l2)
print()
print()
time.sleep(2)
print("end of application")


##Tuple is Immutable object data type and indicated by.()
#Predefined functions in tuple: max(),min(),len(),index().
#Example:

import time
tuple1=(1,3,2,4,3,4,5,6,7,5,43,6)
print(tuple1)
print(max((tuple1)))
print(min((tuple1)))
print(len((tuple1)))
print(tuple1.index(43))
print()
time.sleep(2)
print("end of application")
#In tuple we cannot change or modift values or objects thats why immutable.
#But in list we can modify or change the values or objects thats why mutable.

#Set data types is an mutable data type.
#set does not accept duplicate objects.
#set data type can not be update or modified becuse set doesnot support indexing and slicing methodology.
#empty set will be by default dictionary data type.
#set indicated by{}.
#set predefined functions: add(),remove().
#Examples:

import time
set1={}
print("empty set by default as dictionary")
print(type(set1))
print()
time.sleep(2)
print("end of application")

#
import time
s1={1,2,4,1,2,4}
print("Set not allows duplicates objects")
print(s1)
print(type(s1))
time.sleep(2)
print("end of application")

#

import time
s1={1,2,3,4}
print(type(s1))
s1.add(5)
s1.add(6)
s1.add(7)
print(s1)
s1.add("python")
s1.add("chandra_kiran")
s1.add("full_stack_developer")
print(s1)
print()
s1.remove(1)
s1.remove(2)
s1.remove(3)
s1.remove(4)
s1.remove(5)
s1.remove(6)
s1.remove(7)
print(s1)
print()
time.sleep(2)
print('end of application')

#Dictionary Data type:Dictioinary data can be representd in the form of key and vslue pair.
#dictionary can be indicted by{}.
#Dictionary data type is an mutable object data type.
#Dictionary data type predefined functiions:
#keys(),values(),items(),clear(),copy(),pop(),popitem(),sorted(),updtae(),get().
#Exampels:

import time
d1={"name":"chandra kiran","age":25,"gender":"male"}
print(d1)
print(type(d1))
print()
time.sleep(2)
print("end of appliacation")

#Example:
import time
d1={"name":"chandra kiran","age":25,"gender":"male","cource":"full_stack_python","feez":30000}
print(d1)
print(type(d1))
print()
print(d1.keys())
print(d1.values())
print(d1.copy())
print(d1.items())
print(d1.popitem())
print(d1.update({"hello":"world"}))
print(d1)
print(d1.pop("name"))
print(d1.get("cource"))
print(d1.clear())
print(d1)
print()
time.sleep(2)
print("end of applciation")

#Byte and byte array data type:
#Firstly byte data type. It is a immutale data type.
#Byte data type is used to work o audio and video and semi strcture fules.
#While working with byte data type range must be with in 255 bytes.
#EXAMPLES:

import time
l1=[1,2,3,4,5,6,7]
obj1=bytes(l1)
print(obj1)
print()
print(type(obj1))
print()
time.sleep(2)
print('end of application')

##
import time
t1=(1,2,3,4,5,6)
print(type(t1))
print()
obj1=bytes(t1)
print(obj1)
print(type(obj1))
print()
time.sleep(2)
print("end of applicatipn")

#

import time
l1=[123,23,34,45,56,254]
print(type(l1))
obj1=bytes(l1)
print(*obj1)
print(type(obj1))
print()
time.sleep(2)
print("end of application")

#Byte array data type is also exactly same as bytes data type.
#byte array data type is mutable data type.
#EXAMPLE:
import time
l1=[1,2,3,4,5,67,78]
print(type(l1))
obj1=bytearray(l1)
print(obj1)
print(type(obj1))
print("Immutale Data type")
obj1[0]=45
obj1[1]=54
obj1[2]=67
obj1[3]=89
print(obj1)
print(type(obj1))
print()
time.sleep(2)
print("end of application")
##Frozen set data type:
# set and frozen set data type are same but set data type is mutable and frozenset is immutale.
#Example;

import time
s1={1,2,3,4,5,6,7,8}
print(s1)
print(type(s1))
s2=frozenset(s1)
print(s2)
print(type(s2))
print()
time.sleep(2)
print("End of application")

#None data type:Which means nothing or empty.
#example:
import time
emp_salary=21500
print(emp_salary)
print(type(emp_salary))
Emp_salary=None
print(Emp_salary)
print(type(Emp_salary))
print()
time.sleep(2)
print('end of application')
##Range data type: Range datat type is to produce sequence of integers.
# Range dta type is assosciated with for loop.
#Examples:
#Form1: range(end(end-1))
import time
for x1 in range(10):
    print(x1)
print()
time.sleep(2)
print("endof applcation")

# Form2: range(end(end-1),stepsize)
import time
for a1 in range(10,20):
    print(a1)
    print()
time.sleep(2)
print("end of application")

#form3: range(start,end(end-1),stepsize)

import time
for k1 in range(1,20,2):
    print(k1)
    print()
time.sleep(2)
print("end of application")