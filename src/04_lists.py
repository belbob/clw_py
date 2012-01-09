'''
Created on Jan 7, 2012

@author: robert
'''
print ('Lists')
students1 = ['Jesse','Raf','Niels']
students2 = ['Vince','Robbe','Philip','Ben']
students = students1 + students2
teacher = 'Robert'
print ('students:'),students
print ('last student in list:'),students[-1]
print ('some students:'),students[0:3]
print ('teacher is'),teacher
print ('last letter of teachers name:'),teacher [-1]
print ('some letters from teachers name:'),teacher[1:5]
print ('reverse teacher:'),teacher[::-1] #[start:stop:step]
print 'r' in teacher 
print 'Vince' in students
print len(students)
print len(teacher)
print list(teacher)
students2[0] = 'Vincent'
print students2
del students1[1]
print students1

print ('\nMethods on lists')
students2.append('Gino')
print students2
students2.sort()
print students2
students = students1
students.extend(students2)
students.sort()
print students
print students.index('Gino')
print students.pop(1)
print students
students.insert(0,'Gino')
print students
students.remove('Gino')
print students
students.reverse()
print students

print ('\nList of lists')
listoflists=[[0]*3 for i in range(4)]
print listoflists
listoflists[1][0]=4
print listoflists