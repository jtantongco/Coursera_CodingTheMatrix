from GF2 import one
print("One plus one")
print(one + one)
print("One times one")
print(one * one)
print("One times 0")
print(one * 0)
print("One divided by one")
print(one / one) 


#cryptography

def encrypt(p,k): return p+k
p = one
k = one
c = encrypt(p,k)

print("def encrypt(p,k): return p+k")
print("Encryption of one and one")
print(c)

'''
one-time pad crypto-system
evenly distributed result of outcomes

as long as its one time use, its hard to break
'''
