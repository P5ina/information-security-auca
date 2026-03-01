#!/usr/bin/env python3
"""
Lab 12 Task: Generate a personalized wordlist using victim's info.
Attacker collects name, surname, date of birth — and combines them
in various ways to guess the password.
"""

import itertools
import sys


def generate_wordlist(first: str, last: str, dob: str) -> list[str]:
    """
    dob format: DDMMYYYY  e.g. 24072005
    """
    f = first.lower()
    l = last.lower()
    F = first.capitalize()
    L = last.capitalize()

    day   = dob[:2]   
    month = dob[2:4]  
    year  = dob[4:]   
    yy    = dob[6:]   

    candidates = set()

    # Name/surname combinations
    for a, b in itertools.permutations([f, l]):
        candidates.update([
            f"{a}{b}",
            f"{a}.{b}",
            f"{a}_{b}",
            f"{a}{b}{year}",
            f"{a}{b}{yy}",
            f"{a}{b}{day}{month}",
            f"{a}{b}{dob}",
        ])

    # With date parts
    for name in [f, l, F, L]:
        candidates.update([
            f"{name}{year}",
            f"{name}{yy}",
            f"{name}{day}{month}",
            f"{name}{day}{month}{year}",
            f"{name}{dob}",
            f"{name}123",
            f"{name}1234",
            f"{name}12345",
            f"{name}!",
            f"{name}@{year}",
        ])

    # Pure date variants
    candidates.update([
        dob, day + month + year, year + month + day,
        day + month + yy, f"{day}/{month}/{year}",
    ])

    # Leet speak of first name
    leet = f.replace('a','4').replace('e','3').replace('i','1').replace('o','0').replace('s','5')
    candidates.update([leet, leet + year, leet + dob])

    return sorted(candidates)


if __name__ == "__main__":
    # Example victim info
    first = sys.argv[1] if len(sys.argv) > 1 else "John"
    last  = sys.argv[2] if len(sys.argv) > 2 else "Doe"
    dob   = sys.argv[3] if len(sys.argv) > 3 else "01011990"  # DDMMYYYY

    wordlist = generate_wordlist(first, last, dob)

    output_file = "victim_wordlist.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(wordlist))

    print(f"Generated {len(wordlist)} password candidates → {output_file}")
    print("\nSample entries:")
    for w in wordlist[:15]:
        print(f"  {w}")
