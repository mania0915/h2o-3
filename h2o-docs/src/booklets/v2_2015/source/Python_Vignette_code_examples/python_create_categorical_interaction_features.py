In [163]: df12.interaction(['A','B'], pairwise=False, max_factors=3, min_occurrence=1)

Interactions Progress: [########################] 100%
Out[163]: 
   A_B
   -------
0  foo_one
1  bar_one
2  foo_two
3  other
4  foo_two
5  other
6  foo_one
7  other

[8 rows x 1 column]