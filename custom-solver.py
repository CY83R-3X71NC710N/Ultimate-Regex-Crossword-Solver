# Solves https://regexcrossword.com/playerpuzzles/585e12a824c43
Echo "Solving Challenge"
from crossword import solve_crossword
solve = solve_crossword(["HE|LL|O+","[PLEASE]+"], ["[^SPEAK]+","EP|IP|EF"])
for line in solve:
    print (''.join(line))
