import pytest

def test_params():
    assert 'yes' == 'yes'

@pytest.mark.smoke
def test_params_smoke():
    assert 'yes' == 'yes'

