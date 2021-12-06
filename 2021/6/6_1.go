package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

func fish(i int, time int) int {
	count := 1
	age := i
	left := time
	for left > 0 {
		if age == 0 {
			count += fish(8, left-1)
			age = 6
		} else {
			age--
		}
		left--
	}
	return count
}

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	result := 0
	for scanner.Scan() {
		fishes := strings.Split(scanner.Text(), ",")
		for _, f := range fishes {
			childs := fish(toInt(f), 80)
			result += childs
		}
	}
	fmt.Println(result)
}
