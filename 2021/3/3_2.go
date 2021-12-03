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

func countOccurences(table [][]string, index int) map[string]int {
	dict := make(map[string]int)
	for _, str := range table {
		dict[str[index]] = dict[str[index]] + 1
	}
	return dict
}

func oxygen(table [][]string) int64 {
	filtered := table
	index := 0
	for len(filtered) != 1 {
		counter := countOccurences(filtered, index)
		if counter["1"] >= counter["0"] {
			filtered = filter(filtered, "1", index)
		} else {
			filtered = filter(filtered, "0", index)
		}
		index++
	}
	output, _ := strconv.ParseInt(strings.Join(filtered[0], ""), 2, 64)
	return output
}

func co2(table [][]string) int64 {
	filtered := table
	index := 0
	for len(filtered) != 1 {
		counter := countOccurences(filtered, index)
		if counter["0"] <= counter["1"] {
			filtered = filter(filtered, "0", index)
		} else {
			filtered = filter(filtered, "1", index)
		}
		index++
	}
	output, _ := strconv.ParseInt(strings.Join(filtered[0], ""), 2, 64)
	return output
}
func filter(table [][]string, value string, index int) [][]string {
	var result [][]string
	for _, line := range table {
		if line[index] == value {
			result = append(result, line)
		}
	}
	return result
}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var splittedLines [][]string
	for scanner.Scan() {
		splittedLines = append(splittedLines, strings.Split(scanner.Text(), ""))

	}
	fmt.Println(co2(splittedLines) * oxygen(splittedLines))

}
