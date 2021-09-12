def solution(num):
    cnt = 0
    while num != 1: 
        num = num%2==0 and num//2 or num*3+1
        cnt += 1
    return cnt if cnt < 500 else -1
