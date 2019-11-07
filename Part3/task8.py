def binary_search_tree (some_list):
    new_list = []
    while some_list != []:
        min_item = some_list[0]
        for item in some_list:
            if item < min_item:
                min_item = item
        new_list.append(min_item)
        some_list.remove(min_item)
    return new_list