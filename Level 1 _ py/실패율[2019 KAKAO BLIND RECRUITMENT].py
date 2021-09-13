def solution(N, stages):
    people = {}
    stage_not_clear = {}
    people_num = len(stages)
    
    for i in range(N+1):
        people[i+1] = stages.count(i+1)
    
    for stage, person in people.items():
        if people_num:
            stage_not_clear[stage] = people[stage] / people_num
            people_num -= people[stage]
        else:
            stage_not_clear[stage] = 0
    del stage_not_clear[N+1]
        
    return [i[0] for i in sorted(stage_not_clear.items(), key=lambda x:x[1], reverse=True)]
