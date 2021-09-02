def solution(s):
    return "".join(sorted([i for i in s if i.islower()],reverse=True)+sorted([j for j in s if j.isupper()],reverse=True))
