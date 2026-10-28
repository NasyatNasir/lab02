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

def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    if not is_valid_dna(clean_sequence(seq)):
        raise ValueError("Invalid input")
    return ((clean_sequence(seq).count("G") + clean_sequence(seq).count("C")) / len(clean_sequence(seq))) * 100


def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    is_valid_dna(clean_sequence(dna))
    return clean_sequence(dna).replace("T", "U")


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    if not is_valid_dna(clean_sequence(motif)) and is_valid_dna(clean_sequence(seq)):
        raise ValueError("Invalid clean_sequence(motif)")
    patern = []
    start = clean_sequence(seq).find(clean_sequence(motif))
    while start != -1:
        patern.append(start)
        start = clean_sequence(seq).find(clean_sequence(motif), start+1)
    return patern
