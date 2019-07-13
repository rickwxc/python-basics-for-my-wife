def openAnything(source):
    if source == "−":
        import sys
        return sys.stdin
    # try to open with urllib (if source is http, ftp, or file URL)
    import urllib.request
    #print(urllib.request.urlopen.__doc__) 
    try:
        return urllib.request.urlopen(source)
    except (IOError, OSError, ValueError):
        pass
    # try to open with native open function (if source is pathname)
    try:
        return open(source)
    except (IOError, OSError):
        pass
    # treat source as string
    import io
    return io.StringIO(str(source)) 

ssock = openAnything('https://www.google.com')
#ssock = openAnything('/Users/rick/py/basics/streams/stream-count.py')
print(ssock.read(100))
ssock.close()

