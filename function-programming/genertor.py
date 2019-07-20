"""
Any function containing a yield keyword is a generator function;
this is detected by Python’s bytecode compiler which compiles the function specially as a result.

When you call a generator function: it returns a generator object that supports the iterator protocol.
On executing the yield expression, the generator outputs the value of i, similar to a return statement.
The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved. On the next call to the generator’s __next__() method, the function will resume executing.

"""


def generate_ints(N):
    for i in range(N):
        yield i
    yield -1


gen = generate_ints(3)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1
        print ('val: ', val, i)


it = counter(20)  #doctest: +SKIP
print(next(it))
print(next(it))
print(next(it))
print ('......after send ')
it.send(8)  #doctest: +SKIP
print(next(it))
print(next(it))
print(next(it))

