"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return raw.strip().upper().replace(" ","")
        


def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    allowed = set("")
    
    if seq == "":
        return False
    if allow_n:
        allowed = set("ACGTN")
    else:
        allowed = set("ACGT")
    if set(seq) <= allowed:
        return True
    else:
        raise ValueError("String contains unidentified character(s)")

"""
if allow_n
    if let A C G T N / only consist allowed leter
        return true
    else
        raises ValueError
if !allow_n
    if let A C G T N / only consist allowed leter
        return true
    else raises ValueError"""


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    raise NotImplementedError("TODO: implement gc_content")


def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    raise NotImplementedError("TODO: implement transcribe")


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    raise NotImplementedError("TODO: implement find_motif")
