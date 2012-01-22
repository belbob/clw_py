'''
Created on Jan 17, 2012

@author: robert
'''
## Class ##
class groupClass:
    group='PC2'
    teacher='Robert'
    def teacherMethode(self):
        print self.teacher,'is leerkracht van groep',self.group
        
group1=groupClass()
print '%s' % group1.group  
print group1.teacherMethode() 

## childClass ##
class studentClass(groupClass):
    def createName(self,name):
        self.name=name
    def displayName(self):
        return self.name
    def greetingName(self):
        print 'hallo %s' % self.name
        
student1=studentClass()
student2=studentClass()
student1.createName('Raf')
student1.age=21
student2.createName('Niels')

print student1.displayName() , str(student1.age)
print student2.group,student2.greetingName()

## constructor ##
class newstudentClass:
    def __init__(self):
        self.group='PC Technicus'
        print 'nieuwe student toegevoegd'

student3=newstudentClass()
print student3.group     