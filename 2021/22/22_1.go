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

var onPos map[Position]bool

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
	z int
}

func step(x1 int, x2 int, y1 int, y2 int, z1 int, z2 int, op bool) {
	for x := x1; x <= x2; x++ {
		for y := y1; y <= y2; y++ {
			for z := z1; z <= z2; z++ {
				onPos[Position{x, y, z}] = op
			}
		}
	}
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	min := -50
	max := 50
	onPos = make(map[Position]bool)
	scanner := bufio.NewScanner(file)
	r, _ := regexp.Compile(`(on|off) x=(-?\d*)\.\.(-?\d*),y=(-?\d*)\.\.(-?\d*),z=(-?\d*)\.\.(-?\d*)`)
	for scanner.Scan() {
		target := r.FindStringSubmatch(scanner.Text())
		op := target[1] == "on"
		x1 := toInt(target[2])
		x2 := toInt(target[3])
		if x1 < min {
			if x2 > min {
				x1 = min
			} else {
				break
			}
		}
		if x2 > max {
			if x1 < max {
				x2 = max
			} else {
				break
			}
		}
		y1 := toInt(target[4])
		y2 := toInt(target[5])
		if y1 < min {
			if y2 > min {
				y1 = min
			} else {
				break
			}
		}
		if y2 > max {
			if y1 < max {
				y2 = max
			} else {
				break
			}
		}
		z1 := toInt(target[6])
		z2 := toInt(target[7])
		if z1 < min {
			if z2 > min {
				z1 = min
			} else {
				break
			}
		}
		if z2 > max {
			if z1 < max {
				z2 = max
			} else {
				break
			}
		}
		step(x1, x2, y1, y2, z1, z2, op)

	}
	count := 0
	for _, b := range onPos {
		if b {
			count++
		}
	}
	fmt.Println(count)
}
