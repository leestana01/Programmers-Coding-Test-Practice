def solution(left, right):
    sums=[]
    for i in range(left, right+1):
        check = [j+1 for j in range(i) if i%(j+1) == 0]
        if (len(check)%2 == 0):
            sums.append(i)
        else:
            sums.append(-i)
    return sum(sums)
