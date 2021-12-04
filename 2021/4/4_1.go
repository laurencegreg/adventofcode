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

type box struct {
	value string
	found int
}

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

func callNumber(bingoGrids [][][]box, number string) {
	for _, bingoGrid := range bingoGrids {
		for _, line := range bingoGrid {
			for i, b := range line {
				if b.value == number {
					b.found = 1
					line[i] = b
				}
			}
		}
	}
}

func calcBingo(bingoGrids [][][]box, number string) int {
	for _, bingoGrid := range bingoGrids {
		for i := range bingoGrid {
			if sumLine(bingoGrid, i) == len(bingoGrid[i]) {
				fmt.Println("!!! BINGO !!!")
				fmt.Println()
				for _, line := range bingoGrid {
					fmt.Println(line)
				}
				fmt.Println()
				fmt.Println("!!!!!!!!!!!!!")
				return resultBingo(bingoGrid, number)
			}
		}
		for j := range bingoGrid[0] {
			if sumColumn(bingoGrid, j) == len(bingoGrid) {
				fmt.Println("!!! BINGO !!!")
				fmt.Println()
				for _, line := range bingoGrid {
					fmt.Println(line)
				}
				fmt.Println()
				fmt.Println("!!!!!!!!!!!!!")
				return resultBingo(bingoGrid, number)
			}
		}
	}
	return 0
}

func sumLine(bingoGrid [][]box, index int) int {
	count := 0
	for _, b := range bingoGrid[index] {
		count += b.found
	}
	return count
}

func sumColumn(bingoGrid [][]box, index int) int {
	count := 0
	for i := range bingoGrid {
		count += bingoGrid[i][index].found
	}
	return count
}

func resultBingo(bingoGrid [][]box, number string) int {
	counter := 0
	num, _ := strconv.Atoi(number)
	for _, line := range bingoGrid {
		for _, b := range line {
			if b.found == 0 {
				i, _ := strconv.Atoi(b.value)
				counter += i
			}
		}
	}
	return counter * num
}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var bingoGrids [][][]box
	var bingoGrid [][]box
	scanner.Scan()
	values := strings.Split(scanner.Text(), ",")
	scanner.Scan()
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			bingoGrids = append(bingoGrids, bingoGrid)
			bingoGrid = nil
		} else {
			var bingoLine []box
			for _, str := range strings.Split(line, " ") {
				if str != "" {
					bingoLine = append(bingoLine, box{str, 0})
				}
			}
			bingoGrid = append(bingoGrid, bingoLine)
		}
	}
	bingoGrids = append(bingoGrids, bingoGrid)

	res := 0
	it := 0
	for res == 0 {
		fmt.Println("call for ", values[it])
		callNumber(bingoGrids, values[it])
		res = calcBingo(bingoGrids, values[it])
		it++
		for _, bg := range bingoGrids {
			for _, line := range bg {
				fmt.Println(line)
			}
			fmt.Println()
		}
	}
	fmt.Println(res)
}
