from collections import deque


graph = {}
graph["me"] = ["lol", "lmao", "johanny"]
graph["lol"] = ["lmao", "sarah"]
graph["lmao"] = ["sarah", "johanny"]
graph["sarah"] = ["ali", "kiki"]
graph["johanny"] = ["v", "roge"]


def search():
    q = deque()
    q += graph["me"]
    searched = []
    while q:
        p = q.popleft()
        if p not in searched:
            if p_is_v(p):
                print("person found")
                return True
            else:
                q += graph[p]
                searched.append(p)
    return False

def p_is_v(n):
    if n == "v":
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    search()