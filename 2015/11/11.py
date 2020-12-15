import re
import string
alpha = (string.ascii_lowercase)
triplet = '|'.join([alpha[i:i+3]for i in range(0,len(alpha)-2)])
input = list("vzbxkghb")

def control(list) :
    string = ''.join(list)
    return not re.findall("[iol]",string) and len(re.findall("([a-z])\\1",string))>1  and re.findall(triplet,string)

