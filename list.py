l = ['a', 'b']
#extend : merge into
l.extend(['c', 'd'])
l.extend(['e', 'f'])
print (l)
#a b c d e f


#slicing
print (l[:3]) # until 3 exlude 3
print (l[3:]) # start 3 include 3 to end
print (l[-1]) # last one, element at len() - 1
print (l[-2]) # 2nd last one, element at len() - 2
print (l[:-2]) # start to 2nd last one, exclude -2
print (l[-3:]) # 3nd last one to end, include -3

l.append('g')
l.insert(2, 'x') # a b x c ....

#sort
# sort without modify original
print ('sorted(l)', sorted(l))
print ('org', l)
# sort with modify original
l.sort()
print (l)
#Note: can not sort mixed string and numbers

l.append('a')

#search elements
#only find the first occurence
print (l.index('a'))
#if not found, throw error!
#print (l.index('j')) 

l.append(True)
print (l.index(True))

#remove
print(l.remove('a')) # return nothing

#if not found, throw error!
#l.remove('j')
print (l)
print(l.pop()) #remove last and return pop out value
print (l)

#list merge
l += [100, 200]
print (l)

#list merge with list
l.extend([300, 400])
print (l)

#list merge with tuple
l.extend((500, 600))
print (l)

# use * for duplicate list elments
l += [1, 2] * 3
print (l)

#reverse
l.reverse()
print (l)



numbers = [1, 2, 3,4,5, 6,7]

numbers.append(300)
print (numbers)
