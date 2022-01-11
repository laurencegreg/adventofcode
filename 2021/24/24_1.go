package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

func show(lines []string, mod26 [][2]int, choices []string, it int, x [2]int, y [2]int) {
	//fmt.Println(mod26, choices, it, x, y)
	if len(lines) == 0 {
		if len(mod26) == 1 {
			fmt.Println(choices)
		}
	} else {
		//fmt.Println(lines[0])
		line := strings.Split(lines[0], " ")
		switch line[0] {
		case "inp":
			it++
			show(lines[1:], mod26, choices, it, x, y)
		case "mul":
			if line[1] == "x" {
				//mul x 0
				show(lines[1:], mod26, choices, it, [2]int{0, 0}, y)
			} else if line[1] == "y" {
				if line[2] == "x" {
					if x[1] == 0 {
						show(lines[1:], mod26, choices, it, x, [2]int{0, 0})
					} else {
						show(lines[1:], mod26, choices, it, x, y)
					}
				} else {
					//mul y 0
					show(lines[1:], mod26, choices, it, x, [2]int{0, 0})
				}
			} else {
				//mul z y
				if y[1] == 1 {
					show(lines[1:], mod26, choices, it, x, y)
				} else {
					//y = 26
					new26 := append([][2]int{[2]int{0, 0}}, mod26...)
					show(lines[1:], new26, choices, it, x, y)
				}
			}
		case "add":
			if line[1] == "x" {
				if line[2] == "z" {
					//add x z
					show(lines[1:], mod26, choices, it, mod26[0], y)
				} else {
					//add x int
					x[1] += toInt(line[2])
					show(lines[1:], mod26, choices, it, x, y)
				}
			} else if line[1] == "y" {
				if line[2] != "w" {
					//add y int
					y[1] += toInt(line[2])
					show(lines[1:], mod26, choices, it, x, y)
				} else {
					//add y w
					show(lines[1:], mod26, choices, it, x, [2]int{it, 0})
				}
			} else {
				//add z y
				if y[0] == 0 && y[1] == 0 {
					show(lines[1:], mod26, choices, it, x, y)
				} else {
					new26 := append([][2]int{y}, mod26[1:]...)
					show(lines[1:], new26, choices, it, x, y)
				}
			}
		case "eql":
			if line[2] == "w" {
				//eql x w
				if x[1] < -8 || x[1] > 8 {
					show(lines[1:], mod26, choices, it, [2]int{0, 0}, y)
				} else {
					//	if (x[0] == 3 && x[1] == -8 && it == 4) || (x[0] == 5 && x[1] == 5 && it == 6) || (x[0] == 10 && x[1] == 8 && it == 11) || (x[0] == 13 && x[1] == 2 && it == 14) {
					ok := append(choices, "a"+strconv.Itoa(x[0])+" + "+strconv.Itoa(x[1])+" = a"+strconv.Itoa(it)+" | ")
					show(lines[1:], mod26, ok, it, [2]int{0, 1}, y)
					//	} else {
					ko := append(choices, "a"+strconv.Itoa(x[0])+" + "+strconv.Itoa(x[1])+" != a"+strconv.Itoa(it)+" | ")
					show(lines[1:], mod26, ko, it, [2]int{0, 0}, y)
					//	}
				}
			} else {
				//eql x 0
				x[1] = (x[1] + 1) % 2
				show(lines[1:], mod26, choices, it, x, y)

			}
		case "div":
			if line[2] == "26" {
				//div z 26
				show(lines[1:], mod26[1:], choices, it, x, y)
			} else {
				//div z 1
				show(lines[1:], mod26, choices, it, x, y)
			}
		default:
			show(lines[1:], mod26, choices, it, x, y)
		}
	}
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	show(lines, [][2]int{[2]int{0, 0}}, []string{"choices | "}, 0, [2]int{0, 0}, [2]int{0, 0})

}
