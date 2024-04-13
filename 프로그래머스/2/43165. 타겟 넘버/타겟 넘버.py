def solution(numbers, target):
    # BFS 풀이
    result = [0] # 이진트리로 만들었을 때 최종 결과가 들어갈 배열
    
    for num in numbers:
        temp=[]
        for res in result:
            temp.append(res+num)
            temp.append(res-num)
        result=temp
    
    answer = 0
    for res in result:
        if res==target:
            answer+=1
    
    return answer
    