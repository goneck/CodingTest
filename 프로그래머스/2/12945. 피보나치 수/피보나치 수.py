def solution(n):
    nums=[0,1]
    for i in range(2,n+1):
        nums.append(nums[i-2]+nums[i-1])
    return nums[n]%1234567