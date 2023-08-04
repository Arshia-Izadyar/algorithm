package main

import "strings"

func main() {
	f := "arshia"
	r := merg_sort(f)
	println(r)

}

func merg_sort(arr string) string {
	if len(arr) < 2 {
		return arr
	}
	mid := len(arr) / 2
	left := merg_sort(arr[:mid])
	right := merg_sort(arr[mid:])
	return merg(left, right)
}

func merg(left, right string) string {
	i := 0
	j := 0
	var result []string
	for len(left) > i && len(right) > j {
		if left[i] < right[j] {
			result = append(result, string(left[i]))
			i++
		} else {
			result = append(result, string(right[j]))
			j++
		}
	}
	result = append(result, string(left[i:]))
	result = append(result, string(right[j:]))
	return strings.Join(result,"")

}