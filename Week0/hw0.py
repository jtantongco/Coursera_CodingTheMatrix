# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [ i for i in L if i % num != 0]



## Problem 2
def myLists(L): return [list(range(1,i+1)) for i in L]




## Problem 3
def myFunctionComposition(f, g): return { a:d for (a,b) in f.items() for (c,d) in g.items() if b==c }


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j)
complex_addition_b = 1j
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    count = 0;
    for x in L:
        count += x
    return count


## Problem 7
def myProduct(L): 
    product = 1;
    for x in L:
        product = product*x
    return product

## Problem 8
def myMin(L): 
    mini = L[0]
    for x in L:
        if x < mini:
            mini = x
    return mini

## Problem 9
def myConcat(L):
    fullstring = ''
    for x in L:
        fullstring += x
    return fullstring

## Problem 10
def myUnion(L):
    unionset = set()
    for aset in L:
        unionset = unionset | aset
    return unionset

