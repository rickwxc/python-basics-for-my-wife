import pytest


@pytest.mark.skip(reason='misunderstood the API')
def test_skipping():
    assert 1 == 2


version = 1
@pytest.mark.skipif(version < 2, reason='not supported until version 2')
def test_skipping_2():
    assert 1 == 2
