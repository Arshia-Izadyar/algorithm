package main

import "fmt"

func main() {
	sorted_arr := selection_sort([]int{31, 34, 45, 23, 55, 12, 14, 98, 21})
	fmt.Println(sorted_arr)
}

func findSmallest(arr []int) int {
	// smallest_index := 0
	smallest_number := arr[0]
	for _, v := range arr {
		if v < smallest_number {
			smallest_number = v
			// smallest_index = i

		}
	}
	return smallest_number
}

func selection_sort(arr []int) []int {
	new_arr := []int{}
	for range arr {
		smallest := findSmallest(arr)
		new_arr = append(new_arr, smallest)
		arr = remove(arr, smallest)
	}
	return new_arr
}
func remove(arr []int, n int) []int {
	for i, v := range arr {
		if v == n {
			arr = append(arr[:i], arr[i+1:]...)
		}
	}
	return arr
}
