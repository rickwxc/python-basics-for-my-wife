"""
'b' signed char int 1
'B' unsigned char   int 1
'u' Py_UNICODE  Unicode 2
'h' signed short    int 2
'H' unsigned short  int 2
'i' signed int  int 2
'I' unsigned int    int 2
'l' signed long int 4
'L' unsigned long   int 4
'f' float   float   4
'd' double  float   8
"""
from array import *
a = array('b', [2, 4, 6, 8, 10, 12, 14])
print (a)
a.reverse()
print (a)
a.pop() #remove last
print (a)
for ele in a:
 print(ele)

tmp = [ '[%d]' % (ele * 5) for ele in a]
print (tmp)
