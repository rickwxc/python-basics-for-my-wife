import os
import src.rickw.pkg1
import src.rickw.api


class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    src.rickw.pkg1.get_url2()
    src.rickw.api.get_url
    os.remove.assert_called_once_with('file')
