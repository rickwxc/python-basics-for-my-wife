#tips

#use logging module rather than print()

#better loops for create new collection
#[mapping−expression for element in source−list if filter−expression]

#functional programming: check functools-usage

#list zip, stop when shorted list reached
l1 = range(0, 100)
l2 = ['a','b','c','d','e']
l3 = ['u','v', 'w', 'x','y','z']
print(['%s%s-%s' % (a, b, c) for (a, b, c) in zip(l1,l2, l3)])

#dictionary based string formatting, check ./dictinary-based-string-formatting.py
conf = {
        'name': 'rick',
        'msg': 'hello',
        'uid': 10001,
}
print ( '%(msg)s, %(name)s (uid=%(uid)d)' % conf)

#lambda and boolean control
def formatString(str, flag):
    if flag == True:
        return "<%s>" % str
    else:
        return str

print(formatString('Abc', True))
print(formatString('Abc', False))


def formatString2(str, flag):
    process = (flag and (lambda s: "<%s>" % str)) or (lambda s:s)
    return process(str)

print(formatString2('Def', True))
print(formatString2('Def', False))
