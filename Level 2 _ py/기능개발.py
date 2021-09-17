import math

def solution(progresses, speeds):
    days = [math.ceil((100-pro)/speed) for pro,speed in zip(progresses, speeds)]
    answer = []
    temp = 0
    for i in days:
        if i>temp:
            answer.append(1)
            temp = i
        else: answer[-1] += 1
    return answer
