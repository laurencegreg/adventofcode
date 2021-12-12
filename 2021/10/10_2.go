package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
	"time"
)

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

func open(c string) bool {
	for _, char := range []string{"(", "[", "{", "<"} {
		if c == char {
			return true
		}
	}
	return false
}

func validatorP(s string) (bool, []string) {
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
					return true, pile
				} else {
					pile = pile[:len(pile)-1]
				}
			}

		}
	}
	return false, pile
}

func completion(pile []string) int {
	res := 0
	values := map[string]int{
		"(": 1,
		"[": 2,
		"{": 3,
		"<": 4}
	for i := len(pile) - 1; i >= 0; i-- {
		res = res*5 + values[pile[i]]
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
	var res []int
	for scanner.Scan() {
		err, p := validatorP(scanner.Text())
		if !err {
			res = append(res, completion(p))
		}

	}
	sort.Ints(res)
	fmt.Println(res[(len(res)-1)/2])
}
