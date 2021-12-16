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

func calc(value int, res int, op int) int {
	if value < 0 {
		return res
	} else {
		switch op {
		case 0:
			return value + res
		case 1:
			return value * res
		case 2:
			//min
			if value > res {
				return res
			} else {
				return value
			}
		case 3:
			//max
			if value < res {
				return res
			} else {
				return value
			}
		case 5:
			//greater
			if value > res {
				return 1
			} else {
				return 0
			}
		case 6:
			//lesser
			if value < res {
				return 1
			} else {
				return 0
			}
		case 7:
			//equal
			if value == res {
				return 1
			} else {
				return 0
			}
		default:
			return -1
		}
	}
}

func runCalc(bits []string, pos int, end int, subGroup int, op int) (int, int) {
	fmt.Println("run at position ", pos, " with end at ", end, " and number of subGroup ", subGroup)
	value := -1
	version := BitsToInt(bits[pos : pos+3])
	fmt.Println("version : ", version)
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
		value = BitsToInt(numBits)
		fmt.Println("literal ", value)
		subGroup -= 1
	} else {
		//operator
		if bits[pos] == "0" {
			//length
			length := BitsToInt(bits[pos+1 : pos+16])
			fmt.Println("length : ", length, " bits")
			pos += 16
			tmpPos, res := runCalc(bits, pos, pos+length, -1, typeBits)
			value = res
			pos = tmpPos
			subGroup -= 1
		} else {
			//number of subPackets
			nbSub := BitsToInt(bits[pos+1 : pos+12])
			fmt.Println("numbers of sub Packets : ", nbSub)
			pos += 12
			tmPos, res := runCalc(bits, pos, -1, nbSub, typeBits)
			pos = tmPos
			subGroup -= 1
			value = res
		}
	}
	if pos < end {
		//run length
		fmt.Println("remaining length : ", end-pos, " bits")
		tmpPos, res := runCalc(bits, pos, end, -1, op)
		value = calc(value, res, op)
		pos = tmpPos
	} else if subGroup > 0 {
		//run sub
		fmt.Println("remaining sub packets : ", subGroup)
		tmpPos, res := runCalc(bits, pos, -1, subGroup, op)
		subGroup = -1
		pos = tmpPos
		value = calc(value, res, op)
	}
	return pos, value
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
	//s := "9C0141080250320F1802104A08"
	var bits []string
	for _, c := range s {
		bits = append(bits, hexBin[c]...)
	}
	fmt.Println(runCalc(bits, 0, -1, -1, -1))

}
