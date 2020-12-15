
input = [16,1,0,18,12,14,19]

dico ={}
for i in range(0,len(input)-1) :
    dico[input[i]]=i
i=len(input)
val = input[-1]

while i<2020 :
    if val in dico.keys() :
        tmp=val
        val=i-1-dico[val]
        dico[tmp]=i-1
    else :
        dico[val]=i-1
        val=0
    i+=1

print(val)

