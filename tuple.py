tp = 'a', 'b', 'c'
print (tp)

print(tp.index('b'))
# no remove
# tp.remove('b') 
# no extend
# tp.extend('a')

#check value in tuple
print ('c' in tp)

tp += ('d', 'k')
print (tp)

#slicing (same as list, check list)
print (tp[2:4])
print (tp[2:]) # from idx 2 include 2 
print (tp[:3]) #before idx 3 exclude 3

#loop with if
name = tuple( i for i in tp  if i != "c")
print(name)

#transform each and return new tuple
name = tuple( "(%s)" % i for i in tp )
print(name)
#join with string
print('|'.join(name))

#unpacking
e0, e1, e2, e3, e4 = tp
print (e0, e1, e2, e3, e4)

del tp

#tuple as dict keys
dic={('a', 'b'): 'V'}
print (dic)

numbers =(10,2,4,100,500)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# any() — if any of the value has a boolean value of True
# all() — If all the values in the tuple have a boolean value of True
test=(1,'name', 'trail',  False, True)
print(any(test))
print(all(test))
print(all((True,True)))

#count & find
flowers =('Rose', 'Lily', 'Orchids', 'Lotus', ' Mari Gold', 'Sunflower','Rose')
print(flowers.count('Rose'))
print(flowers.index('Lotus'))

#tuple to dict
t1 =('Constituency','Arizona')
senator=dict([('Name', 'John'), ('Age', 15), t1])
print (senator)
