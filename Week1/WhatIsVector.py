#! /usr/bin/env python3.3
L = [[2,2], [3,2], [1.75,1], [2,1], [2.25, 1], [2.5,1], [2.75,1], [3,1], [3.25,1]]
print(L)

#from plotting import plot
#plot(L)

#add 2 n length vectors if a vector is represented as a n element list
def addn(v,w): return [v[i] + w[i] for i in range(len(v))]

#scale n length vector by alpha if a vector is represented as a n element list
def scalar_vector_mult(alpha,v): return [alpha*v[i] for i in range(len(v))] 

v=[3,2]
plot([scalar_vector_mult(i/10,v) for i in range(11)], 5)
plot([scalar_vector_mult(i/100,v) for i in range(100)], 5)
plot([scalar_vector_mult(i/100,v) for i in range(-1000,1000)], 5)
