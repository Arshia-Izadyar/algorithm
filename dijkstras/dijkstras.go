package main

import (
	"fmt"
	"math"
)

var graph map[string]map[string]float64
var costs map[string]float64
var parents map[string]string
var processed []string

func main() {
	// the graph
	graph = make(map[string]map[string]float64)
	graph["start"] = make(map[string]float64)
	graph["start"]["a"] = 6
	graph["start"]["b"] = 2

	graph["a"] = make(map[string]float64)
	graph["a"]["fin"] = 1

	graph["b"] = make(map[string]float64)
	graph["b"]["a"] = 3
	graph["b"]["fin"] = 5

	graph["fin"] = make(map[string]float64)

	// the costs table
	costs = make(map[string]float64)
	costs["a"] = 6
	costs["b"] = 2
	costs["fin"] = math.Inf(1)

	// the parents table
	parents = make(map[string]string)
	parents["a"] = "start"
	parents["b"] = "start"
	parents["fin"] = ""
	node := find_lowest_cost_node(costs)

	for node != ""{
		cost := costs[node]
		neighbors := graph[node]
		for n := range neighbors{
			new_cost := cost + neighbors[n]
			if new_cost < costs[n]{
				costs[n] = new_cost
				parents[n] = n
			}
		} 
		processed = append(processed, node)
		node = find_lowest_cost_node(costs)
	}
	fmt.Println(costs)



}

func find_lowest_cost_node(costs map[string]float64) (node string){
	lowest_cost := math.Inf(1)
	lowest_cost_node := ""
	for n := range costs{
		if costs[n] < lowest_cost && !contains(processed, n){
			lowest_cost = costs[n]
			lowest_cost_node = n
		}
	} 
	return lowest_cost_node
}

func contains(li []string, n string) bool{
	for _, v := range li{
		if v == n{
			return true
		}
	}
	return false
}