import re
import string
alpha = (string.ascii_lowercase)
triplet = '|'.join([alpha[i:i+3]for i in range(0,len(alpha)-2)])
password = list("vzbxkghb")

def control(password) :
    string = ''.join(password)
    return not re.findall("[iol]",string) and len(re.findall("([a-z])\\1",string))>1  and re.findall(triplet,string)

def add(password):
    add=False
    i=len(password)-1
    while i>=0 and not add :
        char = password[i]
        charInt = alpha.index(char)
        if char in "hkn" :
            password[i]=alpha[charInt+2]
            add = True
        elif char == 'z' :
            password[i]='a'
            i-=1
        else :
            password[i]=alpha[charInt+1]
            add = True
    if not add :
        password = ['a']+password
        i=len(password)-1
        

while not control(password) :
#for j in range(0,1000):
    add(password)
print(''.join(password))
add(password)
while not control(password) :
#for j in range(0,1000):
    add(password)
print(''.join(password))