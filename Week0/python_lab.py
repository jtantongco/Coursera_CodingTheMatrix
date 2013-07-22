## Task 1
minutes_in_week = 60*24*7

## Task 2
remainder_without_mod = 2304811-((2304811//47)*47)

## Task 3
divisible_by_3 = (673+909)%3==0

## Task 4
x = -9
y = 1/2
statement_val = 1.0
#2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { x**2 for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 11, 2, 3 }
Y1 = { 5, 7, 9 }
#{x*y for x in X1 for y in Y1}

## Task 8: enter in the two new sets
X2 = { 1, 2, 4 }
Y2 = { 8, 16, 32 }
#X2 X Y2 should result in a 3X3 matrix with only 5 elements

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {i*(base**2)+j*(base**1)+k*(base**0) for i in range(base) for j in range(base) for k in range(base) }

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { i for i in S for j in T if i in T and j in S}

## Task 11
L = [20,10,15,75]
L_average = sum(L)/len(L) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(i) for i in LofL]) # use form: sum([sum(...) ... ])

## Task 13
letters = {'A','B','C'}
digits = {1,2,3}
cartesian_product = [[i,j] for i in letters for j in digits] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [ (i,j,k) for i in S for j in S for k in S if i+j+k == 0 ] 

## Task 15
exclude_zero_list = [ (i,j,k) for i in S for j in S for k in S if i+j+k == 0 and (i,j,k) != (0,0,0)]

## Task 16
first_of_tuples_list = [ (i,j,k) for i in S for j in S for k in S if i+j+k == 0 and (i,j,k) != (0,0,0)][0]

## Task 17
L1 = [1,2,3,4,5,6,1,2,3] # <-- want len(L1) != len(list(set(L1)))
L2 = [6,5,4,3,2,1] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = { 2*n+1 for n in range(100) if 2*n+1 <= 99 }

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5), L))

## Task 20
L20A = [10,25,40]
L20B = [ 1,15,20]
list_sum_zip = [x+y for (x,y) in zip(L20A, L20B) ]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [ dlist[i][k] for i in range(len(dlist)) if k in dlist[i]]
# value_list = [ dlist[i][k] for i in range(len(dlist)) if k in dlist[i]]
# x[k] for x in dlist
# value_list = [x[k] for x in dlist if k in x]
# none of the 3 seem to pass the test but they seem to generate the correct output on the provided test case...

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = value_list = [ x[k] if k in x else 'NOT PRESENT' for x in dlist ] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [ x[k] if k in x else 'NOT PRESENT' for x in dlist ] # <-- as you do here

## Task 23
square_dict = {k:k*k for k in range(100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {i:i for i in D }

## Task 25
base = 10
digits = set(range(10))
representation_dict = {i*(base**2)+j*(base**1)+k*(base**0):[i,j,k] for i in range(base) for j in range(base) for k in range(base)}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe'] 
#d = {0:1000, 3:990, 1:1200.50}
#L = ['Larry', 'Curly', '', 'Moe']
listdict2dict = { names[i]:d[i] for i in range(len(names)) if i in d }

## Task 27
def nextInts(L): return [ i+1 for i in L ]

## Task 28
def cubes(L): return [ i**3 for i in L ] 

## Task 29
def dict2list(dct, keylist): return [ dct[key] for key in keylist ]

## Task 30 
#def list2dict(L, keylist): return { keylist[l]:L[l] for l in range(len(keylist)) } 
#or
def list2dict(L, keylist): return { x:y for (x,y) in zip(keylist, L) } 


