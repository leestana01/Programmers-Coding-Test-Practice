def solution(n):
    answer = 0
    chk = []
    while(n!=0):
        chk.append(n%3)
        n = n // 3 

    chk.reverse()
    temp = 1
    for i , j in enumerate(chk):
        answer += j * temp
        temp *= 3
    
    return answer

print(solution(45))