import Friendfinder as ff

def fixedStoppingDistanceBFS(start,distance,graph):
    result = []
    parent = {start : -1}
    queue = [start]
    visited = set()
    visited.add(start)
    level = {start : 0}
    i = 1
    while queue:
        next = []
        for u in queue:
            if i > distance+1:
                 break
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        queue = next
        if i > distance+1:
            break
        i += 1
    for element in level:
        if level[element] > 1:
            result.append(element)
    return result


if __name__ == "__main__":
    data = """1
1,1,2
2,2,3
3,4,5
4,5,1
5,3,8
6,5,6
7,6,7
    """
    # file_handle = open("testcase/dummy_friend_list.csv","r")
    # data = file_handle.read()
    data_prime = data.split()

    data_size = len(data_prime)
    root_id = int(data_prime[0])
    friendgraph = {}
    i = 1
    while i < data_size:
        temp = [int(x) for x in data_prime[i].split(",")]
        if (temp[1] in friendgraph) and (temp[2] in friendgraph):
            friendgraph[temp[1]].append(temp[2])
            friendgraph[temp[2]].append(temp[1])
        elif temp[1] in friendgraph:
            friendgraph[temp[1]].append(temp[2])
            friendgraph[temp[2]] = [temp[1]]
        elif temp[2] in friendgraph:
            friendgraph[temp[1]] = [temp[2]]
            friendgraph[temp[2]] = [temp[1]]
        else:
            friendgraph[temp[1]] = [temp[2]]
            friendgraph[temp[2]] = [temp[1]]
        i += 1

    print(friendgraph)

    friend_finder_obj = ff.Friendfinder(1,int)

    result = friend_finder_obj.findSuggestedFriendList(root_id,friendgraph)
    print(result)
