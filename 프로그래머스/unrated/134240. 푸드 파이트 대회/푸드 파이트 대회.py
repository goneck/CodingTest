def solution(food):
    str1=""
    str2=""
    for i in range(len(food)):
        addedStr=str(i)*(food[i]//2)
        str1+=addedStr
        str2=addedStr+str2
    return str1+"0"+str2