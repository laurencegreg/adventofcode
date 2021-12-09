package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
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
		var num []int
		for _, s := range strings.Split(scanner.Text(), "\t") {
			if s != "" {
				num = append(num, toInt(s))
			}
			sort.Ints(num)
		}
		res += num[len(num)-1] - num[0]
	}
	fmt.Println(res)
}
