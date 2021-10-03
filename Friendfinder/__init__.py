


class Friendfinder:
    friend_of_friends_depth = 0
    data_type = int


    def __init__(self,friend_of_friends_depth,data_type):
        self.friend_of_friends_depth = friend_of_friends_depth
        self.data_type = data_type


    def findSuggestedFriendList(self,root_id,friendgraph):
        result = []
        parent = {root_id : -1}
        queue = [root_id]
        visited = set()
        visited.add(root_id)
        level = {root_id : 0}
        i = 1
        while queue:
            next = []
            for u in queue:
                if i > self.friend_of_friends_depth+1:
                     break
                for v in friendgraph[u]:
                    if v not in visited:
                        visited.add(v)
                        level[v] = i
                        parent[v] = u
                        next.append(v)
            queue = next
            if i > self.friend_of_friends_depth+1:
                break
            i += 1
        for element in level:
            if level[element] > 1:
                result.append(element)
        return result


    def mutualFriend(self,root_id,suggested_friend_list,graph):
        mutual_friend = {}
        temp_root = graph[root_id]
        temp_root.sort()
        for element in suggested_friend_list:
            mutual_friend[element] = []
            if element in graph:
                temp_dest = graph[element]
                temp_dest.sort()
                i = j = 0
                while i < len(temp_root) and j < len(temp_dest):
                    if temp_root[i] == temp_dest[j]:
                        mutual_friend[element].append(temp_root[i])
                        i += 1
                        j += 1
                    elif temp_root[i] < temp_dest[j]:
                        i += 1
                    else:
                        j += 1
            else:
                continue
        return mutual_friend
