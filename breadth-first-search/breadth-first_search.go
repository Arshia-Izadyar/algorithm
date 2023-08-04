package main

func person_is_seller(name string) bool {
	return name[len(name)-1] == 'm'
}

var graph = make(map[string][]string)

func main() {
	graph["you"] = []string{"alice", "bob", "claire"}
	graph["bob"] = []string{"anuj", "peggy"}
	graph["alice"] = []string{"peggy"}
	graph["claire"] = []string{"thol", "jonny"}
	graph["anuj"] = []string{"kamran"}
	graph["peggy"] = []string{"ali"}
	graph["thom"] = []string{"koni"}
	graph["jonny"] = []string{"karim"}

	search("you")
}

func inSearched(list []string, item string) (ok bool) {
	for _, v := range list {
		if item == v {
			return true
		}
	}
	return false
}

func search(name string) (ok bool) {
	var q []string
	var searched []string
	var p string
	q = append(q, graph[name]...)
	for len(q) != 0 {
		p = q[0]
		q = q[1:]
		if !inSearched(searched, p) {
			if person_is_seller(p) {
				println(p + " is mango seller!")
				return true
			}
			searched = append(searched, p)
			q = append(q, graph[p]...)
		}
	}
	return false

}
