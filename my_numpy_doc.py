# -*- coding: utf-8 -*-
"""MY_Numpy_Doc.ipynb

1D array
2D array
3D array

NumPy has primarily been written by C and is faster than other libraries.

### 🟡Lists vs. Numpy Array
"""

import numpy as np
l=[1,2,3]
a=np.array([1,2,3])

print(l ," >>  ", type(l))
print(a," >>  ", type(a))

l.append(4)  #when you run it too many times it keeps adding 4s to the list! [1,2,3,4,4,4,4...]
print(l)

#second way of adding an element to a list
l=l+[4]
print(l)

#a.append(4)
#print(a)

#a = a + np.array([4])      # it doesn't work that wy!   _ is called broadcasting
a = a + np.array([4,4,4])   #technically true but numpy is clever enough to understand the first one (a = a + np.array([4]))
print(a)

l=l*2
print(l)

a = a*2        #in numpy, math operations operate elementwise _ in list it works on the list
print(a)

np.sqrt(a)
print(a)

#you should assign it:
a = np.sqrt(a)
print(a)

"""### 🟡 Dot product

the dot product is the sum of the product of corresponding entries:
"""

l1=[1,2,3]
l2=[4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)

#for Lists:
dotL=0
for i in range(len(l1)):
  dotL += l1[i]*l2[i]
print("Dot product in lists=",dotL)

#for NumArray (faster):
dotN= np.dot(a1,a2)
print("Dot product in Numpy=", dotN)

# Method 3:
sum1 = a1 * a2   #elementwise multiplication
print(sum1)
dot3 = np.sum(sum1)   # == dot = (a1 * a2).sum()  >> this works too!
print(dot3)

# Method 4: new versions
 dot4 = a1 @ a2
 print(dot4)

b=np.array(([1,2,3], [4,5,6]))
b_shape = b.shape
print("b matrix dimansion= ", b_shape)
print("rows=", b_shape[0])
print("columns=", b_shape[1])

b[0][0]
b[0][1]
b[0][2]

"""### 🟡Speed Test To Compare lists and Numpy Array"""

from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)  #you can convert a numpy array back to a list, and you can do it the other way around
B = list(b)

T = 1000

def dot1():
  dot=0
  for i in range(len(A)):
    dot += A[i]*B[i]
  return dot

def dot2():
  return np.dot(a,b)

#time calculation:

start = timer()
for t in range(T):
  dot1()
end = timer()
t1 = end-start

start = timer()
for t in range(T):
  dot2()
end = timer()
t2 = end-start


print("list calculation =",t1)
print("np.dot = ", t2)
print("ratio", t1/t2)

"""### 🟡 multi dimensional arraya or ndarray

for making a multidimensional array, we pass a list of lists to array()

.shape : (rows, columns)
"""

a=np.array([1,2])
print(a)
print(a.shape)
print("a[0]=",a[0])

b=np.array([[1,2], [3,4]])
print(b)
print(b.shape)
print("b[0]=",b[0])
print("b[0][1]=",b[0][1])   # b[0,1]

"""## >>np.random

"""

np.random.randn

n1 = np.random.randn(1000)
print(n1, "\n \n")

n2 = np.random.randn()
print(n2,"\n \n")

n3 = np.random.randn(2, 4)
print(n3)
