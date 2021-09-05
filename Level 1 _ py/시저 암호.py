def solution(s, n):
    answer=[0]*len(s)
    for idx, alpha in enumerate(s):
        if alpha == ' ':
            answer[idx]=alpha
            continue
        if ord(alpha) <= 122 and ord(alpha)+n >122 : temp = ord(alpha)+n-26
        elif 65 <= ord(alpha) <= 90 and ord(alpha)+n >90 : temp = ord(alpha)+n-26
        else: temp = ord(alpha)+n
        answer[idx]=chr(temp)
    return ''.join(answer)
