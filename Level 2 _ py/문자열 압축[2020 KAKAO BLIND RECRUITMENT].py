def solution(s):
    min_cnt=1000
    for cut_num in range(1,len(s)+1):
        cut_list = [s[i:i+cut_num] for i in range(0,len(s),cut_num)]
        temp = ''
        string_cnt = []
        for i in cut_list:
            if temp != i:
                temp = i
                string_cnt.extend([1,i])
            else:
                string_cnt[len(string_cnt)-2] += 1
        while 1 in string_cnt: del string_cnt[string_cnt.index(1)]
        result = ''.join(list(map(str, string_cnt)))
        min_cnt = min(min_cnt, len(result))
    return min_cnt
