import warnings


def lame_function():
    warnings.warn("Please stop using this", DeprecationWarning)


def test_lame_function(recwarn):
    lame_function()
    assert len(recwarn) == 1
    assert 1 == 1
