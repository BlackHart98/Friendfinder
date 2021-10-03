import Friendfinder as ff


if __name__ == "__main__":
#     data = """1
# 1,1,2
# 2,2,3
# 3,4,5
# 4,5,1
# 5,3,8
# 6,5,6
# 7,6,7
#     """
    file_handle = open("testcase/dummy_friend_list.csv","r")
    data = file_handle.read()
    data_prime = data.split()

    data_size = len(data_prime)
    root_id = int((data_prime[0].split(","))[0])
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
            # friendgraph[temp[2]] = [temp[1]]
        i += 1

    print(friendgraph)

    friend_finder_obj = ff.Friendfinder(1,int)

    result = friend_finder_obj.findSuggestedFriendList(root_id,friendgraph)
    print(result)

    mutual_friend = friend_finder_obj.mutualFriend(root_id,result,friendgraph)
    print(mutual_friend)
