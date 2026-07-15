#!/bin/python3

import math
import os
import random
import re
import sys

N = int(input())
X = list(map(int, input().strip().split(' ')))

MEAN = sum(X)/N
sum = 0

for i in range(N):
    sum += ((X[i]-MEAN)**2)/N

print(round(sum**0.5, 1))
