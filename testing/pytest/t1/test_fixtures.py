import pytest

def test_some_data(get_user, get_data):
    assert get_user['role'] == 'admin'
    assert get_data['credit'] == 99


# pytest -s -v -k test_user_name
def test_user_name(get_user_name):
    print(get_user_name)

def test_some_data2(user):
    assert user['role'] == 'admin'
