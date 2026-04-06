#Data types in python:integer,float,boolean,list,tuple,set,dictionary,string,byte,byte array,range,frozenset,none,complex.
#examples for Int,float,boolean,complex:

import time
x=15
y=-12
z=9.9
k=2+4j
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(k,type(k))
time.sleep(2)
print("end of application")
# Complex Data Type:
import time
x=4+5j
y=2+5j
print(x.real)
print(y.imag)
add=x+y
print(add)
time.sleep(2)
print('end of application')

#String data type:
#String can be enclosed with single or double or triple quotation.
#example;

str1='pyhton'
str2="python developer"
str3="5"
str4='4.9'
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

#String data type supports slice operation.either positive or negtaive direction.
#for slice operation start and end value and step size will be requires and in string soace will aso takes as charector.
#in slice operation step size must be positive or negative.
#Slice operation with positive direction:

import time
str1="python developer"
print()
print(str1)
print(type(str1))
print()
print("==Slice_operation_using_positive direction")
print(str1[1:6:1])
print("==Slice_operation_using_Negative_Direction")
print(str1[-2:-3:-1])
print()
print(str1[-3:-5:-2])
print()
time.sleep(2)
print("end of application")


#In slice operation start value will be default as 0 and end+1 as end value for psoitive direction and step size will be default as 1.
# in negative direction end value as end-1 and start value and step size will be in negative value.
# Type casting and type conversion in Python.Theer are two types one is implicit and explict type conversion.

#Implict type conversion: Done by python automatically.no data loss.
#example:

x=10
y=2.5
z=x+y
print(z)
#here type conversion done automatically and no data loss.

#explicict type casting: done by user and may be some data loss.
#For type casting use int(),float(),list(),str(),set().
#example;

a=12
b=float(a)
print(b)
print()
c=12.5
d=int(c)
print(d)