import hashlib
s = "iwrupvqb"
i = 0
while hashlib.md5((s+str(i)).encode('utf-8')).hexdigest()[0:5]!="00000" :
    i+=1

print(i)
print(hashlib.md5((s+str(i)).encode('utf-8')).hexdigest())