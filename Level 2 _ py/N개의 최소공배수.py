import math

def solution(arr):
    while True:
        a = arr.pop()
        b = arr.pop()
        arr.append(a * b // math.gcd(a, b))
        if len(arr) == 1: break
    return arr[0]
