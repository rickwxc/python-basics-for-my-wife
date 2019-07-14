import unittest
import re

def getNumber(str):
    regex = re.compile(r'(\d+)')
    find,  = (regex.search(str).groups())
    return find

def getLowerCase(str):
    regex = re.compile(r'([a-z]+)')
    find,  = (regex.search(str).groups())
    print('++++',find)
    return find

class Number(unittest.TestCase): 
    def testEqaul(self):
        self.assertEqual(getNumber('abcd100deb'), '100') 
    def testLowerCase(self):
        self.assertEqual(getLowerCase('1000abcef000'), 'abcef') 

if __name__ == "__main__":
    unittest.main() 
