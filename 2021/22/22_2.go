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

var activePos []Active

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}
func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

type Active struct {
	x1 int
	x2 int
	y1 int
	y2 int
	z1 int
	z2 int
}

func abs(i int) int {
	if i < 0 {
		return -i
	} else {
		return i
	}
}
func size(a Active) int {
	return abs(a.x1-a.x2) * abs(a.y1-a.y2) * abs(a.z1-a.z2)
}

func activate(x1 int, x2 int, y1 int, y2 int, z1 int, z2 int) {
}

func deactivate(x1 int, x2 int, y1 int, y2 int, z1 int, z2 int) {
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	onPos = make(map[Position]bool)
	scanner := bufio.NewScanner(file)
	r, _ := regexp.Compile(`(on|off) x=(-?\d*)\.\.(-?\d*),y=(-?\d*)\.\.(-?\d*),z=(-?\d*)\.\.(-?\d*)`)
	for scanner.Scan() {
		target := r.FindStringSubmatch(scanner.Text())
		op := target[1] == "on"
		x1 := toInt(target[2])
		x2 := toInt(target[3])
		y1 := toInt(target[4])
		y2 := toInt(target[5])
		z1 := toInt(target[6])
		z2 := toInt(target[7])
		if op {
			activate(x1, x2, y1, y2, z1, z2)
		} else {
			deactivate(x1, x2, y1, y2, z1, z2)
		}

	}
}
