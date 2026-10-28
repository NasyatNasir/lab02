import pytest
from lab02_sequences import find_motif

def test_boundary():
    with pytest.raises(ValueError):
        find_motif("ATCGGTAGCGTA", "")

def test_invalid_input():
    with pytest.raises(ValueError):
        find_motif("no idea", "nein")

def test_valid_input():
    assert find_motif("ATCGATCGATCG", "ATCG") == [0, 4, 8]