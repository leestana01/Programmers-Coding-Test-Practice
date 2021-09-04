def solution(table, languages, preference):
    SI = table[0].split(' ')[1:]
    CONTENTS = table[1].split(' ')[1:]
    HARDWARE = table[2].split(' ')[1:]
    PORTAL = table[3].split(' ')[1:]
    GAME = table[4].split(' ')[1:]
    
    sums=[0,0,0,0,0]
    for idx1, part in enumerate([SI, CONTENTS, HARDWARE, PORTAL, GAME]):
        for idx2, lang in enumerate(languages):
            if lang in part:
                sums[idx1]+=(5-part.index(lang))*preference[idx2]
                
    max_scores = list(filter(lambda x : sums[x]==max(sums), range(len(sums))))
    return sorted([table[i].split(' ')[0] for i in max_scores])[0]
