def solution(arr):
    answer = [-1]
    
    for n in arr:
        if answer[len(answer)-1] != n:
            answer.append(n)
    answer.remove(-1)
    return answer
