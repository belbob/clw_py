'''
Created on Jan 4, 2012

@author: robert
'''
print ('Math Module - Wiskundige functies')

import math

x=4.0
y=3.0
z=math.pow(x,y)
print ('\n---Wortels en Machten---')
print ('Vierkantswortel van'),x,('= '), math.sqrt(x)
print x,('tot de'),y,('de = '), z
print y,('de wortel van'),z,('= '), math.pow(z,(1/y))

print ('\n---Logaritmen---')
print ('e = '), math.e
print ('log van 1000 = '),math.log10(1000)

print ('\n---Goniometrie---')
print ('pi = '),math.pi
print ('2 rad = '),math.degrees(math.pi*2),('graden')
print ('sin 60 = '),math.sin(math.radians(60))
print ('tan 60 = '),math.tan(math.pi/3)
print ('acos 0.5 = '),math.acos(0.5),('rad')
print ('acos 0.5 = '),math.degrees(math.acos(0.5)),('graden')