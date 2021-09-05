def solution(n):
    answer = [False,False] + [True]*(n-1)
    for i in range(2,int(n**0.5+1)):
        for j in range(i*2,n+1,i):
            answer[j] = False
    return len([i for i in range(2,n+1) if answer[i]==True])
