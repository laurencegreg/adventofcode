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

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

func step(table [][][]int) int {
	res := 0
	for i := range table {
		for j := range table[i] {
			table[i][j][0]++
		}
	}

	for i := range table {
		for j := range table[i] {
			if table[i][j][0] > 9 {
				res += flash(table, i, j)
			}
		}
	}

	for i := range table {
		for j := range table[i] {
			if table[i][j][0] > 9 {
				table[i][j][0] = 0
				table[i][j][1] = 0
			}
		}
	}

	return res
}

func printTable(table [][][]int) {
	for _, line := range table {
		for _, n := range line {
			//if n[0] < 10 {
			//	fmt.Print(0)
			//}
			fmt.Print(n[0], " ")
		}
		fmt.Println()
	}
}

func flash(table [][][]int, i int, j int) int {
	if table[i][j][1] == 0 {
		table[i][j][1] = 1
		res := 1
		for x := i - 1; x < i+2; x++ {
			if x >= 0 && x < len(table) {
				for y := j - 1; y < j+2; y++ {
					if y >= 0 && y < len(table) {
						table[x][y][0]++
						if table[x][y][0] > 9 {
							res += flash(table, x, y)
						}
					}
				}
			}
		}
		return res
	} else {
		return 0
	}
}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var table [][][]int
	for scanner.Scan() {
		var line [][]int
		for _, i := range strings.Split(scanner.Text(), "") {
			if len(i) == 1 {
				line = append(line, []int{toInt(i), 0})
			}
		}
		table = append(table, line)
	}
	res := 0
	for i := 0; i < 100; i++ {
		res += step(table)
		printTable(table)
	}
	fmt.Println(res)
}
