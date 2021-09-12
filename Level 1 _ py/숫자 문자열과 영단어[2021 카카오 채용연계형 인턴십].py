def solution(s):
    En2Num=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(En2Num)):
        s = s.replace(En2Num[i],str(i))
    return int(s)
