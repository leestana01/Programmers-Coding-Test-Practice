def solution(arr):
    
    chk = arr[0]
    for i in arr:
        if i <= chk:
            chk = i
    arr.remove(chk)
    if len(arr) == 0:
        arr.append(-1)
    return arr