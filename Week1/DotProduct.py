#! /usr/bin/env python3.3

''' My soln: too much? since it has checks?
def list_dot(u,v): return sum([u[x]*v[x] for x in range(len(u)) if len(u) == len(v) else 0])
'''
def list_dot(u,v): return sum([u[i]*v[i] for i in range(len(u))])
'''alternate:
def list_dot(u,v): return sum([a*b for (a,b) in zip(u,v)])
'''

'''
Dot product of two things:
can be used to combine into other units by dot producting two separate unit vectors

if comparing things with +/- and same units
dot product will be a result on similarity: if very high + , similar if - then dissimilar

in search of a needle in haystack -> run a slider dot product
run time complication -> FFT solves it -> another reason to learn FFT

'''


'''
Triangular solve:

Need to run a step through this:
Kinda get why it works but I don't really see how to do it

'''
' necessary function
def zero_vec(D): return Vec(D, {d:0 for d in D})

def triangular_solve(rowlist,b):
	x = zero_vec(rowlist[0].D)
	for i in reversed(range(len(rowlist))):
		x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
	return x

def arb_triangular_solve(rowlist, label_list, b):
	x = zero_vec(set(label_list))
	for r in reversed(range(len(rowlist))):
		x[c] = (b[r] - rowlist[r] * x)/rowlist[r][c]
	return x
