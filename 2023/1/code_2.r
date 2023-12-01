library("stringr")
library("hash")

strReverse <- function(x)
        sapply(lapply(strsplit(x, NULL), rev), paste, collapse="")

h <- hash()
h[["one"]] <- "1"
h[["two"]] <- "2"
h[["three"]] <- "3"
h[["four"]] <- "4"
h[["five"]] <- "5"
h[["six"]] <- "6"
h[["seven"]] <- "7"
h[["eight"]] <- "8"
h[["nine"]] <- "9"

intReplace <- function(x){
        s = h[[x]]
        return(if (is.null(s)) x else s)
}

file = readLines("input")
res = 0
for (i in 1:length(file)){
    line=file[i]
    first = str_extract(line,"(\\d|one|two|three|four|five|six|seven|eight|nine)")
    enil = strReverse(line)
    last = strReverse(str_extract(enil,"(\\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)"))
    val = strtoi(paste(intReplace(first),intReplace(last),sep=""))
    res = res + val
}
print(res)