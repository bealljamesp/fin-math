from math import factorial, exp

MEAN = float(input())
K = int(input())

POISSON = ((MEAN ** K) * exp(-MEAN)) / factorial(K)

print("%.3f" % POISSON)

# 2.5
# 5