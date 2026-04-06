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