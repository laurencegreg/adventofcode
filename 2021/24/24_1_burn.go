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

var vars map[string]int
var input []int

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}
func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

type Computable interface {
	compute() bool
}

type Inp struct {
	v     string
	index int
}

func (i Inp) compute() bool {
	vars[i.v] = input[i.index]
	return true
}

type Add struct {
	a, b string
}

func (add Add) compute() bool {
	b, err := strconv.Atoi(add.b)
	if err != nil {
		b = vars[add.b]
	}
	vars[add.a] += b
	return true
}

type Mul struct {
	a, b string
}

func (mul Mul) compute() bool {
	b, err := strconv.Atoi(mul.b)
	if err != nil {
		b = vars[mul.b]
	}
	vars[mul.a] *= b
	return true
}

type Div struct {
	a, b string
}

func (div Div) compute() bool {
	b, err := strconv.Atoi(div.b)
	if err != nil {
		b = vars[div.b]
	}
	if b != 0 {
		vars[div.a] /= b
	} else {
		return false
	}
	return true
}

type Mod struct {
	a, b string
}

func (mod Mod) compute() bool {
	b, err := strconv.Atoi(mod.b)
	if err != nil {
		b = vars[mod.b]
	}
	if b != 0 {
		vars[mod.a] %= b
	} else {
		return false
	}
	return true
}

type Eql struct {
	a, b string
}

func (eql Eql) compute() bool {
	b, err := strconv.Atoi(eql.b)
	if err != nil {
		b = vars[eql.b]
	}
	if vars[eql.a] == b {
		vars[eql.a] = 1
	} else {
		vars[eql.a] = 0
	}
	return true
}

func run(num []int, fns []Computable) bool {
	vars = make(map[string]int)
	input = num
	for _, fn := range fns {
		if !fn.compute() {
			return false
		}
	}
	return true
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	var fns []Computable
	scanner := bufio.NewScanner(file)
	it := 0
	for scanner.Scan() {
		ins := strings.Split(scanner.Text(), " ")
		switch ins[0] {
		case "inp":
			fns = append(fns, Inp{ins[1], it})
			it++
		case "add":
			fns = append(fns, Add{ins[1], ins[2]})
		case "mul":
			fns = append(fns, Mul{ins[1], ins[2]})
		case "div":
			fns = append(fns, Div{ins[1], ins[2]})
		case "mod":
			fns = append(fns, Mod{ins[1], ins[2]})
		case "eql":
			fns = append(fns, Eql{ins[1], ins[2]})
		}
	}

	//a3 + -8 = a4 |  a5 + 5 = a6 |  a9 + -2 = a10 |  a8 + -4 = a11 |  a7 + -6 = a12 |  a2 + -3 = a13 |  a1 + 3 = a14
	//num := []int{6, 9, 9,1, 4, 9, 9, 9, 9, 7, 5, 3, 6, 9}
	num := []int{1, 4, 9, 1, 1, 6, 7, 5, 3, 1, 1, 1, 1, 4}
	vars = make(map[string]int)
	vars["z"] = 1
	for vars["z"] != 0 {
		fmt.Println(num)
		if !run(num, fns) {
			vars["z"] = 1
		}
		if vars["z"] != 0 {
			minus := true
			i := 13
			for minus {
				if num[i] > 1 {
					num[i]--
					minus = false
				} else {
					num[i] = 9
					i--
				}
			}
		}
	}
	fmt.Println(num)
}
