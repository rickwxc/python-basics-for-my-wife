
def inner():
    try:
        print('inner start')
        raise Exception('inner wrong')
    # if not caught, no inner after finally, no outter after finally
    except Exception:         # try comment off this line
        print('inner caught')
    finally:
        print('inner finally')
    print('inner after finally')

def outter():
    try:
        inner()
    finally:
        print('outer finally')
    print('outer after finally')

try:
    outter()
except Exception:
    print('got Exception!')
