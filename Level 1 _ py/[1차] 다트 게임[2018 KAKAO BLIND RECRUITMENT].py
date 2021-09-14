def solution(dartResult):
    dartResult = list(dartResult)
    for idx, s in enumerate(dartResult):
        if (s == 'S') or (s == 'D') or (s == 'T'):
            if (idx == len(dartResult)-1) or dartResult[idx+1].isalnum():
                dartResult.insert(idx+1,'$')
    # print('수상 없는 dartResult 표기:', dartResult)
    
    while '*' in dartResult:
        star_idx = dartResult.index('*')
        dartResult[star_idx] = 'star+'
        if star_idx > 2:
            dartResult.insert(star_idx-3,'star')
    # print('스타상 처리 후 dartResult:',dartResult)
    
    dartResult = ''.join(dartResult).replace('S','').replace('D','**2').replace('T','**3').replace('star','*2').replace('#','*(-1)+').replace('$','+').rstrip('+')
    return eval(dartResult)
