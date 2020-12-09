import re
f = open("input_full")
lines = f.readlines()
f.close()

valids = 0
fieldsName = {
    "byr":"^(19[2-9][0-9])$|^(200[0-2])$",
    "iyr":"^(201[0-9])$|^2020$",
    "eyr":"^(202[0-9])$|^2030$",
    "hgt":"^(((1[5-8][0-9])|(19[0-3]))cm)$|^(((59)|(6[0-9])|(7[0-6]))in)$",
    "hcl":"^#[a-f0-9]{6}$",
    "ecl":"^amb|blu|brn|gry|grn|hzl|oth$",
    "pid":"^\d{9}$",
    "cid":".*"
}
fieldsIndex = list(fieldsName)
print(fieldsIndex)
basic = [False,False,False,False,False,False,False,False]
basicValues = ["","","","","","","",""]
passport = list(basic)
passportValues = list(basicValues)
for line in lines :
    if line == '\n':
        nbValid = passport.count(True) 
        if nbValid==8 or (nbValid==7 and not passport[fieldsIndex.index("cid")]) :
            print(passportValues)
            valids+=1
        else :
            print(passportValues)
        passport = list(basic)
        passportValues = list(basicValues)
    fields = line.split(" ")
    for field in fields :
        if ":" in field :
            fieldTag = field.split(":")[0]
            passportValues[fieldsIndex.index(fieldTag)]=(field.split(":")[1]).strip('\n')
            passport[fieldsIndex.index(fieldTag)]=bool(re.search(fieldsName[fieldTag],(field.split(":")[1]).strip('\n')))

nbValid = passport.count(True) 

if nbValid==8 or (nbValid==7 and not passport[fieldsIndex.index("cid")]) :
    print(passportValues)
    valids+=1
print(valids)