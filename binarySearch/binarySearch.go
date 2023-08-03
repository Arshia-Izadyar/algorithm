package main

import (
	"fmt"
	"sort"
)

func search(arr []int, num int) (n int, ok bool){
	low := 0
	high := len(arr) - 1
	sort.Slice(arr, func(i, j int) bool {return arr[i] < arr[j]})
	fmt.Println(arr)
	for low <= high{
		mid := (low + high) / 2
		if arr[mid] == num {
			return arr[mid], true
		}
		if arr[mid] > num{
			high = mid -1 
		} else{
			low = mid + 1
		} 
			
	}
	return 0, false
}


func main(){

	a , ok := search([]int{1, 2,3,4,5,6,10,7,8,9,0,11}, 9)
	fmt.Println(a, ok)
}