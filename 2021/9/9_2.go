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

func low(floor [][][]int, x int, y int) bool {
	val := floor[x][y][0]
	if (x == 0 || floor[x-1][y][0] > val) && (y == 0 || floor[x][y-1][0] > val) && (x == (len(floor)-1) || floor[x+1][y][0] > val) && (y == (len(floor[0])-1) || floor[x][y+1][0] > val) {
		return true //basin(floor,x,y)
	} else {
		return false
	}
}

func basin(floor [][][]int, x int, y int) int {
	res := 0
	if floor[x][y][1] == 0 && floor[x][y][0] < 9 {
		floor[x][y][1] = 1
		res += 1
		if x > 0 {
			res += basin(floor, x-1, y)
		}
		if x < (len(floor) - 1) {
			res += basin(floor, x+1, y)
		}
		if y > 0 {
			res += basin(floor, x, y-1)
		}
		if y < (len(floor[0]) - 1) {
			res += basin(floor, x, y+1)
		}

	}
	return res

}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var floor [][][]int

	for scanner.Scan() {
		var line [][]int
		for _, s := range strings.Split(scanner.Text(), "") {
			if len(s) > 0 {
				line = append(line, []int{toInt(s), 0})
			}
		}
		floor = append(floor, line)
	}
	var resTab []int
	for x := range floor {
		for y := range floor[0] {
			if low(floor, x, y) {
				resTab = append(resTab, basin(floor, x, y))
			}
		}
	}
	sort.Ints(resTab)
	l := len(resTab)
	fmt.Println(resTab[l-1] * resTab[l-2] * resTab[l-3])
}
