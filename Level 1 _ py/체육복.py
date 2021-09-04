def solution(n, lost, reserve):
    lost_rm = set(lost) - set(reserve)
    reserve_rm = set(reserve) - set(lost)

    for i in reserve_rm:
        if (i - 1) in lost_rm:
            lost_rm.remove(i - 1)
        elif (i + 1) in lost_rm:
            lost_rm.remove(i + 1)

    return n - len(lost_rm)

'''
--------------------------------------------------------
처음작성한 코드는 아래의 코드이나, 
테스트 케이스 상의 문제로 다른 이의 정답을 참고하여 lost_rm과 reserve_rm을 set을 통해 구하였다.

def solution(n, lost, reserve):
    lost_rm = [i for i in lost if i not in reserve]
    reserve_rm = [i for i in reserve if i not in lost]
    
    for i in reserve_rm:
        if (i - 1) in lost_rm:
            lost_rm.remove(i - 1)
        elif (i + 1) in lost_rm:
            lost_rm.remove(i + 1)
    
    return n - len(lost_rm)
'''
