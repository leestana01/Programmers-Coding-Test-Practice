def solution(n):
    answer = []
    
    while (n != 0):
        answer.append(n%10)
        n = n // 10
    
    return answer

# 이하는 테스트 케이스
print(solution(12345))