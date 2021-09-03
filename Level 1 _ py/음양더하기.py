def solution(absolutes, signs):
    for i,j in enumerate(signs):
        if j == False:
            signs[i] = -1
    return sum([i*j for i,j in zip(absolutes, signs)])
