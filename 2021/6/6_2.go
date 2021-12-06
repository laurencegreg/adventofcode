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

	fishes := make(map[int]int)
	for i := 0; i < 256+8; i++ {
		if i < 8 {
			fishes[i] = 1
			fmt.Println("fish starting at ", i, " will spawn ", 1, " fish(es)")
		} else {
			n := 1
			it := i
			spawn := 8
			for it >= 0 {
				if spawn == 0 {
					n += fishes[it-1]
					spawn = 6
				} else {
					spawn--
				}
				it--
			}
			fishes[i] = n
			fmt.Println("fish starting at ", i, " will spawn ", n, " fish(es)")
		}
	}
	result := 0
	for scanner.Scan() {
		fishList := strings.Split(scanner.Text(), ",")
		for _, f := range fishList {
			childs := fishes[256+8-toInt(f)]
			result += childs
		}
	}
	fmt.Println(result)
}
