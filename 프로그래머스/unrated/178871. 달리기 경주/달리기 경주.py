def solution(players, callings):
    playerDict={player : rank for rank, player in enumerate(players, start=1)}
    rankDict={rank:player for rank, player in enumerate(players, start=1)}
    
    for calling in callings:
        rank=playerDict[calling]
        name=rankDict[rank-1]
        playerDict[calling]-=1
        playerDict[name]+=1
        rankDict[rank]=name
        rankDict[rank-1]=calling
    
    return list(dict(sorted(rankDict.items())).values())