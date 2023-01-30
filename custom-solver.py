# Solves https://regexcrossword.com/playerpuzzles/585e12a824c43
from crossword import solve_crossword

rows = [
    r'(?=(.*[$ORRY_NO_MONEY_HERE]){10})?[AM I POOR]?.*',
    r'(?=(.*[(MORE_THAN_1$)]){4}).*;.*',
    r'(?=(.*[$OME_MORE_DOLLARS]){3}).*',
    r'(?=(.*[STILL_SOME_MORE_DOLLAR$]){4}).*',
    r'(?=(.*[ALL_YOUR_J@CKPOT$_ARE_BELONG_TO_ME]){5}).*',
    r'(?=(.*[\3RD_BUCK\'$_THE_CHARM//]){5}).*[.].*',
    r'(?=(.*[DOLLAR,$,$_AND_DOLLAR.]){10}).*',
    r'(?=(.*[{MORE_THAN_1$}]){6}).*',
    r'(?!.*\$\$)(?=(.*[TOTAL_IN_THI$_LINE=2]){3}).*',
    r'(?!(?:.*;){3})(?=(.*[1$+3$S]){5})..(.)..\2.*',
    r'(?=(.*[{"WINDF@LL"_PROFIT$}]){9}).*}.*{.*',
    r'(?=(.*[2$S+1$]){4})(?=.*\$).*',
    r'(?=(.*[KEEP_DOLL@R$_COMING]){6}).*\.',
    r'(?=(.*[I_WANT_$OME_MORE]){6}).*',
    r'(?=.*,)(?=(.*[3$S+2$S]){6}).*',
    r'(?=(.*[3$S&1#]){5}).*'
]

cols = [
    r'(?!.*\w)(\*)(.)\2.*(.)(.)\)\4\3',
    r'(?!.*\w)\../.+(.+).*\1',
    r'(?=(([^\$])..)+\1\2)(.)(..\3)+\4',
    r'((\W){2}\2)\1{2}.',
    r'(?!.*\w)(.(.+))\1.?\2.',
    r'(?!.*\w)((.)+(.)).*\1.*\1.*\2',
    r'(?!(.*\w){2})(.)((.)+\2)(.+\4\2)\5',
    r'(?!(.*\w){2}).*{{*}}*.(.)\w\[\2\|]*',
    r'(?!.*\w)([$,])+.(}|\)).\1[+](.)\3-*',
    r'(?!.*\w)(?=(.))(\1.+)+',
    r'(?!.*\w)(?=(.))(\1.+){5}',
    r'(?!(.*\w){2}).*{{*}}*@_.*(?=(.))(\2.*){3}',
    r'(?!(.*\w){2})(?=(.))(\2.+)+',
    r'(?!(.*\w){2})(?=(.))(\2.+){5}',
    r'(?!.*\w)(?=^.*\$\^.*$)^\$.*.:.*.\^$',
    r'(?!.*#\$)[$$$ I AM RICH! $$$]*\W*`',

def solve_crossword(rows, cols):
    # Code to solve crossword puzzle

    return answer

answer = solve_crossword(rows, cols)
for line in answer:
    print(' '.join(line))
