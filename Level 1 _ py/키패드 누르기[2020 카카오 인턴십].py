def solution(numbers, hand):
    answer = ''
    pad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    left_idx=(0,3)
    right_idx=(0,3)
    
    for i in numbers:
        check = 0
        
        for idx, left_num in enumerate(pad[0]):
            if i == left_num:
                left_idx=(0,idx)
                check = 1
                answer += 'L'
                
        for idx, right_num in enumerate(pad[2]):
            if i == right_num:
                right_idx=(2,idx)
                check = 1
                answer += 'R'
        
        if check: continue
        
        mid_idx = (1, pad[1].index(i))
        left_distance = abs(mid_idx[0]-left_idx[0]) + abs(mid_idx[1]-left_idx[1])
        right_distance = abs(mid_idx[0]-right_idx[0]) + abs(mid_idx[1]-right_idx[1])
        
        if left_distance < right_distance:
            left_idx = mid_idx
            answer += 'L'
        elif left_distance > right_distance:
            right_idx = mid_idx
            answer += 'R'
        else:
            if hand == 'right':
                right_idx = mid_idx
                answer += 'R'
            else:
                left_idx = mid_idx
                answer += 'L'
    return answer
