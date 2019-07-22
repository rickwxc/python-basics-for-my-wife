import pytest

#pytest -s -v -k  test_fixtures_parametrizing

@pytest.fixture(params=['val00', 'val01', 'val01'], ids=["A", "B", 'B'])
def a(request):
    return request.param

def test_a(a):
    print('test_a:', a)

def idfn(fixture_value):
    if fixture_value == 0:
        return "DD"
    else:
        return 'CC'

@pytest.fixture(params=['val0', 'val1', 'val2'], ids=idfn)
def b(request):
    return request.param

def test_b(b):
    print('test_b:', b)


@pytest.fixture(params=['x', 'y', 'z'])
def c(request):
    return request.param

def test_c(c):
    print('test_c:', c)
