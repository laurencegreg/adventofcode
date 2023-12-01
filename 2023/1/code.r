library("stringr")
file = readLines("input")
res = 0

strReverse <- function(x)
        sapply(lapply(strsplit(x, NULL), rev), paste, collapse="")

for (i in 1:length(file)){
    line=file[i]
    val = strtoi(paste(str_extract(line,"\\d"),str_extract(strReverse(line),"\\d"),sep=""))
    res = res + val
}
print(res)