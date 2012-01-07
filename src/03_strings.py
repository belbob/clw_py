'''
Created on Jan 7, 2012

@author: robert
'''
print ('Werken met strings')
print 'string met \'hoi Robert\''
print "string met \"hoi Robert\""
naam = raw_input ('naam: ')
vnaam = raw_input ('voornaam: ')
leeftijd = input ('leeftijd in jaren: ')
spatie = ' '
volnaam = vnaam + spatie + naam
print volnaam,'is',str(leeftijd)
