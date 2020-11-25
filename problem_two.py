import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for x in range(n+1):
        if x>0:
            print((" ")*(n-x) + ("#")*x)
if __name__ == '__main__':
    n = int(input())

    staircase(n)
