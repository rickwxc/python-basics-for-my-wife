import pytest
import time

@pytest.fixture()
def get_user():
    return {
            'uid': 1001,
            'role': 'admin',
    }

#rename
@pytest.fixture(name='user')
def get_user_data():
    return {
            'uid': 1001,
            'role': 'admin',
    }

@pytest.fixture()
def get_data():
    return {
            'credit': 99
    }

@pytest.fixture(params=('alice', 'bob', 'cathy'))
def get_user_name(request):
    return request.param

@pytest.fixture(autouse=True, scope='session')
def total_test_time():
    """Report total test durations."""
    start = time.time()
    yield
    delta = time.time() - start
    print('\nTotal duration : {:0.3} seconds'.format(delta))

@pytest.fixture(autouse=True)
def each_test_time():
    """Report test durations after each function."""
    start = time.time()
    yield
    delta = time.time() - start
    print('\nduration : {:0.3} seconds'.format(delta))

@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""

@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""

@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""

@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""
