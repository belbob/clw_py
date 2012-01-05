'''
Created on Jan 3, 2012

@author: robert
'''
print ('Basisbewerkingen met Python')
print ('Optellen, Aftrekken, Vermeningvuldigen en Delen')
x=8
y=2
print x,('+'),y, ('= '),x+y
print x,('-'),y, ('= '),x-y
print x,('*'),y, ('= '),x*y
print x,('/'),y, ('= '),x/y

print ('LET OP, problemen bij het delen')
x=9
print x,('/'),y, ('= '),x/y ,('-> FOUT')
print x,('/'),-y, ('= '),x/-y ,('-> FOUT')
x=9.0
print x,('/'),y, ('= '),x/y ,('-> JUIST')
y=2.0
print x,('/'),-y, ('= '),x/-y ,('-> JUIST')

print ('Modulus')
# Het bekendste voorbeeld van modulair rekenen is de tijdrekening in uren, 
# die modulo 12 of modulo 24 gaat. Zo is de tijd bijvoorbeeld 10 uur na 22 
# uur gelijk aan 8 uur.
x=32
y=24
print x,('%'),y, ('= '),x%y

print ('Machtverheffing')
x=8
y=4
print x,('**'),y, ('= '),x**y