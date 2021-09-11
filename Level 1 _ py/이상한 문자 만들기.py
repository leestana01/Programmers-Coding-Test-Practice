def solution(s):
    answer=[]
    
    finder=[]
    idx = 0
    while idx > -1:
        idx = s.find(' ',idx)
        if idx > -1:
            finder.append(idx)
            idx += 1
    
    for splited in s.split(' '):
        for idx, word in enumerate(splited):
            if idx % 2 == 0:
                answer.append(word.upper())
            else:
                answer.append(word.lower())
            
    for i in finder:
        answer.insert(i,' ')
    
    return ''.join(answer)
