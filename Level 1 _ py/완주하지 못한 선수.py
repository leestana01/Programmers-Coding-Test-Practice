from itertools import zip_longest

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    chk=0
    for i, j in zip_longest(participant, completion):
        if (i != j):
            return i
        ++chk
