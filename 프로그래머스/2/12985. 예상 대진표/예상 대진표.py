import math 
def solution(n,a,b):
    answer = 0
    while(math.ceil(a/2)!=math.ceil(b/2)):
        answer+=1
        a=math.ceil(a/2)
        b=math.ceil(b/2)
            
    return answer+1