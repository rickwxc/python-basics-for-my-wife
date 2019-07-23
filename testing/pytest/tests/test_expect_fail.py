import pytest


@pytest.mark.xfail
def test_xfail():
    assert 'no' == 'yes'


@pytest.mark.xfail(reason='this will fail: 2 != 1')
def test_xfail_with_reason():
    assert 2 == 1


# will report error if config pytest.ini as xfail_strict=true
"""
@pytest.mark.xfail()
def test_xfail_but_pass():
    assert 'yes' != 'yes'
"""
