package main

import "fmt"

func main(){
	arr := []int{31, 34 ,45, 23, 55, 12, 14, 98, 21}
	res := Sort(arr)
	fmt.Println(res)
}


func Sort(arr []int) (res []int){
	var lesser []int 
	var grater []int 
	if len(arr) < 2{
		return arr
	}
	pivot := arr[0]
	for _, v := range arr{
		if v < pivot{
			lesser = append(lesser, v)
		}
		if v > pivot{
			grater = append(grater, v)
		}
	}
	result := append(append(Sort(lesser), pivot), Sort(grater)...)
	return result
}