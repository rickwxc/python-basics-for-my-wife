from functools import partial

def prt(cb):
    print("done: ", cb())


def cb(x, y):
    return(100 + x + y)

def cb2(data):
    return(100 + data)

prt(partial(cb, x=1, y=2))

prt(partial(cb2, data=11))
