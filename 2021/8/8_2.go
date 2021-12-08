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

func contains(s []string, searchterm string) bool {
	sort.Strings(s)
	i := sort.SearchStrings(s, searchterm)
	return i < len(s) && s[i] == searchterm
}

func inFirstNotInSecond(first []string, second []string) []string {
	var res []string
	for _, s := range first {
		if !contains(second, s) {
			res = append(res, s)
		}
	}
	return res
}

func traduc(dict map[string]string, s string) string {
	res := ""
	var tab []string
	for _, c := range strings.Split(s, "") {
		tab = append(tab, dict[c])
	}
	sort.Strings(tab)
	for _, c := range tab {
		res += c
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
	var res int
	dicoDigits := make(map[string]int)
	dicoDigits["abcefg"] = 0
	dicoDigits["cf"] = 1
	dicoDigits["acdeg"] = 2
	dicoDigits["acdfg"] = 3
	dicoDigits["bcdf"] = 4
	dicoDigits["abdfg"] = 5
	dicoDigits["abdefg"] = 6
	dicoDigits["acf"] = 7
	dicoDigits["abcdefg"] = 8
	dicoDigits["abcdfg"] = 9

	for scanner.Scan() {
		var digits [][]string
		dict := make(map[string]string)
		revDict := make(map[string]string)
		for _, s := range strings.Split((strings.Split(scanner.Text(), "|")[0]), " ") {
			if len(s) > 0 {
				chars := strings.Split(s, "")
				sort.Strings(chars)
				digits = append(digits, chars)
			}
		}
		sort.SliceStable(digits, func(i, j int) bool { return len(digits[i]) < len(digits[j]) })
		fmt.Println(digits)
		cf := digits[0]
		fmt.Println("cf : ", cf)
		acf := digits[1]
		fmt.Println("acf : ", acf)
		//search a
		a := inFirstNotInSecond(acf, cf)[0]
		fmt.Println("a : ", a)
		dict[a] = "a"
		revDict["a"] = a

		//search c
		abcdefg := digits[9]
		fmt.Println("abcdefg : ", abcdefg)

		if contains(cf, inFirstNotInSecond(abcdefg, digits[6])[0]) {
			fmt.Println("abdefg : ", digits[6])
			c := inFirstNotInSecond(abcdefg, digits[6])[0]
			fmt.Println("c : ", c)
			dict[c] = "c"
			revDict["c"] = c
		} else if contains(cf, inFirstNotInSecond(abcdefg, digits[7])[0]) {
			fmt.Println("abdefg : ", digits[7])
			c := inFirstNotInSecond(abcdefg, digits[7])[0]
			fmt.Println("c : ", c)
			dict[c] = "c"
			revDict["c"] = c
		} else {
			fmt.Println("abdefg : ", digits[8])
			c := inFirstNotInSecond(abcdefg, digits[8])[0]
			fmt.Println("c : ", c)
			dict[c] = "c"
			revDict["c"] = c
		}
		//search f
		f := inFirstNotInSecond(cf, []string{revDict["c"]})[0]
		fmt.Println("f : ", f)
		dict[f] = "f"
		revDict["f"] = f

		//search b and e
		x := inFirstNotInSecond(digits[3], acf)
		y := inFirstNotInSecond(digits[4], acf)
		z := inFirstNotInSecond(digits[5], acf)
		var dg []string
		var other [][]string
		if len(x) == 2 {
			dg = x
			other = [][]string{digits[4], digits[5]}
		} else if len(y) == 2 {
			dg = y
			other = [][]string{digits[3], digits[5]}
		} else {
			dg = z
			other = [][]string{digits[3], digits[4]}
		}

		fmt.Println("dg : ", dg)
		var abdfg []string
		var acdeg []string
		if contains(other[0], revDict["f"]) {
			abdfg = other[0]
			acdeg = other[1]
		} else {
			abdfg = other[1]
			acdeg = other[0]
		}
		fmt.Println("abdfg : ", abdfg)
		fmt.Println("acdeg : ", acdeg)

		b := inFirstNotInSecond(inFirstNotInSecond(abdfg, acf), dg)[0]
		dict[b] = "b"
		revDict["b"] = b
		fmt.Println("b : ", b)

		e := inFirstNotInSecond(inFirstNotInSecond(acdeg, acf), dg)[0]
		fmt.Println("e : ", e)
		dict[e] = "e"
		revDict["e"] = e

		//search d
		bcdf := digits[2]
		fmt.Println("bcdf : ", bcdf)
		fmt.Println(inFirstNotInSecond(bcdf, []string{revDict["b"], revDict["c"], revDict["f"]}))
		d := inFirstNotInSecond(bcdf, []string{revDict["b"], revDict["c"], revDict["f"]})[0]
		fmt.Println("d : ", d)
		dict[d] = "d"
		revDict["d"] = d

		//search g
		g := inFirstNotInSecond(dg, []string{revDict["d"]})[0]
		dict[g] = "g"
		fmt.Println("g : ", g)
		revDict["g"] = g
		it := 1000
		tmpRes := 0
		for _, s := range strings.Split((strings.Split(scanner.Text(), "|")[1]), " ") {
			if s != "" {
				tmpRes += dicoDigits[traduc(dict, s)] * it
				it = it / 10
			}
		}
		fmt.Println(strings.Split(scanner.Text(), "|")[1], " = ", tmpRes)
		res += tmpRes
	}
	fmt.Println(res)
}
