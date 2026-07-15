A, B = map(int, input().strip().split(' '))
C = int(input())

P = float(A/B)

RES = (1-P) ** (C-1) * P

print(round(RES, 3))

# 1 3
# 5