
def upper(s):
    return s.upper()

print(list(map(upper, ['sentence', 'fragment'])))

print([upper(s) for s in ['sentence', 'fragment']])


def is_even(x):
    return (x % 2) == 0

print(list(filter(is_even, range(10))))
print(list(filter(lambda v: v%2 == 1, range(10))))
print([x for x in range(10) if is_even(x)])

#list has same effects with []


for item in enumerate(['subject', 'verb', 'object']):
    print(item)

f = open('./iter.py', 'r')
for i, line in enumerate(f):
    if line.strip() == '':
        print('--Blank line at line #%i' % i)
    else:
        print(line)
    break


"""
['SENTENCE', 'FRAGMENT']
['SENTENCE', 'FRAGMENT']
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]
(0, 'subject')
(1, 'verb')
(2, 'object')
"""





