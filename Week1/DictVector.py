#! /usr/bin/env python3.3

class Vec:
	def __init__(self, labels, function):
		self.D = labels
		self.f = function

v = Vec({'A','B','C'},{'A':1})
'''
Example of iteration and indexing
for d in v.D:
	if d in v.f:
		print(v.f[d])
'''

'''
ex
zero_vec({1,2,3}) => Vec({1,2,3},{1:0, 2:0, 3:0})
'''
def zero_vec(D): return Vec(D, {d:0 for d in D})

'''
sets the index d slot
ex.
let
v = Vec({1,2,3},{1:0, 2:0, 3:0})
setitem(v,1,4) => Vec({1,2,3},{1:4, 2:0, 3:0})
'''
def setitem(v, d, val): v.f[d] = val

'''
return the value of entry d slot
v = Vec({1,2,3},{1:4, 2:0, 3:0})
getitem(v, 1) => 4
'''
''' my ans:
def getitem(v,d): return v.f[d]
Issue: forgets to check for existence of key
'''
def getitem(v,d): return v.f[d] if d in v.f else 0
''' Alternative soln
def getitem(v,d): 
	if d in v.f:
		return v.f[d]
	else:
		return 0
'''

'''not sure what is wrong here:
Turn a list into a vector
def list2vec(L): return Vec({x for x in list(range(len(L)))},{x:L[x] for x in range(len(L))})
'''
def list2vec(L): return Vec( set(range(len(L))), {k:x for k,x in enumerate(L)} )

'''alternate:
def list2vec(L): return Vec( set(range(len(L))), {k:L[k] for k in range(len(L))}
'''



'''
all vec tests:
python3.3 -m doctest test_vec.py
'''
