"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    raise NotImplementedError("TODO: implement clean_sequence")


def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    raise NotImplementedError("TODO: implement is_valid_dna")


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    raise NotImplementedError("TODO: implement gc_content")


def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    raise NotImplementedError("TODO: implement transcribe")


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    raise NotImplementedError("TODO: implement find_motif")
