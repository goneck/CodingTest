def solution(s):
    nums={"zero":"0" ,"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    word=''
    answer=''
    for i in range(len(s)):
        word+=s[i]
        if word.isdigit()==False and word in nums:
            answer+=nums[word]
            word=''
        elif word.isdigit()==True:
            answer+=word
            word=''
    return int(answer)
            