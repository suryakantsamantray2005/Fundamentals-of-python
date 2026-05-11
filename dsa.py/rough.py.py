from itertools import permutations,combinations
s='abc'
result=permutations(s)
for i in result:
   print(''.join(i))