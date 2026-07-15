from sklearn import linear_model

M, N = list(map(int, input().strip().split()))
X = [0]*N
Y = [0]*N

for i in range(N):
    inp = list(map(float, input().strip().split()))
    X[i] = inp[:-1]
    Y[i] = inp[-1]

LM = linear_model.LinearRegression()
LM.fit(X, Y)
A = LM.intercept_
B = LM.coef_

Q = int(input())

for i in range(Q):
    f = list(map(float, input().strip().split()))
    Y = A + sum([B[j] * f[j] for j in range(M)])
    print(round(Y, 2))

# 2 7
# 0.18 0.89 109.85
# 1.0 0.26 155.72
# 0.92 0.11 137.66
# 0.07 0.37 76.17
# 0.85 0.16 139.75
# 0.99 0.41 162.6
# 0.87 0.47 151.77
# 4
# 0.49 0.18
# 0.57 0.83
# 0.56 0.64
# 0.76 0.18
    
# 105.21
# 142.67
# 132.94
# 129.7