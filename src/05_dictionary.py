'''
Created on Jan 12, 2012

@author: robert
'''
student1 = {'lname':'Stiernet','fname':'Gino'}
student2 = {'lname':'Lau','fname':'Philip'}


students = (student1,student2)
print students

for x in students:
    print x["lname"],x["fname"]