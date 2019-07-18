from functools import partial

def prt(cb):
    print("done")
    cb()

def cb(x, y):
    print(100 + x + y)

prt(partial(cb, x=1, y=2))
