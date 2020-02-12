#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) ==1 and s=='a':
        return n
    else:
        times = n//len(s)
        remainder = n%len(s)
        repeated_string = str(s*times + s[:remainder])
        return repeated_string.count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
