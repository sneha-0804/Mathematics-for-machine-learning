import numpy as np
v=np.array([1,-1,2])
w=np.array([2,5,2])
print(v+w)#addition of vectors
print(v-w)#subtraction of vectors
print(3*v)#scalar multiplication
print(np.linalg.norm(v))#length of vector
s=np.dot(v,w)#dot product
print(s)