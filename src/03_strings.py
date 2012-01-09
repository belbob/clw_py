'''
Created on Jan 7, 2012

@author: robert
'''
print ('Strings')
print 'this is string with \'hoi Robert\''
print "this is string with \"hoi Robert\""
lname = raw_input ('naam: ')
fname = raw_input ('voornaam: ')
age = input ('leeftijd in jaren: ')
space = ' '
name = fname + space + lname
print name,'is',str(age)
var = (lname,fname,age)
sense = '%s %s is %s'
print sense % var

print ('\nMethod on Strings')