'''
Created on Jan 17, 2012

@author: robert
'''
def student(naam):
    return 'hallo ' + naam

print student('Raf')

def group (naam,vnaam,groep='PC1'):
    return '%s %s volgt de opleiding %s' % (naam,vnaam,groep)

print group ('Raf','Van Haver')
print group ('Raf','Van Haver','PC2')

def rapport (naam,vnaam,*punten):
    print naam,vnaam
    print punten
    print 'gem. ',sum(punten)/len(punten)
    
rapport ('Raf','Van Haver',68,34,92,34)

def vakken (naam,vnaam,**vak):
    print naam,vnaam
    print vak
    
vakken ('Raf','Van Haver',Nederlands=56,Engels=95,Godsdienst=23)

vakpunten = {'Wiskunde':68,'Frans':34,'Technologie':92}

vakken ('Raf','Van Haver',**vakpunten)




    