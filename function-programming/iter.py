
obj = 1, 2, 3


for i in iter(obj):
    print(i)

for i in obj:
    print(i)


it = iter(obj)

try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print ('Please StopIteration !')



#list tuple to dictionary
L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
print(dict(iter(L)))



#
"""
Generator expressions are surrounded by parentheses (“()”)
and list comprehensions are surrounded by square brackets (“[]”).
Generator expressions have the form:
( expression for expr in sequence1
        if condition1
        for expr2 in sequence2
        if condition2
        for expr3 in sequence3 ...
        if condition3
        for exprN in sequenceN
        if conditionN )
"""

line_list = ['  line 1\n', 'line 2  \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)
print (stripped_iter)
for ele in stripped_iter:
 print(ele)


# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]

print (stripped_list)

