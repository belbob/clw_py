'''
Created on Jan 12, 2012

@author: robert
'''
student=raw_input('Wie ben je: ')

if student=='jesse':
    print 'hallo',student
elif student=='Jesse':
    print 'Oooo, je naam wordt met een hoofdletter geschreven'
else:
    print 'Wie ben je ?????'
    

yn=raw_input('bent u een gebruiker van ons systeem? j/n')
if yn=='j':
    users=('user') 
    admin=raw_input('geef uw gebruikernaam:') 
else:
    users=''     
 
if users=='user':
    if admin=='robert':
        print admin,'u bent onze systeemadmin'
    else:
        print admin,'u bent een gewone systeemgebruiker'
else:
    print 'u hebt hier niets te zoeken'
