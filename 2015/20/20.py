from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) 

input = 36000000

i=1

while sum(factors(i))*10 < input :
    print(i,sum(factors(i))*10)
    i+=1

print(i,sum(factors(i))*10)