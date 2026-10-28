# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 2
- Student name: MUHAMMAD NASYAT BIN MOHAMAD NASIR
- Matric no: A24CS0141
- Group ID: N/A
- AI level: 1
- Tools cited: OpenAI (2026). ChatGPT (GPT-6). Retrieved 29 October 2026 from https://chatgpt.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 29/10/2026, 01:11
- Tool: OpenAI (2026). ChatGPT (GPT-6). Retrieved 29 October 2026 from https://chatgpt.com
- Purpose: debug
- Prompt: 
    >   def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    >   """True for a non-empty string of A, C, G, T (and N when allowed)."""
    >allowed = set("")
    >
    >    if seq == "":
    >        raise ValueError("String must not be empty")
    >    if allow_n:
    >        allowed = set("ACGTN")
    >    else:
    >        allowed = set("ACGT")
    >    if set(seq) <= allowed:
    >        return True
    >    else:
    >        raise ValueError("String contains unidentified character(s)")
- Output: 
  >ChatGPT reviewed the DNA validation function and confirmed that its core validation logic was correct. It explained how set(seq) <= allowed checks whether all characters belong to the permitted DNA alphabet, and recommended removing the unnecessary allowed = set("") initialization.
- Verified by: by using pytest.ini
- My change:  
  >Removed the unnecessary allowed = set("") initialization. Retained the empty-string check, the allow_n option, the character-set validation, and ValueError 
- Used in: is_valid_dna()

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->
