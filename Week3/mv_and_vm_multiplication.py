#! /usr/bin/env python3.3

''' 
Solver for the lights out game
'''
n = 2
D = {(i,j) for i in range(n) for j in range(n)}

from vec import Vec
from GF2 import one
b00 = Vec(D, {(0,0):one, (0,1):one, (1,0):one} )
b01 = Vec(D, {(0,0):one, (0,1):one, (1,1):one} )
b10 = Vec(D, {(0,0):one, (1,0):one, (1,1):one} )
b11 = Vec(D, {(0,1):one, (1,0):one, (1,1):one} )

'''
print(n)
print(D)
print(b00)
print(b01)
print(b10)
print(b11)
'''

from matutil import coldict2mat

possible_moves={(0,0):b00, (0,1):b01, (1,0):b10, (1,1):b11}
A=coldict2mat(possible_moves)

'''
Given problem:
'''
b = Vec(D, {(0,0):one, (1,0):one})

print("Moves:")
print(A)
print("Initial State:")
print(b)

from solver import solve

x = solve(A,b)
print("Solution:")
print(x)
print("Verification:")
print(A*x)
print(b)

''' 
A*x == b is not functioning
Is there a Mat.py that I didn't get that handles parsing operations
'''

print("Done Lights Out")
