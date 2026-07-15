N = int(input())
X = list(map(float, input().strip().split()))
Y = list(map(float, input().strip().split()))

X_COPY = X.copy()

Y_COPY = Y.copy()

X_COPY.sort()

XD = dict(zip(X_COPY, range(1, N+1)))

Y_COPY.sort()

YD = dict(zip(Y_COPY, range(1, N+1)))

RX = [XD[i] for i in X]

RY = [YD[i] for i in Y]

print(round(1-(6*sum([(RX-RY)**2 for RX, RY in zip(RX, RY)]))/((N**3)-N), 3))

# 10
# 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
# 200 44 32 24 22 17 15 12 8 4

# 0.903