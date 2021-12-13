package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
	"time"
)

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

func in(pos [2]int, dots [][2]int) bool {
	for _, p := range dots {
		if p == pos {
			return true
		}
	}
	return false
}

func printDots(dots [][2]int, x int, y int) {
	for i := 0; i < x; i++ {
		for j := 0; j < y; j++ {
			if in([2]int{j, i}, dots) {
				fmt.Print("# ")
			} else {
				fmt.Print(". ")
			}
		}

		fmt.Println()
	}
}

func fold(dots [][2]int, c string, i int) [][2]int {
	//printDots(dots, 15, 11)
	fmt.Println("will fold at ", c, ":", i)
	var newDots [][2]int
	for _, pos := range dots {
		x := pos[0]
		y := pos[1]
		if c == "x" {
			if x > i {
				x = i - (x - i)
			}
		} else {
			if y > i {
				y = i - (y - i)
			}

		}
		pos := [2]int{x, y}
		if !in(pos, newDots) {
			newDots = append(newDots, pos)
		}
	}
	return newDots
}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var dots [][2]int
	r, _ := regexp.Compile("fold along (x|y)=([0-9]*)")
	fmt.Println()
	for scanner.Scan() {
		s := scanner.Text()
		match := r.FindStringSubmatch(s)
		if s != "" {
			if len(match) != 0 {
				dots = fold(dots, match[1], toInt(match[2]))
				fmt.Println(len(dots))
			} else {
				line := strings.Split(s, ",")
				dots = append(dots, [2]int{toInt(line[0]), toInt(line[1])})
			}
		}
	}
	printDots(dots, 6, 39)
}
