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

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	//init table
	var tab [][]int
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

	i := 0
	j := 2
	for i < len(tab) {
		x := i
		y := j
		for y >= 0 && x < len(tab) {
			if x == 0 {
				tab[x][y] += tab[x][y-1]
			} else if y == 0 {
				tab[x][y] += tab[x-1][y]
			} else if tab[x][y-1] < tab[x-1][y] {
				tab[x][y] += tab[x][y-1]
			} else {
				tab[x][y] += tab[x-1][y]
			}
			y -= 1
			x += 1
		}

		if j == len(tab[0])-1 {
			i++
		} else {
			j++
		}

	}
	fmt.Println(tab[i-1][j])
}
