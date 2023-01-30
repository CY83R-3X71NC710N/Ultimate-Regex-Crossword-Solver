# pip install ply z3-solver
# https://regexcrossword.com/playerpuzzles/638abba5-5cfa-430c-b26a-33d1f4f42dab
from crossword import solve_crossword

rows = [
    r"(.)(.)(.)\3\1\2\1",
    r"(.)\1(.)\2\1(.)(.)",
    r"(.)(.)\2\1(.)\3\2",
    r"(.)(.)\1(.)2\1\3",
    r"(.)(.)(.)\2\1\2\3",
    r"(.)(.)\1\2\1(.)\2",
    r"(.)\1(.)(.)\3\1(.)",
]

cols = [
    r"(.)(.)(.)\1(.)\2\4",
    r"(.)(.)\2(.)\1\3\1",
    r"(.){2}(.)\1\2(.)3",
    r"(.)(.)(.)(.)\1\4\1",
    r"(.)(.)(.)\1(.)4\3",
    r"(.)\1(.)\1\2(.)\1",
    r"(.)(.)1(.)\2\2\3",
]

answer = solve_crossword(rows, cols)
for line in answer:
    print ("  ".join(line))
