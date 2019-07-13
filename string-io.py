import io

contents = "0123456789abcdefghijklmopqrstuvw"
ssock = io.StringIO(contents)
print('1. read()', ssock.read())
print('2. read()', ssock.read())

ssock.seek(0)
print('1. read(15)', ssock.read(15))
print('2. read(15)', ssock.read(15))
print('3. read()', ssock.read())
ssock.close()
