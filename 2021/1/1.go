package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
	"strconv"
)

func main() {
    file, err := os.Open("input")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
	scanner.Scan()
    val, err := strconv.Atoi(scanner.Text())
	count := 0
	var newVal int
    for scanner.Scan() {
        newVal, err = strconv.Atoi(scanner.Text())
		if newVal > val {
			count++
		}
		val = newVal
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	fmt.Println(count)
}