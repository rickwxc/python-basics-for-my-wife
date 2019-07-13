Contact_info = {
        'Name':'xyz', 
        'Zip':'2000', 
        'state':'nsw', 
        'Address':'18 street'
        }
Contact_info["Mobile"] = 1234567
print (Contact_info)
# items in list and each with tuple format
print (Contact_info.items())

#update
Contact_info.update({"email":"abc@domain.com"})

#update multi-value
data_1={'City':'Syndey', 'Zip':51234}
Contact_info.update(data_1)

print (Contact_info.get('Address'))
print (Contact_info)

#dump keys, values
print(Contact_info.keys()) 
print(Contact_info.values())

#delete
del Contact_info['email']

#pop() remove by key
print('pop("Mobile")', Contact_info.pop("Mobile"))

#popitem():  remove the last key value pair and returns removed as tuple
print('popitem(): ', Contact_info.popitem())

#assign to x, y
x, y = Contact_info.popitem()
print (x, y)
print (Contact_info)


#loop
lp = {"%s=%s" % (key, value) for (key,value) in Contact_info.items()}
print ('loop:', lp)
#join
print ('loop with join:', '|'.join(lp))

# convert to set
dictLoop = {"%s=%s" % (key, val) for (key,val) in Contact_info.items()}
print ('dictLoop to set:', dictLoop)

# convert to list of tuple 
dictLoop = [ (key, val) for (key,val) in Contact_info.items()]
print ('dictLoop to list of tuple:', dictLoop)

Contact_info.clear()
print (Contact_info)


