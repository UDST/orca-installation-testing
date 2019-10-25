import tables
import orca

def test_version():
    # Conda release has the wrong version number currently, so this test won't pass
    assert orca.__version__ == '1.5.3'
    pass
