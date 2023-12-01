library("stringr")
file = readLines("input")
res = 0
for (i in 1:length(file)){
    line=file[i]
    val = strtoi(paste(str_extract(line,"\\d"),str_extract(str_extract(line,"\\d[^0-9]*$"),"\\d"),sep=""))
    res = res + val
}
print(res)