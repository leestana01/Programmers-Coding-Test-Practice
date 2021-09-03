def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2, 1, 2, 3, 2, 4, 2, 5]
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1=0
    score2=0
    score3=0
    for i,j in enumerate(answers):
        if j==p1[i%5]:
            score1 += 1
        if j==p2[i%8]:
            score2 += 1
        if j==p3[i%10]:
            score3 += 1
    
    answer=[]
    scores=[score1, score2, score3]
    for i,j in enumerate(scores):
        if j == max(scores):
            answer.append(i+1)
    return answer
