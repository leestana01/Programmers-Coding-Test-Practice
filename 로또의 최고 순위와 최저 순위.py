def check(func):
    lank = func
    if lank == 7: lank = 6
    return lank

def solution(lottos, win_nums):
    count = len([i for i in lottos if i in win_nums])
    unknown = len([i for i in lottos if i == 0])
    
    return [check(7-(count+unknown)), check(7-count)]
