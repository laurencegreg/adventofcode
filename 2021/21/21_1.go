package main

import (
	"fmt"
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

func move(nb int, pos int, size int) int {
	return (pos-1+nb)%size + 1
}

func rollDice(dice int, times int) (int, int) {
	res := 0
	for i := 0; i < times; i++ {
		res += dice
		dice++
	}
	return dice, res
}
func main() {

	defer timeTrack(time.Now())
	pos1 := 8
	score1 := 0
	pos2 := 4
	score2 := 0
	dice := 1

	for score1 < 1000 && score2 < 1000 {
		mv := 0
		dice, mv = rollDice(dice, 3)
		pos1 = move(mv, pos1, 10)
		score1 += pos1
		if score1 < 1000 {
			dice, mv = rollDice(dice, 3)
			pos2 = move(mv, pos2, 10)
			score2 += pos2
		}

	}
	if score1 < score2 {
		fmt.Println(score1 * (dice - 1))
	} else {
		fmt.Println(score2 * (dice - 1))
	}

}
