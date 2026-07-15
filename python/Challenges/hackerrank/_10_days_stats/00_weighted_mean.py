X = int(input())
ARRAY = list(map(int, input().split()))
WEIGHT = list(map(int, input().split()))
Y = 0

for i in range(X):
    Y += ARRAY[i]*WEIGHT[i]

print("{:.1f}".format(Y/sum(WEIGHT)))