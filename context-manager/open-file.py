class CustomOpen(object):
    def __init__(self, filename):
        print('...init...')
        self.file = open(filename)

    def __enter__(self):
        print('...enter...')
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        print('...exiting...')
        self.file.close()

with CustomOpen('sample.txt') as f:
    contents = f.read()
    print(contents)
