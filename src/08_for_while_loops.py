'''
Created on Jan 13, 2012

@author: robert
'''
x=1
while x<=10:
    print x
    x += 1

students = ['Robbe','Philip','Gino']
for student in students:
    print student

while 1:
    name = raw_input('Geef nieuwe student in, (stop met quit): ')
    if name == 'quit':
        students.sort()
        break
    elif name:
        students.append(name)
    
for student in students:
    print student
    
age={'Jesse':21,'Raf':23,'Niels':22}
for student in age:
    print student,age[student]

# 
    
student1 = {'lname':'Stiernet','fname':'Gino'}
student2 = {'lname':'Lau','fname':'Philip'}
students = (student1,student2)
print students

for x in students:
    print x["lname"],x["fname"]    