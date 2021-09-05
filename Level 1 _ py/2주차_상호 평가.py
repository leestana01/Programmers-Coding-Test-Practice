def grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 50: return 'D'
    return 'F'

def only_MAXorMIN(student):
    onlythings=[]
    if len([i for i in student if i == max(student)]) == 1: onlythings.append(max(student))
    if len([i for i in student if i == min(student)]) == 1: onlythings.append(min(student))
    return onlythings

def solution(scores):
    student = []
    for i in range(len(scores)):
        student.append([scores[j][i] for j in range(len(scores))])
        student[i] = [score for idx, score in enumerate(student[i]) if not (idx==i and score in only_MAXorMIN(student[i]))]
        student[i] = sum(student[i]) / len(student[i])
        
    return ''.join(list(map(grade,student)))
