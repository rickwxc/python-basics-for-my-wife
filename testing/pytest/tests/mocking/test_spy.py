class Foo(object):
    def bar(self):
        return 42


# make sure method been call
def test_spy(mocker):
    foo = Foo()
    mocker.spy(foo, 'bar')
    assert foo.bar() == 42
    assert foo.bar.call_count == 1
