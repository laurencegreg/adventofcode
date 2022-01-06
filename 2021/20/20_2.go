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

var binary []string

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}
func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

type Position struct {
	x int
	y int
}

func getBinary(p Position, activePos map[Position]string) int {
	s := ""
	for x := p.x - 1; x < p.x+2; x++ {
		for y := p.y - 1; y < p.y+2; y++ {
			if activePos[Position{x, y}] == "#" {
				s += "1"
			} else {
				s += "0"
			}
		}
	}
	if i, err := strconv.ParseInt(s, 2, 64); err != nil {
		return -1
	} else {
		return int(i)
	}
}

func getBinaryUnknown(p Position, activePos map[Position]string) int {
	s := ""
	for x := p.x - 1; x < p.x+2; x++ {
		for y := p.y - 1; y < p.y+2; y++ {
			if activePos[Position{x, y}] != "." {
				s += "1"
			} else {
				s += "0"
			}
		}
	}
	if i, err := strconv.ParseInt(s, 2, 64); err != nil {
		return -1
	} else {
		return int(i)
	}
}

func step(activePos map[Position]string) map[Position]string {
	newPos := make(map[Position]string)
	for p := range activePos {
		for x := p.x - 1; x < p.x+2; x++ {
			for y := p.y - 1; y < p.y+2; y++ {
				newPos[Position{x, y}] = binary[getBinary(Position{x, y}, activePos)]
			}
		}
	}
	return newPos
}

func stepInfinite(activePos map[Position]string) map[Position]string {
	newPos := make(map[Position]string)
	for p := range activePos {
		for x := p.x - 1; x < p.x+2; x++ {
			for y := p.y - 1; y < p.y+2; y++ {
				newPos[Position{x, y}] = binary[getBinaryUnknown(Position{x, y}, activePos)]
			}
		}
	}
	return newPos
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	binary = strings.Split(scanner.Text(), "")
	scanner.Scan()
	activePos := make(map[Position]string)
	x := 0
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "")
		for y, char := range line {
			activePos[Position{x, y}] = char
		}
		x++
	}

	for i := 0; i < 25; i++ {
		activePos = step(activePos)
		activePos = stepInfinite(activePos)
	}
	count := 0
	for _, char := range activePos {
		if char == "#" {
			count += 1
		}
	}
	fmt.Println(count)
}
