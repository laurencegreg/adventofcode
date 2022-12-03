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

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}
func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

type Scanner struct {
	name       string
	beacons    [][3]int
	dictDist   map[int][]int
	dicDicDist map[int]map[int][]int
}

func abs(i int) int {
	if i < 0 {
		return -i
	} else {
		return i
	}
}
func distance(a [3]int, b [3]int) int {
	return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])
}

func (s Scanner) print() {
	fmt.Println("name : ", s.name)
	fmt.Println("  beacons : ")
	for i, b := range s.beacons {
		fmt.Println("  ", i, " : ", b)
	}

	fmt.Println("  distances : ")
	for k, v := range s.dictDist {
		fmt.Println("  ", k, s.beacons[k], " : ", v)
	}
}

func corresp(d1 []int, d2 []int) []int {
	var res []int
	j := 0
	for _, i := range d1 {
		f := 0
		for f < i && j < len(d2) {
			f = d2[j]
			j++
		}
		if i == f {
			res = append(res, f)
		}
	}
	return res
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input.test")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var beacons [][3]int
	name := ""
	var scanners []Scanner
	for scanner.Scan() {
		s := scanner.Text()
		if name == "" {
			name = strings.Split(s, " ")[2]
			beacons = [][3]int{}
		} else if len(s) != 0 {
			num := strings.Split(s, ",")
			pos := [3]int{toInt(num[0]), toInt(num[1]), toInt(num[2])}
			beacons = append(beacons, pos)
		} else {
			dicDicDist := make(map[int]map[int][]int)
			dictDist := make(map[int][]int)
			for i := range beacons {
				var dists []int
				for j := (i + 1) % len(beacons); j != i; j = (j + 1) % len(beacons) {
					dist := distance(beacons[i], beacons[j])

					dists = append(dists, dist)
					if len(dicDicDist[i]) == 0 {
						dicDicDist[i] = make(map[int][]int)
					}
					dicDicDist[i][j] = append(dicDicDist[i][j], dist)
				}
				sort.Ints(dists)
				dictDist[i] = dists

			}
			scanners = append(scanners, Scanner{name, beacons, dictDist, dicDicDist})
			name = ""
		}
	}
	s0 := scanners[1]
	s1 := scanners[4]

	for i, d := range s0.dictDist {
		cor := 0
		corLen := 0
		for j, d2 := range s1.dictDist {
			tmp := corresp(d, d2)
			if corLen < len(tmp) {
				cor = j
				corLen = len(tmp)
			}
		}
		if corLen > 2 {
			fmt.Println("best correspondance of ", i, " : ", cor, "(", corLen, ")")

			fmt.Println(s0.beacons[i][2] + s1.beacons[cor][0])
			fmt.Println(s0.beacons[i][1] + s1.beacons[cor][2])
			fmt.Println(s0.beacons[i][0] - s1.beacons[cor][1])
		}
	}
}
