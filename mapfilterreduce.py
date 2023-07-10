#MAP
def cube(x):
    return x**3

l=[1,2,4,6,5]
newl=list(map(cube,l))
print(newl)

#FILTER
def filter_fn(a):
    return a>3
nenewl=list(filter(filter_fn,l))
print(nenewl)

#REDUCE
from functools import reduce
num=[1,2,4,5,6]
sum=reduce(lambda x,y:x+y,num)
print(sum)