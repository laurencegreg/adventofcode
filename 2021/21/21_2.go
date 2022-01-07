package main

import (
	"fmt"
	"strconv"
	"time"
)

var possDice map[int]int

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

func game(pos1 int, score1 int, pos2 int, score2 int, player int) (int, int) {

	if score1 >= 21 {
		return 1, 0
	} else if score2 >= 21 {
		return 0, 1
	} else {
		win1 := 0
		win2 := 0
		if player == 1 {
			for mv, poss := range possDice {
				p1 := move(mv, pos1, 10)
				w1, w2 := game(p1, score1+p1, pos2, score2, 2)
				win1 += (w1 * poss)
				win2 += (w2 * poss)
			}
		} else {
			for mv, poss := range possDice {
				p2 := move(mv, pos2, 10)
				w1, w2 := game(pos1, score1, p2, score2+p2, 1)
				win1 += (w1 * poss)
				win2 += (w2 * poss)
			}
		}
		return win1, win2

	}
}

func main() {

	defer timeTrack(time.Now())

	possDice = make(map[int]int)
	for i := 1; i < 4; i++ {
		for j := 1; j < 4; j++ {
			for k := 1; k < 4; k++ {
				possDice[i+j+k]++
			}
		}
	}

	fmt.Println(game(8, 0, 4, 0, 1))
}
