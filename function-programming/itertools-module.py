import itertools
import os
rs = itertools.starmap(os.path.join,
        [('/bin', 'python'), ('/usr', 'bin', 'java'), ('/usr', 'bin', 'perl'), ('/usr', 'bin', 'ruby')])
print (list(rs))

#spread tuple as argument
print ([ os.path.join(*i) for i in [('/bin', 'python'), ('/usr', 'bin', 'java'), ('/usr', 'bin', 'perl'), ('/usr', 'bin', 'ruby')]] )
