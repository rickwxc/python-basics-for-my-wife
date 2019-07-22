import pytest


@pytest.mark.smoke
def test_params_smoke():
    assert 'yes' == 'yes'


"""
add --strict to addopts in pytest.ini will make this fail other than warning
@pytest.mark.not_exist_mark
def test_params():
    assert 'yes' == 'yes'
"""
