str = """
multi-line 
string
"""
print(str)

str = "zAbCdEf "
print (str.lower())
print (str.upper())

print (str.title())

print (str.capitalize())

print (len(str))
print (str.strip(' '))
str = "0123456789"
print(str[1:5])

str = 'ABC'
print (str.isupper())
str = 'abc'
print (str.islower())

str = '0'
print (str.isupper())
print (str.islower())

msg='Hello'
for letter in msg:
    print(letter, end='*')
print('')
