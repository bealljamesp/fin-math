#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    for i in range(1, n+1):
        print(arr[n-i], end=" ")

# 4
# 1 4 3 2
        
# 2 3 4 1