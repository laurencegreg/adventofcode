package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
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

func highest(x int, y int, minX int, maxX int, minY int, maxY int) int {
	i := 0
	j := 0
	nextI := x
	nextJ := y
	maxJ := 0
	for nextI <= maxX && nextJ >= minY {
		i = nextI
		j = nextJ

		if x > 0 {
			x--
		}
		if j > maxJ {
			maxJ = j
		}
		y--
		nextI += x
		nextJ += y
		//fmt.Println(nextI, nextJ)
	}
	if i >= minX && j <= maxY {
		return maxJ
	} else {
		return 0
	}
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	r, _ := regexp.Compile(`x=(-?\d*)\.\.(-?\d*), y=(-?\d*)\.\.(-?\d*)`)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	s := scanner.Text()
	target := r.FindStringSubmatch(s)
	fmt.Println(target)
	minX := toInt(target[1])
	maxX := toInt(target[2])
	minY := toInt(target[3])
	maxY := toInt(target[4])
	maxStep := 0
	var maxxerX []int
	dir := 1
	if maxX < 0 {
		dir = -1
	}
	for x := 0; x <= (dir * maxX); x++ {
		slow := x
		dist := 0
		for i := 1; (dist*dir) <= (maxX*dir) && (slow >= 0); i++ {
			dist += (dir * slow)

			if (dist * dir) > (minX * dir) {
				if i > maxStep {
					maxStep = i
					maxxerX = []int{x}
				} else if i == maxStep {
					maxxerX = append(maxxerX, x)
				}
			}
			slow--

		}

	}
	fmt.Println("max steps : ", maxStep, " with x in ", maxxerX)
	higher := 0
	res := 0
	for j := 1; j < 10000; j++ {
		if res > higher {
			higher = res
		}
		res = highest(maxxerX[0], j, minX, maxX, minY, maxY)
		fmt.Println("for y ", j, " highest point : ", res)
	}
	fmt.Println("higher : ", higher)
}
