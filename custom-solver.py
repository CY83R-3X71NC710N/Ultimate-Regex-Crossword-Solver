Echo "Solving Challenge"
from crossword import solve_crossword
solve = solve_crossword(["HE|LL|O+","[PLEASE]+"], ["[^SPEAK]+","EP|IP|EF"])
for line in solve:
    print (''.join(line))
