# Solves https://regexcrossword.com/playerpuzzles/585e12a824c43
from crossword import solve_crossword

rows = [
    r'[^XZVCHFJLQM]+',
]

cols = [
    r'.*\sA?(SA|PE|N\s){2}',
]

answer = solve_crossword(rows, cols)
for line in answer:
    print ('  '.join(line))
