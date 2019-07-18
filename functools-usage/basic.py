from functools import partial

# curry
def prt(x, y):
    print("x: %s, y:%s"  %(x, y))

func2 = partial(prt, 100)
#func2 = prt(100, y)

func2(200)
#x: 100, y:200
func2(300)
#x: 100, y:300
