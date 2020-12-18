def data_compare(online_list, existing_list):
    new_list = []
    online_length = len(online_list)
    existing_length = len(existing_list)
    broke = False

    for i in range(online_length):
        new_compare = online_list[i].desc
        for r in range(existing_length):
            if new_compare == existing_list[r].desc:
                broke = True
                break
        if broke is False:
            new_list.append(online_list[i])
        broke = False

    if not new_list:
        return "empty"
    else:
        return new_list
