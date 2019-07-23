before:

ERRORS ===============================================
ERROR collecting t1/name-collision/b/test_foo.py __________________________
import file mismatch:
imported module 'test_foo' has this __file__ attribute:
  /Users/rick/py/basics/testing/pytest/t1/name-collision/a/test_foo.py
	which is not the same as the test file we want to collect:
	  /Users/rick/py/basics/testing/pytest/t1/name-collision/b/test_foo.py
		HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules

add empty __init__.py for each folder
