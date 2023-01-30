# pip install ply z3-solver
# https://regexcrossword.com/playerpuzzles/638abba5-5cfa-430c-b26a-33d1f4f42dab
from crossword import solve_crossword

rows = [
    r'(?!.*\t)(.).(\1).(\2).--.',
    r'(?!.*\t)\s\.\s+-\.+-\s+',
    r'(?!.*\t).?(-\.|\s\.)+[^-.]',
    r'(?!.*\t)(.)(\1)(\2)(.)\.+\4.',
    r'(?!.*\t)-.\.-.+(.)\1',
    r'(?!.*\t).[^-]+\s[^-]+',
    r'(?!.*\t)(-\.|\s)+([^\s])\2{2}',
    r'(?!.*\t)\s+-+\s(\..)+',
]

cols = [
    r'\.(.)(.)\2[.-]+\1{3}',
    r'([-.]+).\1\s+-+',
    r'.(.)--\1\.+-',
    r'\s([\s-]\.)*-{1,2}',
    r'[.\s]+-(\.[^.]){1,2}',
    r'\s\.+-(\s\.)+',
    r'.(([^.])\2)(.)\s+-\3\1',
    r'-.\.\s(-?\.)+',
    r'\.\s+\.-\.\s+-\.',
]

answer = solve_crossword(rows, cols)
for line in answer:
    print ('  '.join(line))
