#tips

#1. better loops for create new collection
#[mapping−expression for element in source−list if filter−expression]

#2. dictionary based string formatting, check ./dictinary-based-string-formatting.py
conf = {
        'name': 'rick',
        'msg': 'hello',
        'uid': 10001,
}
print ( '%(msg)s, %(name)s (uid=%(uid)d)' % conf)

#2. lambda and boolean control 
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
