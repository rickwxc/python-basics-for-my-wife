def foo(on_something):
    on_something('foo', 'bar')


# make sure message been delivered
def test_stub(mocker):
    stub = mocker.stub(name='on_something_stub')
    foo(stub)
    stub.assert_called_once_with('foo', 'bar')
