def solution(seoul):
    for i,j in enumerate(seoul):
        if j == "Kim":
            return '김서방은 '+str(i)+'에 있다'
