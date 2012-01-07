'''
Created on Jan 3, 2012

@author: robert
'''
print ('Basisbewerkingen met Python')
print ('\nOptellen, Aftrekken, Vermeningvuldigen en Delen')
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

print ('\nModulus')
# Het bekendste voorbeeld van modulair rekenen is de tijdrekening in uren, 
# die modulo 12 of modulo 24 gaat. Zo is de tijd bijvoorbeeld 10 uur na 22 
# uur gelijk aan 8 uur.
x=32
y=24
print x,('%'),y, ('= '),x%y

print ('\nMachtverheffing')
x=8
y=4
print x,('**'),y, ('= '),x**y

print ('\nComplexe getallen')
a=complex(3,4)
b=2+3j
print ('complex getal: '),a
print ('Reele waarde: '),a.real
print ('Imaginaire deel: '),a.imag
print ('Absolute waarde: '),abs(a)
print ('Bewerkingen complexe getallen: \n'),a,('+'),b,('='),a+b