file = open('Countries.txt','w')
file.write('A\n')
file.write('B\n')
file.close() 
file = open('Countries.txt','r')
print(file.read())
file.close() 



