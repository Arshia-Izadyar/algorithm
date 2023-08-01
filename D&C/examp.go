package main

import "fmt"

func sum_(list []int) int {
	tatal := 0
	for _, v := range list {
		tatal += v
	}
	return tatal
}

func r_sum(arr []int) (sum int) {

	if len(arr) == 0 {
		return
	}
	sum = arr[0] + r_sum(arr[1:])
	return
}

func r_count(arr []int) (count int) {
	if len(arr) == 0 {
		return
	}
	count = 1 + r_count(arr[1:])
	return
}

func max_(arr []int) (max int) {
	if len(arr) == 2 {
		if arr[0] > arr[1] {
			return arr[0]
		}
		return arr[1]
	}

	local_max := max_(arr[1:])
	if arr[0] > local_max {
		return arr[0]
	}
	return local_max

}

func max(arr []int) (m int) {
	if len(arr) == 2 {
		if arr[0] > arr[1] {
			return arr[0]
		}
		return arr[1]
	}
	lm := max(arr[1:])
	if arr[0] > lm {
		return arr[0]
	}
	return lm

}

func count_(list []int) int {
	count := 0
	for range list {
		count += 1
	}
	return count
}

func main() {
	arr := []int{9, 2, 3, 4, 5}
	t := max(arr)
	fmt.Println(t)
	c := r_count(arr)
	fmt.Println(c)
}
