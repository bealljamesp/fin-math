from itertools import product
from fractions import Fraction

P = list(product([1, 2, 3, 4, 5, 6], repeat=2))

N = sum(1 for x in P if sum(x) <= 9)

print(Fraction(N, len(P)))