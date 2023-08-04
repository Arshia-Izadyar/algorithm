package main

import "fmt"

func main() {
	arr := []int{64, 34, 25, 12, 22, 11, 90}
	res := bubbleSort(arr)
	fmt.Println(res)

}

func bubbleSort(arr []int) []int {
	for i := range arr {
		var swaped bool = false
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swaped = true
			}
		}
		if swaped == false {
			return arr
		}
	}
	return arr

}