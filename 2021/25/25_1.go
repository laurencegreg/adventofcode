package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	var lines [][]string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, strings.Split(scanner.Text(), ""))
	}
	//for _, line := range lines {
	//	fmt.Println(line)
	//}
	//fmt.Println("-------------")
	count := 0
	moved := true
	for moved {
		count += 1
		moved = false
		for _, line := range lines {
			occupied := (line[0] != ".")
			for i, c := range line {
				if c == ">" {
					if i+1 < len(line) {
						if line[i+1] == "." {
							line[i] = "."
							line[i+1] = "o"
							moved = true
						}
					} else {
						if !occupied {
							line[i] = "."
							line[0] = ">"
						}
					}

				} else if c == "o" {
					line[i] = ">"
				}
			}
		}

		var occupiedLine []bool
		for _, c := range lines[0] {
			occupiedLine = append(occupiedLine, c != ".")
		}

		for j, line := range lines {
			for i, c := range line {
				if c == "v" {
					if j+1 < len(lines) {
						if lines[j+1][i] == "." {
							lines[j][i] = "."
							lines[j+1][i] = "o"
							moved = true
						}
					} else {
						if !occupiedLine[i] {
							lines[j][i] = "."
							lines[0][i] = "v"
						}
					}
				} else if c == "o" {
					line[i] = "v"
				}
			}
		}
		//for _, line := range lines {
		//	fmt.Println(line)
		//}
		//fmt.Println("-------------")
	}
	fmt.Println(count)
}
