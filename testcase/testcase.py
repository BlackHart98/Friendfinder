import random as rd



if __name__ == "__main__":
    file_handle = open("dummy_friend_list.csv","w+")

    user_id = rd.randint(1,10)
    data_size = rd.randint(1,20)

    file_handle.write(f"{user_id},{data_size}\n")

    number_of_registered_data = 0
    registered_data = {}
    while number_of_registered_data < data_size:
        rand_1 =  rd.randint(1,10)
        rand_2 = rd.randint(1,10)
        if rand_1 == rand_2:
            continue
        elif rand_1 not in registered_data:
            temp = set()
            temp.add(rand_2)
            registered_data[rand_1] = ([rand_2],temp)
            number_of_registered_data += 1
        elif rand_2 in registered_data[rand_1][1]:
            continue
        elif rand_2 not in registered_data[rand_1][1]:
            if rand_2 in registered_data and rand_1 in registered_data[rand_2][1]:
                continue
            else:
                registered_data[rand_1][1].add(rand_2)
                registered_data[rand_1][0].append(rand_2)
                registered_data[rand_1] = (registered_data[rand_1][0],registered_data[rand_1][1])
                number_of_registered_data += 1
    # print(registered_data)

    k = 1
    for key in registered_data:
        for element in registered_data[key][0]:
            file_handle.write(f"{k},{key},{element}\n")
            k += 1
    pass
