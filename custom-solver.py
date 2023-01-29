# Solves https://regexcrossword.com/playerpuzzles/585e12a824c43
from crossword import solve_crossword
echo "Solving Challenge"
solve = solve_crossword(["HE|LL|O+","[PLEASE]+"], ["[^SPEAK]+","EP|IP|EF"])
for line in solve:
    print (''.join(line))
