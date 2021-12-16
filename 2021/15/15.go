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

var dumbLimit int
var shortestPaths map[[2]int]Best
var tab [][]int
var minPos map[[2]int]int

type Best struct {
	pos    [2]int
	length int
	path   [][2]int
	ok     bool
}

func New(x int, y int, ok bool) Best {
	return Best{[2]int{x, y}, 0, [][2]int{}, ok}
}

func in(pos [2]int, path [][2]int) bool {
	for _, p := range path {
		if p == pos {
			return true
		}
	}
	return false
}

func keys(shortest map[[2]int]Best) [][2]int {
	var res [][2]int
	for key, _ := range shortest {
		res = append(res, key)
	}
	return res
}

func manatthan(pos [2]int) int {
	return len(tab) - 1 - pos[0] + len(tab[0]) - 1 - pos[1]
}

func move(b Best, target [2]int, max int) (Best, bool) {
	var possible []Best
	x := b.pos[0]
	y := b.pos[1]
	dir := [][2]int{{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}}

	for _, d := range dir {
		//fmt.Println("start with ", b, " go for dir ", d)
		if d[0] >= 0 && d[0] < len(tab) && d[1] >= 0 && d[1] < len(tab[d[0]]) && !in(d, keys(shortestPaths)) {
			bD, keep := b.add(d, tab[d[0]][d[1]])
			if minPos[d] == 0 {
				minPos[d] = bD.length
			}
			if keep && !(bD.length > max) && (bD.length+manatthan(bD.pos)) < dumbLimit && !(minPos[d] < bD.length) {
				if minPos[d] > bD.length {
					minPos[d] = bD.length
				}
				if target == d {

					//fmt.Println("finish ", bD)
					possible = append(possible, bD)
				} else {
					bPoss, keep := move(bD, target, max)
					if keep {
						possible = append(possible, bPoss)
					}
				}
			}

		}
	}
	if len(possible) == 0 {
		return b, false
	} else {
		bBest := possible[0]
		for _, bVar := range possible[1:] {
			if bBest.length > bVar.length {
				bBest = bVar
			}
		}
		return bBest, true
	}
}

func (b Best) add(pos [2]int, value int) (Best, bool) {
	if !in(pos, b.path) {
		b.path = append(b.path, pos)
		b.length += value
		b.pos = pos
		return b, true
	} else {
		return b, false
	}
}

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
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
	//init table
	for scanner.Scan() {
		s := scanner.Text()
		if len(s) != 0 {
			var line []int
			for _, c := range strings.Split(s, "") {
				line = append(line, toInt(c))
			}
			tab = append(tab, line)
		}
	}
	for _, line := range tab {
		fmt.Println(line)
	}
	//one path to the end = max limit
	//for each position, if minimal path to this position + manathan distance (end path with only 1) > max limit -> useless
	dumbLimit = 0
	x := 1
	y := 1
	for x < len(tab) {
		dumbLimit += tab[x][0]
		x++
	}
	x--
	for y < len(tab[x]) {
		dumbLimit += tab[x][y]
		y++
	}

	fmt.Println("max limit : ", dumbLimit)

	//init shortests paths
	shortestPaths = make(map[[2]int]Best)
	minPos = make(map[[2]int]int)
	minPos[[2]int{0, 0}] = 1
	minPos[[2]int{0, 1}] = tab[0][1]
	b := New(0, 1, true)
	b, _ = b.add([2]int{0, 1}, tab[0][1])

	shortestPaths[[2]int{0, 1}] = b

	minPos[[2]int{1, 0}] = tab[1][0]
	b = New(1, 0, true)
	b, _ = b.add([2]int{1, 0}, tab[1][0])
	shortestPaths[[2]int{1, 0}] = b

	prevDiags := [][2]int{{0, 1}, {1, 0}}
	var newDiags [][2]int
	i := 0
	j := 2
	for i < len(tab) {
		diagPoint := [2]int{i, j}
		newDiags = [][2]int{}
		for diagPoint[1] >= 0 && diagPoint[0] < len(tab) {
			var finalB Best
			valuated := false
			fmt.Println("compute position ", diagPoint)
			newDiags = append(newDiags, diagPoint)
			for _, oldD := range prevDiags {
				bOld := shortestPaths[oldD]
				if bOld.ok {
					var limit int
					if valuated {
						limit = finalB.length
					} else {
						limit = bOld.length + tab[diagPoint[0]][diagPoint[1]]
					}
					//fmt.Println("for ", bOld.pos, " and limit ", limit)
					bBest, keep := move(bOld, diagPoint, limit)
					if keep {
						if !valuated || finalB.length > bBest.length {
							valuated = true
							finalB = bBest
						}
					}
				}
			}
			if !valuated {
				shortestPaths[diagPoint] = New(diagPoint[0], diagPoint[1], false)
			} else {
				shortestPaths[diagPoint] = finalB
			}

			diagPoint = [2]int{diagPoint[0] + 1, diagPoint[1] - 1}
		}
		if j == len(tab[0])-1 {
			i++
		} else {
			j++
		}
		prevDiags = newDiags
	}
	fmt.Println(shortestPaths[newDiags[0]])
}
