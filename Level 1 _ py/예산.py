def solution(d, budget):
    answer = 0
    for price in sorted(d):
        if budget>=price:
            budget -= price
            answer += 1
    return answer
