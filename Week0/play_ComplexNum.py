L=[2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j]
print(L)

from plotting import plot

'''
The following lines only work in REPL

from plotting import plot
plot(L)

plot has imaginary part as y axis and real part as x axis
length of num -> dist from point to origin

Computer also says that there is no image in the File not Found
terminal execution cannot launch window
Needs to be in REPL
'''

'''
f(z) = z + (complex number) = z + real1 + real2*i
shifts plot real1 to the right
shifts plot real2 upwards

right 1 and up 2 for plot
plot({z+(1+2j) for z in L})

scaling
f(z) = real1*z
scale by real1 - real1 > 0
is multiplying by a complex still scaling?
plot({z*0.5 for z in L})

reflection
f(z) = -1*z
plot({z*-1 for z in L}) -> vertical reflection

'''

from math import e, pi

'''
Circles / rotations
for any point z satisfying - |z| = e^(i*theta)
e is natural number

creates a circle
plot([e**(t*2*pi*1j/20) for t in range(20)])

scale the circle
plot([2*e**(t*2*pi*1j/20) for t in range(20)])

rotation by pi/2 (90 deg)
f(z) = j*z
plot({1j*z for z in L})

rotation by tau degrees
f(z) = e^[(theta+tau)*j] or f(z) = z*e^(tau*j)

plot([e**(pi*1j/4)*z for z in L])
'''

#------------------------ zlib dependency here ------------------------

'''
from image import *
I = color2gray(file2image('__imgName__.png')
r = len(I)
c = len(I[0])
M = [ x + y*1j for x in range(c) for y in range(r) of I[r-y-1][x] < 120]
flattens a color image into a 2 color image

plots image in quadrant 1 with bottom right corner at origin
plot(M,max(r,c),1)

centers image at origin
plot([z - (c/2+(r/2)*1j) for z in M], max(r,c), 1)

*note the transformations above can be applied*
'''
