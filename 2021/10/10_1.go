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

func open(c string) bool {
	for _, char := range []string{"(", "[", "{", "<"} {
		if c == char {
			return true
		}
	}
	return false
}

func close(c string) bool {
	return !open(c)
}

func score(c string, dict map[string]int) int {

	return dict[c]
}

func validator(s string) (string, bool) {
	var pile []string
	corresp := map[string]string{
		")": "(",
		"]": "[",
		"}": "{",
		">": "<"}
	for _, c := range strings.Split(s, "") {
		if len(c) > 0 {
			if open(c) {
				pile = append(pile, c)
			} else {
				if corresp[c] != pile[len(pile)-1] {
					return c, true
				} else {
					pile = pile[:len(pile)-1]
				}
			}

		}
	}
	return "", false
}

func main() {
	dict := map[string]int{
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137}
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	res := 0
	for scanner.Scan() {
		c, err := validator(scanner.Text())
		if err {
			res += score(c, dict)
		}

	}
	fmt.Println(res)
}
