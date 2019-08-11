class DownloadFileAndProcess:
    def __enter__(self):
        self.path = '/tmp/file.txt'
        # download content
        return 'content in file.txt'

    def __exit__(self, type, value, traceback):
        print('delete [%s] and done' % self.path)

with DownloadFileAndProcess() as content:
    print('processing: ', content)
