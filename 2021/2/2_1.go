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
func main() {
	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	x, y := 0, 0

	direction := ""
	for scanner.Scan() {
		direction = scanner.Text()
		s := strings.Split(direction, " ")
		i, err := strconv.Atoi(s[1])
		if err != nil {
			log.Fatal(err)
		}
		switch dir := s[0]; dir {
		case "forward":
			x += i
		case "down":
			y += i
		case "up":
			y -= i
		default:
			log.Fatal(err)
		}

	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(x * y)
}
