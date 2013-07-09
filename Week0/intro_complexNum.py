#! /usr/bin/env python3.3

# j  is the imaginary number i
# 1j + 2j -> should be 3j
# just j will make python think of the variable j
variable=1+3j
print(variable)
print("The real part:")       
print(variable.real)
print("The imaginary part:")
print(variable.imag)
# imaginary numbers dont seem to work when executed in script

def solve(a,b,c): return (c-b)/a
#works on both real numbers and complex numbers!

print("Solve ax+b=c when a=10,b=5,c=30")
print(solve(10,5,30))
print("Solve ax+b=c when a=10+5j,b=5,c=20")
print(solve(10+5j,5,20)) #solution should be 1.2-6.0j
