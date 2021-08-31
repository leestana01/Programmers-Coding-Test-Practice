def solution(numbers):
    answer = []
    
    for i,j in enumerate(numbers):
        for k in numbers[i+1:len(numbers)]:
            answer.append(j+k)
            
    return sorted(list(set(answer)))
