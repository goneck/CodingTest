def solution(a, b, n):
    answer = 0
    while(n>=a):
        answer+=(n//a)*b
        origin=n
        n-=(origin//a)*a
        n+=(origin//a)*b
    return answer