class controlled_execution:
    def __enter__(self):
        print('setup')
    def __exit__(self, type, value, traceback):
        print('delete and done')

with controlled_execution() as thing:
    pass
