#Variableis nothing but Name Tag or Label.All variables are identifiers but alla identifiers are not variables Because some of will e functions.
#There are 5 rules for variables:
#* varaible must strat with A-Z and a-z But not with Numbers.
#* Variable do not start with numbers like 0-9.
#* Variables can start with underscore_.
#* There is no limit for variable length.
#* if Variable start with double underscore python wil take it as private.
# Snake case: All letters in lower charector and words are seperated by underscore_ like chandra_kiran_user.
# Camel case: First letter in lower case after that word start with capital letter like chandraKiranUser.
# Pascal Case: All letters sholud Be in capital letters like ChandraKiranUser.
#Varuables assiagnment can be done in 2 ways one is multiple assignment and multiple value assignment.
#multiple assignment: we can assign same value to multiple variables like a=b=c=10.
#Multiple value assignment means we can assign different values in single line like age,name,course=23,kiran,python.

import time
Chandu=50
print(Chandu)
chandu=50.5
print(chandu)
KIRAN=45
print(KIRAN)
CHANDU=2
print(CHANDU)
_python="Very Intresting languge"
print(_python)
Chandrakiranisabeutifulstudent=True
print(Chandrakiranisabeutifulstudent)
print()
python_developer="snake_case"
print(python_developer)
pythonDeveloper="Camel_Case"
print(pythonDeveloper)
PythonDeveloper="Pascal_case"
print(PythonDeveloper)
Python=50
python=50
print(id(Python))
print(id(python))
print()
time.sleep(5)
print("This code literally decribes about Identifiers/Variables in Python...")

#Case Sensitive and Case insesensitive:

a=10000
b=10000
print(id(a))
print(id(b))



