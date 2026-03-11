import pytest

def test_skew_array():
    from scripts.skew_analysis import SkewArray
    assert SkewArray("CATGGGCATCGGCCATACGCC") == [0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2]
    

def test_minimum_skew():
    from scripts.skew_analysis import MinimumSkew
    assert MinimumSkew("ACCGGGTATTGGCC") == [3]
