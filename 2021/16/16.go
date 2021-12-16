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

func BitsToInt(bits []string) int {
	num, err := strconv.ParseInt(strings.Join(bits, ""), 2, 64)
	if err != nil {
		fmt.Printf("err ParseInt : %s", err)
	}
	return int(num)
}

func run(bits []string, pos int, end int, subGroup int) (int, int) {
	fmt.Println("run at position ", pos, " with end at ", end, " and number of subGroup ", subGroup)
	version := BitsToInt(bits[pos : pos+3])
	fmt.Println("version : ", version)
	finalVersion := version
	pos += 3
	typeBits := BitsToInt(bits[pos : pos+3])
	pos += 3
	fmt.Println("type ", typeBits)
	if typeBits == 4 {
		//literal
		fmt.Println("type literal")
		var numBits []string
		for bits[pos] != "0" {
			numBits = append(numBits, bits[pos+1:pos+5]...)
			pos += 5
		}
		numBits = append(numBits, bits[pos+1:pos+5]...)
		pos += 5
		fmt.Println("literal : ", BitsToInt(numBits))
		subGroup -= 1
	} else {
		//operator
		if bits[pos] == "0" {
			//length
			length := BitsToInt(bits[pos+1 : pos+16])
			fmt.Println("length : ", length, " bits")
			pos += 16
			tmpPos, res := run(bits, pos, pos+length, -1)
			finalVersion += res
			pos = tmpPos
			subGroup -= 1
		} else {
			//number of subPackets
			nbSub := BitsToInt(bits[pos+1 : pos+12])
			fmt.Println("numbers of sub Packets : ", nbSub)
			pos += 12
			tmPos, res := run(bits, pos, -1, nbSub)
			pos = tmPos
			subGroup -= 1
			finalVersion += res
		}
	}
	if pos < end {
		//run length
		fmt.Println("remaining length : ", end-pos, " bits")
		tmpPos, res := run(bits, pos, end, -1)
		finalVersion += res
		pos = tmpPos
	} else if subGroup > 0 {
		//run sub
		fmt.Println("remaining sub packets : ", subGroup)
		tmpPos, res := run(bits, pos, -1, subGroup)
		subGroup = -1
		pos = tmpPos
		finalVersion += res
	}
	return pos, finalVersion
}

func main() {

	defer timeTrack(time.Now())
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	hexBin := make(map[rune][]string)
	hexBin['0'] = []string{"0", "0", "0", "0"}
	hexBin['1'] = []string{"0", "0", "0", "1"}
	hexBin['2'] = []string{"0", "0", "1", "0"}
	hexBin['3'] = []string{"0", "0", "1", "1"}
	hexBin['4'] = []string{"0", "1", "0", "0"}
	hexBin['5'] = []string{"0", "1", "0", "1"}
	hexBin['6'] = []string{"0", "1", "1", "0"}
	hexBin['7'] = []string{"0", "1", "1", "1"}
	hexBin['8'] = []string{"1", "0", "0", "0"}
	hexBin['9'] = []string{"1", "0", "0", "1"}
	hexBin['A'] = []string{"1", "0", "1", "0"}
	hexBin['B'] = []string{"1", "0", "1", "1"}
	hexBin['C'] = []string{"1", "1", "0", "0"}
	hexBin['D'] = []string{"1", "1", "0", "1"}
	hexBin['E'] = []string{"1", "1", "1", "0"}
	hexBin['F'] = []string{"1", "1", "1", "1"}
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	s := scanner.Text()
	//s := "A0016C880162017C3686B18A3D4780"
	var bits []string
	for _, c := range s {
		bits = append(bits, hexBin[c]...)
	}
	fmt.Println(run(bits, 0, -1, -1))

}
