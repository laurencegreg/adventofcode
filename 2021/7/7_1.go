package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
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
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func moveCrabs(nums []int, target int) int {
	result := 0
	for _, i := range nums {
		result += abs(i - target)
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
	var nums []int
	for scanner.Scan() {
		for _, s := range strings.Split(scanner.Text(), ",") {
			nums = append(nums, toInt(s))
			sort.Ints(nums)
		}
	}
	bestRes := moveCrabs(nums, nums[0])
	currRes := bestRes
	for i := nums[0] + 1; bestRes >= currRes; i++ {
		bestRes = currRes
		currRes = moveCrabs(nums, i)
	}
	fmt.Println(bestRes)
}
