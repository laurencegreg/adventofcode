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

func divider(num []int, i int) int {
	for j := i + 1; j < len(num); j++ {
		if num[j] > num[i] {
			if num[j]%num[i] == 0 {
				return num[j] / num[i]
			}
		} else {
			if num[i]%num[j] == 0 {
				return num[i] / num[j]
			}
		}
	}
	return 0
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
		var num []int
		for _, s := range strings.Split(scanner.Text(), "\t") {
			if s != "" {
				num = append(num, toInt(s))
			}
		}

		for i, _ := range num {
			tmp := divider(num, i)
			if tmp != 0 {
				res += tmp
				break
			}
		}
	}

	fmt.Println(res)
}
