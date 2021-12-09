package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"time"
)

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}
func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	target := 368078
	racine := int(math.Floor(math.Sqrt(float64(target))))
	if racine%2 != 1 {
		racine--
	}
	fmt.Println(racine)
	limit := (racine - 1) / 2
	x := (racine - 1) / 2
	y := x
	var dx int
	var dy int
	it := racine * racine
	for it < target {
		if x == limit && y == limit {
			x += 1
			limit += 1
			dx = 0
			dy = -1
		} else {
			if dx != 0 && x == dx*limit {
				dy = -1 * dx
				dx = 0
			} else if dy != 0 && y == dy*limit {
				dx = dy
				dy = 0
			}
			x += dx
			y += dy
		}
		it++
		fmt.Println(it, " : ", x, ",", y)
	}
}
