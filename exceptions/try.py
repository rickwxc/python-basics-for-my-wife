
try:
    try:
        raise Exception('e1')
    except Exception: # try comment off
        print('caught')
    finally:
        print('inner finally')
    print('after')
finally:
    print('outer finally')
print('outer after')
