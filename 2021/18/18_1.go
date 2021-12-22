package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}
func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

type Snailfish struct {
	value    int
	isPair   bool
	maxDepth int
	maxValue int
	pair     []Snailfish
}

func (s Snailfish) toString() string {
	if s.isPair {
		return "[" + s.pair[0].toString() + "," + s.pair[1].toString() + "]"
	} else {
		return strconv.Itoa(s.value)
	}
}

func (s Snailfish) print() {
	fmt.Println("max Depth : ", s.maxDepth)
	fmt.Println("max Value : ", s.maxValue)
	fmt.Println("snail fish : ", s.toString())
}

func max(i int, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}

func newValue(val int) Snailfish {
	return Snailfish{val, false, 0, val, []Snailfish{}}
}

func newSnail(s Snailfish, s2 Snailfish) Snailfish {
	return Snailfish{0, true, max(s.maxDepth, s2.maxDepth) + 1, max(s.maxValue, s2.maxValue), []Snailfish{s, s2}}
}

func (s Snailfish) add(s2 Snailfish) Snailfish {
	snail := Snailfish{0, true, max(s.maxDepth, s2.maxDepth) + 1, max(s.maxValue, s2.maxValue), []Snailfish{s, s2}}
	for snail.maxDepth > 4 || snail.maxValue > 9 {
		snail.print()
		if snail.maxDepth > 4 {
			snail, _, _ = snail.explodes(5)
		} else {
			snail = snail.split()
		}
	}
	return snail
}

func (s Snailfish) split() Snailfish {
	if !s.isPair {
		val := s.value
		return newSnail(newValue(val/2), newValue(val/2+val%2))
	} else {
		if s.pair[0].maxValue > 9 {
			s.pair[0] = s.pair[0].split()
		} else {
			s.pair[1] = s.pair[1].split()
		}
		s.maxValue = max(s.pair[0].maxValue, s.pair[1].maxValue)
		s.maxDepth = max(s.pair[0].maxDepth, s.pair[1].maxDepth) + 1
		return s
	}
}

func (s Snailfish) addLeft(i int) Snailfish {
	if !s.isPair {
		s.value = s.value + i
		s.maxValue = s.value
		return s
	} else {
		s.pair[0] = s.pair[0].addLeft(i)
		s.maxValue = max(s.pair[0].maxValue, s.pair[1].maxValue)
		return s
	}
}

func (s Snailfish) addRight(i int) Snailfish {
	if !s.isPair {
		s.value = s.value + i
		s.maxValue = s.value
		return s
	} else {
		s.pair[1] = s.pair[1].addRight(i)
		s.maxValue = max(s.pair[1].maxValue, s.pair[0].maxValue)
		return s
	}
}
func (s Snailfish) explodes(i int) (Snailfish, int, int) {
	if i <= 1 && s.maxDepth == 1 {
		return newValue(0), s.pair[0].value, s.pair[1].value
	} else {
		upleft := -1
		upright := -1
		if s.pair[0].maxDepth >= i-1 && s.pair[0].maxDepth != 0 {
			snail, left, right := s.pair[0].explodes(i - 1)
			upleft = left
			s.pair[0] = snail
			if right >= 1 {
				s.pair[1] = s.pair[1].addLeft(right)
			}

		} else {
			snail, left, right := s.pair[1].explodes(i - 1)
			upright = right
			s.pair[1] = snail
			if left >= 1 {
				s.pair[0] = s.pair[0].addRight(left)
			}
		}
		s.maxDepth = max(s.pair[0].maxDepth, s.pair[1].maxDepth) + 1
		s.maxValue = max(s.pair[0].maxValue, s.pair[1].maxValue)
		return s, upleft, upright
	}
}

func toSnail(str string) Snailfish {
	if str[0] == '[' {
		clean := str[1:(len(str) - 1)]
		left, right := splitString(clean)
		return newSnail(toSnail(left), toSnail(right))
	} else {
		return newValue(toInt(str))
	}
}

func splitString(str string) (string, string) {
	pos := 0
	if str[pos] == '[' {
		count := 1
		pos += 1
		for count > 0 {
			if str[pos] == '[' {
				count += 1
			} else if str[pos] == ']' {
				count -= 1
			}
			pos += 1
		}

	} else {
		pos += 1
		for str[pos] != ',' {
			pos += 1
		}
	}
	return str[0:pos], str[pos+1:]
}

func magnitude(s Snailfish, mult int) int {
	if !s.isPair {
		return s.value * mult
	} else {
		return mult * (magnitude(s.pair[0], 3) + magnitude(s.pair[1], 2))
	}
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var snail Snailfish
	scanner.Scan()
	snail = toSnail(scanner.Text())

	for scanner.Scan() {
		snail = snail.add(toSnail(scanner.Text()))
		snail.print()
	}
	fmt.Println(magnitude(snail, 1))
}
