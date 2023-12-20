from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

reg = re.compile('(.*){(.*)}')

def stringToFun(x,exp):
    if ':' in exp :
        splitted = exp.split(':')
        return splitted[1] if eval("x['"+splitted[0][0]+"']"+splitted[0][1:]) else ''
    else:
        return exp

func = {}
runs = []
for line in lines :
    if line != "\n":
        extract = re.search(r"(.*){(.*)}",line.strip('\n')).groups()
        if extract[0]=='':
            val={}
            for e in extract[1].split(','):
                sp = e.split('=')
                val[sp[0]]=int(sp[1])
            runs.append(val)
        else:
            func[extract[0]]=extract[1].split(',')

res=0
for run in runs:
    step = 'in'
    while step != 'A' and step != 'R':
        fun = func[step]
        found = ''
        idx = 0
        while found == '' :
            found = stringToFun(run,fun[idx])
            idx+=1
        step = found
    if step == 'A':
        res+=sum(run.values())

print(res)