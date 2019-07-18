from functools import partial

# curry
def prt(x, y):
    print("x: %s, y:%s"  %(x, y))

func2 = partial(prt, y=100)
#func2 = prt(100, y)

func2(x=200)
#x: 200, y:100
func2(x=300)
#x: 300, y:100
