import pytest
from lab02_sequences import find_motif, gc_content

def test_find_motif_boundary():
    with pytest.raises(ValueError):
        find_motif("ATCGGTAGCGTA", "")

def test_find_motif_invalid_input():
    with pytest.raises(ValueError):
        find_motif("no idea", "nein")

def test_find_motif_valid_input():
    assert find_motif("AAAA", "AA") == [0, 1, 2]

def test_gc_content_lowercase():
    assert gc_content("atcg") == pytest.approx(50.0)

def test_gc_content_invalid_input():
    with pytest.raises(ValueError):
        gc_content("test")