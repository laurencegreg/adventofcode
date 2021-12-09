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
	var res int
	var num []int
	for scanner.Scan() {
		for _, s := range strings.Split(scanner.Text(), "") {
			num = append(num, toInt(s))
		}
	}
	mid := len(num) / 2
	for i, n := range num {
		if n == num[(i+mid)%len(num)] {
			res += n
		}
	}
	fmt.Println(res)
}
