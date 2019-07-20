import functools
import operator
import itertools

product = 1
for i in [1, 2, 3]:
    product *= i

# use reduce:
# functools.reduce(FUNC, [...data...], Initial_Value)
# Initial_Value can be ommitted, and first element of data is the initial value
product = functools.reduce(operator.mul, [1, 2, 3], 1)
print('product: ', product)

product = functools.reduce(operator.mul, [1])
print('product: ', product)

product = functools.reduce(lambda x,y: x*y, [1, 2, 3], 1)
print('product: ', product)

def mul(x, y):
    print(x,y)
    return x * y

product = functools.reduce(mul, [1, 2, 3], 1)
print('product: ', product)

total = functools.reduce(lambda a, b: (0, a[1] + b[1]), [(1,2),(30, 40), (500, 600)])[1]
print (total)
total = functools.reduce(lambda a, b: (0, a[1] + b[1]), [(1,2),(30, 40), (500, 600)])
print (total)

total = functools.reduce(lambda a, b: (0, a[1] + b[1]), [('ab','cd'),('ef', 'gh')])
print (total)

def fadd(a,b):
    print('fadd: ', a[1], b[1])
    return 0, a[1] + b[1]

total = functools.reduce(fadd, [('ab','cd'),('ef', 'gh'), ('uv', 'xy')])
print (total)


#A related function is itertools.accumulate(iterable, func=operator.add). It performs the same calculation, but instead of returning only the final result, accumulate() returns an iterator that also yields each partial result:

print(list(itertools.accumulate([1, 2, 3, 4, 5])))
print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.add)))
print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.mul)))
print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.sub)))

m = itertools.accumulate([1, 2, 3, 4, 5], operator.mul)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))


