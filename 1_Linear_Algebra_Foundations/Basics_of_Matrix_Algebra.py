import numpy as np
a=np.array([[1,7],[2,1],[3,2]])
#print(a)
b=np.array([[1,1],[1,-1],[1,0]])
#print(b)

c=np.add(a,b)
#print(c)
d=np.subtract(a,b)
#print(d)
e=np.array([[1,3,1],[1,0,1]])
#print(e)
f=np.dot(a,e)
#print(f)
det=np.linalg.det(f)
#print(det)
#g=np.linalg.inv(f)
#print(g)
h=np.array([[1,-1],[2,3]])
print(np.linalg.inv(h))