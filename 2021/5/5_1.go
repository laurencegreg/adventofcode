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

type position struct {
	x int
	y int
}

func negPos(i int, j int) int {
	diff := j - i
	if diff == 0 {
		return 0
	} else if diff > 0 {
		return 1
	} else {
		return -1
	}
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
	dict := make(map[position]int)
	for scanner.Scan() {
		positions := strings.Split(scanner.Text(), " -> ")
		p1 := strings.Split(positions[0], ",")
		p2 := strings.Split(positions[1], ",")
		x1 := toInt(p1[0])
		y1 := toInt(p1[1])
		x2 := toInt(p2[0])
		y2 := toInt(p2[1])
		dx := negPos(x1, x2)
		dy := negPos(y1, y2)
		if x1 == x2 || y1 == y2 {
			for y1 != y2 || x1 != x2 {
				dict[position{x1, y1}] += 1
				x1 += dx
				y1 += dy
			}
			dict[position{x1, y1}] += 1
		}
	}
	counter := 0
	for _, value := range dict {
		if value > 1 {
			counter += 1
		}
	}
	fmt.Println(counter)
}
