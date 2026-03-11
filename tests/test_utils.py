import pytest

def test_hamming():
    from scripts.utils import HammingDistance
    assert HammingDistance("AGCT", "AGCT") == 0
    assert HammingDistance("AGCT", "AGTT") == 1
    assert HammingDistance("AGCT", "TGCA") == 2
    with pytest.raises(ValueError):
        HammingDistance("AGCT", "AGC")