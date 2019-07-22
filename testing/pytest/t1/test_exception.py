import pytest

def willGiveTypeError():
    return 1 + '2'

def test_add_raises():
    with pytest.raises(TypeError) as excinfo:
        willGiveTypeError()
    err_msg = excinfo.value.args[0]

    assert err_msg == "unsupported operand type(s) for +: 'int' and 'str'"

