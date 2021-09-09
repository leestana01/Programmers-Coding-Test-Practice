def solution(weights, head2head):
    person = []
    for i, r in enumerate(head2head):
        p_win = 0
        p_win2 = 0
        games = 0
        for idx, result in enumerate(r):
            if result != 'N':
                games += 1
            if result == 'W':
                p_win += 1
                if weights[i] < weights[idx]:
                    p_win2 += 1
        p_win_percent = p_win / games * 100 if games != 0 else 0
        person.append([p_win_percent, p_win2, weights[i], i+1])
    
    person.sort(key=lambda x: (-x[0],-x[1],-x[2],x[3]))
    return [i[3] for i in person]
