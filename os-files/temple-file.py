import tempfile


fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
fp.seek(0)
print(fp.read())
fp.close()


with tempfile.TemporaryFile() as fp:
     fp.write(b'Hello world!')
     fp.seek(0)
     print(fp.read())

# file is now closed and removed


with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
# # directory and contents have been removed
