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
		for _, s := range strings.Split((strings.Split(scanner.Text(), "|")[1]), " ") {
			length := len(s)
			if length == 3 || length == 2 || length == 4 || length == 7 {
				res++
			}
		}
	}

	fmt.Println(res)
}
