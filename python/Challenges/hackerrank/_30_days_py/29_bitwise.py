if __name__ == '__main__':
    T = int(input())

    for t_itr in range(T):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        count = 0

        for x in range(n, 1, -1):
            for y in range(x-1, 0, -1):
                kk = x & y
                if kk > count and kk < k:
                    count = kk
                if count == k - 1:
                    break
            if count == k - 1:
                break

        print(count)





# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'bitwiseAnd' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER N
# #  2. INTEGER K
# #

# def bitwiseAnd(N, K):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         count = int(first_multiple_input[0])

#         lim = int(first_multiple_input[1])

#         res = bitwiseAnd(count, lim)

#         fptr.write(str(res) + '\n')

#     fptr.close()
