# all false

if [] or 0 or {} or () or '':
 print('not here')
else:
 print('All false')


 print('a' and 'b') # 'b'
 print('' and 'b') # ''
 print('' or 'b') # 'b'
 print('' or []) #  []


a = ""
b = "second"
print('1 and a or b:' ,(1 and a or b)) # second

print('(1 and [a] or [b])[0]: ',  (1 and [a] or [b])[0]) # ''
