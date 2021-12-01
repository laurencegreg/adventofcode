package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
	"strconv"
)

func sum(array [3]int) int {  
	result := 0  
	for _, v := range array {  
		result += v  
	}  
	return result  
} 
func main() {
    file, err := os.Open("input")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
	var a [3]int
	count := 0
	it := 0
	newVal := 0
	oldSum := 0
	newSum := 0
    for scanner.Scan() {
        newVal, err = strconv.Atoi(scanner.Text())
		a[it%3] = newVal
		if (it>=2){
			newSum= sum(a)
			if (it>2 && newSum>oldSum){
				count++
			}
		}
		oldSum = newSum
		it++
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	fmt.Println(count)
}