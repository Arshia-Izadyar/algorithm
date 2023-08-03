package main

import "fmt"

func main() {
	var stations = make(map[string][]string)
	stations["kone"] = []string{"id", "nv", "ut"}
	stations["ktwo"] = []string{"wa", "id", "mt"}
	stations["kthree"] = []string{"or", "nv", "ca"}
	stations["kfour"] = []string{"nv", "ut"}
	stations["kfive"] = []string{"ca", "az"}

	var states_needed = []string{"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
	final_stations := covering(states_needed, stations)
	fmt.Println(final_stations)

}

func covering(sn []string, stations map[string][]string) (final_stations []string) {


	for len(sn) > 0 {
		var best_station string
		var states_covered []string
		for k := range stations {
			covered := and(sn, stations[k])
			if len(covered) > len(states_covered) {
				states_covered = covered
				best_station = k
			}

		}
		if best_station != "" {
			final_stations = append(final_stations, best_station)
			sn = removeData(sn, states_covered)
		}
	}
	return 

}

func and(s1, s2 []string) (res []string) {
	for _, i := range s1 {
		for _, j := range s2 {
			if i == j {
				res = append(res, i)
			}
		}
	}
	return res
}

func removeData(states_needed, covered []string) (res []string) {
	for _, data := range covered {
		states_needed = remove(states_needed, data)
	}
	return states_needed
}

func remove(states_needed []string, value string) (res []string) {
	for i, item := range states_needed {
		if item == value {
			states_needed = append(states_needed[:i], states_needed[i+1:]...)

		}
	}
	return states_needed
}