class Calculator:
    def power(self, n, p):
        '''Checks whether n or p are negative'''
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p

myCalculator = Calculator()
T = int(input())

for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

# Sample Input
# 4
# 3 5
# 2 4
# -1 -2
# -1 3
# Sample Output
# 243
# 16
# n and p should be non-negative