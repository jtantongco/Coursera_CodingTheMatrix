#! /usr/bin/env python3.3

' 3 by 4 0 value matrix
' matrix as a list of lists*
[[0 for x in range(4)] for y in range(3)]

' 3 by 4 matrix with difference between rows and columns
[[x-y for x in range(3)] for y in range(4)]

' representation of matrix
' dictionary of rows (key being name of row, value being a vector) -> may be convenient
' dictionary of columns (key being name of column, value being a vector) -> may be convenient
' special class Mat -> reference by A[row, column]
class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function
''' Example:
Mat((row_labels,column_labels), {(x *in row_labels*, y *in column_labels*)):val})

concrete example: 3 by 3 identity matrix with row and column labels of a,b,c
Mat( ({'a','b','c'},{'a','b','c'}) , {('a','a'):1,('b','b'):1, ('c','c'):1})
'''

'returns a D by D identity matrix
def identity(D):
    return Mat( (D,D), {(x,x):1 for x in D})

def mat2coldict(A):
    return {c:Vec( A.D[0], { r:A[r,c] for r in A.D[0]} ) for c in A.D[1]}

def transpose(M):
    return Mat( (M.D[1], M.D[0]), {(col,row):val for (row,col), val in M.f.items()} )


