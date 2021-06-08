import numpy as np

a = np.array([1,2,3,4,5])
print(a)

b = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(b)

iden = np.identity(5)
# print(iden)

transp = np.transpose(b)
print(transp)

d = np.zeros([3,5])
print(d)

vector = np.arange(10,30)
print(vector)