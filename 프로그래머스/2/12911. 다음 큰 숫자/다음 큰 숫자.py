def solution(n):
    # 십진수를 이진수로 변환후 정수 리스트로 변환
    n=list(map(int, bin(n)[2:]))
    pivot=-1
    for i in range(len(n)-1, 0, -1):
        if n[i]==1 and n[i-1]==0:
            pivot=i
            n[i], n[i-1]= n[i-1],n[i]
            break
    if pivot==-1 and n[-1]!=0:
        return int("0b10"+"1"*(len(n)-1), 2)
    elif pivot==-1 and n[-1]==0:
        return int("0b1"+"0"*(n.count(0)+1)+"1"*(n.count(1)-1),2)
    else:
        n[pivot:]=sorted(n[pivot:])
        return int("0b"+''.join(map(str, n)),2)