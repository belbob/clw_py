'''
Created on Jan 12, 2012

@author: robert
'''
# initiele lijst studenten
student = {'Gino':'PC1','Robbe':'PC1','Ben':'PC1'}
print 'initiele lijst studenten',student
#toevoegen student
student ['Philip']='PC1'
print 'toevoegen student Philip',student
# verwijderen student
del student ['Ben']
print 'vewijderen student Ben',student
# bijwerken student
student ['Philip']='PC2'
print 'Philip naar een andere groep',student

print 'Philipe zit in groep',student['Philip']
print 'namen van studenten',student.keys()
print 'bestaat Philip als student:','Philip' in student
print 'studenten in alfabetische volgorde',sorted(student)

