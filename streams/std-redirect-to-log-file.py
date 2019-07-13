import sys
fsock = open('error.log', 'w')
sys.stderr = fsock

for i in range(10):
    sys.stderr.write("error: %s \n" % i)

# save console output
saveout = sys.stdout
fsock = open('out.log', 'w')
sys.stdout = fsock
for i in range(10):
    print('message: %s' % i)

sys.stdout = saveout
fsock.close()
for i in range(10):
    print('message: %s' % i)
