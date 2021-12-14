package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"sort"
	"time"
)

var polys map[string]Polymere

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Println("It took", elapsed)
}

type Polymere struct {
	name  string
	added string
	life  map[int]map[rune]int
}

func New(name string, added string) Polymere {
	life := make(map[int]map[rune]int)
	life[1] = make(map[rune]int)
	for _, c := range name + added {
		life[1][c]++
	}
	polymere := Polymere{name, added, life}
	return polymere
}

func (p Polymere) step(i int) map[rune]int {
	if dic, ok := p.life[i]; ok {
		//fmt.Println(p.name, " step ", i)
		//printDic(dic)
		return dic
	} else {
		//fmt.Println("add ", string(p.name[0])+p.added, " and ", p.added+string(p.name[1]), " at step ", i-1)
		fst := polys[string(p.name[0])+p.added].step(i - 1)
		scd := polys[p.added+string(p.name[1])].step(i - 1)
		newDic := make(map[rune]int)
		for key, value := range fst {
			newDic[key] = value
		}
		for key, value := range scd {
			newDic[key] += value
		}
		c := []rune(p.added)
		newDic[c[0]]--
		p.life[i] = newDic
		//fmt.Println("newDic")
		//printDic(newDic)
		return newDic
	}
}

func printDic(dic map[rune]int) {
	for key, value := range dic {
		fmt.Println(string(key), " : ", value)
	}
}

func compute(target string, nbStep int) int {
	fmt.Println("compute final polymere distribution for ", target, " after ", nbStep, " steps")
	finalDic := make(map[rune]int)
	for i := 0; i < len(target)-1; i++ {
		for key, value := range polys[target[i:i+2]].step(nbStep) {
			finalDic[key] += value
		}
	}
	for _, c := range target[1 : len(target)-1] {
		finalDic[c]--
	}
	printDic(finalDic)
	var counter []int
	for _, value := range finalDic {
		counter = append(counter, value)
	}
	sort.Ints(counter)
	return counter[len(counter)-1] - counter[0]
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	r, _ := regexp.Compile("([A-Z][A-Z]) -> ([A-Z])")
	polys = make(map[string]Polymere)
	target := ""
	for scanner.Scan() {
		s := scanner.Text()
		match := r.FindStringSubmatch(s)
		if s != "" {
			if len(match) != 0 {
				polys[match[1]] = New(match[1], match[2])
			} else {
				target = s
			}
		}
	}

	fmt.Println("Part 1")
	fmt.Println("result : ", compute(target, 10), "\n")
	fmt.Println("Part 2")
	fmt.Println("result : ", compute(target, 40))

}
