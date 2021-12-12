package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"time"
	"unicode"
)

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}
func in(char string, path []string) bool {
	for _, c := range path {
		if c == char {
			return true
		}
	}
	return false
}

func run(path []string, dict map[string][]string) [][]string {
	var res [][]string
	for _, c := range dict[path[len(path)-1]] {
		newPath := path
		uni := []rune(c)
		if c == "end" {
			newPath = append(newPath, c)
			res = append(res, newPath)
		} else if !unicode.IsUpper(uni[0]) {
			if !in(c, newPath) {
				newPath = append(newPath, c)
				res = append(res, run(newPath, dict)...)
			}
		} else {
			newPath = append(newPath, c)
			res = append(res, run(newPath, dict)...)
		}
	}
	return res
}
func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	dict := make(map[string][]string)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "-")
		dict[line[0]] = append(dict[line[0]], line[1])
		dict[line[1]] = append(dict[line[1]], line[0])
	}
	var final [][]string
	for _, s := range dict["start"] {
		final = append(final, run([]string{"start", s}, dict)...)
	}
	for _, s := range final {
		fmt.Println(s)
	}
	fmt.Println(len(final))
}
