from functools import reduce

def factors50(n):    
    res = set()
    for i in range(1, int(n**0.5) + 1) :
        if n % i == 0 :
            ni = n//i
            if i<= 50 :
                res.add(ni)
            if ni<=50 :
                res.add(i)

    return res
input = 36000000

i=1
while (sum(list(map(lambda j : i//j,range(1,50)))))*11 < input :
    i+=1
print(i)
while sum(factors50(i))*11 < input :
    
    i+=1

print(i,sum(factors50(i))*11)