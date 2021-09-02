def solution(a, b):
    
    mday = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_end = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    day_sum = b
    for i,j in enumerate(mday):
        if i+1 < a:
            day_sum += j
    
    return day_end[day_sum%7]
