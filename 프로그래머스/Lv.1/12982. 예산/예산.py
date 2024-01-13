def solution(d, budget):
    d=sorted(d)
    whole=0
    for i in range(len(d)):
        if whole+d[i]<=budget:
            whole+=d[i]
        else:
            return i
    if whole==sum(d):
        return len(d)
        
