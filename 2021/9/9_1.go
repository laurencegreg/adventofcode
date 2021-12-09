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

func low(floor [][]int, x int, y int) int {
	val := floor[x][y]
	if (x == 0 || floor[x-1][y] > val) && (y == 0 || floor[x][y-1] > val) && (x == (len(floor)-1) || floor[x+1][y] > val) && (y == (len(floor[0])-1) || floor[x][y+1] > val) {
		return val + 1
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
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var floor [][]int

	for scanner.Scan() {
		var line []int
		for _, s := range strings.Split(scanner.Text(), "") {
			if len(s) > 0 {
				line = append(line, toInt(s))
			}
		}
		floor = append(floor, line)
	}
	res := 0
	for x := range floor {
		for y := range floor[0] {
			res += low(floor, x, y)
		}
	}
	fmt.Println(res)
}
