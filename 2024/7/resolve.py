from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

def calc(sum,nums,targ):
    if sum > targ :
        return False
    elif len(nums)==0 :
        return sum == targ
    else :
        return calc(sum+nums[0],nums[1:],targ) or calc(sum*nums[0],nums[1:],targ)


res = 0
for line in lines :
    arr = line.strip('\n').split(' ')
    target = int(arr[0][:-1])
    if calc(int(arr[1]),list(map(int,arr[2:])),target):
        res+=target

print(res)
