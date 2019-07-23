import pytest


@pytest.mark.parametrize('size, color, weight', [
    ('10x10', 'red', '1kg'),
    ('20x10', 'blue', '2kg'),
    ('5x10', 'green', '1.5kg'),
])
@pytest.mark.smoke
def test_parametrize(size, color, weight):
    """do save into the db then load and compare"""
    db = []
    db.append((size, color, weight))
    assert db == [(size, color, weight)]


testdata = [
    (1, 2, 3),
    (10, 2, 12),
    (10, -3, 7),
]
@pytest.mark.parametrize("x,y,expected", testdata)
def test_a(x, y, expected):
    assert x + y == expected
