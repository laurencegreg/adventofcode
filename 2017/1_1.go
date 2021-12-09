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
	for scanner.Scan() {
		var first string
		var prev string
		for i, s := range strings.Split(scanner.Text(), "") {
			if i == 0 {
				first = s
				prev = s
			} else {
				if s == prev {
					res += toInt(s)
				}
				prev = s
			}
		}
		if prev == first {
			res += toInt(first)
		}
	}
	fmt.Println(res)

}
