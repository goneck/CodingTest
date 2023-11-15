def solution(s):
    removed_zeros=0
    cnt=0
    while s!="1":
        removed_zeros+=s.count('0');
        cnt+=1
        s=format(len(s.translate({ord('0'):None})), 'b')
    return [cnt, removed_zeros]
        