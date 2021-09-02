def solution(strings, n):
    return [j[1:]for j in sorted([i[n]+i for i in strings])]
