package main

import (
	"fmt"
	"log"
	"os"
	"time"
)

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

type pos struct {
	x int
	y int
}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	target := 368078
	limit := 0
	x := 0
	y := 0

	var dx int
	var dy int
	it := 1
	dic := make(map[pos]int)
	dic[pos{x, y}] = 1
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
		add := 0
		fmt.Println("****************************")
		for i := x - 1; i <= x+1; i++ {
			for j := y - 1; j <= y+1; j++ {
				add += dic[pos{i, j}]
				fmt.Println("ij", i, " ", j, " : ", dic[pos{i, j}])
			}

		}
		dic[pos{x, y}] = add
		it = add
		fmt.Println(x, ",", y, " : ", add)

	}
	fmt.Println(dic)
}
