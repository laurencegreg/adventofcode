package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}
func main() {
	defer timeTrack(time.Now())
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
	for scanner.Scan() {
		newVal, err = strconv.Atoi(scanner.Text())
		if it >= 2 {
			if it > 2 && a[it%3] < newVal {
				count++
			}
		}
		a[it%3] = newVal
		it++
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(count)
}
