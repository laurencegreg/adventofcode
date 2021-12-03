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

func gamma(diffBinary [12]int) int64 {
	result := ""
	for _, element := range diffBinary {
		if element > 0 {
			result += "1"
		} else {
			result += "0"
		}
	}
	output, _ := strconv.ParseInt(result, 2, 64)
	return output

}

func epsilon(diffBinary [12]int) int64 {
	result := ""
	for _, element := range diffBinary {
		if element > 0 {
			result += "0"
		} else {
			result += "1"
		}
	}
	output, _ := strconv.ParseInt(result, 2, 64)
	return output

}

func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var diffBinary [12]int
	var splitted []string
	for scanner.Scan() {
		splitted = strings.Split(scanner.Text(), "")
		for index, element := range splitted {
			i, err := strconv.Atoi(element)
			if err != nil {
				log.Fatal(err)
			}
			i = -1 + 2*i
			diffBinary[index] += i
		}
	}

	fmt.Println(gamma(diffBinary) * epsilon(diffBinary))

}
