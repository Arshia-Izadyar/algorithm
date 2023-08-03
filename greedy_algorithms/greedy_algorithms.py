
stations = {}
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

def covering(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = {}
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station

            if len(covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = covered
        if best_station is not None:
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
        else:
            return None
    return final_stations


def test(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = {}
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            
            if len(covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = covered
        if best_station is not None:
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
        else:
            return None
    return final_stations





print(test(states_needed, stations))
# print(covering(states_needed, stations))
  
        