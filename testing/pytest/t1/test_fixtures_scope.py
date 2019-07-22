import pytest
#pytest --setup-show

def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""

def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""

@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo class scope fixtures."""
    def test_3(self):
        """Test using a class scope fixture."""
    def test_4(self):
        """Again, multiple tests are more fun."""

"""
t1/test_fixtures_scope.py
SETUP    S sess_scope
    SETUP    M mod_scope
        SETUP    F func_scope
            t1/test_fixtures_scope.py::test_1 (fixtures used: func_scope, mod_scope, sess_scope).
        TEARDOWN F func_scope
        SETUP    F func_scope
            t1/test_fixtures_scope.py::test_2 (fixtures used: func_scope, mod_scope, sess_scope).
        TEARDOWN F func_scope
        SETUP    C class_scope
            t1/test_fixtures_scope.py::TestSomething::test_3 (fixtures used: class_scope).
            t1/test_fixtures_scope.py::TestSomething::test_4 (fixtures used: class_scope).
        TEARDOWN C class_scope
    TEARDOWN M mod_scope
TEARDOWN S sess_scope

"""
